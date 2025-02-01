import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from notificaciones.models import Fotocopiadora, Notificacion, Tecnico, Mantenimiento

# 📌 Insertar fotocopiadoras (30 datos)
fotocopiadoras_data = [
    ("Canon MX922", "Canon", "Oficina de Ventas"),
    ("Xerox Phaser 3020", "Xerox", "Almacén"),
    ("Epson EcoTank 789", "Epson", "Oficina Cuenca"),
    ("HP LaserJet 456", "HP", "Oficina Guayaquil"),
    ("Canon X123", "Canon", "Oficina Quito"),
    ("Brother MFC-J995DW", "Brother", "Oficina de Recursos Humanos"),
    ("Ricoh MP 301", "Ricoh", "Oficina Administrativa"),
    ("Lexmark MB2236adw", "Lexmark", "Oficina Técnica"),
    ("Kyocera ECOSYS P5021cdw", "Kyocera", "Oficina de Proyectos"),
    ("Dell E310dw", "Dell", "Oficina de TI"),
    ("HP Color LaserJet Pro MFP M477fdw", "HP", "Oficina de Marketing"),
    ("Canon imageCLASS MF445dw", "Canon", "Oficina Legal"),
    ("Xerox WorkCentre 6515", "Xerox", "Sala de Juntas"),
    ("Epson WorkForce WF-2760DWF", "Epson", "Oficina de Diseño"),
    ("Brother HL-L8360CDW", "Brother", "Oficina de Ventas Internacionales"),
]

# Generar datos adicionales aleatorios para completar 30
for i in range(15):  # 15 más para llegar a 30
    Fotocopiadora.objects.create(
        modelo=f"Modelo {i+1}", 
        marca=f"Marca {random.choice(['A', 'B', 'C', 'D', 'E'])}", 
        ubicacion=f"Ubicación {random.choice(['A', 'B', 'C', 'D', 'E'])}",
        contador_impresiones=random.randint(1000, 60000),
        toner_actual=random.randint(5, 100),
        ultima_revision=datetime.now() - timedelta(days=random.randint(30, 365))
    )

# Insertar técnicos (puedes mantener los mismos o agregar más)
tecnicos_data = [
    ("Carlos Méndez", "carlos@empresa.com", "0991234567"),
    ("Laura Pérez", "laura@empresa.com", "0997654321"),
    ("Fernando Díaz", "fernando@empresa.com", "0993344556"),
]

for nombre, correo, telefono in tecnicos_data:
    Tecnico.objects.create(nombre=nombre, correo=correo, telefono=telefono)

# 📌 Insertar notificaciones (30 datos)
fotocopiadoras = Fotocopiadora.objects.all()
mensajes_notificacion = [
    "Nivel de tóner bajo",
    "Mantenimiento preventivo requerido",
    "Contador de impresiones alto",
    "Error de hardware detectado"
]

for _ in range(30):  # Cambiar a 30 para notificaciones
    Notificacion.objects.create(
        fotocopiadora=random.choice(fotocopiadoras),
        mensaje=random.choice(mensajes_notificacion),
        estado="pendiente"
    )

print("✅ Datos insertados en la base de datos.")
