from django import forms


class ContactUsForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput({
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    name = forms.CharField(
        required=True,
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Name'
        })
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea({
            'class': 'form-control',
            'placeholder': 'Message'
        })
    )
