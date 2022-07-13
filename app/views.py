import datetime
from django.shortcuts import redirect, render
#importacion del modulo de mensajes 
from django.contrib import messages
#importacion de los modelos en models.py
from .models import *

# Create your views here.

def registro(request):
    if request.method == 'POST':
        #estructura de condicion que verifica si el usuario que se intenta registrar existe
        if Usuario.objects.filter(email = request.POST['correo']).exists(): # se verifica la existencia por el campo de email
            messages.success(request, 'El usuario ingresado ya existe')
        else:
            #creacion del nuevo usuario, entre [] se coloca el atributo "name" de los input en el html
            newUser = Usuario(
                rut = request.POST['rut'],
                nombre = request.POST['nombre'],
                apellido = request.POST['apellido'],
                telefono = request.POST['telefono'],
                email = request.POST['correo'],
                pwd = request.POST['password']
            )
            Carrito(username = request.POST['correo'], subtotal = 0).save()
            #se guarda el nuevo usuario en la base de datos
            newUser.save()
            messages.success(request, 'Usuario registrado correctamente')
    return render(request, 'app/registro.html')

def tienda(request):
    contexto = Producto.objects.all()
    return render(request, 'app/tienda.html', {"productos":contexto})

def login(request):
    if request.method == 'POST':
        try:
            newUser = Usuario.objects.get(email = request.POST['email'], pwd = request.POST['password'])
            request.session['email'] = newUser.email 
            contexto = Producto.objects.all()
            return redirect('home')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Correo o constraseña no son correctos')
    return render(request, 'app/login.html')

def producto(request, prod_id):
    producto = Producto.objects.filter(codigo = prod_id)
    return render(request, 'app/producto.html', {"producto":producto})

def arr_form(request):
    if request.method == 'POST':
        try:
            new_arriendo = Reserva_arriendo(
                tipo_bici = request.POST['tipo_bici'],
                tiempo_arriendo =  request.POST['tiempo_arriendo'],
                tipo_garantia =  request.POST['tipo_garantia'],
                usuario = request.session['email']                                                                  
            )
            new_arriendo.save()
            messages.success(request, 'Formulario de arriendo registrado.')
            return redirect('arriendo-form')
        except:
            messages.success(request, 'Debe Iniciar sesión para enviar el formulario.')
    return render(request, 'app/arriendo_form.html')

def mant_form(request):
    if request.method == 'POST':
        try:
            new_mantencion = Reserva_mantencion(
                usuario = request.session['email'],
                tipo_bici = request.POST['tipo_bici'], 
                tipo_mantencio = request.POST['tipo_mantencio'], 
                detalles = request.POST['detalles']
            )

            new_mantencion.save()
            messages.success(request, 'Mantencion registrada correctamente')
            return redirect('mantencion-form')
        except: messages.success(request, 'Debes estar registrado')    
    return render(request, 'app/mantencion_form.html')


def carrito(request):
    cart = Carrito.objects.filter(username=request.session['email'])
    cartitems = CarritoItem.objects.filter(id_carrito = Carrito.objects.get(username = request.session['email']).id_carrito)
    return render(request, 'app/carrito.html', {"cartitems":cartitems, "cart":cart})

def agregarProducto(request, user_id, prod_id):
    item = CarritoItem.objects.filter(id_carrito = Carrito.objects.get(username = user_id).id_carrito).filter(id_producto = prod_id)
    if item.exists():
        prod = Producto.objects.get(codigo=prod_id)
        prod.stock -= 1
        prod.save()
        item = CarritoItem.objects.get(id_carrito = Carrito.objects.get(username = user_id).id_carrito, id_producto = prod_id)
        item.cantidad += 1
        item.subtotal_producto += Producto.objects.get(codigo = prod_id).precio
        item.save()
        #actualizacion de carrito:
        subt = 0
        carrito = Carrito.objects.get(username = user_id)
        items = CarritoItem.objects.filter(id_carrito = carrito.id_carrito)
        for i in items:
            subt += i.subtotal_producto
        carrito.subtotal = subt
        carrito.save()        
    else:
        prod = Producto.objects.get(codigo=prod_id)
        prod.stock -= 1
        prod.save()
        newItem = CarritoItem(id_carrito = Carrito.objects.get(username = user_id).id_carrito, nombre = Producto.objects.get(codigo = prod_id).nombre , id_producto = Producto.objects.get(codigo = prod_id).codigo, cantidad = 1, subtotal_producto = Producto.objects.get(codigo = prod_id).precio)
        newItem.save()
        #actualizacion de carrito:
        subt = 0
        carrito = Carrito.objects.get(username = user_id)
        items = CarritoItem.objects.filter(id_carrito = carrito.id_carrito)
        for i in items:
            subt += i.subtotal_producto
        carrito.subtotal = subt
        carrito.save()
    return redirect('tienda')  

