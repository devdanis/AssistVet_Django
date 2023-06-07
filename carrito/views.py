from django.shortcuts import render, get_object_or_404, redirect
from carrito.models import Product
from carrito.forms import ProductForm
from django.contrib import messages


# def home(request):
#     return render(request,'carrito/home.html')

def cart(request):
    products = Product.objects.all()
    return render(request,'carrito/cart.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'carrito/product_list.html', {'products': products})

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'carrito/product_detail.html', {'product': product})

# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#             return redirect('administration')
#     else:
#         form = ProductForm()
#     return render(request, 'carrito/product_create.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        cantidad = int(request.POST.get('Cantidad'))  # Obtén el valor de la cantidad del formulario
        product.Cantidad = cantidad  # Actualiza el campo "Cantidad" del objeto "Product"
        product.save()  # Guarda el objeto "Product" actualizado en la base de datos
        messages.success(request,'Se ha editado el valor correctamente')
        
        return redirect('cart')
    return render(request, 'carrito/product_update.html', {'product': product})

# def product_update(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             product = form.save()
#             messages.success(request,'Se ha editado el valor correctamente')
#             return redirect('cart')
#         else:
#             messages.error(request,'Algo ha fallado')
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'carrito/product_update.html', {'form': form, 'product': product})
 

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('cart')
    return render(request, 'carrito/product_delete.html', {'product': product})