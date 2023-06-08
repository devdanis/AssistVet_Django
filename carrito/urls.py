from django.urls import path
from . import views
from .views import ProductUpdateView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.cart, name='cart'),
    path('products/', views.product_list, name='product_list'),
    # path('products/create/', views.product_create, name='product_create'),
    # path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
]