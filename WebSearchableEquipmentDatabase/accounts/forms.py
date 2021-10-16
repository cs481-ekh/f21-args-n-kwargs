from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Account
from django import forms


class AccountCreationForm(UserCreationForm):
    email = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email address'})
    )

    password1 = forms.CharField(
        label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
    )

    """Account creation extends UserCreationForm to create a form based on the definition of our account model"""

    class Meta(UserCreationForm):
        model = Account
        fields = ('email', 'password1', 'password2')
