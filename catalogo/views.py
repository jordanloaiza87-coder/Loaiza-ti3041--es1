from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto

def lista_productos(request):
    # Obtiene los productos directamente desde la base de datos local
    productos = Producto.objects.all()
    
    total_productos = productos.count()
    con_stock = sum(1 for p in productos if p.stock > 0)
    
    contexto = {
        'productos': productos,
        'total_productos': total_productos,
        'con_stock': con_stock,
    }
    return render(request, 'catalogo/lista.html', contexto)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    contexto = {
        'producto': producto
    }
    return render(request, 'catalogo/detalle.html', contexto)

@login_required
def gestionar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo/gestionar.html', {'productos': productos})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        imagen = request.POST.get('imagen')

        Producto.objects.create(nombre=nombre, categoria=categoria, precio=precio, stock=stock, imagen=imagen)
        return redirect('gestionar_productos')
    
    return render(request, 'catalogo/form_producto.html')

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.categoria = request.POST.get('categoria')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.imagen = request.POST.get('imagen')
        producto.save()
        return redirect('gestionar_productos')
        
    return render(request, 'catalogo/form_producto.html', {'producto': producto})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('gestionar_productos')