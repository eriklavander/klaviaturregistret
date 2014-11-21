from django.contrib import admin
from web.models import Venue, Contact, Image, Description, Equipment
# Register your models here.
from django.contrib import admin
from polls.models import Question

admin.site.register(Venue)
admin.site.register(Contact)
admin.site.register(Image)
admin.site.register(Description)
admin.site.register(Equipment)