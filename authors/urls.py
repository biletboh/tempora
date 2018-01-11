from django.conf.urls import url

from . import views


app_name = 'authors'


urlpatterns = [
            url(r'^$', views.AuthorList.as_view(), name='list'),
            url(r'^(?P<slug>[-\w]+)/$', views.AuthorPage.as_view(),
                name='page'),
            url(r'^create/$', views.CreateAuthor.as_view(),
                name='create'),
            url(r'^update/list/$', views.AdminAuthorList.as_view(),
                name='update_list'),
            url(r'^update/(?P<slug>[-\w]+)/$',
                views.UpdateAuthor.as_view(),
                name='update'),
            url(r'^delete/(?P<pk>[0-9]+)/$',
                views.DeleteAuthor.as_view(),
                name='delete'),
            ]
