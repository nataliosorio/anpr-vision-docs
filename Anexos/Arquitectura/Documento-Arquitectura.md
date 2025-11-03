# 🧩 Documento de Arquitectura — ANPR VISION

## 1. Introducción

El presente documento describe la arquitectura del sistema **ANPR VISION**, una plataforma integral de reconocimiento automático de matrículas (ANPR) diseñada para la gestión inteligente de parqueaderos.  
Su arquitectura se basa en principios de **modularidad**, **escalabilidad** y **resiliencia**, garantizando un desempeño óptimo en escenarios de tiempo real.

---

## 2. Enfoque de Diseño

La solución se ha construido bajo dos pilares arquitectónicos:

1. **Arquitectura Onion (Backend ASP.NET Core)**  
   - Promueve la separación de responsabilidades y bajo acoplamiento entre capas.  
   - Facilita las pruebas unitarias y el mantenimiento del código.  
   - Permite reemplazar tecnologías externas sin afectar el núcleo del dominio.

2. **Arquitectura Orientada a Eventos (Kafka + Microservicio ANPR)**  
   - Permite comunicación asíncrona entre componentes.  
   - Asegura la persistencia y entrega confiable de eventos.  
   - Mejora el rendimiento y tolerancia a fallos.

---

## 3. Decisiones Arquitectónicas (ADR)

A continuación se resumen las principales decisiones de diseño registradas en los **Architecture Decision Records (ADR)**:

| Código | Título | Descripción | Estado |
|--------|---------|-------------|--------|
| ADR-001 | Uso de Apache Kafka | Se adopta Kafka para comunicación asíncrona entre microservicios. | ✅ Implementado |
| ADR-002 | Arquitectura Onion | Se adopta Onion Architecture para el backend en .NET. | ✅ En uso |

---

## 4. Vistas Arquitectónicas — Modelo C4

La arquitectura del sistema se documenta siguiendo el modelo **C4**, que proporciona una representación jerárquica desde el contexto general hasta el código fuente.

### 🔹 **Nivel 1 — Contexto del Sistema (C1)**
Representa cómo **ANPR VISION** se relaciona con sus actores externos y otros sistemas.

📄 [`C1_Context.mmd`](./C4/C1_Context.mmd)

Principales actores:
- **Administrador:** gestiona parqueaderos, usuarios, cámaras y reportes.  
- **Empleado:** controla ingresos, alertas y cobros.  
- **Usuario final:** consulta historial, notificaciones y pagos.  
- **Cámaras ANPR:** capturan imágenes en tiempo real.

---

### 🔹 **Nivel 2 — Contenedores (C2)**
Muestra los principales **módulos o contenedores** del sistema y sus interacciones.

📄 [`C2_Contenedores.mmd`](./C4/C2_Contenedores.mmd)

Contenedores principales:
- **Backend API (.NET Core):** lógica de negocio y comunicación.  
- **Microservicio ANPR (Python):** detección de placas mediante IA.  
- **Frontend Web (Angular):** interfaz administrativa.  
- **App Móvil (Ionic):** interfaz de usuario final.  
- **Kafka:** canal de comunicación entre backend y microservicio.  
- **PostgreSQL:** almacenamiento persistente.

---

### 🔹 **Nivel 3 — Componentes (C3)**
Describe los **componentes internos del Backend**, sus responsabilidades y relaciones.

📄 [`C3_Componentes.mmd`](./C4/C3_Componentes.mmd)

Principales componentes:
- **Controllers:** exponen endpoints REST y hubs SignalR.  
- **Application Services:** casos de uso y reglas de negocio.  
- **Domain:** entidades y modelos base.  
- **Infrastructure:** repositorios, Kafka, EF Core.  
- **Notification Service:** envío de alertas en tiempo real.

---

### 🔹 **Nivel 4 — Código (C4)**
Desglosa la estructura interna de los módulos y servicios.

📄 [`C4_Codigo.mmd`](./C4/C4_Codigo.mmd)

Incluye:
- **VehicleIngressManager:** orquestador de detecciones.  
- **NotificationBusiness:** persistencia y emisión de notificaciones.  
- **CameraHandler (Python):** administración de streams RTSP.  
- **PlateDetector + OCRReader:** pipeline de detección y lectura de matrículas.  

---

## 5. Integración Tecnológica

| Tecnología | Rol en el sistema |
|-------------|------------------|
| **ASP.NET Core 8** | Backend API, lógica de negocio, SignalR |
| **Python + OpenCV + YOLOv5** | Microservicio ANPR, detección de matrículas |
| **Apache Kafka** | Comunicación asíncrona entre backend y microservicio |
| **PostgreSQL** | Base de datos relacional |
| **Angular / Ionic** | Frontend web y móvil |
| **Docker** | Contenedorización de servicios |
| **SignalR** | Comunicación en tiempo real (notificaciones) |

---

## 6. Seguridad y Escalabilidad

- **Autenticación JWT** y control de acceso basado en roles.  
- **Comunicación cifrada (HTTPS / WSS)** entre servicios.  
- **Despliegue en contenedores Docker Compose.**  
- **Kafka** garantiza la escalabilidad horizontal y tolerancia a fallos.  

---

## 7. Conclusiones

La arquitectura propuesta permite:
- Procesar detecciones en tiempo real sin bloquear la operación.  
- Integrar múltiples cámaras ANPR en paralelo.  
- Escalar fácilmente el microservicio de visión artificial.  
- Mantener un backend robusto, limpio y mantenible.  

> 📘 **ANPR VISION** es una solución modular, distribuida y lista para escalar hacia entornos productivos basados en microservicios.
