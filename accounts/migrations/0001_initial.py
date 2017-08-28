# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 17:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, db_index=True)),
                ('upadted', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('gender', models.CharField(blank=True, db_index=True, help_text='Optional, Maximum of 50 Characters', max_length=50, null=True, verbose_name='Gender')),
                ('nick_name', models.CharField(blank=True, help_text='Optional, Maximum of 255 Characters', max_length=255, null=True, verbose_name='Nick Name')),
                ('dob', models.DateField(blank=True, db_index=True, help_text='Pick a Date', null=True, verbose_name='Date of Birth')),
                ('phone', models.CharField(blank=True, db_index=True, help_text='Optional, Phone Number', max_length=255, null=True, verbose_name='Phone')),
                ('website', models.URLField(blank=True, help_text='Optional, Website URL', max_length=255, null=True, verbose_name='Website')),
                ('bio', models.TextField(blank=True, help_text='Optional, Short Bio Text', null=True, verbose_name='Bio')),
                ('current_job', models.CharField(blank=True, help_text='Optional, Maximum of 255', max_length=255, null=True, verbose_name='Current Job')),
                ('degree', models.CharField(blank=True, help_text='Optional, Maximum of 255 Characters', max_length=255, null=True, verbose_name='Degree')),
                ('nationality', models.CharField(blank=True, db_index=True, help_text='Required, Choose from a list', max_length=255, null=True, verbose_name='Nationality')),
                ('location', models.CharField(blank=True, db_index=True, help_text='Optional, Choose from a list', max_length=255, null=True, verbose_name='Location')),
                ('pgp_public', models.TextField(blank=True, help_text='Optional, Recommended', null=True, verbose_name='PGP Public Key')),
                ('facebook', models.URLField(blank=True, help_text='Optional, URL to Profile page', max_length=255, null=True, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, help_text='Optional, Twitter Handler @example', max_length=255, null=True, verbose_name='Twitter')),
                ('google', models.URLField(blank=True, help_text='Optional, URL to Google+ profile', max_length=255, null=True, verbose_name='Google')),
                ('linkedin', models.URLField(blank=True, help_text='Optional, URL to Linkedin Profile', max_length=255, null=True, verbose_name='Linkedin')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'users_profiles',
                'verbose_name': 'user_profile',
                'ordering': ['created'],
            },
        ),
    ]
