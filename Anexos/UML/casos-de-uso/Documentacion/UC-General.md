# 📘 Diagrama General de Casos de Uso — ANPR VISION

---

## 🧭 Propósito del Diagrama
El presente diagrama representa una vista general del comportamiento del sistema **ANPR VISION**, mostrando las interacciones entre los actores principales y los casos de uso que conforman el sistema.  
El objetivo es ilustrar cómo los diferentes componentes (cámaras, operadores, backend y usuarios) colaboran para lograr la automatización del reconocimiento de matrículas vehiculares, la gestión del parqueadero y la emisión de comprobantes.

---

## 👥 Actores Principales

| Actor | Descripción |
|-------|--------------|
| **Cámara ANPR** | Dispositivo encargado de capturar imágenes y enviar frames al microservicio de detección. |
| **Operador del Parqueadero** | Empleado que supervisa el ingreso y salida de vehículos, puede registrar manualmente y validar alertas. |
| **Administrador del Sistema** | Responsable de la configuración general: cámaras, roles, usuarios, tarifas y reportes. |
| **Conductor / Usuario** | Persona propietaria del vehículo, que ingresa o sale del parqueadero, consulta pagos o alertas. |
| **Sistema de Gestión / Backend** | Módulo central que coordina eventos entre el microservicio ANPR, la base de datos y los servicios web. |
| **Servicio de Impresión Local** | Aplicación cliente (Windows Service) encargada de imprimir tickets y facturas desde la API central. |

---

## 🧩 Casos de Uso Identificados

| Código | Nombre | Actor Principal | Relación |
|---------|---------|----------------|-----------|
| **UC-001** | Registrar Entrada de Vehículo | Sistema / Operador | `include` → UC-003, UC-004 |
| **UC-002** | Registrar Salida de Vehículo | Conductor / Usuario | — |
| **UC-003** | Detectar Placa | Cámara ANPR | `extend` → UC-011, `include` → UC-001, UC-004 |
| **UC-004** | Notificar Detección al Operador | Sistema Backend | `include` → UC-001 |
| **UC-005** | Consultar Disponibilidad de Cupos | Operador / Sistema | `include` → UC-001 |
| **UC-006** | Asignar Zona o Espacio | Operador | `include` → UC-005 |
| **UC-007** | Gestionar Tarifas y Tiempos | Operador | — |
| **UC-008** | Generar Ticket o Factura | Sistema Backend | `extend` → UC-001, UC-002 |
| **UC-009** | Enviar Ticket al Servicio de Impresión | Sistema Backend | `include` → UC-008 |
| **UC-010** | Gestionar Usuarios y Roles | Administrador | — |
| **UC-011** | Gestionar Cámaras y Dispositivos | Administrador | `extend` → UC-003 |
| **UC-012** | Visualizar Reportes y Estadísticas | Administrador | — |

---

## 🔗 Relaciones Entre Casos de Uso

| Tipo | Descripción | Ejemplo |
|------|--------------|----------|
| **Include (<<include>>)** | Un caso de uso depende de otro para completarse. | UC-001 incluye UC-004 (notificación al operador). |
| **Extend (<<extend>>)** | Un caso puede extender el comportamiento de otro bajo condiciones específicas. | UC-003 extiende UC-011 cuando requiere configuración de cámara. |

---

## ⚙️ Descripción General del Flujo

1. La **Cámara ANPR (UC-003)** detecta un vehículo y captura su matrícula.  
2. El sistema **notifica al operador (UC-004)** y crea un evento de **registro de entrada (UC-001)**.  
3. El operador puede consultar **disponibilidad de cupos (UC-005)** o **asignar espacio (UC-006)**.  
4. Al finalizar la estancia, el **usuario solicita salida (UC-002)**, y el sistema **genera factura o ticket (UC-008)**.  
5. El documento se envía al **servicio de impresión local (UC-009)**.  
6. El **administrador (UC-010, UC-011, UC-012)** gestiona cámaras, roles y estadísticas.  
7. Todo el flujo se ejecuta a través del **backend**, que coordina eventos entre los módulos y almacena la trazabilidad.

---

## 📊 Representación Visual

📁 `Diagrama/Diagrama_CasosUso_ANPR_VISION.png`

El diagrama UML muestra las interacciones entre los actores y los casos de uso mencionados, con relaciones `include` y `extend` que definen dependencias lógicas y extensiones condicionales del comportamiento del sistema.

---

## 🧠 Observaciones Técnicas
- El sistema está dividido entre **backend**, **microservicio de visión artificial (ANPR)** y **servicio de impresión local**.  
- La comunicación entre módulos usa **SignalR, Kafka y REST API**.  
- Todos los flujos de detección generan **notificaciones en tiempo real**.  
- Se implementa **control de acceso basado en roles (RBAC)** para todos los módulos administrativos.

---

## 📆 Control de Cambios
| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|--------------|
| 1.0 | [dd/mm/aaaa] | Equipo ANPR-VISION | Versión inicial del documento. |
| 1.1 | [dd/mm/aaaa] | [Tu nombre] | Integración del diagrama actualizado. |

---
