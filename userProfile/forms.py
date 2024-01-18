from account.models import UserAccount
from django import forms

class UpdateForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['age', 'city', 'country', 'last_donate']

        widgets ={
            'last_donate': forms.DateInput(attrs={"type": "date"})
        }