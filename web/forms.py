# -*- coding: utf-8 -*-
from django import forms
from web.models import Contact, Venue, Image, Description

class AdvancedSearchForm(forms.Form):
  q = forms.CharField(label="Sökord", max_length=128, required=False)
  audience = forms.IntegerField(min_value=1, required=False, label="Publikmängd")

class VenueForm(forms.Form):
  name = forms.CharField(label='Namn')
  address = forms.CharField(label='Adress')
  description = forms.CharField(widget=forms.Textarea, label='Beskrivning', help_text='Scen, loger, ljusutrustning, instrument etc.')
  audience_min = forms.IntegerField(label='Minsta publik')
  audience_max = forms.IntegerField(label='Max publik')

class DescriptionForm(forms.ModelForm):
  class Meta:
    model = Description
    fields = ['text']

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['name', 'email', 'phone']

class ImageForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ['image', 'caption']

# class ImageForm(forms.Form):
#   image = forms.ImageField(required=False)
#   caption = forms.CharField(max_length=128, required=False)

class DeleteVenueForm(forms.Form):
  pass
