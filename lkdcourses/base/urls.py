from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^resetpassword/done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'registration/reset_done.html'}, name='password_reset_done'),
    url(r'^resetpassword/complete/$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'registration/reset_complete.html'}, name='password_reset_complete'),
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'registration/reset.html'}, name='password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'registration/reset_form.html'}, name='password_reset_confirm'),
    url(r'^', include('courses.urls', namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
]
