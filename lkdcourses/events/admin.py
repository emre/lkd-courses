from django.contrib import admin

from .models import (Venue, Event, Sponsor)


class SponsorAdmin(admin.ModelAdmin):
    pass


class VenueAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'latitude', 'longitude')


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_display = ('name', 'start_date', 'end_date', 'venue')


admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Sponsor, SponsorAdmin)
