from django.contrib import admin

from .models import *


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('instructors',)
    search_fields = ['name']
    list_display = ('name', 'event', 'start_date', 'end_date', 'deadline_date', 'quota')


class InstructorAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ApplicationAdmin(admin.ModelAdmin):
    pass


class UserChoiceAdmin(admin.ModelAdmin):
    pass



admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)

admin.site.register(Application, ApplicationAdmin)
admin.site.register(UserChoice, UserChoiceAdmin)
