from django.db import models

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=64,null=True,blank=True)
    auther = models.CharField(max_length=64,null=True,blank=True)
    Publishs = models.ForeignKey(to='Publishs')
class Publishs(models.Model):
    name = models.CharField(max_length=64,null=True,blank=True)