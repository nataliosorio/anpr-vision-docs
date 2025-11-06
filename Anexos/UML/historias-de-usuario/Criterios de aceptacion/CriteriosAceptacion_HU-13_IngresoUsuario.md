# ✅ Criterios de Aceptación — HU-13: Ingreso del Usuario Final con Placa y Documento

---

## 🧩 Identificador
**HU-13 — Ingreso del Usuario Final con Placa y Documento**

---

## 🎯 Descripción
Como usuario final, quiero ingresar al sistema con mi placa y documento para ver la información relacionada con mi vehículo, incluyendo historial, pagos y alertas, garantizando un acceso rápido y seguro.

---

## ✅ Criterios de Aceptación

| Nº | Criterio | Tipo | Resultado Esperado |
|----|-----------|------|--------------------|
| 1 | El sistema permite ingresar usando la placa y documento del vehículo. | Funcional | El usuario accede correctamente sin necesidad de usuario y contraseña tradicionales. |
| 2 | El sistema valida que la combinación de placa y documento exista en la base de datos. | Funcional | Si los datos coinciden, se concede acceso; si no, se muestra mensaje de error. |
| 3 | Las credenciales viajan cifradas durante la autenticación. | Seguridad | Se implementa cifrado HTTPS/TLS y los tokens de sesión son seguros. |
| 4 | El usuario visualiza su información personal y la de su vehículo al ingresar. | Funcional | Se muestra el historial, estado de pago, y alertas asociadas al vehículo. |
| 5 | El sistema bloquea el acceso tras tres intentos fallidos consecutivos. | Seguridad | Se genera un mensaje: “Ha superado el número de intentos permitidos.” |
| 6 | El usuario puede cerrar sesión de forma segura. | Funcional | El token de autenticación expira y el sistema redirige al login. |
| 7 | Si ocurre un error de conexión, se notifica al usuario sin mostrar detalles técnicos. | Excepción | Se muestra un mensaje genérico y se registra el error en logs del sistema. |

---

## ⚙️ Condiciones de Validación

- Validar autenticación con **placas y documentos válidos e inválidos**.  
- Verificar cifrado de credenciales mediante **inspección de red (HTTPS)**.  
- Probar tres intentos fallidos consecutivos para confirmar el bloqueo temporal.  
- Validar cierre de sesión y expiración de token.  
- Revisar que la vista de información del vehículo cargue correctamente tras autenticación.  

---

## 🧠 Observaciones

- El tiempo máximo de respuesta para autenticación no debe superar **2 segundos**.  
- El sistema no debe permitir múltiples sesiones simultáneas con la misma placa y documento.  
- Los tokens de sesión deben expirar automáticamente tras **15 minutos de inactividad**.  
- Todos los eventos de autenticación deben registrarse para auditoría.  

---

## 📆 Control de Cambios

| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|-------------|
| 1.0 | [dd/mm/aaaa] | Equipo ANPR-VISION | Versión inicial del documento de criterios de aceptación para la HU-13. |
| 1.1 | [dd/mm/aaaa] | Karol Natalia Osorio Poveda | Ajustes de seguridad y pruebas de expiración de sesión. |

---
