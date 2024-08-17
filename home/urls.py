from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("list", views.product_list, name='list'),
    path("product", views.product, name='product'),
    path("vendor", views.vendor, name='vendor'),


]
