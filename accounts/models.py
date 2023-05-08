from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


def profile_img_path(instance, filename):
    return f'images/profile/{instance.username}/{filename}'


class User(AbstractUser):
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers')
    profile_image = models.ImageField(blank=True, upload_to=profile_img_path)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