def comprar(request, p_total, id_carrito):
    newVenta = Venta(usuario = request.session['email'], fecha = datetime.datetime.now(), total=p_total)
    newVenta.save()

    for item in CarritoItem.objects.filter(id_carrito = id_carrito):
        item.delete()

    cart = Carrito.objects.get(id_carrito = id_carrito)
    cart.subtotal = 0
    cart.save()

    return redirect('carrito')

def multiCompra(request, prod_id, user_id):
    if request.method == 'POST':
        item = CarritoItem.objects.filter(id_carrito = Carrito.objects.get(username = user_id).id_carrito).filter(id_producto = prod_id)
        if item.exists():
            prod = Producto.objects.get(codigo=prod_id)
            prod.stock -= int(request.POST['cantidad'])
            prod.save()
            item = CarritoItem.objects.get(id_carrito = Carrito.objects.get(username = user_id).id_carrito, id_producto = prod_id)
            item.cantidad += int(request.POST['cantidad'])
            item.subtotal_producto += Producto.objects.get(codigo = prod_id).precio * int(request.POST['cantidad'])
            item.save()
            #actualizacion de carrito:
            subt = 0
            carrito = Carrito.objects.get(username = user_id)
            items = CarritoItem.objects.filter(id_carrito = carrito.id_carrito)
            for i in items:
                subt += i.subtotal_producto
            carrito.subtotal = subt
            carrito.save()  
        else:
            prod = Producto.objects.get(codigo=prod_id)
            prod.stock -= int(request.POST['cantidad'])
            prod.save()
            newItem = CarritoItem(id_carrito = Carrito.objects.get(username = user_id).id_carrito, nombre = Producto.objects.get(codigo = prod_id).nombre , id_producto = Producto.objects.get(codigo = prod_id).codigo, cantidad = int(request.POST['cantidad']), subtotal_producto = Producto.objects.get(codigo = prod_id).precio * int(request.POST['cantidad']))
            newItem.save()
            #actualizacion de carrito:
            subt = 0
            carrito = Carrito.objects.get(username = user_id)
            items = CarritoItem.objects.filter(id_carrito = carrito.id_carrito)
            for i in items:
                subt += i.subtotal_producto
            carrito.subtotal = subt
            carrito.save()
        return redirect('producto', prod_id=prod_id)

def home(request):
    return render(request, 'app/home.html')

def crudPromos(request):
    promos = Promo.objects.all()
    return render(request, 'app/crudPromos.html', {"promos": promos})

def addPromo(request):
    codigoN = request.POST['code']
    pct = request.POST['pct']
    newPromo = Promo(descripcion = request.POST['descripcion'], porcentaje = request.POST['pct'], codigo = request.POST['code'])
    newPromo.save()
    prod = Producto.objects.get(codigo = codigoN)
    precioNuevo = float(prod.precio) * (float(pct) * 0.01)
    prod.precio = round(precioNuevo)
    prod.save() 
    print('funca')
    return redirect('crudPromos')

def delPromo(request, code):
    promo = Promo.objects.filter(id_promo = code)
    promo.delete()
    return redirect('crudPromos')

def editPromo(request, code):
    promo = Promo.objects.filter(id_promo = code)
    if request.method == 'POST':
        oldPromo = Promo.objects.get(id_promo = code)
        if request.POST['newdesc'] != '':
            oldPromo.descripcion = request.POST['newdesc']
            oldPromo.save()
        return redirect('crudPromos')
    else:        
        return render(request, 'app/editarPromo.html', {"promo":promo})   
def crudProductos(request):
    contexto = {'producto':Producto.objects.all()}
    return render(request, 'app/crud_productos.html', contexto)

def registroProductos(request):
    return render(request, 'app/registro_productos.html')

def añadirProductos(request):
    try:
        if Producto.objects.filter(codigo = request.POST['codigo']).exists():
            messages.success(request, 'Ya hay un producto con ese codigo')
            return render(request, 'app/registro_productos.html')

        else:
            codigo = request.POST['codigo']
            nombre = request.POST['nombre']
            marca = request.POST['marca']
            precio = request.POST['precio']
            stock = request.POST['stock']
            imagen = request.POST['imagen']
            producto = Producto.objects.create(codigo=codigo, nombre=nombre, marca=marca, precio=precio, stock=stock, imagen=imagen)
            producto.save()
            return redirect('crudProductos')
    except:
        return render(request, 'app/registro_productos.html')

            
        

    