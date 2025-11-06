# ✅ Criterios de Aceptación — HU-12: Consulta de Disponibilidad de Espacios

---

## 🧩 Identificador
**HU-12 — Consulta de Disponibilidad de Espacios**

---

## 🎯 Descripción
Como usuario final, quiero consultar la disponibilidad de espacios en el parqueadero para decidir si ingreso o busco otro lugar, permitiendo así optimizar mi tiempo y facilitar la toma de decisiones.

---

## ✅ Criterios de Aceptación

| Nº | Criterio | Tipo | Resultado Esperado |
|----|-----------|------|--------------------|
| 1 | El usuario visualiza la cantidad de cupos disponibles en tiempo real. | Funcional | Se muestra en pantalla el número de espacios libres y ocupados de forma actualizada. |
| 2 | El sistema actualiza automáticamente la información cuando un vehículo entra o sale. | Integración | La disponibilidad cambia en tiempo real mediante SignalR o WebSocket. |
| 3 | Si no hay cupos disponibles, el sistema muestra el mensaje “Parqueadero lleno”. | Alterno | El usuario recibe una alerta visual y puede decidir no ingresar. |
| 4 | El sistema diferencia por tipo de vehículo (carro, moto, bicicleta). | Funcional | Se muestran los cupos libres por categoría. |
| 5 | Si ocurre un error de conexión o consulta, el sistema informa al usuario. | Excepción | Se muestra un mensaje “No se pudo obtener la disponibilidad, intente nuevamente”. |
| 6 | El tiempo de respuesta no debe superar los 2 segundos. | No funcional | Los datos de disponibilidad se cargan con baja latencia. |
| 7 | La información debe ser consistente con el backend y el sistema de cámaras. | Integración | No deben existir diferencias entre el dashboard del operador y la app del usuario. |

---

## ⚙️ Condiciones de Validación

- Probar al menos **tres escenarios**: parqueadero lleno, parcialmente ocupado y vacío.  
- Verificar sincronización entre **backend y frontend**.  
- Validar actualización de datos al registrar **entradas y salidas simultáneas**.  
- Simular desconexión del microservicio o del backend para probar los mensajes de error.  

---

## 🧠 Observaciones

- Los datos deben reflejarse en tiempo real con una latencia máxima de **1 segundo**.  
- El sistema debe mostrar una interfaz clara e intuitiva.  
- La información de cupos debe coincidir con el conteo físico del parqueadero.  
- El mensaje de error no debe mostrar información técnica.  

---

## 📆 Control de Cambios

| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|-------------|
| 1.0 | [dd/mm/aaaa] | Equipo ANPR-VISION | Versión inicial del documento de criterios de aceptación para la HU-12. |
| 1.1 | [dd/mm/aaaa] | Karol Natalia Osorio Poveda | Ajustes tras pruebas de integración con backend y microservicio. |

---
