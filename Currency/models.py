from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TransactionCurrency(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    CURRENCYNAME =  models.CharField(max_length=300,blank=True)
    DESCRIPTION =  models.CharField(max_length=300,blank=True)
    ISO =  models.CharField(max_length=300,blank=True)
    MAXIMUMVALUE =  models.FloatField()
    MINIMUMVALUE =  models.FloatField()
    REMARKS =  models.CharField(max_length=300,blank=True)
    CREATEDBY = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
