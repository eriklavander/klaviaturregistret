from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse

from PIL import Image as PILImage
import os
import StringIO

# Create your models here.
class Description(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __unicode__(self):
        # Return the first five words.
        return ' '.join(self.text.split()[:5])

class Contact(models.Model):
    name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(max_length=512, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Image(models.Model):
    caption = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to='images')
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User)

    def make_thumbnail(self):
        image = PILImage.open(self.image.path)
        image.thumbnail((200,200))
        thumb_io = StringIO.StringIO()
        image.save(thumb_io, format='JPEG')

        image_basename, image_extension = os.path.splitext(os.path.basename(self.image.path))
        thumbnail_filename = "{basename}_tn{extension}".format(basename=image_basename, extension=image_extension)

        thumb_file = InMemoryUploadedFile(thumb_io, None, thumbnail_filename, 'image/jpeg', thumb_io.len, None)

        self.thumbnail.save(thumbnail_filename, thumb_file, save=True)

    def __unicode__(self):
        if self.caption:
            return self.caption
        else:
            return "Image {pk}".format(self.pk)

class Venue(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField(max_length=512, blank=True)
    descriptions = models.ManyToManyField(Description, blank=True)
    contacts = models.ManyToManyField(Contact, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    audience_min = models.IntegerField(blank=True)
    audience_max = models.IntegerField(blank=True)
    equipment = models.ManyToManyField(Equipment, blank=True)

    # def latest_update(self):
    #     latest = self.descriptions.order_by('-timestamp')

    def get_absolute_url(self):
        return reverse('venue_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name
