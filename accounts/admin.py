from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = [
        'gender',
        'nick_name',
        'dob',
        'phone',
        'website',
        'bio',
        'current_job',
        'degree',
        'nationality',
        'location',
        'pgp_public',
        'facebook',
        'twitter',
        'google',
        'linkedin',
    ]
    list_display = (
        'gender',
        'nick_name',
        'dob',
        'phone',
        'nationality',
        'location',
        'twitter',
    )
    list_filter = (
        'gender',
    )
    search_fields = [
        'gender',
        'nick_name',
        'dob',
        'phone',
        'website',
        'bio',
        'current_job',
        'degree',
        'nationality',
        'location',
        'pgp_public',
        'facebook',
        'twitter',
        'google',
        'linkedin',
    ]
    date_hierarchy = 'created'
