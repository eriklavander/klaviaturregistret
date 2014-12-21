from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from web.models import Venue
from web.views import LandingPage, AdvancedSearchView, VenueList, VenueDetail, CreateVenue, DeleteVenue, CreateDescription, CreateContact, CreateImage

urlpatterns = patterns('',
    url(r'^$', login_required(VenueList.as_view()), name='venue_list'),
    url(r'^venue/(?P<pk>\d+)/$', login_required(VenueDetail.as_view()), name='venue_detail'),
    url(r'^venue/(?P<pk>\d+)/delete$', login_required(DeleteVenue.as_view()), name='delete_venue'),
    url(r'^venue/(?P<pk>\d+)/create_description$', login_required(CreateDescription.as_view()), name='create_description'),
    url(r'^venue/(?P<pk>\d+)/create_contact$', login_required(CreateContact.as_view()), name='create_contact'),
    url(r'^venue/(?P<pk>\d+)/create_image$', login_required(CreateImage.as_view()), name='create_image'),
    url(r'^create_venue$', login_required(CreateVenue.as_view()), name='create_venue'),
    url(r'^search$', login_required(AdvancedSearchView.as_view()), name='search'),

    url(r'^accounts/login', LandingPage.as_view(), name='landingpage'),
    url(r'accounts/profile', login_required(TemplateView.as_view(template_name="profile.html")), name='profile'),
    url(r'accounts/logout', logout, {'next_page': '/'}, name='logout'),
)