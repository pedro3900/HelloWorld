from django.db import models

# Create your models here.
class HelloWorld(models.Model):
    string = models.CharField(max_length=255)
