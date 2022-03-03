import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Equipment(models.Model):
    """Equipment Model with associated fields to describe a new piece of equipment"""
    student = "student"
    faculty = "faculty"
    guest = "guest"

    Permission = (
        (student, "Student"),
        (faculty, "Faculty"),
        (guest, "Guest"),
    )
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    pi = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, blank=True, null=True)
    center_lab = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    permission = models.CharField(max_length=255, choices=Permission)
    photo = models.ImageField(blank=True, null=True, upload_to="images")

    def __str__(self):
        return f'{self.name}, {self.model}'


class Category(models.Model):
    """Categories that allow improved searches of the equipment based on job characterization of equipment"""
    processing = "Processing"
    structural = "Structural"
    chemical = "Chemical"
    mechanical = "Mechanical"
    electrical = "Electrical"
    thermal = "Thermal"
    other = "Other"

    CATEGORY = (
        (processing, "Processing"),  # A
        (structural, "Structural"),  # B
        (chemical, "Chemical"),  # C
        (mechanical, "Mechanical"),  # D
        (electrical, "Electrical"),  # E
        (thermal, "Thermal"),  # F
        (other, "Other")  # O

    )
    label = models.CharField(max_length=200, null=True, choices=CATEGORY)
    equipment = models.ForeignKey(Equipment, related_name="equipCat", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.label}: {self.equipment.name}'


class Center_Lab(models.Model):
    """Center_Lab that allow improved searches of the equipment based on location of equipment"""
    LOCATION = (
        ("BSCMC", "BSCMC"),
        ("SSL", "SSL"),
        ("MaCS", "MaCS"),
        ("AML (CAES)", "AML (CAES)"),
        ("AML (MSMSE)", "AML (MSMSE)"),
        ("Materials Teaching Lab", "Materials Teaching Lab"),
        ("Keck", "Keck"),
        ("Other MSE Labs", "Other MSE Labs"),
        ("Phys-Chem-Biol-Other", "Phys-Chem-Biol-Other"),
        ("IML", "IML"),

    )
    center_lab_label = models.CharField(max_length=200, null=True, choices=LOCATION)
    equipment = models.ForeignKey(Equipment, related_name="equipment_center_lab", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.center_lab_label}: {self.equipment.name}'
