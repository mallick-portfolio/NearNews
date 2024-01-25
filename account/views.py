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
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from account.models import CustomUser


# Create your views here.

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = CustomUser.objects.get(pk=uid)
    except(CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your email verified successfully!!!. Login now.")
        return redirect('login')
    else:
        return redirect('register')



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
      return redirect('dashboard')
    else:
      messages.error(request,"Your email or password not correct")
      return render(request, './account/login.html')
  else:
    return render(request, './account/login.html')




class UserRegistration(FormView):
  form_class = forms.CustomUserCreationForm
  template_name = './account/register.html'
  success_url = reverse_lazy('home')

  def form_valid(self,form):
    print("form_valid")

    user = form.save()
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    confirm_link = f"http://127.0.0.1:8000/account/active/{uid}/{token}"
    email_subject = "Confirm Your Email"
    data = {}
    data['confirm_link'] = confirm_link
    data['email_subject'] = email_subject
    email_template(user.email, data, 'Verify email address', './email/verify_email.html')
    messages.success(self.request, "Your register successfully!!!. Please check your email to verify!!!")
    return super().form_valid(form)

