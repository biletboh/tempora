from django.conf.urls import url

from . import views


app_name = 'projects'


urlpatterns = [
            url(r'^create/$', views.CreateProject.as_view(),
                name='create'),
            url(r'^(?P<slug>[-\w]+)/$', views.ProjectPage.as_view(),
                name='page'),
            url(r'^update/list/$', views.UpdateProjectList.as_view(),
                name='update_list'),
            url(r'^update/(?P<slug>[-\w]+)/$',
                views.UpdateProject.as_view(),
                name='update'),
            url(r'^delete/(?P<pk>[0-9]+)/$',
                views.DeleteProject.as_view(),
                name='delete'),
            ]
