from django.shortcuts import render
from django.views import View
# Create your views here.
from news.models import Post, Category


def home(request):
  posts = Post.objects.all()
  categories = Category.objects.all()
  return render(request, './pages/home.html', {"posts": posts, "categories": categories})