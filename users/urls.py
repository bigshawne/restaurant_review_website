from django.urls import re_path
from . import views

app_name = 'users'

# define urls for registion and login

urlpatterns = [
    # registration
    re_path(r'register/$', views.register, name='register'),
    # login
    re_path(r'^login/$', views.login, name='login'),
    # profile
    re_path(r'^user/(?P<pk>\d+)/profile/$', views.profile, name='profile'),
    # profile update
    re_path(r'user/(?P<pk>\d+)/profile/update/$', views.profile_update, name='profile_update'),
    # password change
    re_path(r'user/(?P<pk>\d+)/pwdchange/$', views.pwd_change, name='pwd_change'),
    # log out
    re_path(r'logout/$', views.logout, name='logout')
]
