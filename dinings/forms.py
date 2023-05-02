from django import forms
from .models import Dining, Review, Menu


class DiningForm(forms.ModelForm):
    class Meta:
        model = Dining
        fields = '__all__'
        exclude = ['like_users']
        labels = {
            'title':'글 제목',
            'content':'내용',
            'address_mc_do': '주소/행정구역',
            'address_city': '시',
            'address_dong' :'동/읍/면',
            'address_detail' :'상세 주소',
            'opening_hours': '영업 시간',
            'phone_number': '연락처',
            'tags':'태그',
            'menu_tags':'메뉴',
            'price_tags': '가격',
        }




class ReviewForm(forms.ModelForm):
    rating = forms.FloatField(label='평점', widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))
    rating_taste = forms.FloatField(label='맛', widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))
    rating_price = forms.FloatField(label='가격', widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))
    rating_kind = forms.FloatField(label='서비스', widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))

    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['user', 'dining', 'like_users',]
        labels = {
            'content':'내용',
            'purpose_tags':'방문 목적',
            'atmosphere_tags':'분위기',
            'facility_tags': '시설',
        }


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'price',)
        labels = {
            'name':'메뉴명',
            'price':'가격',
        }