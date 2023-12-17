from django.urls import path
from . import views

urlpatterns = [
    
    path("brand/",views.add_brand,name = 'brand'),
  
]