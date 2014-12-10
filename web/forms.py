from django import forms
from web.models import Contact, Equipment, Venue, Image, Description

class AdvancedSearchForm(forms.Form):
	q = forms.CharField(label="Search terms", max_length=128, required=False)
	audience = forms.IntegerField(min_value=1, required=False)

class VenueForm(forms.Form):
	name = forms.CharField()
	address = forms.CharField()
	description = forms.CharField()
	audience_min = forms.IntegerField()
	audience_max = forms.IntegerField()

class DescriptionForm(forms.ModelForm):
	class Meta:
		model = Description
		fields = ['text']

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'phone']

class EquipmentForm(forms.ModelForm):
	class Meta:
		model = Equipment
		fields = ['name', 'desc']

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['image', 'caption']

class DeleteVenueForm(forms.Form):
	pass
