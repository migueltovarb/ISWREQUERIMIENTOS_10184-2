from django.shortcuts import render, redirect
from .forms import SolicitudForm
from django.contrib import messages
from django.core.mail import send_mail  
from django.conf import settings

def registrar_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save()
            send_mail(
                subject='Confirmación de solicitud',
                message=f'Estimado cliente,\n\nSu solicitud con el nombre "{solicitud.titulo}" ha sido registrada exitosamente.\n\nGracias por contactarnos.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[solicitud.correo],
                fail_silently=False
            )
            messages.success(request, 'Solicitud registrada con éxito')
            return redirect('tasks') 

        else:
            messages.error(request, 'Inténtalo de nuevo')

    else:
        form = SolicitudForm()
    return render(request, 'registrar_solicitud.html', {'form': form})