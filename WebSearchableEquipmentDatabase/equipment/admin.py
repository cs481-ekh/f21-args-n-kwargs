from django.contrib import admin

from equipment.models import Category, Equipment


# registers the equipment model along with the backend admin to manipulate the  model
admin.site.register(Equipment)
admin.site.register(Category)
