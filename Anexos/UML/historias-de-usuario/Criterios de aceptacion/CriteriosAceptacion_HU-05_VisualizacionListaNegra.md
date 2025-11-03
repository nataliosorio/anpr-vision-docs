# ✅ Criterios de Aceptación — HU-05: Visualización de la Lista Negra

---

## 🧩 Identificador
**HU-05 — Visualización de la Lista Negra**

---

## 🎯 Descripción
Como administrador o trabajador, quiero visualizar y gestionar la lista negra de vehículos o personas restringidas, para evitar accesos no autorizados y mejorar el control de seguridad del parqueadero.

---

## ✅ Criterios de Aceptación

| Nº | Criterio | Tipo | Resultado Esperado |
|----|-----------|------|--------------------|
| 1 | El sistema muestra una lista actualizada de todos los vehículos o personas restringidas. | Funcional | La interfaz carga la lista completa desde la base de datos en tiempo real. |
| 2 | El administrador puede agregar nuevos registros a la lista negra indicando la placa o identificación. | Funcional | El registro se guarda correctamente y aparece inmediatamente en la lista. |
| 3 | Los trabajadores pueden consultar pero no eliminar registros (según permisos). | Seguridad | El sistema respeta los roles definidos en RF-15. |
| 4 | Si un vehículo en lista negra intenta ingresar, el sistema genera una alerta automática. | Integración | Se emite una notificación en tiempo real (RF-05, RF-18). |
| 5 | El administrador puede eliminar o desactivar registros de la lista negra. | Funcional | El registro desaparece de la lista visible pero queda almacenado para auditoría. |
| 6 | Si la consulta falla, el sistema muestra un mensaje informativo. | Excepción | Aparece: “No fue posible cargar los registros, intente nuevamente.” |
| 7 | Todas las acciones (agregar, eliminar, modificar) quedan registradas en logs de auditoría. | Auditoría | Se almacena usuario, fecha y acción realizada. |

---

## ⚙️ Condiciones de Validación

- Probar la creación, consulta, edición y eliminación de registros en distintos roles (administrador y trabajador).  
- Verificar que los vehículos en lista negra generen alerta automática al intentar ingresar.  
- Confirmar que los datos se sincronizan correctamente entre módulos de seguridad y notificaciones.  
- Validar persistencia de registros tras reiniciar el sistema.  
- Revisar logs para asegurar trazabilidad completa de acciones.  

---

## 🧠 Observaciones

- Las alertas deben mostrarse también en el dashboard administrativo y de empleados.  
- El sistema debe impedir duplicar una placa o identificación en la lista negra.  
- La lista debe actualizarse automáticamente sin necesidad de recargar la página.  
- Los mensajes deben ser claros y sin información técnica innecesaria.  

---

## 📆 Control de Cambios

| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|-------------|
| 1.0 | [dd/mm/aaaa] | Equipo ANPR-VISION | Versión inicial del documento de criterios de aceptación para la HU-05. |
| 1.1 | [dd/mm/aaaa] | Karol Natalia Osorio Poveda | Ajustes tras pruebas de sincronización de alertas y roles de usuario. |

---
