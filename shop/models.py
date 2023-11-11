from django.db import models
from django.conf import settings
'''
Django user model has the following fields:
username
password
'''
# Create your models here.
class SportsEquipment(models.Model):
    name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    # make price a decimal field
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name
''' 
i need user from django.contrib.auth.models import User
i can make a CustomerProfile model with a OneToOneField to User
i need a order model with a ForeignKey to User 
i need a OrderItem model with a ForeignKey to Order and a ForeignKey to SportsEquipment
'''
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # this is the user who made the order
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE) 
    equipment = models.ForeignKey(SportsEquipment, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.quantity} x {self.equipment.name}'
    def get_cost(self):
        return self.price * self.quantity
    