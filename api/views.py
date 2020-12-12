from django.shortcuts import render
from rest_framework import generics

from Portfolio.models import News, Picture, Product, ProfileImage
from .serializers import NewsSerializer, PictureSerializer, ProductSerializer, ProfileImageSerializer


class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class PictureAPIView(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProfileImageAPIView(generics.ListAPIView):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer
