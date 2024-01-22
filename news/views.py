from django.shortcuts import render, redirect
from news.models import Post, Category
from django.shortcuts import get_object_or_404

# Create your views here.
def post_details(request, slug):
  post = get_object_or_404(Post, slug=slug)
  related_post = Post.objects.filter(category=post.category).exclude(id=post.id)[:3]
  return render(request, './pages/post_details.html', {
    "post": post,
    "related_post": related_post
  })