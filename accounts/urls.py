from django.conf.urls import url
from django.contrib import admin

from .views import (
    MyProfileDetailView,
    MyProfileFormView
)


urlpatterns = [
    url(r'^profile/$', MyProfileDetailView.as_view(), name='profile_details'),
    url('^profile/edit/$', MyProfileFormView.as_view(), name='profile_edit'),
]
