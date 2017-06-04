from django.conf.urls import url

from . import views 


app_name = 'blog'


urlpatterns = [

            #  Blog urls 
            url(r'^blog/$', views.PostList.as_view(), name='blog'),
            url(r'^blog/(?P<pk>[0-9]+)/$', views.Page.as_view(), name='page'),
            url(r'^post/create/$', views.CreatePost.as_view(), name='create'),
            ]

