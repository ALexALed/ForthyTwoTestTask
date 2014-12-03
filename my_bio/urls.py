# - *- coding: utf- 8 - *-
__author__ = 'alexaled'


from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'my_bio.views.bio_home', name='home'),
    url(r'^$', 'my_bio.views.bio_home', name='home'),
)
