from django.conf.urls import url

from . import views


app_name = 'users'


urlpatterns = [

            #  UserProfile urls 
            url(r'^user/$', views.UserProfile.as_view(), name='profile'),
            url(
                r'^user/create/$', 
                views.CreateUser.as_view(), name='create'),
            url(
                r'^user/update/(?P<pk>[0-9]+)/$', views.EditUser.as_view(),
                name='edit'),
            url(
                r'^user/delete/(?P<pk>[0-9]+)/$', views.DeleteUser.as_view(),
                name='delete'),

            url(
                r'^user/list/$', views.EditUserList.as_view(),
                name='user_list'),
            ]

