# ✅ Criterios de Aceptación — HU-01: Registrar Entrada de Vehículo

---

## 🧩 Identificador
**HU-01 — Registrar Entrada Automática de Vehículo**

---

## 🎯 Descripción
Como operador del parqueadero, quiero que el sistema registre automáticamente la entrada de los vehículos mediante el reconocimiento de matrículas, para agilizar el control de acceso y mantener un registro confiable de los ingresos.

---

## ✅ Criterios de Aceptación

| Nº | Criterio | Tipo | Resultado Esperado |
|----|-----------|------|--------------------|
| 1 | La cámara ANPR detecta correctamente la placa del vehículo al ingresar. | Funcional | El sistema muestra la matrícula detectada en el panel en tiempo real. |
| 2 | El sistema crea automáticamente un registro de entrada asociado a la placa. | Funcional | Se almacena la información del vehículo (placa, fecha, hora, tipo) en la base de datos con estado **Activo**. |
| 3 | Si el reconocimiento falla, se habilita el registro manual. | Alterno | El operador puede ingresar manualmente la placa y crear el registro de entrada. |
| 4 | Si el vehículo está en lista negra, el sistema bloquea el ingreso. | Seguridad | Se muestra una alerta visual y sonora al operador, y el registro no se crea. |
| 5 | El evento de detección genera una notificación al backend. | Integración | El microservicio ANPR envía la información al backend mediante Kafka o WebSocket. |
| 6 | El backend notifica al panel administrativo y actualiza la disponibilidad de cupos. | Integración | SignalR envía el evento al dashboard del operador y al sistema de control. |
| 7 | El registro queda disponible para el cálculo del tiempo y cobro posterior. | Funcional | El sistema asocia el registro a un posible evento de salida (RF-04 / RF-10). |

---

## ⚙️ Condiciones de Validación

- Se deben probar al menos **3 placas válidas y 2 con error** (placa ilegible o desconocida).  
- Las pruebas deben incluir escenarios con **cámara activa y cámara desconectada**.  
- El operador debe poder **cambiar a modo manual** sin reiniciar el sistema.  
- Todos los registros deben aparecer en la tabla de entradas activas del dashboard.  

---

## 🧠 Observaciones

- El sistema debe mostrar la detección en menos de **2 segundos** tras el ingreso.  
- Los registros se almacenan incluso si el backend pierde conexión temporal.  
- Los mensajes de error deben ser claros y no revelar información técnica.  
- El evento debe generar **una notificación persistente** en la interfaz administrativa.  

---

## 📆 Control de Cambios

| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|-------------|
| 1.0 | [dd/mm/aaaa] | Equipo ANPR-VISION | Versión inicial del documento de criterios de aceptación para la HU-01. |
| 1.1 | [dd/mm/aaaa] | Karol Natalia Osorio Poveda | Ajustes según pruebas de integración con microservicio ANPR. |

---
