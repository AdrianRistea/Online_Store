from store.models import Category,Cart


def navbar_data(request):
    if request.user.is_authenticated:
        open_cart, created = Cart.objects.get_or_create(user=request.user, status='open')
        cart_items = open_cart.cartitem_set.all()
        product_count = sum([cart_item.quantity for cart_item in cart_items])
    else:
        product_count = 0
    return {'categories':Category.objects.filter(parent_category=None), 'product_count':product_count}

