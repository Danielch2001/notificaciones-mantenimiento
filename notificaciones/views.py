from rest_framework import viewsets
from .models import Fotocopiadora, Notificacion, Tecnico, Mantenimiento
from .serializers import FotocopiadoraSerializer, NotificacionSerializer, TecnicoSerializer, MantenimientoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Fotocopiadora, Notificacion
from django.utils import timezone

class FotocopiadoraViewSet(viewsets.ModelViewSet):
    queryset = Fotocopiadora.objects.all()
    serializer_class = FotocopiadoraSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer

@api_view(['POST'])
def simular_notificacion(request):
    """
    Simula una notificación de mantenimiento para una fotocopiadora específica.
    """
    fotocopiadora_id = request.data.get("fotocopiadora_id")
    mensaje = request.data.get("mensaje", "Requiere mantenimiento urgente.")

    try:
        fotocopiadora = Fotocopiadora.objects.get(id=fotocopiadora_id)
        notificacion = Notificacion.objects.create(
            fotocopiadora=fotocopiadora,
            mensaje=mensaje,
            fecha=timezone.now(),
            estado="pendiente"
        )
        return Response({"message": "Notificación generada correctamente", "id": notificacion.id}, status=201)
    except Fotocopiadora.DoesNotExist:
        return Response({"error": "Fotocopiadora no encontrada"}, status=404)