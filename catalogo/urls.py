from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    
    # Autenticación
    path('login/', LoginView.as_view(template_name='catalogo/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='lista_productos'), name='logout'),
    
    # Gestión propia de productos
    path('gestion/', views.gestionar_productos, name='gestionar_productos'),
    path('gestion/nuevo/', views.agregar_producto, name='agregar_producto'),
    path('gestion/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('gestion/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]