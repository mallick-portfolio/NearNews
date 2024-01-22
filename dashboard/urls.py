from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name="profile"),
    path('posts/', views.news_posts, name="dashboard_posts"),
    path('posts/details/<slug:slug>/', views.post_details, name="dashboard_post_detail"),
    path('posts/add/', views.add_post, name="add_post"),
    path('posts/edit/<slug:slug>/', views.edit_post, name="edit_post"),
    path('posts/delete/<slug:slug>/', views.delete_post, name="delete_post"),
    path('users/', views.get_users, name='dashboard_users'),
    path('users/<int:id>/', views.make_admin, name='make_admin')
]
