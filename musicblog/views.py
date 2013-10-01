from django.core.paginator import Paginator
from .decorators import *
from .models import *

@render_to('home.html')
def home(request):
    pages = Paginator(Event.objects.all(), 10)
    page = request.REQUEST.get('page', 1)
    events = pages.page(page)
    return locals()

@render_to('show_artist.html')
def show_artist(request, slug):
    artist = Artist.objects.get(slug=slug)
    return locals()

@render_to('show_venue.html')
def show_venue(request, slug):
    artist = Artist.objects.get(slug=slug)
    return locals()

@render_to('show_event.html')
def show_event(request, slug):
    artist = Artist.objects.get(slug=slug)
    return locals()