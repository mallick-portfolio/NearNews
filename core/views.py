from django.shortcuts import render
from django.views import View
# Create your views here.
from news.models import Post, Category


def home(request, cat_slug=None):
  if cat_slug is not None:
    posts = Post.objects.filter(category__slug=cat_slug)
    print(posts)
  else:
    posts = Post.objects.all()
  categories = Category.objects.all()
  return render(request, './pages/home.html', {"posts": posts, "categories": categories})

