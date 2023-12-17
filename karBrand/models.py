from django.db import models

# Create your models here.
class Brand(models.Model):
    b_name = models.CharField(max_length=50)
    def __str__(self):
     return self.b_name
