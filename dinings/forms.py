from django import forms
from .models import Dining, Review, Menu
from taggit.forms import TagField


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
    # address_mc_do = forms.CharField(
    #     label='주소/행정구역',
    #     label_suffix='', 
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    # address_city = forms.CharField(
    #     label='시',
    #     label_suffix='', 
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    # address_dong = forms.CharField(
    #     label='동/읍/면',
    #     label_suffix='', 
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    # address_detail = forms.CharField(
    #     label='상세 주소',
    #     label_suffix='', 
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
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
    tags = TagField(
        label='태그',
        label_suffix='', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
  
    
    class Meta:
        model = Dining
        fields = ['title', 'content', 'image1', 'image2', 'image3', 'image4', 'image5',  'opening_hours', 'phone_number', 'tags']
        exclude = ['like_users', 'menu_tags', 'price_tags','address_mc_do', 'address_city', 'address_dong', 'address_detail', ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['user', 'dining', 'like_users', 'rating', 'rating_taste', 'rating_price', 'rating_kind', 'purpose_tags', 'atmosphere_tags', 'facility_tags',]
        labels = {
            'content':'방문 후기',
            'purpose_tags':'방문목적',
            'atmosphere_tags':'분위기',
            'facility_tags': '편의시설',
            'image1': '사진1',
            'image2': '사진2',
            'image3': '사진3',
            'image4': '사진4',
            'image5': '사진5',
        }
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '음식, 서비스, 분위기, 위생상태 등의 방문 경험을 적어주세요.',
                }
            ),
            'image1': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image2': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image3': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image4': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image5': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'price',)
        labels = {
            'name':'메뉴명',
            'price':'가격',
        }