from django.contrib import admin

from .models import *


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
    filter_horizontal = ('instructors',)
    search_fields = ['name']
    list_display = ('name', 'event', 'start_date', 'end_date', 'deadline_date', 'quota')


class InstructorAdmin(admin.ModelAdmin):
    search_fields = ['name']


class VenueAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'latitude', 'longitude')


class EventAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'start_date', 'end_date', 'venue')


class ApplicationAdmin(admin.ModelAdmin):
    pass


class UserChoiceAdmin(admin.ModelAdmin):
    pass


class AdministrativeNoteAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass


class SponsorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(UserChoice, UserChoiceAdmin)
admin.site.register(AdministrativeNote, AdministrativeNoteAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Sponsor, SponsorAdmin)