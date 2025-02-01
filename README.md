# 🛠️ API de Notificaciones de Mantenimiento 🚀

Este repositorio contiene una **API RESTful** desarrollada con **Django y Django REST Framework**, diseñada para **gestionar y enviar notificaciones de mantenimiento** a una aplicación React externa. 📢

La API permite supervisar el estado de diversas **fotocopiadoras** en la empresa **TecnoQuito** y enviar alertas cuando se detectan **problemas** como:

- 🔴 **Bajo nivel de tóner**
- ⚠️ **Falta de papel**
- 🛠 **Revisión por alto uso**
- 🔧 **Reparación requerida**
- 🏭 **Mantenimiento preventivo**

---

## 🌐 Repositorio del Frontend
👉 La aplicación React que consume esta API se encuentra en el siguiente repositorio:  
**🔗 [[LINK_A_REACT_REPO](https://github.com/Danielch2001/gestion-fotocopiadoras)]** *(Actualiza este link)*

---

## 📌 ¿Qué puedes lograr con esta API?

1. **Gestión eficiente del mantenimiento:** Recibir alertas sobre el estado de las fotocopiadoras.
2. **Monitoreo en tiempo real:** Notificaciones inmediatas sobre problemas en los equipos.
3. **Optimización de costos:** Previene daños mayores al detectar problemas a tiempo.
4. **Interfaz administrativa:** Los administradores pueden revisar notificaciones y programar mantenimientos.
5. **Escalabilidad:** Puede integrarse con otros sistemas y reportes.

---

## ⚙️ Características principales

✔ **API RESTful** con Django Rest Framework  
✔ **PostgreSQL** como base de datos principal  
✔ **Autenticación y seguridad con tokens**  
✔ **CORS habilitado** para permitir el acceso desde React  
✔ **Sistema de notificaciones basado en eventos**  
✔ **Simulación de problemas en fotocopiadoras**  
✔ **Generación de reportes sobre mantenimiento**  

---

## 📥 Instalación

### 1️⃣ Clonar el repositorio
```sh
git clone https://github.com/Danielch2001/notificaciones-mantenimiento
cd NotificacionesMantenimientoDjango
```

### 2️⃣ Configurar entorno virtual y dependencias
```sh
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
pip install -r backend/requirements.txt
```

### 3️⃣ Configurar base de datos PostgreSQL
Crea una base de datos con:
```sql
CREATE DATABASE notificaciones_db;
```
Luego, configura las credenciales en `backend/.env`:
```sh
DATABASE_URL=postgres://USUARIO:CONTRASEÑA@localhost:5432/notificaciones_db
```

### 4️⃣ Ejecutar migraciones
```sh
cd backend
python manage.py makemigrations notificaciones
python manage.py migrate
```

### 5️⃣ Cargar datos de prueba (opcional)
```sh
python manage.py loaddata notificaciones/seed.json
```

### 6️⃣ Ejecutar el servidor
```sh
python manage.py runserver
```
La API estará disponible en:  
📌 `http://127.0.0.1:8000/api/`

---

## 🔌 Endpoints disponibles

### 📢 Notificaciones
| Método | URL | Descripción |
|--------|-----|-------------|
| GET | `/api/notificaciones/` | Obtener todas las notificaciones |
| POST | `/api/notificaciones/` | Crear una nueva notificación |
| DELETE | `/api/notificaciones/{id}/` | Eliminar una notificación |

### 🏭 Fotocopiadoras
| Método | URL | Descripción |
|--------|-----|-------------|
| GET | `/api/fotocopiadoras/` | Listar todas las fotocopiadoras |
| POST | `/api/fotocopiadoras/` | Agregar una nueva fotocopiadora |
| PATCH | `/api/fotocopiadoras/{id}/` | Actualizar el estado de una fotocopiadora |

### 🚨 Simulación de problemas
| Método | URL | Descripción |
|--------|-----|-------------|
| POST | `/api/simular/` | Simular una falla o requerimiento de mantenimiento |

Ejemplo de JSON para simular una notificación:
```json
{
  "fotocopiadora_id": 1,
  "mensaje": "Falta tóner en la impresora."
}
```

---

## 🎯 ¿Cómo funciona la simulación de notificaciones?

1. Un administrador puede enviar una solicitud `POST /api/simular/` para indicar que una fotocopiadora tiene un problema.
2. La API crea automáticamente una notificación en la base de datos.
3. La aplicación en React (ver repositorio 🔗 [[LINK_A_REACT_REPO](https://github.com/Danielch2001/gestion-fotocopiadoras)]) consume esta API y muestra las alertas en tiempo real.
4. Los técnicos pueden visualizar las notificaciones y resolver los problemas.

---

## 🚀 Beneficios para TecnoQuito

✅ **Automatización:** Reduce la carga de trabajo al detectar fallos automáticamente.  
✅ **Reducción de costos:** Evita reparaciones mayores al prevenir fallos tempranos.  
✅ **Mejora en el servicio:** Los clientes siempre tendrán equipos en óptimo estado.  
✅ **Historial de mantenimientos:** Permite generar reportes y planificar mantenimientos.  

---

## 📧 Contacto
Si tienes dudas, problemas o sugerencias, por favor abre un issue en este repositorio o contáctame a **daniel.chicaiza@udla.edu.ec** 📩

---

## 📌 ¿Qué sigue?

✅ Conectar la API con el frontend en React.  
✅ Agregar WebSockets para notificaciones en tiempo real.  
✅ Incluir un sistema de roles para diferenciar administradores y técnicos.  
