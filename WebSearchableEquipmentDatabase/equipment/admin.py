from abc import ABC

from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from equipment.models import Category, Equipment, Location


class CategoryInline(admin.StackedInline):
    """Creates a class that allows the admin to change category inline with equipment"""
    model = Category


class LocationInline(admin.StackedInline):
    """Creates a class that allows the admin to change location inline with equipment"""
    model = Location


class CategoryFilter(SimpleListFilter):
    title = "Category"
    parameter_name = "category_label"

    def lookups(self, request, model_admin):
        return (
            ("Processing", "Processing"),
            ("Structural", "Structural"),
            ("Chemical", "Chemical"),
            ("Mechanical", "Mechanical"),
            ("Electrical", "Electrical"),
            ("Thermal", "Thermal"),
            ("Other", "Other")

        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'processing':
            return queryset.filter(equipCat__label__contains='processing')
        if self.value().lower() == 'structural':
            return queryset.filter(equipCat__label__contains='structural')
        if self.value().lower() == 'chemical':
            return queryset.filter(equipCat__label__contains='chemical')
        if self.value().lower() == 'mechanical':
            return queryset.filter(equipCat__label__contains='mechanical')
        if self.value().lower() == 'electrical':
            return queryset.filter(equipCat__label__contains='electrical')
        if self.value().lower() == 'thermal':
            return queryset.filter(equipCat__label__contains='thermal')
        if self.value().lower() == 'other':
            return queryset.filter(equipCat__label__contains='other')


class LocationFilter(SimpleListFilter):
    title = "Location"
    parameter_name = "location__location_label"

    def lookups(self, request, model_admin):
        return (
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

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'bscmc':
            return queryset.filter(equipment_location__location_label__contains='bscmc')
        if self.value().lower() == 'ssl':
            return queryset.filter(equipment_location__location_label__contains='ssl')
        if self.value().lower() == 'macs':
            return queryset.filter(equipment_location__location_label__contains='macs')
        if self.value().lower() == 'aml (caes)':
            return queryset.filter(equipment_location__location_label__contains='aml (caes)')
        if self.value().lower() == 'aml (msme)':
            return queryset.filter(equipment_location__location_label__contains='aml (msme)')
        if self.value().lower() == 'materials teaching lab':
            return queryset.filter(equipment_location__location_label__contains='materials teaching lab')
        if self.value().lower() == 'keck':
            return queryset.filter(equipment_location__location_label__contains='keck')
        if self.value().lower() == 'other mse labs':
            return queryset.filter(equipment_location__location_label__contains='other mse labs')
        if self.value().lower() == 'phys-chem-biol-other':
            return queryset.filter(equipment_location__location_label__contains='phys-chem-biol-other')
        if self.value().lower() == 'iml':
            return queryset.filter(equipment_location__location_label__contains='iml')

class EquipmentAdmin(admin.ModelAdmin):
    """Uses the inline category class to improve ease of use by admin to edit category with same interface
        as the equipment table"""
    list_display = ('name', 'model', 'manufacturer', 'year',)
    list_filter = ('name', 'model', 'manufacturer', 'permission', CategoryFilter, LocationFilter)
    inlines = [
        CategoryInline,
        LocationInline
    ]


# registers the equipment model along with the backend admin to manipulate the  model
admin.site.register(Equipment, EquipmentAdmin)
