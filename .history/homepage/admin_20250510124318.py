from django.contrib import admin

# Register your models here.
from .models import Product, Feedback

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # columns of laptop list
    list_display   = ('name', 'price')
    # allows admins to search using brand, name, os, or type
    search_fields  = ('name', 'price')
    # filter by brand, operating system, and release year
    list_filter    = ('brand', 'os', 'release_year')

@admin.register(Feedback)
class RegistrationAdmin(admin.ModelAdmin):
    # columns of registration list
    list_display   = ('product', 'rating', 'comment')
    # allows admins to search using name, email, or subject
    search_fields  = ('name', 'email', 'subject')

