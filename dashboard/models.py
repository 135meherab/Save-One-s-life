from django.db import models
from django.contrib.auth.models import User
from account.models import UserBloodGroup
# Create your models here.
class RequestForBlood(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    phone = models.CharField(max_length=14)
    blood_group = models.ForeignKey(UserBloodGroup, on_delete = models.CASCADE)
    village = models.CharField(max_length=100)
    union = models.CharField(max_length=100, blank=True, null=True)
    psot_office = models.CharField(max_length=100, blank=True, null=True)
    Upazila = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=200)
    is_accecpted = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.blood_group.name}"
    

class DonationHistory(models.Model):
    doner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='doner')
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name='receiver')
    canceled = models.BooleanField(default=False, null=True,blank=True)
    donation_done = models.BooleanField(default=False, null=True, blank=True)
    donate_date = models.DateField(auto_now_add=True)