# ✅ Criterios de Aceptación — HU-14: Visualizar Alertas o Notificaciones del Vehículo

---

## 🧩 Identificador
**HU-14 — Visualización de Alertas o Notificaciones del Vehículo**

---

## 🎯 Descripción
Como usuario final, quiero ver las alertas o notificaciones asociadas a mi vehículo para estar informado de cualquier infracción, novedad o actualización importante del sistema.

---

## ✅ Criterios de Aceptación

| Nº | Criterio | Tipo | Resultado Esperado |
|----|-----------|------|--------------------|
| 1 | El usuario puede visualizar en tiempo real las alertas o notificaciones relacionadas con su vehículo. | Funcional | Las notificaciones aparecen automáticamente en la interfaz sin necesidad de recargar la página. |
| 2 | Las alertas incluyen información relevante (fecha, tipo, mensaje y estado). | Funcional | Cada notificación muestra datos completos y legibles para el usuario. |
| 3 | El sistema marca las notificaciones como leídas al ser abiertas. | Funcional | El estado cambia a “leída” y desaparece del contador de nuevas notificaciones. |
| 4 | Las notificaciones se actualizan automáticamente mediante SignalR o WebSocket. | Integración | Se reciben en tiempo real desde el backend sin retraso perceptible. |
| 5 | Si el sistema no puede cargar las notificaciones, muestra un mensaje informativo. | Excepción | Aparece “No se pudieron cargar las notificaciones, intente nuevamente.” |
| 6 | El usuario puede eliminar o archivar notificaciones leídas. | Funcional | Las notificaciones se eliminan visualmente pero permanecen registradas en la base de datos. |
| 7 | Cada notificación queda registrada en el historial del sistema. | Auditoría | El backend guarda los eventos con fecha, usuario y tipo de alerta. |

---

## ⚙️ Condiciones de Validación

- Validar recepción de alertas en tiempo real mediante pruebas con SignalR.  
- Comprobar que al marcar como “leída” se actualiza el estado en base de datos.  
- Probar desconexión de red para verificar mensaje de error.  
- Generar alertas de diferentes tipos (infracción, membresía, pago pendiente).  
- Confirmar que las notificaciones son persistentes tras reiniciar la aplicación.  

---

## 🧠 Observaciones

- El tiempo de recepción de alertas no debe superar **1 segundo** desde su emisión.  
- Las notificaciones deben tener un diseño visual coherente con el panel del sistema.  
- Las alertas críticas deben destacarse visualmente (ícono o color).  
- Los mensajes no deben mostrar información técnica o confidencial.  

---

## 📆 Control de Cambios

| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|-------------|
| 1.0 | [dd/mm/aaaa] | Equipo ANPR-VISION | Versión inicial del documento de criterios de aceptación para la HU-14. |
| 1.1 | [dd/mm/aaaa] | Karol Natalia Osorio Poveda | Ajustes tras pruebas de recepción de alertas en tiempo real. |

---
