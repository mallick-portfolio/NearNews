from django.urls import path
from . import views
urlpatterns = [
    path("register/", views.UserRegistration.as_view(), name='register'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.user_logout, name='logout'),
]
