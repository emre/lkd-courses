# -*- coding: utf-8 -*-


from django.core.urlresolvers import reverse_lazy

from .models import UserProfile
from .mixins import LoginRequiredMixin
from .forms import (UserForm, UserCreationForm)

from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserForm
    template_name = 'profiles/user_profile.html'
    success_url = reverse_lazy('profiles:profile_edit')
    success_message = 'Profiliniz başarıyla düzenlendi.'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(UserProfileUpdate, self).form_valid(form)


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/'
    success_message = 'Kaydınız gerçekleştirildi. Lütfen giriş yapın.'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(RegisterView, self).form_valid(form)