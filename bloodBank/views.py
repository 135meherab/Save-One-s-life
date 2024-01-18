from django.shortcuts import render
from account.models import UserAccount, UserBloodGroup

def home_page(request, blood_slug=None):
    blood = UserBloodGroup.objects.all()
    all_data = UserAccount.objects.filter(can_donate=True)
    if blood_slug is not None:
        blood_name = UserBloodGroup.objects.get(slug = blood_slug)
        all_data = UserAccount.objects.filter(can_donate=True, blood_group = blood_name)
    return render(request, 'home.html', {'all_data': all_data, 'blood_groups': blood})