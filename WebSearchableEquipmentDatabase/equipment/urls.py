from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.index),
    path('datatable/', views.data_table, name='home'),
    path('uploadcsv/', views.upload_csv, name='uploadCSV'),
]
