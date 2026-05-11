from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list, name='products_list'),

    path('products/<slug:gender_slug>/',views.products_list,name='products_by_gender'),
    path('products/<slug:category_slug>/', views.products_list, name='products_by_category'),
    path('product/<slug:category_slug>/<slug:product_slug>/<slug:gender_slug>/', views.product_details, name='product_details'),
]