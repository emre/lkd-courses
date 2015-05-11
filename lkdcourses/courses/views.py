# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import UserProfile, Event
from .forms import UserProfileForm


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())


class IndexView(ListView):
    model = Event
    template_name = 'courses/index.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/'
    success_message = 'Kaydınız gerçekleştirildi. Lütfen giriş yapın.'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(RegisterView, self).form_valid(form)


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'courses/user_profile.html'
    success_url = reverse_lazy('courses:profile_edit')
    success_message = 'Profiliniz başarıyla düzenlendi.'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(UserProfileUpdate, self).form_valid(form)
