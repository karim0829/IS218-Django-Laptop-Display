from django.contrib import admin

# Register your models here.
from .models import Laptop, Registration, Review

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    # columns of laptop list
    list_display   = ('brand', 'name', 'os', 'type', 'price', 'rating', 'release_year')
    # allows admins to search using brand, name, os, or type
    search_fields  = ('brand', 'name', 'os', 'type')
    # filter by brand, operating system, and release year
    list_filter    = ('brand', 'os', 'release_year')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    # columns of registration list
    list_display   = ('name', 'email', 'subject')
    # allows admins to search using name, email, or subject
    search_fields  = ('name', 'email', 'subject')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # columns of review list
    list_display   = ('name', 'laptop', 'rating', 'timestamp')
    # allows admins to search using comment text and related fields
    search_fields  = ('comment', 'name__name', 'laptop__name')
    # filter by rating and timestamp
    list_filter    = ('rating', 'timestamp')
