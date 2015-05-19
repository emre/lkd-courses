# coding: utf-8

from .models import Event

from django.views.generic.list import ListView


class IndexView(ListView):
    model = Event
    template_name = 'events/index.html'