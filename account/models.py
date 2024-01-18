from django.db import models
from django.contrib.auth.models import User
# Create your models here.
BLOOD_GROUP = {
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
}
class UserBloodGroup(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)
    def __str__(self):
        return str(self.name)

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user_account')
    image = models.ImageField(upload_to= 'account/images/')
    blood_group = models.ForeignKey(UserBloodGroup, on_delete = models.CASCADE, related_name = 'blood_group', blank = True, null = True)
    age = models.CharField(max_length = 2)
    last_donate = models.DateField(blank=True, null=True)
    can_donate = models.BooleanField(default=True)
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    


