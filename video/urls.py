from django.conf.urls import url

from . import views


app_name = 'video'


urlpatterns = [

            #  Video urls
            url(r'^$', views.VideoList.as_view(), name='list'),
            url(r'^(?P<slug>[\w-]+)/$', views.Page.as_view(), name='page'),
            url(r'^new/create/$',
                views.CreateVideo.as_view(), name='create'),
            url(
                r'^update/list/$', views.UpdateVideoList.as_view(),
                name='update_list'),
            url(
                r'^update/(?P<slug>[\w-]+)/$',
                views.UpdateVideo.as_view(),
                name='update'),
            url(
                r'^delete/(?P<pk>[0-9]+)/$',
                views.DeleteVideo.as_view(),
                name='delete'),
            ]
