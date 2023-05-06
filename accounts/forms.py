from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('username', 'email', 'phonenumber', 'first_name',
                  'last_name', 'profile_image',)
        label_suffix = ''

    username = forms.CharField(label='ID', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='이메일', label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    phonenumber = forms.CharField(label='전화번호', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='이름', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='성', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='비밀번호', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='비밀번호 확인', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    profile_image = ProcessedImageField(
        spec_id='profile_image_thumbnail',
        processors=[ResizeToFill(70, 70)],
        format='JPEG',
        options={'quality': 90},
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        label='프로필 이미지',
        label_suffix='',
    )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('profile_image' , 'username', 'email', 'phonenumber' , )
        label_suffix = ''

    username = forms.CharField(label='ID', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='이메일', label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    phonenumber = forms.CharField(label='전화번호', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    profile_image = ProcessedImageField(
        spec_id='profile_image_thumbnail',
        processors=[ResizeToFill(70, 70)],
        format='JPEG',
        options={'quality': 90},
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        label='프로필 이미지',
        label_suffix='',
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2',)
      
    old_password = forms.CharField(label='기존 비밀번호', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    new_password1 = forms.CharField(label='새 비밀번호', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    new_password2 = forms.CharField(label='새 비밀번호 확인', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))