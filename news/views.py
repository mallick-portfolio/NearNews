from django.shortcuts import render, redirect
from news.models import Post, Category, PostCommentRating
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostCommentForm
from django.db.models import Avg



# Create your views here.
def post_details(request, slug):
  post = get_object_or_404(Post, slug=slug)
  comments = post.comments.all()
  total_rating = 0
  for c in comments:
    total_rating = total_rating + float(c.rating)
  if total_rating:
    avg_rating = round(total_rating / len(comments), 2)
  else:
    avg_rating = 0



  if request.method =="POST":
    form = PostCommentForm(request.POST)
    if form.is_valid():
      obj = form.save(commit=False)
      obj.user = request.user
      obj.post = post
      post.avg_rating = avg_rating
      post.save()
      obj.save()
      messages.success(request, "Comment added successfully")
      form = PostCommentForm()

  else:
    form = PostCommentForm()

  related_post = Post.objects.filter(category=post.category).exclude(id=post.id)[:3]
  return render(request, './pages/post_details.html', {
    "post": post,
    "related_post": related_post,
    "form": form,
    "avg_rating" : avg_rating
  })

def category_post(request, cat_slug=None):
  posts = Post.objects.filter(category__slug=cat_slug).order_by('avg_rating')
  return render(request, './pages/category_post.html', {"posts": posts})




