from django.db import models

# Create your models here.
class Articles(models.Model):
    article_heading = models.CharField(max_length = 50 , blank=True)
    article_title = models.CharField(max_length= 50,blank=True)
    article_des = models.TextField(blank=True)
    article_image = models.FileField(upload_to="articles/",max_length=250,null=True,default=None,blank=True)