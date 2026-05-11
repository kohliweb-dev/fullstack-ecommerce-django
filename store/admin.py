from django.contrib import admin
from .models import Product,offers,Banner,ShoeSize,Gender,ProductImage


class ShoeSizeInline(admin.TabularInline):
    model = ShoeSize
    extra = 1




class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4    

class ProductAdmin(admin.ModelAdmin):
    list_display=('title','price','slug','category','stoke','rate')
    prepopulated_fields ={'slug':('title',)}
    inlines = [ShoeSizeInline,ProductImageInline]  
admin.site.register(Product,ProductAdmin)


admin.site.register(offers)
admin.site.register(Banner)
admin.site.register(Gender)
