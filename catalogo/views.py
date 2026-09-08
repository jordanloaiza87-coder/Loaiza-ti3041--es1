import json
import os
from django.conf import settings
from django.shortcuts import render

def cargar_productos():
    # Ruta del archivo JSON dentro de la app
    ruta_json = os.path.join(settings.BASE_DIR, 'catalogo', 'data', 'productos.json')
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def lista_productos(val):
    productos = cargar_productos()
    
    # Lógica de la Etapa 3 (resumen calculado anticipado para aprovechar)
    total_productos = len(productos)
    con_stock = sum(1 for p in productos if p['stock'] > 0)
    
    contexto = {
        'productos': productos,
        'total_productos': total_productos,
        'con_stock': con_stock,
    }
    return render(val, 'catalogo/lista.html', contexto)

def detalle_producto(val, producto_id):
    productos = cargar_productos()
    # Buscar el producto por id
    producto = next((p for p in productos if p['id'] == producto_id), None)
    
    contexto = {
        'producto': producto
    }
    return render(val, 'catalogo/detalle.html', contexto)