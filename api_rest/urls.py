
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.get_users, name='get_all_users'),
    path('user/<str:nick>', views.get_by_nick), 
    path('data', views.user_manager),
    path('new_user', views.new_user),
    path('edit_user', views.edit_user),
    path('delete_user', views.delete_user),
]
