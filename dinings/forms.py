from django import forms
from .models import Dining, Review, Menu


class DiningForm(forms.ModelForm):
    title = forms.CharField(
        label='글 제목', 
        label_suffix='', 
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    content = forms.CharField(
        label='내용',
        label_suffix='', 
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    image1 = forms.ImageField(
    required=False,
    label='사진 1',
    label_suffix='',
    widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    image2 = forms.ImageField(
        required=False,
        label='사진 2',
        label_suffix='',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    image3 = forms.ImageField(
        required=False,
        label='사진 3',
        label_suffix='',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    image4 = forms.ImageField(
        required=False,
        label='사진 4',
        label_suffix='',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    image5 = forms.ImageField(
        required=False,
        label='사진 5',
        label_suffix='',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    address_mc_do = forms.CharField(
        label='주소/행정구역',
        label_suffix='', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_city = forms.CharField(
        label='시',
        label_suffix='', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_dong = forms.CharField(
        label='동/읍/면',
        label_suffix='', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_detail = forms.CharField(
        label='상세 주소',
        label_suffix='', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    opening_hours = forms.CharField(
        label='영업 시간',
        label_suffix='', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        label='연락처',
        label_suffix='', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tags = forms.CharField(
        label='태그',
        label_suffix='', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    # menu_tags = forms.CharField(
    #     label='메뉴',
    #     label_suffix='', 
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    # price_tags = forms.CharField(
    #     label='가격',
    #     label_suffix='', 
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    
    class Meta:
        model = Dining
        fields = ['title', 'content', 'image1', 'image2', 'image3', 'image4', 'image5', 
              'address_mc_do', 'address_city', 'address_dong', 'address_detail', 
              'opening_hours', 'phone_number', 'tags']
        exclude = ['like_users', 'menu_tags', 'price_tags']


class ReviewForm(forms.ModelForm):
    # rating = forms.FloatField(label='평점', widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))
    rating_taste = forms.FloatField(label='맛', widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))
    rating_price = forms.FloatField(label='가격', widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))
    rating_kind = forms.FloatField(label='서비스', widget=forms.NumberInput(attrs={'step': 0.5, 'min':0, 'max':5}))
    
    content = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'style': 'width:50%',
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['user', 'dining', 'like_users', 'rating',]
        labels = {
            'content':'방문 후기',
            'purpose_tags':'방문목적',
            'atmosphere_tags':'분위기',
            'facility_tags': '편의시설',
        }


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'price',)
        labels = {
            'name':'메뉴명',
            'price':'가격',
        }