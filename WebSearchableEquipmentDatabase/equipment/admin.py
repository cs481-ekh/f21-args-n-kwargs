from django.contrib import admin

from equipment.models import Category, Equipment


class CategoryInline(admin.StackedInline):
    """Creates a class that allows the admin to change category inline with equipment"""
    model = Category


class EquipmentAdmin(admin.ModelAdmin):
    """Uses the inline category class to improve ease of use by admin to edit category with same interface
        as the equipment table"""
    inlines = [
        CategoryInline,
    ]


# registers the equipment model along with the backend admin to manipulate the  model
admin.site.register(Equipment, EquipmentAdmin)
