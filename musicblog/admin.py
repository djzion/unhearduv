from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin
from .models import *

artist_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
artist_fieldsets[0][1]["fields"].extend(["content"])
artist_fieldsets[0][1]["fields"].insert(-2, "featured_image")

class ArtistAdmin(DisplayableAdmin):
    fieldsets = artist_fieldsets
    list_display = ('admin_thumb', 'title', 'status', 'slug')

event_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
event_fieldsets[0][1]["fields"].extend(['date', 'artists', 'venue', 'facebook_event', 'ticket_url', 'price'])
event_fieldsets[0][1]["fields"].insert(-2, "featured_image")

class EventAdmin(DisplayableAdmin):
    model = Event
    fieldsets = event_fieldsets

venue_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
venue_fieldsets[0][1]["fields"].extend(["address", 'city'])
venue_fieldsets[0][1]["fields"].insert(-2, "featured_image")

class VenueAdmin(DisplayableAdmin):
    fieldsets = venue_fieldsets

from mezzanine.blog.admin import BlogPostAdmin
post_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
post_fieldsets[0][1]["fields"].extend(['featured', 'content_type', 'object_id'])

from django.contrib.contenttypes.generic import GenericTabularInline

class PostSubjectInline(GenericTabularInline):
    model = MusicBlogPost
    ct_field_name = 'content_type'
    id_field_name = 'object_id'


class PostAdmin(admin.ModelAdmin):
    content_type_whitelist = ('musicblog/artist', 'musicblog/event', 'musicblog/track' )


class TrackAdmin(admin.ModelAdmin):
    model = Track
    class Media:
        js = ("js/admin.js",)



admin.site.register(Artist, ArtistAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(MusicBlogPost, PostAdmin)
admin.site.register(Track, TrackAdmin)