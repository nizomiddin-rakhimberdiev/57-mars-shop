from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinLengthValidator

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    TYPE_CHOICES = (
        ('kg', 'kg'),
        ('dona', 'dona'),
        ('litr', 'litr'),
        ('metr', 'metr'),

    )
    name = models.CharField(max_length=100, unique=True, help_text="Maxsulot nomini kirit: ", validators=[MinLengthValidator(3)])
    product_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='kg')
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name