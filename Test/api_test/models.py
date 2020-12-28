from django.db import models
import datetime

# Create your models here.
class TestAPI(models.Model):
  ticker = models.CharField(max_length=20, blank=False, default='')
  day = models.DateField(default=datetime.date.today, null=True, blank=True)
  price = models.FloatField(default=0)
  