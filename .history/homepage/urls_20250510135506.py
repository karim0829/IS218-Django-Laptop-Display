from django.urls import path
from . import views 


urlpatterns = [
    path("index/", views.index, name="index"), 
    path("about/", views.about, name="about"),  
    path("contact/", views.contact, name="contact"),
    path("support/", views.review_form, name="support"),
    path("feedback/", views.review_form, name="feedback"),
    path("products/", views.product_list, name="product_list")



]
