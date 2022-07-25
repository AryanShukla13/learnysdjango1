from django.db import models

class Cards(models.Model):
    cards_heading = models.CharField(max_length=50)
    cards_title = models.CharField(max_length=50)
    cards_des = models.TextField()
    cards_link = models.CharField(max_length=50,default='/articles1.html')
    cards_image = models.FileField(upload_to="cards/",max_length=250,null=True,default=None)
    
    # cards_date = models.DateField()




# Create your models here.
