from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from common.models import TimestampModel


class UserProfile(TimestampModel):
    # CHOICES VARIABLES
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'

    # CHOCIES LISTS
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    )
    user = models.OneToOneField(
        User,
        related_name="profile"
    )
    gender = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=GENDER_CHOICES,
        help_text=_("Optional, Maximum of 50 Characters"),
        verbose_name=_("Gender"),
        db_index=True
    )
    nick_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional, Maximum of 255 Characters"),
        verbose_name=_("Nick Name"),
    )
    dob = models.DateField(
        null=True,
        blank=True,
        help_text=_("Pick a Date"),
        verbose_name=_("Date of Birth"),
        db_index=True
    )
    phone = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional, Phone Number"),
        verbose_name=_("Phone"),
        db_index=True
    )
    website = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional, Website URL"),
        verbose_name=_("Website"),
    )
    bio = models.TextField(
        null=True,
        blank=True,
        help_text=_("Optional, Short Bio Text"),
        verbose_name=_("Bio"),
    )
    current_job = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional, Maximum of 255"),
        verbose_name=_("Current Job"),
    )
    degree = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional, Maximum of 255 Characters"),
        verbose_name=_("Degree"),
    )
    nationality = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Required, Choose from a list"),
        verbose_name=_("Nationality"),
        db_index=True
    )
    location = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional, Choose from a list"),
        verbose_name=_("Location"),
        db_index=True
    )
    pgp_public = models.TextField(
        null=True,
        blank=True,
        help_text=_("Optional, Recommended"),
        verbose_name=_("PGP Public Key"),
    )
    facebook = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional, URL to Profile page"),
        verbose_name=_("Facebook"),
    )
    twitter = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional, Twitter Handler @example"),
        verbose_name=_("Twitter")
    )
    google = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional, URL to Google+ profile"),
        verbose_name=_("Google")
    )
    linkedin = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional, URL to Linkedin Profile"),
        verbose_name=_("Linkedin")
    )

    class Meta:
        ordering = ["created"]
        verbose_name = "User Profile"
        verbose_name_plural = "Users Profiles"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def age(self):
        user_age = datetime.date.today() - self.dob
        return user_age

    @property
    def name(self):
        return ''.format(self.user.first_name, self.user.last_name)
