from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("index/", views.index, name="index"), 
    path("about/", views.about, name="about"),  
    path("contact/", views.contact, name="contact"),
    path("support/", views.review_form, name="support"),
    path("feedback/", views.review_form, name="feedback"),
    path("products/", views.product_list, name="product_list"),
    path("highend/", views.highend, name="highend"),
    path("studio/", views.studio, name="studio"),
    path("budget/", views.budget, name="budget"),
    path("restricted/", views.budget, name="restricted"),







]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
