from django.conf.urls import url

from .views import index, register


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register/$', register, name='register'),
]
