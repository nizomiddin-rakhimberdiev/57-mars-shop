from django.forms import ModelForm
from .models import Product, CustomUser

class ProdouctForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'quantity', 'description', 'image', 'price', 'category']


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']