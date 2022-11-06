
from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    amazon = models.CharField(max_length=300)
    elitehub = models.CharField(max_length=300)
    flipkart = models.CharField(max_length=300)
    imagelink = models.CharField(max_length=300)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name