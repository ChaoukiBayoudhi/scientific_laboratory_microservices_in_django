from django.utils import timezone
from django.db import models

# Create your models here.
class Exprementation(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField()
    #date=models.DateTimeField(auto_now=True)
    date=models.DateTimeField(default=timezone.now)
    class Meta:
        db_table='exprementations'
        ordering=['-date','name']

class Result(models.Model):
    name=models.CharField(max_length=100)
    result_value=models.DecimalField(decimal_places=5,max_digits=10,null=True,blank=True)
    description=models.TextField()
    exprementation=models.ForeignKey(Exprementation,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        db_table='results'