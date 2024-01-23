from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import RequestForBlood, DonationHistory
from .forms import BloodReqestForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from account.models import UserAccount, UserBloodGroup
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

@login_required()
def dashboard(request, blood_slug=None):
    blood = UserBloodGroup.objects.all()
    all_requests = RequestForBlood.objects.all()
    if blood_slug is not None:
        blood_name = UserBloodGroup.objects.get(slug = blood_slug)
        all_requests = RequestForBlood.objects.filter(blood_group = blood_name)
     
    return render(request, 'dashboard.html', {'all_request': all_requests, 'user': request.user, 'blood_groups': blood})


class BloodRequestView(LoginRequiredMixin,CreateView):
    model = RequestForBlood
    form_class = BloodReqestForm
    template_name = 'blood_request.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    


@login_required()  
def Accept(request,id):
    user_request = RequestForBlood.objects.get(id = id)
    current_object = DonationHistory.objects.create(
        doner = request.user,
        receiver = user_request.user
    )
    
    user_request.is_accecpted = True
    user_request.save()
    
    return redirect('dashboard')

@login_required()
def DonateHistory(request):
    all_data = DonationHistory.objects.filter(doner = request.user)
    return render(request, 'donation_history.html', {'all_data': all_data})

@login_required()
def donation_done(request, id):
    request_object = DonationHistory.objects.get(id = id)
    request_object.donation_done = True
    request_object.save()
    user_account = UserAccount.objects.get(user = request_object.doner)
    user_account.last_donate = request_object.donate_date
    user_account.save()
    return redirect('donation_history')

@login_required()
def donation_cancel(request, id):
    request_object = DonationHistory.objects.get(id = id)
    request_object.canceled = True
    request_object.save()
    return redirect('donation_history')
