from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('youtube_publisher_robot.views',
    url(r'^creative/$', 'creative', name='creative'),
    # Examples:
    # url(r'^$', 'youtube_publisher_robot.views.home', name='home'),
    # url(r'^youtube_publisher_robot/', include('youtube_publisher_robot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
