from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('perros/', views.perros, name='perros'),
    path('gatos/', views.gatos, name='gatos'),
    path('servicios/', views.servicios, name='servicios'),
    path('registro/', views.CustomerRegistrationView.as_view(), name='registro'),
    path('login/', auth_view.LoginView.as_view(template_name= 'tienda/login.html'), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]