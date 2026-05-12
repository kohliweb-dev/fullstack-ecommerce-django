from django.shortcuts import render
from store.models import Product

def home_view(request):
   
    all_products = Product.objects.filter(is_available=True)[:6]  # 👈 limit here

    context = {
        'all_products': all_products,
    }

    return render(request, 'home.html', context)


def about_view(request):
    return render(request , 'about.html')

def contact_view(request):
    return render(request , 'contact.html')