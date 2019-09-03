from django.db import models

# Create your models here.
class CarDetail(models.Model):
    car_plate = models.CharField(max_length = 8, blank=False)
    car_make = models.CharField (max_length = 30, blank=False)
    year_of_make = models.IntegerField (blank=False)
    car_price = models.IntegerField (blank=False)
    mileage = models.IntegerField ()
    description = models.CharField (max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    availablility = models.CharField (max_length = 10)
    def __str__(self):
        return self.car_plate