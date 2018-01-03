from django.conf.urls import url

from . import views


app_name = 'blog'


urlpatterns = [

            #  Blog urls
            url(r'^$', views.PostList.as_view(), name='blog'),
            url(r'^(?P<pk>[0-9]+)/$', views.Page.as_view(), name='page'),
            url(r'^post/create/$', views.CreatePost.as_view(), name='create'),
            url(
                r'^update/list/$', views.EditPostList.as_view(),
                name='edit_list'),
            url(
                r'^post/update/(?P<slug>[\w-]+)/$',
                views.UpdatePost.as_view(),
                name='update'),
            url(
                r'^post/delete/(?P<pk>[0-9]+)/$',
                views.DeletePost.as_view(),
                name='delete'),
            ]
