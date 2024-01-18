from .models import RequestForBlood
from django import forms
class BloodReqestForm(forms.ModelForm):
    class Meta:
        model = RequestForBlood
        exclude = ['user', 'is_accecpted']

        def __init__(self, *args, **kwargs):
            super(BloodReqestForm, self).__init__(*args, **kwargs)
            self.fields['union'].required = False
            self.fields['post_offce'].required = False

        labels = {
            'village': 'village/Rood No'
        }