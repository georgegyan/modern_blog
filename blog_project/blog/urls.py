from django.urls import path
from .views import dashboard, post_list, post_create, post_edit, post_delete, register, user_login, user_logout, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('posts/', post_list, name='post_list'),
    path('posts/create/', post_create, name='post_create'),
    path('posts/edit/<int:post_id>/', post_edit, name='post_edit'),
    path('posts/delete/<int:post_id>/', post_delete, name='post_delete'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
]
