from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notificaciones.views import FotocopiadoraViewSet, NotificacionViewSet, TecnicoViewSet, MantenimientoViewSet, simular_notificacion

router = DefaultRouter()
router.register('fotocopiadoras', FotocopiadoraViewSet)
router.register('notificaciones', NotificacionViewSet)
router.register('tecnicos', TecnicoViewSet)
router.register('mantenimientos', MantenimientoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/simular/', simular_notificacion, name="simular_notificacion"),
]
