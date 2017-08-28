from django.conf.urls import url
from django.contrib import admin

from .views import (
    HomeView,
    AboutView,
    ServicesView,
    ContactView
)


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home_page'),
    url('^about/$', AboutView.as_view(), name='about_page'),
    url('^services/$', ServicesView.as_view(), name='services_page'),
    url('^contact/$', ContactView.as_view(), name='contact_page'),
]
