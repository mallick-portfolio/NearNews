from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . import forms
from account import models
from account.helpers import email_template
from django.contrib.auth.decorators import login_required

# Create your views here.



def user_logout(request):
  logout(request)
  messages.success(request, "Logout successfully!!!")
  return redirect('login')


def login_user(request):
  if request.method == "POST":
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)
    if user is not None:
      print(user)
      login(request, user)
      messages.success(request, "User login successfull!!!")
      return redirect('home')
    else:
      messages.error(request,"Your email or password not correct")
      return render(request, './accounts/login.html')
  else:
    return render(request, './accounts/login.html')




class UserRegistration(FormView):
  form_class = forms.CustomUserCreationForm
  template_name = './account/register.html'
  success_url = reverse_lazy('home')

  def form_valid(self,form):

    user = form.save()
    messages.success(self.request, "Your register successfully!!!")
    return super().form_valid(form)
