from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'css/main.css', 'cms_put.views.css'),
    url(r'main.css', 'cms_put.views.css'),
    url(r'css/(.*)', 'cms_put.views.server'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'(.*)', 'cms_put.views.serverCSS'),
)
