from django.contrib import admin

# Register your models here.
from .models import Product, Feedback

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # columns of laptop list
    list_display   = ('name', 'description', 'price', 'image')
    

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    # columns of feedback list
    list_display   = ('name', 'product', 'rating', 'comment', 'timestamp')
    
