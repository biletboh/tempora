from django.conf.urls import url

from . import views


app_name = 'users'


urlpatterns = [
            #  UserProfile urls
            url(r'^dashboard/$', views.Profile.as_view(), name='dashboard'),
            url(
                r'^create/$',
                views.CreateUser.as_view(), name='create'),
            url(
                r'^update/(?P<pk>[0-9]+)/$', views.UpdateUser.as_view(),
                name='update'),
            url(
                r'^update/account/(?P<pk>[0-9]+)/$',
                views.AccountUpdateUser.as_view(),
                name='account_update'),
            url(
                r'^delete/(?P<pk>[0-9]+)/$', views.DeleteUser.as_view(),
                name='delete'),

            url(
                r'^list/$', views.UserList.as_view(),
                name='user_list'),
            ]
