from django.db import models
from karBrand.models import Brand
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    brand = models.ManyToManyField(Brand)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='karDetail/media/uploads/', blank = True,
     null = True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE ,related_name='comments')
    user = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add =True)
    def __str__(self):
     return f'comments by {self.user}'