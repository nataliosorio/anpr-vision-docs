# 🏗️ Arquitectura — ANPR VISION

Este módulo documenta la **arquitectura general del sistema ANPR VISION**, un ecosistema distribuido basado en microservicios, visión artificial e integración en tiempo real.

---

## 📂 Estructura de la Carpeta

04-arquitectura/
├── ADR/ # Architecture Decision Records
│ ├── ADR-001_Usar-Kafka.md
│ └── ADR-002_Backend-Onion.md
├── C4/ # Diagramas de arquitectura (modelo C4)
│ ├── C1_Context.mmd
│ ├── C2_Contenedores.mmd
│ ├── C3_Componentes.mmd
│ └── C4_Codigo.mmd
├── Documento-Arquitectura.md # Documento técnico de arquitectura
└── README.md # Guía general de la sección


---

## 🧠 Propósito

Esta documentación tiene como objetivo:
- Describir la **arquitectura técnica** del proyecto ANPR VISION.  
- Explicar las **decisiones clave (ADR)** que guían el diseño del sistema.  
- Proporcionar una **visión jerárquica (C4)** del software desde el contexto hasta el código.  

---

## 🧩 Contenido Principal

| Archivo | Descripción |
|----------|-------------|
| **ADR-001_Usar-Kafka.md** | Justificación del uso de Apache Kafka para comunicación asíncrona. |
| **ADR-002_Backend-Onion.md** | Decisión de adoptar arquitectura Onion en el backend. |
| **C1_Context.mmd** | Diagrama de contexto del sistema. |
| **C2_Contenedores.mmd** | Diagrama de contenedores y sus relaciones. |
| **C3_Componentes.mmd** | Componentes internos del backend. |
| **C4_Codigo.mmd** | Estructura del código en backend y microservicio. |
| **Documento-Arquitectura.md** | Explicación técnica completa de la arquitectura. |

---

## 🧰 Tecnologías Representadas
- **Backend:** ASP.NET Core 8, EF Core, SignalR  
- **Microservicio ANPR:** Python, OpenCV, YOLOv5, Tesseract OCR  
- **Mensajería:** Apache Kafka  
- **Frontend:** Angular + Ionic  
- **Base de Datos:** PostgreSQL  
- **Infraestructura:** Docker Compose

---

## 🧾 Referencias
- [Modelo C4](https://c4model.com/)  
- [Microsoft Clean/Onion Architecture](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures)  
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)  

---

> ✨ **ANPR VISION** — Arquitectura moderna, modular y escalable para control vehicular inteligente.
