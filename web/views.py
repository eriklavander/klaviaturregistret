import datetime
import logging
import sys

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.views.generic.edit  import CreateView, DeleteView
from django.forms import ModelForm
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from web.models import Venue, Contact, Description, Address, Image
from web.forms import AdvancedSearchForm, VenueForm, ImageForm, DescriptionForm, ContactForm, DeleteVenueForm

logger = logging.getLogger(__name__)

class ProtectedView(TemplateView):
  template_name = 'secret.html'

  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super(ProtectedView, self).dispatch(*args, **kwargs)

# Create your views here.
class Profile(TemplateView):
  template_name = 'home.html'

class LandingPage(TemplateView):
  template_name = 'landingpage.html'

class AdvancedSearchView(TemplateView):
  template_name = 'search.html'

  def get_context_data(self, **kwargs):
    context = super(AdvancedSearchView, self).get_context_data(**kwargs)
    context['searchform'] = AdvancedSearchForm(self.request.GET)
    terms = self.request.GET.get('q', None)
    audience = self.request.GET.get('audience', None)
    if terms or audience:
      hits = Venue.objects.all()
      if terms:
        for term in terms.split('+'):
          hits = hits.filter(
            Q(name__icontains=term) |
            Q(descriptions__text__icontains=term) |
            Q(images__caption__icontains=term) |
            Q(address__text__icontains=term)
          )
      if audience:
        hits = hits.filter(audience_max__gte=audience, audience_min__lte=audience)
      context['hits'] = hits
    else:
      context['hits'] = []
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
    context['delete_venue_form'] = DeleteVenueForm
    return context

class CreateVenue(FormView):
  form_class = VenueForm

  def form_valid(self, form):
    sys.stderr.write('User: ' + str(self.request.user) + '\n')
    self.new_venue = Venue(
      name=form.cleaned_data['name'],
      audience_min=form.cleaned_data['audience_min'],
      audience_max=form.cleaned_data['audience_max']
    )
    self.new_venue.save()
    self.new_description = Description(
      text=form.cleaned_data['description'],
      author=self.request.user,
      venue=self.new_venue,
    )
    self.new_description.save()
    self.new_address = Address(
      text = form.cleaned_data['address'],
      author=self.request.user,
      venue=self.new_venue,
    )
    self.new_address.save()

    return super(CreateVenue, self).form_valid(form)

  def get_success_url(self):
    return reverse('venue_detail', kwargs={'pk': self.new_venue.id})

class DeleteVenue(DeleteView):
  model = Venue
  form_name = DeleteVenueForm
  #success_url = reverse('venue_list')
  success_url = '/'

class CreateContact(FormView):
  template_name = 'create_contact.html'
  form_class = ContactForm

  def form_valid(self, form):
    self.venue = Venue.objects.get(pk=self.kwargs['pk'])
    self.new_contact = Contact(
      name = form.cleaned_data['name'],
      phone = form.cleaned_data['phone'],
      email = form.cleaned_data['email'],
      added_by = self.request.user,
      venue = self.venue,
    )
    self.new_contact.save()
    # Figure out, based on URL, which Venue we belong to.
    return super(CreateContact, self).form_valid(form)

  def get_success_url(self):
    return reverse('venue_detail', kwargs={'pk': self.venue.id})

class CreateImage(FormView):
  template_name = 'create_image.html'
  form_class = ImageForm

  def form_valid(self, form):
    sys.stderr.write('In form_valid\n{}\n'.format((self.request)))
    self.venue = Venue.objects.get(pk=self.kwargs['pk'])
    self.new_image = Image(
      image = form.cleaned_data['image'],
      caption = form.cleaned_data['caption'],
      added_by = self.request.user,
      venue = self.venue,
    )
    self.new_image.make_thumbnail()
    self.new_image.save()

    return super(CreateImage, self).form_valid(form)

  def get_success_url(self):
    return reverse('venue_detail', kwargs={'pk': self.venue.id})

class CreateDescription(FormView):
  template_name = 'create_description.html'
  form_class = DescriptionForm

  def form_valid(self, form):
    self.venue = Venue.objects.get(pk=self.kwargs['pk'])
    self.new_description = Description(
      text = form.cleaned_data['text'],
      author = self.request.user,
      venue = self.venue,
    )
    self.new_description.save()
    return super(CreateDescription, self).form_valid(form)

  def get_success_url(self):
    return reverse('venue_detail', kwargs={'pk': self.venue.id})


