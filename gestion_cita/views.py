from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from usuario.models import Usuario


def gestion_citas(request):

    nombre = request.session.get('nombre')
    id = request.session.get('usuario_id')

    return render(request, 'gestion_citas.html', {
        'nombre': nombre,
        'id_user': id
    })


def crear_cita(request):

    # =====================================
    # VALIDAR SESIÓN
    # =====================================

    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('/Login/')

    # =====================================
    # TRAER DATOS
    # =====================================

    especialidades = Especialidad.objects.all()

    doctores = Doctor.objects.select_related(
        'usuario',
        'especialidad'
    ).all()

    # =====================================
    # DEBUG CONSOLA
    # =====================================

    print("\n========== DEBUG ==========")

    print("\nESPECIALIDADES:")
    for e in especialidades:
        print(
            "ID:", e.id,
            "| NOMBRE:", e.nombre
        )

    print("\nDOCTORES:")
    for d in doctores:
        print(
            "ID:", d.id,
            "| NOMBRE:", d.usuario.nombre,
            d.usuario.apellido,
            "| ESPECIALIDAD:", d.especialidad.nombre
        )

    print("===========================\n")

    # =====================================
    # BUSCAR USUARIO LOGUEADO
    # =====================================

    try:

        usuario = Usuario.objects.get(id=usuario_id)

        print("USUARIO LOGUEADO:")
        print(
            usuario.id,
            usuario.nombre,
            usuario.apellido
        )

    except Usuario.DoesNotExist:

        return redirect('/Login/')

    # =====================================
    # MENSAJE
    # =====================================

    mensaje = ""

    # =====================================
    # CREAR CITA
    # =====================================

    if request.method == "POST":

        try:

            # =====================================
            # DATOS FORMULARIO
            # =====================================

            doctor_id = request.POST.get('doctor')
            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora')
            motivo = request.POST.get('motivo')

            print("\n====== DATOS FORM ======")
            print("DOCTOR:", doctor_id)
            print("FECHA:", fecha)
            print("HORA:", hora)
            print("MOTIVO:", motivo)
            print("========================\n")

            # =====================================
            # BUSCAR DOCTOR
            # =====================================

            doctor = Doctor.objects.get(id=doctor_id)

            # =====================================
            # VALIDAR HORARIO
            # =====================================

            existe = Cita.objects.filter(
                usuario_id=usuario_id,
                fecha=fecha,
                hora=hora
            ).exists()

            if existe:

                mensaje = "Ya tienes una cita en ese horario"

            else:

                # =====================================
                # CREAR CITA
                # =====================================

                Cita.objects.create(

                    usuario_id=usuario_id,
                    doctor=doctor,
                    fecha=fecha,
                    hora=hora,
                    motivo=motivo,
                    estado='Pendiente'
                )

                mensaje = "Cita creada correctamente"

                print("\n✅ CITA CREADA CORRECTAMENTE\n")

                return redirect('/gestion/')
        except Exception as e:

            print("\n❌ ERROR:")
            print(e)

            mensaje = f"Error: {e}"

    # =====================================
    # ENVIAR AL TEMPLATE
    # =====================================

    return render(request, "crear_cita.html", {

        'especialidades': especialidades,
        'doctores': doctores,
        'mensaje': mensaje,
        'usuario': usuario
    })



def mis_citas(request):

    # =========================
    # VALIDAR SESIÓN
    # =========================

    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('/Login/')

    # =========================
    # TRAER CITAS DEL USUARIO
    # =========================

    citas = Cita.objects.select_related(
        'doctor',
        'doctor__especialidad'
    ).filter(
        usuario_id=usuario_id
    )

    # =========================
    # ENVIAR TEMPLATE
    # =========================

    return render(request, 'mis_citas.html', {
        'citas': citas
    })

def eliminar_cita(request, id):

    # =========================
    # VALIDAR SESIÓN
    # =========================

    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('/Login/')

    # =========================
    # BUSCAR CITA
    # =========================

    try:

        cita = Cita.objects.get(
            id=id,
            usuario_id=usuario_id
        )

        # =========================
        # ELIMINAR
        # =========================

        cita.delete()

    except Cita.DoesNotExist:

        pass

    # =========================
    # VOLVER A MIS CITAS
    # =========================

    return redirect('/mis_citas/')

def editar_cita(request, id):

    # ==========================
    # VALIDAR SESIÓN
    # ==========================

    usuario_id = request.session.get('usuario_id')

    if not usuario_id:

        return redirect('/login/')

    # ==========================
    # BUSCAR CITA
    # ==========================

    cita = get_object_or_404(

        Cita,
        id=id,
        usuario_id=usuario_id
    )

    mensaje = ""

    # ==========================
    # EDITAR
    # ==========================

    if request.method == "POST":

        try:

            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora')

            cita.fecha = fecha
            cita.hora = hora

            cita.save()

            print("\n✅ CITA EDITADA\n")

            return redirect('/mis_citas/')

        except Exception as e:

            print(e)

            mensaje = f"Error: {e}"

    # ==========================
    # TEMPLATE
    # ==========================

    return render(request, 'editar_cita.html', {

        'cita': cita,
        'mensaje': mensaje
    })