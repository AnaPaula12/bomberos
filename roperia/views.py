from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Persona, RopaDeIncendio


def index(request):
    personas_list = Persona.objects.order_by('apellido')
    context = {
        'personas_list': personas_list,
    }
    return render(request, 'roperia/index.html', context)


def detalle_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    return render(request, 'roperia/detalle_persona.html', {'persona': persona})


def detalle_ropa(request, ropadeincendio_id):
    ropa = get_object_or_404(RopaDeIncendio, pk=ropadeincendio_id)
    return render(request, 'roperia/detalle_ropa.html', {'ropa': ropa})


def guardar(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    try:
        selected_prenda = persona.ropadeincendio_set.get(
            pk=request.POST['ropadeincendio']
            )
    except (KeyError, RopaDeIncendio.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'roperia/detalle_persona.html', {
            'persona': persona,
            'error_message': "You didn't select a choice.",
        })
    else:
        RopaDeIncendio.comodatario = persona
        RopaDeIncendio.comodatario.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse(
                'roperia:detalle_persona', args=(persona.id,))
                )