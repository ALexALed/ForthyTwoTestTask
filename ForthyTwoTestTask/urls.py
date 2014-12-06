from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/registration/logout/$', 'my_bio.views.logout_view', name='logout'),
    url(r'^', include('my_bio.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

