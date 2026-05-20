from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Usuario


def usuario(request):

    mensaje = ""

    if request.method == 'POST':

        correo = request.POST['usuario']
        password = request.POST['password']

        try:

            user = Usuario.objects.get(correo=correo)

            if check_password(password, user.password):

                # GUARDAR SESION
                request.session['usuario_id'] = user.id
                request.session['nombre'] = user.nombre
                request.session['apellido'] = user.apellido
                request.session['correo'] = user.correo

                return redirect('/MenuPrincipal/')

            else:
                mensaje = "Contraseña incorrecta"

        except Usuario.DoesNotExist:

            mensaje = "El usuario no existe"

    return render(request, "Login.html", {
        'mensaje': mensaje
    })

def Registro(request):

    if request.method == 'POST':

        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        documento = request.POST['Documento']
        correo = request.POST['correo']
        edad = request.POST['edad']
        password = request.POST['password']
        confirmar = request.POST['confirmar']

        
        if password == confirmar:

            Usuario.objects.create(
                nombre=nombre,
                apellido=apellido,
                documento=documento,
                correo=correo,
                edad=edad,
                password=make_password(password)
            )

            return redirect('/Login/')

    return render(request, "Registro.html")

def MenuPrincipal(request):

    nombre = request.session.get('nombre')

    return render(request, 'MenuInicio.html', {
        'nombre': nombre
    })

def inicio(request):
    return render(request, 'inicio.html')

