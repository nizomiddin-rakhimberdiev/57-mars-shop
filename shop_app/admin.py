from django.contrib import admin
from .models import CustomUser, Category, Product
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'quantity', 'price', 'category', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('product_type', 'category')
    

admin.site.register(Product, ProductAdmin)