from django.db import models

# Create your models here.

class Profile(models.Model):
    username        =  models.CharField(max_length=50, blank=False)
    firstname       =  models.CharField(max_length=70, blank=False)
    lastname        = models.CharField(max_length=70, blank=False)
    contact_number  = models.IntegerField()
