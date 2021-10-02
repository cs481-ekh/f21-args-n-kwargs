from django.contrib.auth.forms import UserCreationForm
from .models import Account


class AccountCreationForm(UserCreationForm):
    """Account creation extends UserCreationForm to create a form based on the definition of our account model"""
    class Meta:
        model = Account
        fields = ['email', 'password1', 'password2']
