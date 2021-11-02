from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_table, name='home'),
    path('uploadcsv/', views.upload_csv, name='uploadCSV'),
    path('testing', views.testing, name='testing'),
    path('ajax/crud/delete/', views.DeleteEquipm.as_view(), name='crud_ajax_delete'),
]
