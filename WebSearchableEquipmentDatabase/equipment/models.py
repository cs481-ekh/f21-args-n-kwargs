import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    year = models.IntegerField('year', validators=[MinValueValidator(1950), MaxValueValidator(3000)])
    pi = models.CharField(max_length=255)
    contact = models.TextField(blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    lab = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    permission = models.CharField(max_length=255, choices=Permission)

    def __str__(self):
        return f'{self.name}, {self.model}'


class Category(models.Model):
    """Categories that allow improved searches of the equipment based on job characterization of equipment"""
    CATEGORY = (
        ("Processing", "Processing"),
        ("Structural", "Structural"),
        ("Chemical", "Chemical"),
        ("Mechanical", "Mechanical"),
        ("Electrical", "Electrical"),
        ("Thermal", "Thermal"),
        ("Other", "Other")

    )
    label = models.CharField(max_length=200, null=True, choices=CATEGORY)
    equipment = models.ForeignKey(Equipment, related_name="equipCat", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.label}: {self.equipment.name}'
