from django import forms
from .models import Dining


class DiningForm(forms.ModelForm):
    class Meta:
        model = Dining
        fields = '__all__'
        exclude = ['like_users']
