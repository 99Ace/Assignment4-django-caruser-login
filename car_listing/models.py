from django.db import models
from pyuploadcare.dj.models import ImageField
from accounts.models import MyUser

# Create your models here.
class Vehicle(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE,
        null= False,
        blank = False
        )
    
    """ CAR PLATE WILL BE THE REFERENCE ID FOR DELETION"""
    carplate = models.CharField(
        max_length=8,
        blank=False
    )
    
    """ PREFIX INPUT FOR 4 TYPES OF MAKE AVAILABLE FOR ENTRY"""
    CAR_MAKE = [
        ('Audi','Audi'),
        ('BMW','BMW'),
        ('Mercedes-Benz','Mercedes-Benz'),
        ('Volvo','Volvo'),
    ]
    car_make = models.CharField(
        max_length=15,
        choices=CAR_MAKE,
        default='Audi',
        blank=False
    )
    """ FIELD TO LET USER ENTER THE CAR MODEL """
    car_model = models.CharField(max_length=30)
    
    """ PREFIX SELECTION FOR USER TO ASSIGN THE CAR TYPE TO THE CAR ENTERED """
    CAR_TYPE = [
        ('Luxury Sedan',"Luxury Sedan"),                    
        ('Hatchback',"Hatchback"),
        ('SUV', 'SUV'),
        ('MPV',"MPV"),
        ('Sports',"Sports"),
        ('Stationwagon',"Stationwagon"),
        ('Hybrid',"Hybrid")
    ]
    car_type = models.CharField(
        max_length=15,
        choices=CAR_TYPE,
        default='Luxury Sedan',
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
    price = models.IntegerField(
         blank=False
         )
    mileage = models.IntegerField()
    
    """ FOR USER TO ENTER SOME MARKETING LINER FOR THEIR LISTED CAR """
    description = models.TextField(max_length = 255)
    
    """ PREFIX THE NEW ENTRY AS AVAILABLE """
    STATUS = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
    ]
    status = models.CharField(
        max_length = 10,
        choices = STATUS,
        default= 'Available'
    )
    
    # ALLOW USER TO UPLOAD PICTURE TO SHOW THE CAR - (Limit to 1 pic for this project)
    image = ImageField(null=True)

    
    """ AUTO ADD THE CREATION DATE """
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (self.carplate)
    

