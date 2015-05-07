# coding: utf-8

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import UpdateView

from .models import UserProfile
from .forms import UserProfileForm


def index(request):
    return render(request, 'courses/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfileForm()
            upf = user_profile.save(commit=False)
            upf.user = user
            upf.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())


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
