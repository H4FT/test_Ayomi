from django.db import models

# Create your models here.

class Identif(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)