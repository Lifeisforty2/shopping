from django.contrib import admin
from .models import SportsEquipment, Order, OrderItem
# Register your models here.
admin.site.register(SportsEquipment)
admin.site.register(Order)
admin.site.register(OrderItem)

