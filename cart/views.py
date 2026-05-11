from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart,Cartitem
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
        cart = request.session.session_key
    return cart
    

def add_cart(request,product_id):
    c_product = Product.objects.get(id= product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)

        )   
    cart.save()
    
    try:
        cart_item = Cartitem.objects.get(c_product=c_product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item = Cartitem.objects.create(
            c_product=c_product,
            quantity =1,
            cart=cart,
        )    
        cart_item.save()
   
    return redirect('cart')

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    c_product=  get_object_or_404(Product,id=product_id)
    cart_item = Cartitem.objects.get(c_product=c_product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')    

        

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    c_product=  get_object_or_404(Product,id=product_id)
    cart_item = Cartitem.objects.get(c_product=c_product,cart=cart)
    cart_item.delete()
    return redirect('cart')

def cart(request,total=0,quantity=0,cart_items=None):
    tax = 0
    grand_total = 0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = Cartitem.objects.filter(cart=cart ,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.c_product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2* total)/100 
        grand_total = total + tax 
    except ObjectDoesNotExist:
        pass
    
    context ={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,

        }
    return render(request,'cart.html',context)