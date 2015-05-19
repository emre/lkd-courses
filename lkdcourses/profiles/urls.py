
from django.conf.urls import url

from .views import UserProfileUpdate, RegisterView


urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^profile/$', UserProfileUpdate.as_view(), name='profile_edit'),
]
