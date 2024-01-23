from django.shortcuts import render
from account.models import UserAccount, UserBloodGroup
from datetime import datetime, timedelta
def home_page(request):
    return render(request, 'home.html')

def donners(request):
    all_data = UserAccount.objects.all()
    today_date = datetime.now().date()
    min_day = timedelta(days=90)
    return render(request, 'donners.html', {'all_data': all_data, 'today_date': today_date, 'min_day': min_day})