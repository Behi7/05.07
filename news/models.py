from django.db import models

class Head_news(models.Model):
    img_news = models.ImageField()
    text = models.CharField(max_length=255)

class Popular_post(models.Model):
    img_post = models.ImageField()
    info = models.TextField()
    time = models.DateTimeField()

class Comment(models.Model):
    text = models.TextField()
    user = models.CharField(max_length=255)
    user_img = models.ImageField()
    time = models.DateField()

class News_all(models.Model):
    like = models.IntegerField()
    title = models.CharField(max_length=233)
    info = models.TextField()
    img_post = models.ImageField()
    time = models.DateField()

class Mini_news(models.Model):
    img = models.ImageField()
    txt = models.CharField(max_length=244)
