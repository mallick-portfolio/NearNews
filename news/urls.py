from django.urls import path
from . import views
from core.views import home

urlpatterns = [
    path('<slug:slug>/', views.post_details, name='post_details' ),
    path('category/<slug:cat_slug>/', views.category_post, name='category_post'),
    path('page/category/<slug:cat_slug>/', home, name='filter_post'),

]
