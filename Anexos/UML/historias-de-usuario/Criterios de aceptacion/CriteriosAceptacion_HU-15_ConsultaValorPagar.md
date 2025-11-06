# ✅ Criterios de Aceptación — HU-15: Consulta del Valor a Pagar Antes de Salir

---

## 🧩 Identificador
**HU-15 — Consulta del Valor a Pagar Antes de Salir**

---

## 🎯 Descripción
Como usuario final, quiero consultar cuánto debo pagar hasta el momento para poder preparar el pago antes de salir del parqueadero, evitando retrasos y mejorando la experiencia del servicio.

---

## ✅ Criterios de Aceptación

| Nº | Criterio | Tipo | Resultado Esperado |
|----|-----------|------|--------------------|
| 1 | El usuario puede consultar el monto total a pagar en cualquier momento antes de salir. | Funcional | El sistema muestra el valor actualizado según el tiempo transcurrido y la tarifa activa. |
| 2 | El cálculo se realiza automáticamente según las tarifas configuradas. | Funcional | El sistema aplica correctamente la tarifa por tipo de vehículo, horario o membresía. |
| 3 | El usuario puede visualizar el detalle del cálculo (tiempo, tarifa aplicada, monto acumulado). | Funcional | Se presenta un resumen con los datos utilizados para el cálculo. |
| 4 | Si el usuario tiene una membresía activa, se aplica el descuento o tarifa correspondiente. | Alterno | El valor mostrado refleja el beneficio del plan o membresía. |
| 5 | Si el vehículo no tiene un registro activo, el sistema muestra un mensaje informativo. | Excepción | Aparece: “No se encontró un registro activo para esta placa.” |
| 6 | El cálculo debe realizarse en tiempo real sin recargar la página. | Integración | SignalR actualiza el monto automáticamente a medida que pasa el tiempo. |
| 7 | El usuario puede descargar o visualizar un comprobante previo al pago. | Funcional | Se muestra un resumen descargable en formato PDF o ticket. |

---

## ⚙️ Condiciones de Validación

- Probar con vehículos **con diferentes tipos de tarifa (por hora, por fracción, por membresía)**.  
- Validar que los cálculos sean consistentes con los valores configurados por el administrador (RF-09).  
- Confirmar actualización automática del monto sin intervención del usuario.  
- Probar escenarios de error (placa inexistente, vehículo ya salido, desconexión de red).  

---

## 🧠 Observaciones

- El cálculo del valor debe realizarse en menos de **1 segundo**.  
- Los resultados deben ser precisos y coincidir con el monto final del ticket de salida.  
- La interfaz debe permitir consultar sin necesidad de autenticación adicional si ya está logueado.  
- Los mensajes deben ser claros, sin mostrar información técnica.  

---

## 📆 Control de Cambios

| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|-------------|
| 1.0 | [dd/mm/aaaa] | Equipo ANPR-VISION | Versión inicial del documento de criterios de aceptación para la HU-15. |
| 1.1 | [dd/mm/aaaa] | Karol Natalia Osorio Poveda | Ajustes según validaciones de cálculo de tarifas dinámicas. |

---
