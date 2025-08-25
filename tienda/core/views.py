from decimal import Decimal
from django.shortcuts import get_object_or_404, render,redirect
from .models import ItemPedido, Pedido, Producto,Categoria
# Create your views here.
def tienda_view(request):
    productos=Producto.objects.all()
    categorias=Categoria.objects.all()
    return render(request,'tienda.html',{
        'productos':productos,
        'categorias':categorias
    })

def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)] += 1
    else:
        carrito[str(producto_id)] = 1

    request.session['carrito'] = carrito
    return redirect('tienda')  # redirige a la tienda

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = Producto.objects.filter(id__in=carrito.keys())
    categorias=Categoria.objects.all()
    total = 0
    items = []
    for producto in productos:
        cantidad = carrito[str(producto.id)]
        subtotal = producto.precio * cantidad
        total += subtotal
        items.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    return render(request, 'carrito.html', {
        'items': items,
        'total': total,
        'categorias':categorias
    })

def quitar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
        request.session['carrito'] = carrito
    return redirect('ver_carrito')

def productos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()  # Para seguir mostrando el menú

    return render(request, 'productos_por_categoria.html', {
        'productos': productos,
        'categoria': categoria,
        'categorias': categorias
    })

def finalizar_pedido(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')

        carrito = request.session.get('carrito', {})
        if not carrito:
            return render(request, 'carrito.html')

        productos = Producto.objects.filter(id__in=carrito.keys())
        total = Decimal('0.00')

        pedido = Pedido.objects.create(
            nombre=nombre,
            email=email,
            direccion=direccion,
            pagado=False,
            total=0  # lo actualizamos después
        )

        for producto in productos:
            cantidad = carrito[str(producto.id)]
            precio_unitario = producto.precio
            subtotal = precio_unitario * cantidad
            total += subtotal

            ItemPedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario
            )

        pedido.total = total
        pedido.save()

        # Limpiar el carrito
        request.session['carrito'] = {}
        request.session.modified = True

        categorias = Categoria.objects.all()
        return render(request, 'pedido_exitoso.html', {
            'pedido': pedido,
            'categorias': categorias
        })
    else:
        categorias = Categoria.objects.all()
        return render(request, 'formulario_pedido.html', {
            'categorias': categorias
        })
