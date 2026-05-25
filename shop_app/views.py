from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from .forms import ProdouctForm, CustomUserForm
from .models import Product, CustomUser
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        user = CustomUser.objects.create_user(username=username, password=password, phone=phone)
        user.save()
        return redirect('login')
    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('home')

def add_product(request):
    if request.method == 'POST':
        form = ProdouctForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdouctForm()
    return render(request, 'add_product.html', {'form': form})

def profile_view(request):
    return render(request, 'profile.html')

def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})