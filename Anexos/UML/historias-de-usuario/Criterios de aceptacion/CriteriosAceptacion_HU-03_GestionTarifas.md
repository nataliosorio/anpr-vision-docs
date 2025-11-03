# ✅ Criterios de Aceptación — HU-03: Gestión de Tarifas

---

## 🧩 Identificador
**HU-03 — Gestión de Tarifas**

---

## 🎯 Descripción
Como administrador, quiero gestionar las tarifas del sistema para definir los valores que se aplicarán según el tipo de vehículo, horario o duración, garantizando que los cálculos sean precisos y reflejen las políticas del parqueadero.

---

## ✅ Criterios de Aceptación

| Nº | Criterio | Tipo | Resultado Esperado |
|----|-----------|------|--------------------|
| 1 | El administrador puede crear nuevas tarifas especificando tipo de vehículo, franja horaria y valor. | Funcional | La tarifa se registra correctamente en la base de datos y queda disponible para su uso inmediato. |
| 2 | El sistema valida que no existan tarifas duplicadas o superpuestas. | Validación | Si existe una tarifa con la misma configuración, se muestra un mensaje: “Ya existe una tarifa activa con estos parámetros.” |
| 3 | El administrador puede editar o eliminar tarifas existentes. | Funcional | Los cambios se reflejan inmediatamente en el cálculo de pagos. |
| 4 | Las tarifas se aplican automáticamente en los cálculos de pago (RF-13). | Integración | El sistema usa la tarifa configurada según el horario y tipo de vehículo. |
| 5 | El sistema permite activar o desactivar tarifas sin eliminarlas. | Funcional | Las tarifas desactivadas no se aplican, pero permanecen registradas. |
| 6 | Si ocurre un error al guardar, el sistema muestra un mensaje de error. | Excepción | Se muestra: “No fue posible guardar la tarifa, intente nuevamente.” |
| 7 | Los cambios en tarifas quedan registrados en logs de auditoría. | Auditoría | Se almacena quién creó, editó o eliminó cada tarifa y cuándo. |

---

## ⚙️ Condiciones de Validación

- Crear, editar y eliminar tarifas desde la interfaz administrativa.  
- Verificar que los cálculos de pago (HU-15, RF-13) reflejen correctamente las nuevas tarifas.  
- Probar tarifas simultáneas en diferentes franjas horarias.  
- Validar comportamiento del sistema al intentar guardar tarifas duplicadas.  
- Confirmar que los logs registran cada acción de modificación o eliminación.  

---

## 🧠 Observaciones

- Los cambios de tarifas deben reflejarse **sin necesidad de reiniciar el sistema**.  
- Las tarifas inactivas deben conservar su historial para reportes y auditoría.  
- La interfaz debe prevenir errores de ingreso mediante validaciones automáticas.  
- El tiempo de respuesta máximo al guardar o editar tarifas no debe superar **1 segundo**.  

---

## 📆 Control de Cambios

| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|-------------|
| 1.0 | [dd/mm/aaaa] | Equipo ANPR-VISION | Versión inicial del documento de criterios de aceptación para la HU-03. |
| 1.1 | [dd/mm/aaaa] | Karol Natalia Osorio Poveda | Ajustes según validaciones de integridad y pruebas de actualización en tiempo real. |

---
