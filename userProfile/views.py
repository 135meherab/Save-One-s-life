from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import UpdateView, DetailView
from .forms import UpdateForm
from account.models import UserAccount
from datetime import datetime, timedelta
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# Create your views here.


class ProfileView(LoginRequiredMixin,DetailView):
    model = UserAccount
    template_name = 'profile.html'

    def get_object(self, queryset = None):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_account = UserAccount.objects.get(user = self.request.user)
        last_donate_date = user_account.last_donate
        today_date = datetime.now().date()
        if last_donate_date is not None:
            difference = today_date - last_donate_date
            if  difference >= timedelta(days=90):
                user_account.can_donate = True
            else:
                user_account.can_donate = False
        user_account.save()
        context["user_account"] = user_account
        return context
    

class UserUpdateView(LoginRequiredMixin,UpdateView):
    form_class = UpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset = None):
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user_account = UserAccount.objects.get(user = self.request.user)
        form.fields['age'].initial = user_account.age
        form.fields['city'].initial = user_account.city
        form.fields['country'].initial = user_account.country
        form.fields['last_donate'].initial = user_account.last_donate
        return form

    def form_valid(self, form):
        user_account = UserAccount.objects.get(user = self.request.user)
        user_account.age = form.cleaned_data['age']
        user_account.city = form.cleaned_data['city']
        user_account.country = form.cleaned_data['country']
        user_account.last_donate = form.cleaned_data['last_donate']

        last_donate_date = form.cleaned_data['last_donate']
        today_date = datetime.now().date()
        if last_donate_date is not None:
            difference = today_date - last_donate_date
            if  difference >= timedelta(days=90):
                user_account.can_donate = True
            else:
                user_account.can_donate = False

        user_account.save()
        messages.success(self.request,"Profile updated successfully")
        return super().form_valid(form)