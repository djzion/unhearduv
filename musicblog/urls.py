from django.conf.urls import patterns, url

urlpatterns = patterns("musicblog.views",
    url("^$", "home", name="home"),
    url("^artist/(?P<slug>.*)/$", "show_artist"),
    url("^venue/(?P<slug>.*)/$", "show_venue"),
    url("^event/(?P<slug>.*)/$", "show_event"),
)