from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.html import format_html
from django import forms


class CustomTextInput(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        attrs.setdefault('class', '')
        attrs['class'] += ' custom-text-input'
        html = super().render(name, value, attrs, renderer)
        if self.attrs.get('help_text'):
            html += format_html('<p class="help_text">{}</p>', self.attrs['help_text'])
        else:
            html += '<p class="help_text"></p>'
        return html
    
    
class CustomPasswordInput(forms.PasswordInput):
    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        attrs.setdefault('class', '')
        attrs['class'] += ' custom-text-input'
        html = super().render(name, value, attrs, renderer)
        if self.attrs.get('help_text'):
            html += format_html('<p class="help_text">{}</p>', self.attrs['help_text'])
        else:
            html += '<p class="help_text"></p>'
        return html
    

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='ID',
        widget=CustomTextInput(attrs={'placeholder': '',
                                      'help_text': '사용자 이름은 고유해야하며 문자, 숫자 및 @/./+/-/_ 문자를 포함할 수 있습니다.'})
    )
    email = forms.EmailField(
        label='이메일',
        widget=CustomTextInput(attrs={'placeholder': '',
                                      'help_text': ''})
    )
    password1 = forms.CharField(
        label='비밀번호',
        strip=False,
        widget=CustomPasswordInput(attrs={'placeholder': ''}),
        help_text='비밀번호는 최소 8자 이상이어야하며, 숫자만으로 구성될 수 없습니다.'
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        strip=False,
        widget=CustomPasswordInput(attrs={'placeholder': ''}),
        help_text='비밀번호를 다시 입력하세요.'
    )
    first_name = forms.CharField(
        label='이름',
        max_length=30,
        required=True,
        widget=CustomTextInput(attrs={'placeholder': ''})
    )
    last_name = forms.CharField(
        label='성',
        max_length=30,
        required=True,
        widget=CustomTextInput(attrs={'placeholder': ''})
    )
    profile_image = ProcessedImageField(
        spec_id='profile_image_thumbnail',
        processors=[ResizeToFill(70, 70)],
        format='JPEG',
        options={'quality': 90},
        required=False,
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name', 'profile_image',)


class CustomUserChangeForm(UserChangeForm):
    profile_image = ProcessedImageField(
        spec_id='profile_image_thumbnail',
        processors=[ResizeToFill(70, 70)],
        format='JPEG',
        options={'quality': 90},
        required=False,
    )

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('username', 'email', 'first_name',
                  'last_name', 'profile_image',)
