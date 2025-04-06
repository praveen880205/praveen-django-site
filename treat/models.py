from django.db import models

class Datas (models.Model):
    Name=models.CharField (max_length=50)
    Address=models.CharField(max_length=50)
    Gmail=models.CharField(max_length=50)
    Phone=models.IntegerField()

    

 

