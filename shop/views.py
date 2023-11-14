from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import SportsEquipment, Order, OrderItem
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def home_view(request):
    products = SportsEquipment.objects.all()
    sort_option = request.GET.get('sort')

    # Check if a search query is provided
    query = request.GET.get('query')
    if query:
        # Perform a case-insensitive search across multiple fields
        products = products.filter(name__icontains=query)

    # Default sorting is "Featured"
    if sort_option == 'price_low':
        products = products.order_by('price')
    elif sort_option == 'price_high':
        products = products.order_by('-price')

    return render(request, "home.html", {"products": products, "query": query, "sort_option": sort_option})
'''
when a user clicks on a link to add an item to the order the page 
the equipment_id is passed to the add_to_order view by the url
equipment_id is the id of the equipment that the user wants to add to the order and is not
'''

@login_required
def add_to_order(request, equipment_id):
    equipment = get_object_or_404(SportsEquipment, id=equipment_id)
    
    order, _ = Order.objects.get_or_create(user=request.user, ordered=False) # get the order for the user if it exists, otherwise create a new order

    # check if the order item is in the order
    order_item, created = OrderItem.objects.get_or_create(order=order, equipment=equipment, defaults={'price': equipment.price})
    if not created:
        order_item.quantity += 1 # increase the quantity of the order item by 1
    order_item.save()

    return redirect("home") # redirect to the home page

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # save the user
            login(request, user) # log the user in
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})
