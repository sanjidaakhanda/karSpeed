
from django.shortcuts import render
from karDetail.models import Car,Brand
 

def home(request,brand_slug = None):
    cars = Car.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        cars = Car.objects.filter(brand = brand)

    brands = Brand.objects.all()
    return render(request, 'home.html', {'cars': cars, 'brand':brands})