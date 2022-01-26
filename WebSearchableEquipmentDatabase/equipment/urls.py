from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.data_table, name="home"),
    path('filter/', views.filter_data, name="filter_data"),
    path('uploadcsv/', views.upload_csv, name='uploadCSV'),
    path('testing', views.testing, name='testing'),
    path('crud/delete/', views.delete_equipment, name='crud_delete'),
    path('crud/edit', views.get_item_by_id, name='crud_edit'),
    path('crud/create', views.create_equipment, name='crud_create')
]
