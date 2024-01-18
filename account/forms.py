from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccount, UserBloodGroup
from django.core.files.images import ImageFile

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

class RegisterForm(UserCreationForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(), required=True)
    blood_group = forms.ChoiceField(choices = BLOOD_GROUP, required=True)
    age = forms.CharField(max_length = 2, required=True)
    city = forms.CharField(max_length=25, required=True)
    country = forms.CharField(max_length=25, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'image', 'age', 'blood_group', 'city', 'country', 'email']
    
    def save(self, commit =True):
        current_user =  super().save(commit = False)
        if commit:
            current_user.save()
            age = self.cleaned_data['age']
            blood_group = UserBloodGroup.objects.get(name = self.cleaned_data['blood_group'])
            city = self.cleaned_data['city']
            country = self.cleaned_data['country']
            image = self.cleaned_data['image']

            user_account =UserAccount.objects.create(
                user = current_user,
                age = age,
                blood_group = blood_group,
                city = city,
                country = country,
                image = image.name
            )
            user_account.image.save(image.name, ImageFile(image))
        return current_user