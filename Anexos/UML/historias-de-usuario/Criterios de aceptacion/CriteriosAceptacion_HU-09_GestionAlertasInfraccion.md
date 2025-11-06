# ✅ Criterios de Aceptación — HU-09: Gestión de Alertas de Infracción

---

## 🧩 Identificador
**HU-09 — Gestión y Visualización de Alertas de Infracción**

---

## 🎯 Descripción
Como trabajador, quiero visualizar y gestionar las alertas de infracción para notificar al cliente o registrar eventos importantes, garantizando el control y la trazabilidad de las infracciones detectadas en el parqueadero.

---

## ✅ Criterios de Aceptación

| Nº | Criterio | Tipo | Resultado Esperado |
|----|-----------|------|--------------------|
| 1 | El trabajador puede visualizar todas las alertas activas y su estado (pendiente, atendida, cerrada). | Funcional | El sistema muestra una lista actualizada con la información de cada infracción. |
| 2 | El trabajador puede registrar nuevas alertas asociadas a una placa o persona. | Funcional | La alerta se guarda correctamente en la base de datos y genera notificación automática (RF-05, RF-18). |
| 3 | Las alertas se generan automáticamente cuando un vehículo en lista negra intenta ingresar. | Integración | Se crea una alerta vinculada con la lista negra (RF-07). |
| 4 | El trabajador puede marcar una alerta como resuelta o añadir observaciones. | Funcional | El estado de la alerta cambia a “Cerrada” y se actualiza en la interfaz. |
| 5 | El sistema envía notificaciones en tiempo real al administrador cuando se genera una nueva alerta. | Integración | SignalR actualiza el dashboard administrativo inmediatamente. |
| 6 | Si ocurre un error al registrar o cargar alertas, el sistema muestra un mensaje informativo. | Excepción | Aparece: “No fue posible procesar la alerta, intente nuevamente.” |
| 7 | Todas las acciones sobre alertas quedan registradas en logs para auditoría. | Auditoría | Se almacena usuario, fecha, acción y tipo de alerta. |

---

## ⚙️ Condiciones de Validación

- Verificar la creación y actualización de alertas tanto manuales como automáticas.  
- Comprobar la correcta sincronización con la lista negra y las notificaciones.  
- Validar los permisos de acceso: solo los trabajadores pueden gestionarlas, los administradores solo visualizarlas.  
- Confirmar la actualización automática de la interfaz sin necesidad de recargar la página.  
- Revisar registros en logs y base de datos para trazabilidad completa.  

---

## 🧠 Observaciones

- Las alertas deben mostrarse con prioridad visual en el panel de empleados y administradores.  
- El sistema debe soportar distintos tipos de alertas (infracción, intento de acceso, error de cámara, etc.).  
- Las notificaciones deben incluir fecha, tipo de alerta y descripción breve.  
- Los mensajes deben ser claros, sin exponer información técnica o sensible.  

---

## 📆 Control de Cambios

| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|-------------|
| 1.0 | [dd/mm/aaaa] | Equipo ANPR-VISION | Versión inicial del documento de criterios de aceptación para la HU-09. |
| 1.1 | [dd/mm/aaaa] | Karol Natalia Osorio Poveda | Ajustes tras integración con módulo de notificaciones (SignalR). |

---
