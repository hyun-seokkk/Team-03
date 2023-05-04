from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

# Create your models here.
def dining_img_path(instance, filename):
    return f'images/dining/{instance.title}/{filename}'


def review_img_path(instance, filename):
    return f'images/review/{instance.dining}/{instance.user.username}/{filename}'


class PurposeTaggedItem(TaggedItemBase):
    content_object = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='purpose_tagged_items')


class AtmosphereTaggedItem(TaggedItemBase):
    content_object = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='atmosphere_tagged_items')


class FacilityaggedItem(TaggedItemBase):
    content_object = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='facility_tagged_items')


class Dining(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)

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

    image1 = models.ImageField(blank=True, upload_to=review_img_path)
    image2 = models.ImageField(blank=True, upload_to=review_img_path)
    image3 = models.ImageField(blank=True, upload_to=review_img_path)
    image4 = models.ImageField(blank=True, upload_to=review_img_path)
    image5 = models.ImageField(blank=True, upload_to=review_img_path)

    rating = models.FloatField(verbose_name='평점')
    rating_taste = models.FloatField(verbose_name='맛')
    rating_price = models.FloatField(verbose_name='가격')
    rating_kind = models.FloatField(verbose_name='서비스')

    def star_rating(self):
        rounded_rating = round(self.rating * 2) / 2
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    
    def star_rating_taste(self):
        rounded_rating = round(self.rating_taste * 2) / 2
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    
    def star_rating_price(self):
        rounded_rating = round(self.rating_price * 2) / 2
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    
    def star_rating_kind(self):
        rounded_rating = round(self.rating_kind * 2) / 2
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    purpose_tags = TaggableManager(blank=True, through=PurposeTaggedItem, related_name='purpose_tags')
    atmosphere_tags = TaggableManager(blank=True, through=AtmosphereTaggedItem, related_name='atmosphere_tags')
    facility_tags = TaggableManager(blank=True, through=FacilityaggedItem, related_name='facility_tags')


class Menu(models.Model):
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()