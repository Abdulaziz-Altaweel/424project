from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, primary_key=True)  # Set username as primary key
    email = models.EmailField(unique=True)
    objects = UserManager()  # Add UserManager for custom user model


    def __str__(self):
        return self.username

class Item(models.Model):
    name = models.CharField(max_length=100)  # Item name
    description = models.TextField()  # Item description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Item price
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    purchased_by = models.ManyToManyField(CustomUser, blank=True, related_name='purchased_items')

    def __str__(self):
        return self.name  # Show item name in the admin panel
