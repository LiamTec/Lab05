from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event, Participant, Registration

def event_list(request):
    # Obtén todos los eventos y ordénalos por fecha de inicio.
    events = Event.objects.all().order_by('start_time')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, slug):
    # Muestra los detalles de un evento específico.
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'events/event_detail.html', {'event': event})

def register_to_event(request, slug):
    # Registra a un participante en un evento sin necesidad de login.
    event = get_object_or_404(Event, slug=slug)

    if event.is_full:
        messages.error(request, "Este evento ya está lleno.")
        return redirect('events:event_detail', slug=slug)

    # Crea un participante sin necesidad de autenticación.
    phone = request.POST.get('phone')  # Obtener el teléfono del formulario.
    participant = Participant.objects.create(phone=phone)

    if Registration.objects.filter(event=event, participant=participant).exists():
        messages.warning(request, "Ya estás registrado en este evento.")
        return redirect('events:event_detail', slug=slug)

    # Crea la inscripción (registro) del participante en el evento.
    Registration.objects.create(event=event, participant=participant)
    messages.success(request, "¡Te has registrado exitosamente en el evento!")
    return redirect('events:event_detail', slug=slug)
