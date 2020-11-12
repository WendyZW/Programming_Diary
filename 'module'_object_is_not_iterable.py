# 11.11.20
# TypeError: 'module' object is not iterable
#   If you see valid patterns in the file then the issue is probably caused by a circular import.

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

app_name = 'accounts'
urlpatternes = [
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('singup/$', views.SignUp.as_view(), name='signup'),
]
