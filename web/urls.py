from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import logout
from web.models import Venue
from web.forms import AdvancedSearchForm
from web.views import AdvancedSearchView, VenueList, VenueDetail, DeleteVenue

urlpatterns = patterns('',
    url(r'^$', VenueList.as_view(), name='venue_list'),
    url(r'^venue/(?P<pk>\d+)/$', VenueDetail.as_view(), name='venue_detail'),
    url(r'^venue/(?P<pk>\d+)/delete$', DeleteVenue.as_view(), name='delete_venue'),
    url(r'^create_venue$', CreateView.as_view(model=Venue, fields=['name', 'address', 'audience_min', 'audience_max']), name='create_venue'),
    url(r'^search$', AdvancedSearchView.as_view(), name='advanced_search'),

    url(r'accounts/profile', TemplateView.as_view(template_name="profile.html"), name='profile'),
    url(r'accounts/logout', logout, {'next_page': '/'}, name='logout'),
)