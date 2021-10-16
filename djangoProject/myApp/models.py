from django.db import models

# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=100)
    photo= models.ImageField(upload_to='pics')

class Gist:
    name = models.CharField(max_length=100)
    filetype= models.CharField(max_length=100)
    forks= [User]
    content = models.TextField()
