from django.db import models
from django.contrib.auth.models import User

from PIL import Image as PILImage

# Create your models here.
class Description(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()

class Equipment(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(max_length=512)

class Image(models.Model):
    author = models.ForeignKey(User)
    caption = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images')
    thumbnail = models.ImageField(upload_to='thumbnails')

    def makeThumbnail(self):
        try:
            image = PILImage.open(self.image)
            new_thumbnail = image.thumbnail((200, 200))
            self.thumbnail = new_thumbnail.write()
        except IOError:
            print("Cannot create thumbnail for {filename}".format(filename=self.image.url))

class Venue(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField(max_length=512)
    contacts = models.ManyToManyField(Contact)
    images = models.ManyToManyField(Image)
    audience_min = models.IntegerField()
    audience_max = models.IntegerField()
    equipment = models.ManyToManyField(Equipment)
