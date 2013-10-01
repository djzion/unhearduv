from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Displayable, RichText
from mezzanine.core.fields import FileField
from mezzanine.utils.models import AdminThumbMixin
from mezzanine.blog.models import BlogPost


class Artist(Displayable, RichText, AdminThumbMixin):
    name = models.CharField(max_length=255)

    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to="images", format="Image",
        max_length=255, null=True, blank=True)
    admin_thumb_field = 'featured_image'

    @models.permalink
    def get_absolute_url(self):
        return ('musicblog.views.show_artist', (), {'slug': self.slug})


class ArtistLink(models.Model):
    artist = models.ForeignKey(Artist)
    site = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class Venue(Displayable, AdminThumbMixin):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    featured_image = FileField(verbose_name=_("Featured Image"),
    upload_to="images", format="Image",
    max_length=255, null=True, blank=True)
    admin_thumb_field = 'featured_image'

    @models.permalink
    def get_absolute_url(self):
        return ('musicblog.views.show_venue', (), {'slug': self.slug})


class Event(Displayable, AdminThumbMixin):
    date = models.DateTimeField()
    venue = models.ForeignKey(Venue, null=True)
    artists = models.ManyToManyField(Artist)
    facebook_event = models.CharField(max_length=100, null=True, blank=True)
    ticket_url = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)

    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to="images", format="Image",
        max_length=255, null=True, blank=True)
    admin_thumb_field = 'featured_image'

    @models.permalink
    def get_absolute_url(self):
        return ('musicblog.views.show_event', (), {'slug': self.slug})

class Track(models.Model):
    artist = models.ForeignKey(Artist, null=True)
    artist_name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='tracks', null=True)


class SoundCloudTrack(Track):
    soundcloud_id = models.CharField(max_length=255)
    url = models.URLField()


class MusicBlogPost(BlogPost):
    artist = models.ForeignKey(Artist, null=True, blank=True)
    event = models.ForeignKey(Event, null=True, blank=True)
    track = models.ForeignKey(Track, null=True, blank=True)
    featured = models.BooleanField(default=False)