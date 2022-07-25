from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models

class LoginSignup(models.Model):
    login_email = models.CharField(max_length = 50)
    login_password = models.CharField(max_length= 50)
    signup_email = models.CharField(max_length=50)
    signup_password = models.CharField(max_length=50)

    



# Create your models here.
