from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.index),
    path('dataTable/', views.dataTable, name='home'),
    path('uploadcsv/', views.upload_csv, name='uploadCSV'),
]
