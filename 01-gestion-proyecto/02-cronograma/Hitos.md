# 🗓 Cronograma General — Proyecto ANPR-VISION

**Duración del Proyecto:** 2025-07-01 → 2025-10-30 (4 meses)  
**Versión del documento:** v1.0  
**Responsable:** Karol Natalia Osorio Poveda  
**Última actualización:** 2025-10-20  

---

## 🧩 Descripción General

El cronograma del proyecto **ANPR-VISION** se desarrolló en un periodo de **6 meses académicos**, organizando las tareas por fases secuenciales: planificación, análisis, diseño, desarrollo, pruebas y cierre.  
Cada tarea cuenta con su responsable, duración estimada y dependencias.  
El documento principal (`Cronograma.xlsx`) presenta la planificación visual tipo **Gantt**, mientras que este archivo (`Hitos.md`) resume los **entregables y puntos de control clave**.

---

## 🧱 Fases Principales

| Fase | Periodo | Actividades | Responsable |
|------|----------|-------------|--------------|
| **1. Inicio del Proyecto** | 2025-07-01 → 2025-07-05 | Inicio formal del proyecto, definición de alcance, conformación del equipo. | Karol |
| **2. Recolección y Análisis** | 2025-07-06 → 2025-07-31 | Entrevistas, levantamiento de requerimientos, elaboración del SRS. | Equipo / Karol |
| **3. Arquitectura y Diseño** | 2025-08-01 → 2025-08-31 | Arquitectura C4 + ADR, modelado UML, base de datos y prototipos UX/UI. | Aníbal / Equipo |
| **4. Desarrollo e Integración** | 2025-09-01 → 2025-09-30 | Backend, microservicio de visión (OCR), frontend Angular, integración Kafka + SignalR. | Karol / Aníbal / Yerson |
| **5. QA y Capacitación** | 2025-10-01 → 2025-10-25 | Pruebas funcionales, documentación, capacitación a usuarios finales. | Equipo QA / Equipo |
| **6. Publicación y Cierre** | 2025-10-26 → 2025-10-30 | Release v1.0, publicación en CIES, cierre formal y entrega final. | Karol / DevOps |

---

## 🚀 Hitos del Proyecto

| ID | Hito | Fecha | Responsable | Dependencias | Estado |
|----|-------|--------|--------------|--------------|---------|
| 4 | ✅ **Aprobación del SRS (Documento de Requerimientos)** | 2025-08-01 | Cliente | SRS (Tarea 3) | 🟢 Planeado |
| 6 | ✅ **Aprobación de Arquitectura** | 2025-08-16 | Cliente | Arquitectura (Tarea 5) | 🟢 Planeado |
| 12 | ⚙️ **MVP Funcional Integrado** | 2025-10-01 | Equipo | Integración Kafka + SignalR | 🟢 Planeado |
| 15 | 🚀 **Release v1.0 (Staging → Producción)** | 2025-10-26 | DevOps | QA / Capacitación | 🟢 Planeado |
| 16 | 📣 **Publicación CIES / Presentación Final** | 2025-10-27 | Karol | Release v1.0 | 🟢 Planeado |
| 17 | 🏁 **Cierre Formal del Proyecto** | 2025-10-30 | Karol | Publicación CIES | 🟢 Planeado |

---

## 📊 Resumen de Actividades

| ID | Tarea | Responsable | Inicio | Fin | Duración (días) | Estado |
|----|--------|--------------|--------|-----|-----------------|---------|
| 1 | Inicio de proyecto | Karol | 2025-07-01 | 2025-07-05 | 5 | ✅ Done |
| 2 | Recolección de información | Equipo | 2025-07-06 | 2025-07-20 | 15 | ✅ Done |
| 3 | Documento SRS | Karol | 2025-07-15 | 2025-07-31 | 14 | 🟡 En revisión |
| 5 | Arquitectura (C4 + ADR) | Aníbal | 2025-08-02 | 2025-08-15 | 14 | 🟡 Planeado |
| 7 | Diseño (UML + BD + UX) | Equipo | 2025-08-17 | 2025-08-31 | 15 | 🟡 Planeado |
| 8 | Backend Core | Karol | 2025-09-01 | 2025-09-15 | 15 | 🟡 Planeado |
| 9 | Microservicio ANPR (OCR) | Aníbal | 2025-09-01 | 2025-09-20 | 20 | 🟡 Planeado |
| 10 | Frontend Angular | Yerson | 2025-09-05 | 2025-09-25 | 21 | 🟡 Planeado |
| 11 | Integración Kafka + SignalR | Equipo | 2025-09-21 | 2025-09-30 | 10 | 🟡 Planeado |
| 13 | QA/Testing | Equipo QA | 2025-10-02 | 2025-10-20 | 19 | 🟡 Planeado |
| 14 | Capacitación a usuarios | Equipo | 2025-10-21 | 2025-10-25 | 5 | 🟡 Planeado |
| 15 | Release v1.0 | DevOps | 2025-10-26 | 2025-10-26 | 1 | 🟡 Planeado |
| 16 | Publicación CIES | Karol | 2025-10-27 | 2025-10-27 | 1 | 🟡 Planeado |
| 17 | Cierre del proyecto | Karol | 2025-10-28 | 2025-10-30 | 3 | 🟡 Planeado |

---

## 🧭 Observaciones Generales

- El **SRS y la Arquitectura** son prerrequisitos críticos antes de iniciar el desarrollo.  
- La fase de desarrollo (septiembre) será concurrente entre backend, frontend y microservicio, sincronizada mediante **Kafka**.  
- Se contempla un **MVP funcional el 1 de octubre**, para validación temprana con el cliente.  
- La entrega oficial **Release v1.0** se prevé el **26 de octubre**, seguida de la **presentación CIES** y cierre del proyecto.

---

## 📎 Archivos Relacionados

- 📊 [`Cronograma.xlsx`](./Cronograma.xlsx) — Diagrama de Gantt completo del proyecto.  
- 🧾 [`Hitos.md`](./Hitos.md) — Documento actual (resumen de hitos).  
- 📘 `/01-gestion-proyecto/actas/` — Registro de reuniones y decisiones.  
- 📗 `/03-requisitos/` — Documento SRS y casos de uso.  
- 📙 `/04-arquitectura/` — Diagramas C4 y ADRs.

---

✍️ *Elaborado por:* Karol Natalia Osorio Poveda  
📅 *Fecha de elaboración:* 2025-10-20  
🧩 *Versión:* v1.0 — Cronograma inicial aprobado para seguimiento.
