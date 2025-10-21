# 📋 Gestión del Proyecto — ANPR-VISION

📘 Archivo: `01-gestion-proyecto/README.md`

El módulo **Gestión del Proyecto** recopila toda la documentación administrativa, técnica y de seguimiento del desarrollo del sistema **ANPR-VISION**, un software de reconocimiento automático de matrículas (ANPR) enfocado en la gestión inteligente de parqueaderos.

Su propósito es mantener un control estructurado del avance del proyecto, desde el anteproyecto inicial hasta la identificación de riesgos, cronogramas y actas de reunión.

---

## 🧭 Objetivos del Módulo

- Centralizar la documentación de gestión y planeación del proyecto.  
- Dar trazabilidad a los avances, decisiones y entregas.  
- Estandarizar el formato de documentos administrativos.  
- Facilitar auditorías, revisiones y presentaciones del equipo ante el cliente o el SENA.

---

## 🗂 Estructura de Carpetas

| Carpeta | Contenido | Descripción |
|----------|------------|-------------|
| **01-anteproyecto/** | `Anteproyecto.md`, `Objetivos.md`, `Alcance.md`, etc. | Contiene la propuesta inicial del proyecto: justificación, objetivos, alcance, problemática, y recursos necesarios. |
| **02-cronograma/** | `Cronograma.xlsx`, `Hitos.md` | Incluye el cronograma Gantt y los hitos del proyecto con sus responsables, dependencias y duraciones. |
| **03-actas/** | `plantilla_acta.md`, `YYYY-MM-DD_acta.md`, `README.md` | Registra las actas oficiales de reuniones, con su formato estandarizado y seguimiento de compromisos. |
| **04-riesgos/** | `MatrizRiesgos.xlsx`, `README.md` | Documento de identificación, evaluación y mitigación de riesgos técnicos, de planificación y operativos. |

---

## 🧩 Flujo de Actualización

1. **Desarrollo del contenido:**  
   Cada subcarpeta se mantiene actualizada por el responsable asignado.  
2. **Control de versiones:**  
   Los cambios se registran mediante ramas `feature/docs-*` y se fusionan a `develop`.  
3. **Validación:**  
   Los documentos clave (cronograma, riesgos, actas importantes) deben ser revisados por el líder del proyecto antes de integrarse a `qa`.  
4. **Publicación:**  
   Las versiones estables de documentación se liberan como `release.docs.vX.Y.Z` y se enlazan con el repositorio principal del sistema.

---

## 👥 Roles y Responsabilidades

| Integrante | Rol | Responsabilidades |
|-------------|-----|-------------------|
| **Karol Natalia Osorio Poveda** | Líder del Proyecto / Backend / Frontend / Móvil | Coordinación general, documentación de gestión y control de versiones. |
| **Yerson Stiven Cuellar Rubiano** | Desarrollador Frontend y Móvil | Apoyo en documentación técnica, cronogramas y evidencia de entregas. |
| **Aníbal Alvarado** | Backend / Microservicio / IA | Responsable técnico del microservicio ANPR, documentación de arquitectura y gestión de riesgos técnicos. |

---

## 🧾 Entregables Principales

| Documento | Descripción | Responsable |
|------------|-------------|--------------|
| **Anteproyecto** | Documento base con la justificación y alcance del proyecto. | Karol Natalia Osorio |
| **Cronograma** | Plan de trabajo con tareas, fechas y dependencias. | Equipo |
| **Actas** | Registro de reuniones, decisiones y compromisos. | Karol Natalia Osorio |
| **Matriz de Riesgos** | Identificación, impacto y plan de mitigación. | Aníbal Alvarado |

---

## 🧱 Integración con la Documentación General

Este módulo hace parte del repositorio principal de documentación:  
📂 `ANPR-VISION-DOCS`

Y se relaciona con las siguientes carpetas:

- **00-presentacion/** → Portada, pitch y presentación institucional.  
- **03-requisitos/** → Documento SRS y casos de uso.  
- **04-arquitectura/** → Diagramas C4, ADRs y estructura del sistema.  
- **08-implementacion/** → Detalle técnico del código y despliegues.  

---

## ✅ Buenas Prácticas

- Nombrar los archivos con **fechas o versiones** (`YYYY-MM-DD` o `vX.Y.Z`).  
- Evitar espacios o acentos en nombres de carpetas.  
- Mantener los documentos actualizados después de cada entrega o reunión.  
- Documentar todos los acuerdos importantes mediante actas oficiales.  
- Usar el formato Markdown (`.md`) para mantener compatibilidad con GitHub.

---

📅 *Última actualización:* 2025-10-20  
✍️ *Elaborado por:* Karol Natalia Osorio Poveda  
📘 *Versión:* v1.0 — Módulo de Gestión del Proyecto ANPR-VISION
