from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns





urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^requestinfo/$', 'home.views.requestinfo', name='requestinfo'),
    # url(r'^detail/(?P<slug>[^/]+)/$', 'home.views.detail', name='detail'),



    url(r'^index/$', 'apps.views.index', name='index'),
    url(r'^about/$', 'apps.views.about', name='about'),
    url(r'^contact/$', 'apps.views.contact', name='contact'),
    url(r'^products/$', 'apps.views.products', name='products'),
    url(r'^details/$', 'apps.views.details', name='details'),
    url(r'^product_filter/(?P<slug>[^/]+)/$', 'apps.views.product_filter', name='product_filter'),
    url(r'^testimonial/$', 'apps.views.testimonial', name='testimonial'),


    url(r'^grappelli/', include('grappelli.urls')),

)
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

)



urlpatterns += staticfiles_urlpatterns()
