from django.conf.urls import patterns, include, url
from django.contrib import admin

from mysite import view

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace = 'polls')),
    url(r'^$', view.index, name = 'home'),
)
