from .models import Order
def cart_processor(request):
    if request.user.is_authenticated:
        order, _ = Order.objects.get_or_create(user=request.user, ordered=False)
        return {'cart': order}
    return {}