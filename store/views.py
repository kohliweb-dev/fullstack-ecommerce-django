
from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
from cart.models import Cartitem
from cart.views import _cart_id
 # from django.shortcuts import get_object_or_404, redirect
def products_list(request, category_slug=None, gender_slug=None):
    products = Product.objects.filter(is_available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if gender_slug:
        products = products.filter(gender__slug=gender_slug)

    return render(request, 'products_list.html', {'products': products})


def product_details(request, category_slug, product_slug, gender_slug):
    product = get_object_or_404(
        Product,
        slug=product_slug,
        category__slug=category_slug,
        gender__slug=gender_slug,
    )
    in_cart = Cartitem.objects.filter(cart__cart_id=_cart_id(request),c_product=product).exists()
    context={
        'in_cart':in_cart,
        'product': product
    }
    return render(request, 'product_details.html',context)


