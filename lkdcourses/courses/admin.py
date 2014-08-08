from django.contrib import admin

from .models import *


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
    filter_horizontal = ('instructors',)


class InstructorAdmin(admin.ModelAdmin):
    pass


class VenueAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


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