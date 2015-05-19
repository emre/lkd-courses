from django.forms import ModelForm

from .models import UserProfile

from django.contrib.auth.forms import UserCreationForm as AuthModuleUserCreationForm


class UserCreationForm(AuthModuleUserCreationForm):

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
