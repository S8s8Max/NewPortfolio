from django.contrib import admin
from .models import Picture, News, Product, ProfileImage

# Register your models here.
admin.site.register(Picture)
admin.site.register(News)
admin.site.register(Product)
admin.site.register(ProfileImage)
