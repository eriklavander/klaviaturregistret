# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse

from PIL import Image as PILImage
import os
import StringIO

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=128, verbose_name='Namn')
    audience_min = models.IntegerField(blank=True)
    audience_max = models.IntegerField(blank=True)

    def get_absolute_url(self):
        return reverse('venue_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name

class Description(models.Model):
    author = models.ForeignKey(User, verbose_name="Användare")
    text = models.TextField(max_length=512, verbose_name="Beskrivning")
    timestamp = models.DateTimeField(auto_now_add=True)
    venue = models.ForeignKey(Venue, related_name="descriptions")

    class Meta:
        ordering = ['-timestamp']

    def __unicode__(self):
        # Return the first five words.
        return ' '.join(self.text.split()[:5])

class Address(models.Model):
    author = models.ForeignKey(User, verbose_name="Användare")
    text = models.TextField(max_length=512, verbose_name="Adress")
    venue = models.OneToOneField(Venue, blank=True, related_name="address")

    def __unicode__(self):
        return '{venue}, {address}'.format(venue=self.venue.name, address=self.text)

class Contact(models.Model):
    name = models.CharField(max_length=128, blank=True, verbose_name="Namn")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=128, blank=True, null=True, verbose_name="Telefon")
    timestamp = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User)
    venue = models.ForeignKey(Venue, related_name="contacts")

    def __unicode__(self):
        return self.name

class Image(models.Model):
    caption = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User)
    venue = models.ForeignKey(Venue, related_name="images")

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

