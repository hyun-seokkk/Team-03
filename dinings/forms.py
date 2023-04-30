from django import forms
from .models import Dining, Review


class DiningForm(forms.ModelForm):
    class Meta:
        model = Dining
        fields = '__all__'
        exclude = ['like_users']


class ReviewForm(forms.ModelForm):
    rating = forms.FloatField(widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))
    rating_taste = forms.FloatField(widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))
    rating_price = forms.FloatField(widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))
    rating_kind = forms.FloatField(widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))

    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['user', 'dining', 'like_users',]
