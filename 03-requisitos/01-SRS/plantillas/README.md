# 📗 Especificación de Requerimientos de Software (SRS)

> Proyecto: **ANPR VISION — Sistema de Reconocimiento Automático de Matrículas**  
> Programa: **Análisis y Desarrollo de Software (ADSO - SENA)**  
> Versión del documento: **1.0**  
> Fecha de actualización: **29/10/2025**  

---

## 🧩 Descripción General

El presente documento **SRS (Software Requirements Specification)** detalla los requerimientos funcionales y no funcionales del sistema **ANPR VISION**, una plataforma basada en inteligencia artificial y visión por computadora para el reconocimiento automático de matrículas vehiculares (ANPR).

El propósito del documento es servir como guía técnica y funcional para el desarrollo, validación y mantenimiento del sistema, garantizando trazabilidad entre los requerimientos, los casos de uso y las historias de usuario.

---

## 🧱 Estructura del Documento

El documento completo se encuentra en `Plantilla-SRS.docx` y se organiza conforme al estándar **IEEE 830**, dividido en las siguientes secciones:

| Nº | Sección | Descripción |
|----|----------|-------------|
| **1** | **Marco conceptual y organización** | Describe el contexto, propósito, alcance y objetivos del sistema. |
| **2** | **Descripción general** | Define las características de los usuarios, las perspectivas del sistema y sus restricciones. |
| **3** | **Requerimientos específicos** | Lista los requerimientos funcionales (RF) y no funcionales (RNF). |
| **4** | **Casos de uso y diagramas UML** | Presenta los diagramas y la caracterización de los casos de uso. |
| **5** | **Anexos y control de versiones** | Contiene mockups, diagramas y registro de cambios. |

---

## ⚙️ Componentes Principales del Sistema

- **Microservicio ANPR (Python):** Procesa video en tiempo real y detecta matrículas.  
- **Backend API (C# / .NET):** Gestiona la información de vehículos, usuarios y notificaciones.  
- **Frontend Web (Angular):** Panel de control administrativo y de empleados.  
- **Aplicación Móvil (Ionic):** Interfaz para usuarios finales (clientes).  
- **Base de Datos (PostgreSQL):** Almacena registros de matrículas, alertas y configuraciones.

---

## 🧾 Requerimientos Destacados

### 🔹 Requerimientos Funcionales
- RF-01 – Registro automático de vehículos.  
- RF-02 – Consulta de disponibilidad de estacionamiento.  
- RF-03 – Registro manual de vehículos.  
- RF-05 – Alertas de infracciones y notificaciones.  
- RF-09 – Gestión de tarifas.  
- RF-10 – Autenticación y autorización.  
- RF-11 – Dashboard administrativo.  
- RF-17 – Reconocimiento automático de matrículas (ANPR).

### 🔹 Requerimientos No Funcionales
- RNF-01 – Latencia de procesamiento inferior a 200 ms.  
- RNF-02 – Compatibilidad con cámaras RTSP.  
- RNF-03 – Seguridad basada en roles y tokens JWT.  
- RNF-04 – Escalabilidad horizontal mediante microservicios.  
- RNF-05 – Mantenibilidad bajo principios SOLID y Clean Architecture.

---

## 👥 Equipo de Trabajo

| Nombre | Rol | Responsabilidad Principal |
|---------|-----|----------------------------|
| **Karol Natalia Osorio Poveda** | Líder de desarrollo | Frontend Web / Coordinación general |
| **Aníbal Alvarado Andrade** | Programador Fullstack | Backend y microservicio ANPR |
| **Yerson Stiven Cuellar Rubiano** | Desarrollador | Frontend móvil y validaciones API |

---

## 📎 Archivos Incluidos

| Archivo | Descripción |
|----------|-------------|
| `Plantilla-SRS.docx` | Documento oficial con el formato IEEE/SENA. |
| `SRS.md` | Versión extendida en Markdown con el contenido completo. |
| `README.md` | Este archivo, resumen y guía de navegación. |

---

## 🧠 Cómo Usar este Documento

1. **Lectura:** revisa el `SRS.md` o el documento `.docx` para conocer el alcance funcional.  
2. **Trazabilidad:** relaciona cada **HU (Historia de Usuario)** con su respectivo **RF/RNF**.  
3. **Desarrollo:** utiliza los requerimientos como base para las tareas de implementación y pruebas.  
4. **Control de cambios:** actualiza el control de versiones al modificar o agregar requerimientos.

---


