from django.contrib import admin

from .models import (UserProfile, AdministrativeNote)


class AdministrativeNoteAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(AdministrativeNote, AdministrativeNoteAdmin)
admin.site.register(UserProfile, UserAdmin)
