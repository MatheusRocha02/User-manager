from django.urls import path
from .views_html import user_list_view, user_create_view, user_edit_view, user_delete_view

urlpatterns = [
    path('users/', user_list_view, name='user_list_view'), # 1- endpoint que defini 2- qual view que será chamada ao acessar esse endpoint 3- nome da view (que será usada nos forms HTML)
    path('users/create/', user_create_view, name='user_create_view'),
      path('users/edit/<str:nickname>/', user_edit_view, name='user_edit_view'),
    path('users/delete/<str:nickname>/', user_delete_view, name='user_delete_view'),
]

