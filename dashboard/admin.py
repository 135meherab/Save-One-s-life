from django.contrib import admin
from .models import RequestForBlood, DonationHistory
# Register your models here.
class AdminBloodRequest(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'blood_group', 'phone']
    def first_name(self, obj):
        return obj.user.first_name
    def last_name(self, obj):
        return obj.user.last_name
    

class AdminDonationHistory(admin.ModelAdmin):
    list_display = ['doner_name', 'receiver_name', 'donate_date']

    def doner_name(self, obj):
        return obj.doner
    
    def receiver_name(self, obj):
        return obj.receiver
    

admin.site.register(RequestForBlood, AdminBloodRequest)
admin.site.register(DonationHistory, AdminDonationHistory)