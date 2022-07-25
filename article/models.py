from django.db import models
class Article(models.Model):
    article_icon = models.CharField(max_length = 100)
    article_title = models.CharField(max_length=100)
    article_des = models.TextField()
# Create your models here.
