from django.shortcuts import render
from django.views import View
# Create your views here.
from news.models import Post, Category


def home(request, cat_slug=None):
  if cat_slug is not None:
    posts = Post.objects.filter(category__slug=cat_slug)
  else:
    posts = Post.objects.all()[:6]
  slider_post = Post.objects.all()[:5]
  latest = Post.objects.filter(category__slug='latest')[:3]
  entertainment = Post.objects.filter(category__slug='entertainment')[:3]
  categories = Category.objects.all()
  return render(request, './pages/home.html', {
    "posts": posts,
    "categories": categories,
    "slider_post" : slider_post,
    "latest" :latest,
    "entertainment" :entertainment,
    })

def contact(request):
  return render(request, './pages/contact.html')