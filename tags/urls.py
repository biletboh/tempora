from django.conf.urls import url

from . import views 


app_name = 'tags'


urlpatterns = [

            #  Tag urls 
            url(r'^create/$', views.CreateTag.as_view(), name='create'),
            #url(
            #    r'^update/list/$', views.EditTagList.as_view(),
            #    name='edit_list'),
            #url(
            #    r'^update/(?P<pk>[0-9]+)/$',
            #    views.EditTag.as_view(),
            #    name='edit'),
            #url(
            #    r'^delete/(?P<pk>[0-9]+)/$',
            #    views.DeleteTag.as_view(),
            #    name='delete'),
            ]

