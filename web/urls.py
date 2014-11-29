from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.views import logout
from web.models import Venue

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Venue, template_name="venue_list.html"), name='venue_list'),
    url(r'^venue/(?P<pk>\d+)/$', DetailView.as_view(model=Venue, template_name="venue_detail.html"), name='venue_detail'),
    url(r'^landingpage$', TemplateView.as_view(template_name="landingpage.html"), name='landingpage'),
    url(r'accounts/profile', TemplateView.as_view(template_name="profile.html"), name='profile'),
    url(r'accounts/logout', logout, {'next_page': '/'}, name='logout'),
)