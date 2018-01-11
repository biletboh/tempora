from django.conf.urls import url

from . import views


app_name = 'tags'


urlpatterns = [
            url(r'^create/$', views.CreateTag.as_view(),
                name='create'),
            url(r'^update/list/$', views.AdminTagList.as_view(),
                name='update_list'),
            url(r'^update/(?P<pk>[0-9]+)/$',
                views.UpdateTag.as_view(),
                name='update'),
            url(r'^delete/(?P<pk>[0-9]+)/$',
                views.DeleteTag.as_view(),
                name='delete'),
            ]
