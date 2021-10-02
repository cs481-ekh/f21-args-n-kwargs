from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class AccountManager(BaseUserManager):
    """Account Manager is the interface that we interact with our Accounts when interacting with the db account"""

    def create_user(self, email, password=None):
        """create_user creates a user account with email and password saving it to the Accounts table
            if email is not specified it will block with a ValueErrror"""
        if not email:
            raise ValueError("Email cannot be empty")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """create_superuser creates a superuser with email and password and sets accounts permissions all to true"""
        user = self.create_user(email=self.normalize_email(email), password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    """Account model that will be stored in db that extends abstractBaseuser and requires email and password
        username will be the users email and will be saved to the Accounts table with default permissions"""
    email = models.EmailField(verbose_name="email", max_length=254, unique=True)

    # to track user status level
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # what we want the user to login in with
    USERNAME_FIELD = 'email'

    # interface we use to interace with this model with the db
    objects = AccountManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["email"]  # how the rows will be ordered
        db_table = "Accounts"
