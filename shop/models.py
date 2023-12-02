from django.db import models
from django.conf import settings
'''
Django user model has the following fields:
username
password
'''
# equipmentid = models.AutoField(primary_key=True)

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
    
'''
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # this is the user who made the order
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('ShippingAddress', related_name='orders', null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'Order {self.id} by {self.user.username}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE) 
    equipment = models.ForeignKey(SportsEquipment, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.quantity} x {self.equipment.name}'
    def get_cost(self):
        return self.price * self.quantity
    
    
# need a class to hold the shipping address
class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    def __str__(self):
        return self.address
    