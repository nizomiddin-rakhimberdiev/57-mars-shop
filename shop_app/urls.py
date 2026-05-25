from django.urls import path, include
from .views import home, register, login_page, logout_page, add_product, profile_view, edit_profile

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('add_product/', add_product, name='add_product'),
    path('profile/', profile_view, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),

]