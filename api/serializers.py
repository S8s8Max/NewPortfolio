from rest_framework import serializers
from Portfolio.models import News, Picture, Product, ProfileImage

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("label", "title", "content", "date", "thumb_nail")

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("title", "picture")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title", "sub_title", "description", "date", "thumb_nail")

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ("title", "image")
