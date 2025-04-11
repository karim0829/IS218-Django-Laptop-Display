from django.db import models

# Create your models here.
#database 1 - luis idk if it is good i didnt do anything in terminal because i do not know how to integrate it within my system( You can change if you want , I just wanted to see if this is good ) 
class Laptop(models.Model):
    name = models.CharField(max_length=100) #macbook air 
    brand = models.CharField(max_length=50) #dell,windows,
    os = models.CharField(max_length=50) #is it a mac or windows etc
    type = models.CharField(max_length=50) #type of laptop
    price = models.DecimalField(max_digits=7, decimal_places=2) #js the price of the laptop 
    rating = models.IntegerField() #rating on if they should get it 
    description = models.TextField() #description about the certian laptop what specs are in it etc
    release_year = models.IntegerField() #what year it came out
    image = models.ImageField(upload_to='laptop_images/', blank=True) #idk if this one is good might need to change

    def __str__(self):
        return f"{self.brand} {self.name}"
