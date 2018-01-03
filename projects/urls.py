from django.conf.urls import url

from . import views


app_name = 'projects'


urlpatterns = [
    url(r'^$', views.ProjectPage.as_view(), name='page'),
        url(r'^create/$', views.ProjectCreate.as_view(), name='create'),
        ]

