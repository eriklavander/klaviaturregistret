from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.views.generic.edit	import CreateView, DeleteView
from django.forms import ModelForm
from django.db.models import Q
from django.core.urlresolvers import reverse

from web.models import Venue
from web.forms import AdvancedSearchForm, VenueForm, ImageForm, DescriptionForm, ContactForm, EquipmentForm, DeleteVenueForm

# Create your views here.
class Profile(TemplateView):
	template_name = 'home.html'

class AdvancedSearchView(TemplateView):
	template_name = 'search.html'

	def get_context_data(self, **kwargs):
		context = super(AdvancedSearchView, self).get_context_data(**kwargs)
		searchform = AdvancedSearchForm(self.request.GET)
		if searchform.is_valid():
			context['searchform'] = searchform
			context['hits'] = Venue.objects.filter(name__icontains=searchform.fields['q'])
		return context

class VenueList(ListView):
	model = Venue
	template_name = 'venue_list.html'

	def get_context_data(self, **kwargs):
		context = super(VenueList, self).get_context_data(**kwargs)
		context['create_venue_form'] = VenueForm
		return context	

class VenueDetail(DetailView):
	template_name = 'venue_detail.html'
	model = Venue

	def get_context_data(self, **kwargs):
		context = super(VenueDetail, self).get_context_data(**kwargs)
		context['image_form'] = ImageForm
		context['description_form'] = DescriptionForm
		context['contact_form'] = ContactForm
		context['equipment_form'] = EquipmentForm
		context['delete_venue_form'] = DeleteVenueForm
		return context

class CreateVenue(CreateView):
	form_name = VenueForm

class DeleteVenue(DeleteView):
	model = Venue
	form_name = DeleteVenueForm
	#success_url = reverse('venue_list')
	success_url = '/'