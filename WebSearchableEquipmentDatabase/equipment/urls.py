from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_table, name='home'),
    path('uploadcsv/', views.upload_csv, name='uploadCSV'),
    path('testing', views.testing, name='testing'),
    path('crud/delete/', views.delete_equipment, name='crud_delete'),
]
