from django.contrib import admin
from .models import Dining, Review, PurposeTag, AtmosphereTag, FacilityTag

# Register your models here.
admin.site.register(Dining)
admin.site.register(Review)
admin.site.register(PurposeTag)
admin.site.register(AtmosphereTag)
admin.site.register(FacilityTag)