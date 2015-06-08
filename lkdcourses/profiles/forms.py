from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm as AuthModuleUserCreationForm
from django.forms import ModelForm

from .models import UserProfile


class UserCreationForm(AuthModuleUserCreationForm):

    required_css_class = 'required'

    class Meta:
        model = UserProfile
        fields = ("username",)


class UserForm(ModelForm):

    class Meta:
        model = UserProfile
        exclude = [
            'is_staff',
            'is_active',
            'date_joined',
            'is_superuser',
            'last_login',
            'password',
            'groups',
            'user_permissions',
            'username',
        ]
