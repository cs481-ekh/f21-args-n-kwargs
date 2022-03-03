from django.contrib.auth.forms import UserCreationForm, UsernameField, SetPasswordForm
from .models import Account
from django import forms
from django.contrib.auth.forms import PasswordResetForm


class AccountCreationForm(UserCreationForm):
    email = forms.CharField(
        label="Email address",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})
    )

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}),
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}),
    )

    """Account creation extends UserCreationForm to create a form based on the definition of our account model"""

    class Meta(UserCreationForm):
        model = Account
        fields = ('email', 'password1', 'password2')


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'type': 'email',
        'name': 'email'
    }))



class UserPasswordConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordConfirmForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'New Password',
        'class': 'form-control'
    }))

    new_password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'New password confirmation',
        'class': 'form-control'
    }))
