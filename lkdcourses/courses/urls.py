from django.conf.urls import url

from .views import IndexView, UserProfileUpdate, RegisterView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^profile/$', UserProfileUpdate.as_view(), name='profile_edit'),
]
