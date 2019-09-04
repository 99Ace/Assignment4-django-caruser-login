from django.db import models

# Create your models here.
class Vehicle(models.Model):
    """ CAR PLATE WILL BE THE REFERENCE ID FOR DELETION"""
    carplate = models.CharField(max_length=8)
    
    """ PREFIX INPUT FOR 4 TYPES OF MAKE AVAILABLE FOR ENTRY"""
    CAR_MAKE = [
        ('AUD','Audi'),
        ('BMW','BMW'),
        ('MER','Mercedes-Benz'),
        ('VOL','Volvo'),
    ]
    car_make = models.CharField(
        max_length=3,
        choices=CAR_MAKE,
        default='AUD',
    )
    """ FIELD TO LET USER ENTER THE CAR MODEL """
    car_model = models.CharField(max_length=30)
    
    """ PREFIX SELECTION FOR USER TO ASSIGN THE CAR TYPE TO THE CAR ENTERED """
    CAR_TYPE = [
        ('LUXSEDAN',"Luxury Sedan"),                    
        ('HATCHBACK',"Hatchback"),
        ('SUV', 'SUV'),
        ('MPV',"MPV"),
        ('SPORT',"Sports"),
        ('SWAGON',"Stationwagon"),
        ('HYBRID',"Hybrid")
    ]
    car_type = models.CharField(
        max_length=10,
        choices=CAR_TYPE,
        default='LUXSEDAN',
    )
    """ PREFIX SELECTION FOR YEAR OF MANUFACTURE FOR THE CAR - LIMIT SET TO 10YEAR FOR PROJECT PURPOSE """
    YOM = [
        (2009,'2009'),
        (2010,'2010'),
        (2011,'2011'),
        (2012,'2012'),
        (2013,'2013'),
        (2014,'2014'),
        (2015,'2015'),
        (2016,'2016'),
        (2017,'2017'),
        (2018,'2018'),
        (2019,'2019'),
    ]
    year_of_make = models.IntegerField(
        choices = YOM,
        default = '2009'
    )
    """ FOR USER TO ENTER THE LISTED PRICE AND MILEAGE OF THE CAR """
    price = models.IntegerField()
    mileage = models.IntegerField()
    
    """ FOR USER TO ENTER SOME MARKETING LINER FOR THEIR LISTED CAR """
    description = models.TextField(max_length = 255)
    
    """ PREFIX THE NEW ENTRY AS AVAILABLE """
    STATUS = [
        (True, 'Available'),
        (False, 'Sold'),
    ]
    status = models.BooleanField(
        choices = STATUS,
        default= True
    )
    
    """ AUTO ADD THE CREATION DATE """
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (self.carplate)
    

