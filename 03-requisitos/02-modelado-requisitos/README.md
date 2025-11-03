# 🧩 Modelado de Requisitos — ANPR VISION

El presente módulo reúne todos los **artefactos del modelado de requisitos** del proyecto **ANPR VISION**, donde se especifican, documentan y relacionan los requerimientos del sistema.  
Este conjunto de documentos permite validar la correspondencia entre las **necesidades del cliente** y las **funcionalidades técnicas** que el sistema implementará.

---

## 📁 Estructura General de la Carpeta

02-modelado-requisitos/
├── casos-de-uso/
├── historias-de-usuario/
└── trazabilidad/


Cada subcarpeta representa una fase distinta del proceso de modelado y análisis, detallada a continuación 👇

---

## 🎭 1. Casos de Uso (`casos-de-uso/`)

Contiene la documentación y diagramas UML que describen las interacciones entre los **actores** (administrador, operador, usuario final, cámara ANPR, etc.) y el **sistema ANPR-VISION**.

### 📂 Estructura interna:
casos-de-uso/
├── UC-001_RegistrarEntradaVehiculo/
│ ├── Diagrama/
│ │ └── UC-001_RegistrarEntradaVehiculo.png
│ └── Documentacion/
│ └── UC-001_RegistrarEntradaVehiculo.md
├── UC-002_ConsultarDisponibilidad/
│ ├── Diagrama/
│ └── Documentacion/
└── ...


### 📘 Contenido típico:
Cada caso de uso incluye:
- **Identificador (UC-XXX)** y nombre.  
- **Actores involucrados.**  
- **Descripción general del flujo principal y alterno.**  
- **Entradas, salidas y condiciones de éxito.**  
- **Relación con requerimientos funcionales (RF).**  

📈 Ejemplo:  
`UC-001 – Registrar Entrada de Vehículo` describe cómo el sistema detecta una placa, genera la notificación y registra el ingreso en la base de datos.

---

## 💡 2. Historias de Usuario (`historias-de-usuario/`)

Documenta las historias de usuario definidas para el proyecto, siguiendo el formato:
> “Como [rol], quiero [acción] para [beneficio].”

Cada historia se asocia con uno o varios **requerimientos funcionales (RF)** y **casos de uso (UC)**, y contiene criterios de aceptación claros y verificables.

### 📂 Estructura interna:
historias-de-usuario/
├── HU-01_IniciarSesion/
│ ├── Criterios de aceptacion/
│ │ └── HU-01_Criterios.txt
│ └── Documentacion/
│ └── Historial de usuario.xlsx
├── HU-02_VisualizarDashboard/
│ └── ...
└── README.md


### 📘 Contenido típico:
- **Identificador (HU-XX)** y descripción.  
- **Requerimientos asociados (RF).**  
- **Criterios de aceptación.**  
- **Prioridad y estado.**

📋 Ejemplo:  
`HU-01 – Iniciar sesión en el sistema` → relacionada con `RF01. Autenticación y autorización`.

---

## 🔗 3. Trazabilidad (`trazabilidad/`)

Esta sección integra toda la **correspondencia entre los requerimientos, historias de usuario y casos de uso**, asegurando cobertura total del sistema.

### 📂 Estructura interna:
trazabilidad/
├── matriz-trazabilidad_RF-HU-Casos.xlsx
├── especificaciones-RF-RNF.xlsx
└── README.md


### 📘 Contenido principal:
- **matriz-trazabilidad_RF-HU-Casos.xlsx** → relaciona HU ↔ RF ↔ UC.  
- **especificaciones-RF-RNF.xlsx** → detalla requerimientos funcionales y no funcionales.  
- **README.md** → explica la metodología de trazabilidad.

📊 Esta trazabilidad garantiza que ningún requerimiento quede sin implementación ni prueba.

---

## 🎯 Objetivo del Modelado de Requisitos

El propósito de esta etapa es:
1. Asegurar la **coherencia** entre requerimientos, historias y casos de uso.  
2. Definir claramente el **alcance funcional** del sistema.  
3. Facilitar la **verificación y validación** durante el desarrollo.  
4. Servir como base para el diseño técnico, pruebas y documentación final.

---

## 🧠 Herramientas Utilizadas

| Herramienta | Propósito |
|--------------|------------|
| **Visual Paradigm / Draw.io / PlantUML** | Creación de diagramas UML de casos de uso. |
| **Microsoft Excel / Google Sheets** | Matrices de trazabilidad y especificaciones. |
| **Markdown / Word (.docx)** | Documentación descriptiva y narrativa de los casos y HU. |

---

## 👥 Equipo Responsable

| Rol | Nombre | Responsabilidad |
|------|---------|----------------|
| Líder de desarrollo | **Karol Natalia Osorio Poveda** | Coordinación, modelado de requisitos y documentación. |
| Backend / Microservicios | **Aníbal Alvarado Andrade** | Análisis técnico y relación con casos de uso. |
| Frontend / QA | **Yerson Stiven Cuéllar Rubiano** | Validación funcional y pruebas de aceptación. |

---

📅 **Última actualización:** _[coloca la fecha actual]_  
📄 **Versión:** 1.0  
🧾 **Proyecto:** ANPR VISION — Sistema de Reconocimiento Automático de Matrículas  
🏫 **Programa:** ADSO – SENA  

---

> “Modelar los requisitos es construir el mapa que guía todo el desarrollo del sistema.”
