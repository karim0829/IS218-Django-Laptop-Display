from django.db import models
#
# Create your models here.
#database 1 - luis idk if it is good i didnt do anything in terminal because i do not know how to integrate it within my system( You can change if you want , I just wanted to see if this is good ) 
#4.17 - karim - Created registration table... thinking about changing it to a contact form.  commented out images for now. Dont think we'll need it but you did great starting off the database
#4.17 - karim - Migrations are updated and database is deployed. Website is functional.
# u can start off forms if youd like

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




#Adding User Registration Table 

class Registration(models.Model): 
    name = models.CharField(max_length = 30) 
    email = models.CharField(max_length=30) 
    subject = models.CharField(max_length=30) 
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.ForeignKey(Registration, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE) 
    rating = models.IntegerField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.laptop.name} - {self.rating} Stars"
    

