import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def max_value_current_year(value):
    """small helper function to set max year allowed for equipment also together
        allow validators on year field to be callable"""
    return 3000


# Create your models here.
class Equipment(models.Model):
    """Equipment Model with associated fields to describe a new piece of equipment"""
    Permission = (
        ("Student", "Student"),
        ("Faculty", "Faculty"),
        ("Guest", "Guest"),
    )
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    year = models.IntegerField('year', validators=[MinValueValidator(1950), max_value_current_year])
    pi = models.CharField(max_length=255)
    contact = models.TextField(blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    lab = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    permission = models.CharField(max_length=255, choices=Permission)

    def __str__(self):
        return f'{self.name}, {self.model}'
