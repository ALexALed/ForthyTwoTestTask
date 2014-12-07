# - *- coding: utf- 8 - *-
__author__ = 'alexaled'


from django.conf.urls import patterns, url

urlpatterns = patterns('', url(r'^$', 'my_bio.views.bio_home', name='home'),
    url(r'^requests/$', 'my_bio.views.requests', name='requests'),
    url(r'^edit/(?P<bio_pk>\w{1,50})/$',
        'my_bio.views.edit_bio_data', name="edit"),
    )
