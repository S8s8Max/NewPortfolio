from django.db import models

# Create your models here.
class Picture(models.Model):

    class Meta(object):
        db_table = "picture"

    picture = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class News(models.Model):

    class Meta:
        db_table = "news"

    label = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    thumb_nail = models.ImageField(upload_to="thumb_nails")

    def __str__(self):
        name = str(self.date) + "[" + str(self.title[7]) + "...]"
        return name



class Product(models.Model):

    class Meta:
        db_table = "product"

    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    thumb_nail = models.ImageField(upload_to="products")

    def __str__(self):
        return self.title


class ProfileImage(models.Model):

    class Meta:
        db_table = "profileimage"

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="profile")

    def __str__(self):
        return self.title

