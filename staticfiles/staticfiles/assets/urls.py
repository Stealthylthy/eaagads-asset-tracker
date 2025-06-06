from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home/dashboard
    path('add/', views.add_asset, name='add_asset'),
    path('edit/<int:pk>/', views.edit_asset, name='edit_asset'),
    path('maintenance/', views.maintenance_list, name='maintenance'),
    path('register/', views.register, name='register'),
    path('department/<int:department_id>/', views.home, name='department_assets'),
]
