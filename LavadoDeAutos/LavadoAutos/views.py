from django.shortcuts import render, redirect
from .models import Insumos, Instalaciones, Empleados, Mision, Vision, Slider
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as iniciosesion
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages

# Create your views here.
def logout_vista(request):
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    logout(request)
    return render(request,'core/index.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast})

def login(request):
    if request.POST:
        user = request.POST.get("Usuario")
        password = request.POST.get("Contraseña")
        us = authenticate(request, username=user, password=password)
        if us is not None and us.is_active:
           iniciosesion(request, us)
           return redirect(index)
        else:
            messages.info(request, 'usuario/contraseña inválida')
            return redirect(login)

    return render(request, 'core/login.html')

def index(request):
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'core/index.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast})

def base(request):
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'core/base.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast})
    
def quienesSomos(request):
    mision = Mision.objects.first()
    vision = Vision.objects.first()
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'core/Quienes_somos.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast, 'mision':mision, 'vision':vision})

def galeria(request):
    instalacion = Instalaciones.objects.all()
    empleado  = Empleados.objects.all()
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'core/Galeria.html', {'lista_instalaciones':instalacion, 'lista_empleados':empleado, 'slider':slider, 'first':sliderFirst, 'last':sliderLast})

def registro(request):
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    if request.POST:
        nombre      = request.POST.get("Nombre")
        apellido    = request.POST.get("Apellido")
        correo      = request.POST.get("phone")
        usuario     = request.POST.get("Usuario")
        contraseña  = request.POST.get("Contraseña")
        reccontraseña = request.POST.get("RepetirContraseña")

        if contraseña!= reccontraseña:
            messages.info(request, 'El contraseñas incorrectas')
            return redirect(registro)
        try:
            u = User.objects.get(username=usuario)
            messages.info(request, 'El usuario ya existe')
            return redirect(registro)
        except:
            try:
                u = User.objects.get(email=correo)
                messages.info(request, 'El correo ya existe')
                return redirect(registro)
            except:
                u = User()
                u.first_name = nombre
                u.last_name  = apellido
                u.username   = usuario
                u.email      = correo
                u.set_password(contraseña)
                u.save()

                us = authenticate(request, username=usuario, password=contraseña)
                iniciosesion(request, us)
                return redirect(index)

    return render(request, 'core/Registro.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast})

@login_required(login_url='/login')
@permission_required('LavadoAutos.add_insumos', login_url='/login/')
def admin_insumos(request):
    insumo = Insumos.objects.all()
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    if request.POST:
        accion = request.POST.get("accion")

        if accion == "registrar":
            nombre      = request.POST.get("NombreInsumo")
            precio      = request.POST.get("Precio")
            stock       = request.POST.get("Stock")
            descripcion = request.POST.get("Descripcion")

            insumos = Insumos(
                nombreinsumo = nombre,
                descripcion = descripcion,
                precio      = precio,
                stock       = stock
            )
            insumos.save()
            messages.success(request, 'Se agregó un insumo')

            return redirect(admin_insumos)

    return render(request, 'core/admin_insumos.html', {'lista_insumos':insumo, 'slider':slider, 'first':sliderFirst, 'last':sliderLast})

@login_required(login_url='/login')
@permission_required('LavadoAutos.delete_insumos', login_url='/login/')
def eliminarInsumo(request, id):
    try:
        eliminarInsumo = Insumos.objects.get(cod = id)
        eliminarInsumo.delete()
        messages.success(request, 'Eliminado Correctamente')
    except:
        messages.info(request, 'No se ha podido Eliminar Correctamente')

    return redirect(admin_insumos)

@login_required(login_url='/login')
@permission_required('LavadoAutos.change_insumos', login_url='/login/')
def modificarInsumo(request, id):
    try:
        sliderFirst = Slider.objects.first()
        sliderLast  = Slider.objects.last()
        slider = Slider.objects.all()
        modificar_Insumo = Insumos.objects.get(cod=id)
        return render(request, 'core/modificar_Insumo.html', {'item':modificar_Insumo, 'slider':slider, 'first':sliderFirst, 'last':sliderLast})
    except:
        return redirect(admin_insumos)

@login_required(login_url='/login')
@permission_required('LavadoAutos.change_insumos', login_url='/login/')
def Actualizar(request):
    if request.POST:
        nombre      = request.POST.get("NombreInsumo")
        precio      = request.POST.get("Precio")
        stock       = request.POST.get("Stock")
        descripcion = request.POST.get("Descripcion")

        try:
            Ins = Insumos.objects.get(nombreinsumo=nombre)
            Ins.precio      = precio
            Ins.stock       = stock
            Ins.descripcion = descripcion

            Ins.save()
            messages.success(request, 'Se Actualizo Correctamente')
        except:
            messages.info(request, 'No se pudo Actualizar Correctamente')

        return redirect(admin_insumos)