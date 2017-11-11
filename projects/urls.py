from django.conf.urls import url

from . import views


app_name = 'projects'


urlpatterns = [
            url(r'^$', views.ProjectList.as_view(), name='projects'),
            url(r'^dashboard/$', views.DashboardProjectList.as_view(),
                name='dashboard_projects'),
            url(r'^create/$', views.ProjectCreate.as_view(), name='create'),
            url(r'^update/(?P<slug>[\w-]+)/$', views.ProjectUpdate.as_view(),
                name='update'),
            url(r'^(?P<slug>[\w-]+)/$', views.ProjectPage.as_view(),
                name='page'),
            url(r'^delete/(?P<slug>[\w-]+)/$', views.ProjectDelete.as_view(),
                name='delete'),
        ]

