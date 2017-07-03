from django.conf.urls import url

from . import views

app_name = 'pbhouse'

urlpatterns = [
            url(r'^$', views.LandingPage.as_view(), name = 'landing'),
            url(r'^team/$', views.Team.as_view(), name = 'team'),
            url(r'^dashboard/$', views.UserProfile.as_view(), name = 'profile'),
            ]

