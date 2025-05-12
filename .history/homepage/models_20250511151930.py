from django.db import models
#
# Create your models here.
#database 1 - luis idk if it is good i didnt do anything in terminal because i do not know how to integrate it within my system( You can change if you want , I just wanted to see if this is good ) 
#4.17 - karim - Created registration table... thinking about changing it to a contact form.  commented out images for now. Dont think we'll need it but you did great starting off the database
#4.17 - karim - Migrations are updated and database is deployed. Website is functional.
# u can start off forms if youd like



#product model
class Product(models.Model):
    model_c = [
        ('highend', 'High End'),
        ('budget', 'Budget'),
        ('studio', 'Studio'),

    ]
    fullname = models.CharField(max_length=100) #macbook air 
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2) #js the price of the laptop 
    image = models.ImageField(upload_to='homepage/', blank=True) 
    model = models.CharField(max_length = 20, choices = model_c, default = 'budget')
    def __str__(self):
        return f"{self.name}"




#feedback model

class Feedback(models.Model):
    user = models.CharField(max_length=100) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i,i) for i in range (1,6)])
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating} Stars"
    

