from django.db import models

# Create your models here.

class User:
    name= models.CharField(max_length=100)
    photo= models.ImageField(upload_to='pics')

class File:
    name = models.CharField(max_length=100)
    content = models.TextField()
    filetype= models.CharField(max_length=100)

class Gist:
    name = models.CharField(max_length=100)
    files = [File]
    forks= [User]
