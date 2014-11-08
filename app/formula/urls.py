from django.conf.urls import patterns, include, url
from django.contrib import admin
from formula.views import IndexView, MagicView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^magic/$', MagicView.as_view(), name='magic'),
)
