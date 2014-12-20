from django.contrib import admin
from web.models import Venue, Address, Contact, Image, Description

# from django.contrib import admin
# from myapp.models import Article

# def make_published(modeladmin, request, queryset):
#     queryset.update(status='p')
# make_published.short_description = "Mark selected stories as published"

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title', 'status']
#     ordering = ['title']
#     actions = [make_published]

def make_thumbnails(modeladmin, request, queryset):
	for image in queryset:
		image.make_thumbnail()

class ImageAdmin(admin.ModelAdmin):
	def make_thumbnails(self, request, queryset):
		for image in queryset:
			image.make_thumbnail()
	make_thumbnails.short_description = 'Create thumbnails for selected images'
	actions = ['make_thumbnails']

class AddressInline(admin.StackedInline):
	model = Address

class VenueAdmin(admin.ModelAdmin):
	inlines = (AddressInline, )

# Register your models here.
admin.site.register(Venue, VenueAdmin)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Image, ImageAdmin)
admin.site.register(Description)
