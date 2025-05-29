from django.shortcuts import render, redirect
from .forms import ReclamoForm
import uuid
from .models import Reclamo
from django.contrib import messages
from .forms import ReclamoForm
from django.core.mail import send_mail  
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def registrar_reclamo(request):
    if request.method == 'POST':
        form = ReclamoForm(request.POST, request.FILES)
        if form.is_valid():
            reclamo = form.save(commit=False)

            while True:
                nuevo_ticket = str(uuid.uuid4())[:8]  
                if not Reclamo.objects.filter(ticket=nuevo_ticket).exists():
                    reclamo.ticket = nuevo_ticket
                    break

            reclamo.save() 

            send_mail(
                subject = 'Confirmación de reclamo',
                message = f'Estimado cliente,\n\nSu reclamo con el nombre "{reclamo.titulo}" ha sido registrado exitosamente.\n\nNúmero de Ticket: {reclamo.ticket}\n\nGracias por contactarnos.',
                from_email = None,
                recipient_list = [reclamo.correo],
                fail_silently = False
            )

            messages.success(request, "¡Reclamo enviado con éxito!")

            return render(request, 'tasks.html',{'ticket': reclamo.ticket})
    else:
        form = ReclamoForm()

    return render(request, 'registrar_reclamo.html', {'form': form})

@login_required
def ver_estado_reclamo(request):

    if request.method == 'POST':
        ticket = request.POST.get('ticket')
        try:
            reclamo = Reclamo.objects.get(ticket=ticket)
            return render(request, 'ver_estado_reclamo.html', {'reclamo': reclamo})

        except Reclamo.DoesNotExist:
            messages.error(request, 'El ticket no existe, intentalo de nuevo.')
            return redirect ('ver_estado_reclamo')

    return render(request, 'ver_estado_reclamo.html')

