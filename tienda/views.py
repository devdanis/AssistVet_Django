from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from tienda.forms import CustomerRegistrationForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'tienda/index.html')

def perros(request):
    return render(request, 'tienda/perros.html')

def gatos(request):
    return render(request, 'tienda/gatos.html')

def servicios(request):
    return render(request, 'tienda/servicios.html')



class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'tienda/customer_registration.html', locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Felicitaciones! Te has registrado con exito')
        else:
            messages.warning(request, 'Datos ingresados incorrectos')
        return render(request, 'tienda/customer_registration.html', locals())
        
class ProfileView(View):
    def get(self, request):
        return render(request, 'tienda/profile.html', locals)
    
    def post(self, request):
        return render(request, 'tienda/profile.html', locals)

            
# def home(request):
#     return render(request,'tienda/home.html')

# def administration(request):
#     products = Product.objects.all()
#     return render(request,'tienda/administration.html', {'products': products})

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'tienda/product_list.html', {'products': products})

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'tienda/product_detail.html', {'product': product})

# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#             return redirect('administration')
#     else:
#         form = ProductForm()
#     return render(request, 'tienda/product_create.html', {'form': form})

# def product_update(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             product = form.save()
#             return redirect('administration')
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'tienda/product_update.html', {'form': form, 'product': product})

# def product_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('administration')
#     return render(request, 'tienda/product_delete.html', {'product': product})