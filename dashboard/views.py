from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from news.models import Post
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from account.models import CustomUser

# Create your views here.
@login_required
def dashboard(request):
  return render(request, './dashboard/layout.html')


@login_required
def profile(request):
  return render(request, './dashboard/profile.html')

@login_required
def news_posts(request):
  posts = Post.objects.all()
  return render(request, './dashboard/posts.html', {"posts": posts})

@login_required
def post_details(request, slug):
  post = get_object_or_404(Post, slug=slug)
  return render(request, './dashboard/post_details.html', {"post": post})


@login_required
def add_post(request):
  print(request.user)
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      obj = form.save(commit=False)
      obj.author = request.user
      obj.save()
      messages.success(request,"Post added successfully")
      return redirect('dashboard_posts')
    else:
      return render(request, './dashboard/add_post.html', {"form": form})
  else:
    form = PostForm()
  return render(request, './dashboard/add_post.html', {"form": form})


@login_required
def edit_post(request, slug):
  post = get_object_or_404(Post, slug=slug)
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      obj = form.save(commit=False)
      obj.author = request.user
      obj.save()
      messages.success(request,"Post updated successfully")
      return redirect('dashboard_posts')
    else:
      return render(request, './dashboard/add_post.html', {"form": form})
  else:
    form = PostForm(instance=post)
  return render(request, './dashboard/add_post.html', {"form": form})

def delete_post(request, slug):
  post = get_object_or_404(Post, slug=slug)
  post.delete()
  messages.success(request, "Post deleted successfully!!!")
  return redirect('dashboard_posts')


# user list
@login_required
def get_users(request):
  users = CustomUser.objects.all()
  return render(request, './dashboard/users.html', {"users": users})

# user list
@login_required
def make_admin(request, id):
  user = get_object_or_404(CustomUser, id=id)
  user.is_staff = True
  user.save()
  return redirect('dashboard_users')
