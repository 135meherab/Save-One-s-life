from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView


# Create your views here.


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        form.save()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activation_link = f'https://save-ones-life.onrender.com/user/activate/{uid}/{token}'
        mail_subject = "Varify Account"
        mail_body = render_to_string("verify_account.html",{"user": user, "activation_link": activation_link})
        mail = EmailMultiAlternatives(mail_subject, "", to=[user.email])
        mail.attach_alternative(mail_body, 'text/html')
        mail.send()
        messages.success(self.request, "Account created successfully.Please check your email and verify to active your account")
        return super().form_valid(form)


def activate_account(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User.objects.get(pk = uid)
    except user.DoesNotExist:
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request,'Your account is now active. Please log in')
        return redirect('login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home_page')
    
    def form_valid(self, form):
        messages.success(self.request,'login successful')
        return super().form_valid(form)