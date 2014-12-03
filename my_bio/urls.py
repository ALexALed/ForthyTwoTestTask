# - *- coding: utf- 8 - *-
__author__ = 'alexaled'


from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'my_bio.views.bio_home', name='home'),
    url(r'^requests/$', 'my_bio.views.requests', name='requests'),
)
