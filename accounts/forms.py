from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):

        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'first_name','last_name',)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('username', 'email', 'first_name','last_name',)
 