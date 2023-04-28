from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.
def dining_img_path(instance, filename):
    return f'images/{instance.title}/{filename}'

class Dining(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)

    # 이미지는 5개까지 업로드 가능하게
    image1 = models.ImageField(blank=True, upload_to=dining_img_path)
    image2 = models.ImageField(blank=True, upload_to=dining_img_path)
    image3 = models.ImageField(blank=True, upload_to=dining_img_path)
    image4 = models.ImageField(blank=True, upload_to=dining_img_path)
    image5 = models.ImageField(blank=True, upload_to=dining_img_path)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_dinings")
    address_mc_do = models.CharField(max_length=20)
    address_city = models.CharField(max_length=20)
    address_dong = models.CharField(max_length=20)
    address_detail = models.CharField(max_length=20)
    opening_hours = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True)
    
    tags = TaggableManager(blank=True)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE)

    content = models.TextField(null=True)

    # 이미지는 5개까지 업로드 가능하게
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)

    rating = models.FloatField()

    def half_star_rating(self):
        # 반올림한 별점 값을 구함
        rounded_rating = round(self.rating * 2) / 2

        # 별점 반개 문자열을 반환
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")