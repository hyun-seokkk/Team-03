from django import forms
from .models import Dining, Review


class DiningForm(forms.ModelForm):
    class Meta:
        model = Dining
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'