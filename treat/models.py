from django.db import models

class Datas (models.Model):
    NAME=models.CharField (max_length=50)
    Address = models.CharField(max_length=255, null=True, blank=True)
    Gmail=models.CharField(max_length=50)
    Phone=models.IntegerField()

    

 

