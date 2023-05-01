from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill


class CustomUserCreationForm(UserCreationForm):
    profile_image = ProcessedImageField(
    spec_id='profile_image_thumbnail',
    processors=[ResizeToFill(70,70)],
    format='JPEG',
    options={'quality' : 90},
    required=False,
    )
    class Meta(UserCreationForm):

        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'first_name','last_name', 'profile_image',)


class CustomUserChangeForm(UserChangeForm):
    profile_image = ProcessedImageField(
    spec_id='profile_image_thumbnail',
    processors=[ResizeToFill(70,70)],
    format='JPEG',
    options={'quality' : 90},
    required=False,
    )
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('username', 'email', 'first_name','last_name', 'profile_image',)