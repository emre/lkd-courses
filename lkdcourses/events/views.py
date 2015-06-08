from __future__ import unicode_literals

from django.views.generic.list import ListView

from .models import Event


class IndexView(ListView):
    model = Event
    template_name = 'events/index.html'
