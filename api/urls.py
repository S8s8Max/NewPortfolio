from django.urls import path
from .views import NewsAPIView
from .views import PictureAPIView
from .views import ProductAPIView
from .views import ProfileImageAPIView

urlpatterns = [
    path("news/", NewsAPIView.as_view()),
    path("picture/", PictureAPIView.as_view()),
    path("product/", ProductAPIView.as_view()),
    path("profileimage/", ProfileImageAPIView.as_view()),
]
