from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.views.generic import ListView
from django.contrib import admin
from print_string.models import HelloWorld
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^HelloWorld/', include('HelloWorld.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$',ListView.as_view(
       model=HelloWorld, template_name='index.html'
    ), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
