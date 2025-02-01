from rest_framework import serializers
from .models import Fotocopiadora, Notificacion, Tecnico, Mantenimiento  # Asegúrate de importar Mantenimiento

class FotocopiadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotocopiadora
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'

# ✅ Agregar este serializador si falta
class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
