# ✅ Criterios de Aceptación — HU-02: Registrar Salida de Vehículo

---

## 🧩 Identificador
**HU-02 — Registrar Salida de Vehículo**

---

## 🎯 Descripción
Como operador del parqueadero, quiero registrar la salida del vehículo mediante el reconocimiento de la matrícula, para calcular el valor a pagar y liberar el cupo ocupado en el sistema.

---

## ✅ Criterios de Aceptación

| Nº | Criterio | Tipo | Resultado Esperado |
|----|-----------|------|--------------------|
| 1 | La cámara ANPR detecta la matrícula del vehículo al salir. | Funcional | El sistema reconoce la placa y la asocia al registro de entrada correspondiente. |
| 2 | El sistema calcula automáticamente el valor a pagar. | Funcional | Se genera el monto en función de la tarifa configurada, el tipo de vehículo y el tiempo de permanencia. |
| 3 | Si el vehículo tiene membresía activa, no se genera cobro. | Alterno | El sistema valida el estado de membresía y aplica tarifa cero o preferencial. |
| 4 | Si no se detecta la placa, el operador puede registrar la salida manualmente. | Alterno | Se permite la búsqueda por número de placa o documento del cliente. |
| 5 | El sistema genera un ticket o factura de salida. | Integración | El ticket se crea en el backend y se envía al servicio de impresión local. |
| 6 | El cupo del parqueadero se actualiza en tiempo real. | Funcional | El sistema incrementa la cantidad de cupos disponibles. |
| 7 | El evento de salida se registra en el historial del vehículo. | Funcional | Se guarda la fecha y hora de salida con trazabilidad completa (automático o manual). |

---

## ⚙️ Condiciones de Validación

- Probar con al menos **tres tipos de tarifa diferentes**.  
- Verificar flujo con **vehículos con y sin membresía**.  
- Comprobar generación de ticket en el **servicio de impresión local (POS)**.  
- Validar que el sistema **actualice la disponibilidad de cupos** tras cada salida.  

---

## 🧠 Observaciones

- El cálculo del cobro debe realizarse en menos de **2 segundos**.  
- Las transacciones deben registrarse en la base de datos con control de auditoría.  
- Los registros deben conservar el vínculo entre el evento de entrada y salida.  
- El operador puede visualizar un resumen antes de confirmar la salida.  

---

## 📆 Control de Cambios

| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|-------------|
| 1.0 | [dd/mm/aaaa] | Equipo ANPR-VISION | Versión inicial del documento de criterios de aceptación para la HU-02. |
| 1.1 | [dd/mm/aaaa] | Karol Natalia Osorio Poveda | Ajustes según validaciones de cobro y flujo de salida. |

---
