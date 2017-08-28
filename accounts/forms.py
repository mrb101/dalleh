from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
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
        localized_fields = (
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
        )
        widgets = {
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Gender',
                }
            ),
            'nick_name': forms.TextInput(
                attrs={
                    'class':  'form-control',
                    'placeholder': 'Nickname',
                }
            ),
            'dob': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone Number'
                }
            ),
            'website': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Website'
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Bio'
                }
            ),
            'current_job': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Current Job'
                }
            ),
            'degree': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Degree'
                }
            ),
            'nationality': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nationality'
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Location'
                }
            ),
            'pgp_public': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'PGP Public Key'
                }
            ),
            'facebook': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Facebook Profile URL'
                }
            ),
            'twitter': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Twitter Handler'
                }
            ),
            'google': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Google Profile URL'
                }
            ),
            'linkedin': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Linkedin Profile URL'
                }
            ),
        }
