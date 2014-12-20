from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import logout
from web.models import Venue
from web.views import LandingPage, AdvancedSearchView, VenueList, VenueDetail, CreateVenue, DeleteVenue, CreateDescription, CreateContact, CreateImage

urlpatterns = patterns('',
    url(r'^$', VenueList.as_view(), name='venue_list'),
    url(r'^venue/(?P<pk>\d+)/$', VenueDetail.as_view(), name='venue_detail'),
    url(r'^venue/(?P<pk>\d+)/delete$', DeleteVenue.as_view(), name='delete_venue'),
    url(r'^venue/(?P<pk>\d+)/create_description$', CreateDescription.as_view(), name='create_description'),
    url(r'^venue/(?P<pk>\d+)/create_contact$', CreateContact.as_view(), name='create_contact'),
    url(r'^venue/(?P<pk>\d+)/create_image$', CreateImage.as_view(), name='create_image'),
    url(r'^create_venue$', CreateVenue.as_view(), name='create_venue'),
    url(r'^search$', AdvancedSearchView.as_view(), name='search'),

    url(r'^accounts/login', LandingPage.as_view(), name='landingpage'),
    url(r'accounts/profile', TemplateView.as_view(template_name="profile.html"), name='profile'),
    url(r'accounts/logout', logout, {'next_page': '/'}, name='logout'),
)