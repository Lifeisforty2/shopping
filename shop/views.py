from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import SportsEquipment, Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import SportsEquipment, Order, OrderItem, ShippingAddress, Product


def home_view(request):
    products = SportsEquipment.objects.all() # get all the products
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

    # cart total
    cart_total = 0
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, ordered=False)
        cart_items = order.items.all() # get all the items in the cart
        # calculate the total cost of the order
        for item in cart_items:
            cart_total += item.get_cost()
        cart_total = round(cart_total, 2) # round to 2 decimal places
    else:
        cart_items = []

    return render(request, "home.html", {"products": products, "query": query, "sort_option": sort_option, "cart_total": cart_total})
        
@login_required
def remove_from_order(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user, order__ordered=False)
    updated_quantity = 0

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        updated_quantity = item.quantity
    else:
        item.delete()

    # recalculate the total cost of the order
    new_cart_total = 0
    order = Order.objects.filter(user=request.user, ordered=False)
    if order.exists():
        order = order[0]
        cart_items = order.items.all() # get all the items in the cart
        for item in cart_items:
            new_cart_total += item.get_cost()
        new_cart_total = round(new_cart_total, 2) # round to 2 decimal places
    


    return JsonResponse({'success': True, 'new_cart_total': new_cart_total, 'updated_quantity': updated_quantity})

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
# process order view
# this view is called when the user clicks on the checkout button
@login_required
def process_checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')

        # create or update the shipping address
        shipping_address, _ = ShippingAddress.objects.get_or_create(user=request.user, defaults={'address': address, 'city': city, 'postal_code': postal_code})
        
        # update the order
        order = Order.objects.get(user=request.user, ordered=False)
        order.shipping_address = shipping_address
        order.ordered = True
        order.save()

        messages.success(request, 'Your order was successful!')
        return redirect('order_confirmation', order_id=order.id) # redirect to the order confirmation page
    else:
        return render(request, 'checkout.html')
# order confirmation view
@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    cart_total = sum(item.get_cost() for item in order.items.all())
    cart_total = round(cart_total, 2)
    return render(request, 'order_confirmation.html', {'order': order,"cart_total": cart_total})
@login_required
def checkout(request):
    return render(request, "checkout.html")

# product view
def product(request, equipment_id):
    equipment = get_object_or_404(SportsEquipment, pk=equipment_id)
    return render(request, 'product.html', {'equipment': equipment})