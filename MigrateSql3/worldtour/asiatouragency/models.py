from django.db import models

# Create your models here.
class Tour(models.Model):
    #origin country , destination ,number of nights,price:
    origin_country = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()
