from .models import Category
from store.models import offers,Banner,Product
def menu_links(request):
    links = Category.objects.only('category_name', 'slug')
    return dict(links=links)



def global_offers(request):
    return {
        "offeres": offers.objects.filter(is_active=True)
    }


def dynamic_banner(request):
    path = request.path
    if path.startswith('/about'):
        page = 'about'
    elif path.startswith('/products'):
        page = 'products'
    else:
        page = 'home'

    banner = Banner.objects.filter(page=page ,is_active=True).first()            

    return{'banner':banner}


def global_products(request):
    products = Product.objects.filter(is_available=True)

    return {
        'all_products': products
    }