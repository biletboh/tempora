from django.conf.urls import url

from . import views

app_name = 'pbhouse'

urlpatterns = [
            url(r'^$', views.LandingPage.as_view(), name = 'landing'),
            ]

