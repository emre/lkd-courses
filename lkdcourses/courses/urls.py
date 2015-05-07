from django.conf.urls import url

from .views import index, register, UserProfileUpdate


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', UserProfileUpdate.as_view(), name='profile_edit'),
]
