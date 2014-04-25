from django.conf.urls import patterns, include, url
from paste.text import views as text

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', text.add_view),
    url(r'^p/(.*)/$', text.edit_view),
    url(r'^e/(.*)/$', text.edit_view),
    url(r'^r/(.*)/$', text.raw_view),
    url(r'^d/(.*)/$', text.raw_view, {'mime': 'application/octet-stream'}),
    url(r'^admin/', include(admin.site.urls)),
)
