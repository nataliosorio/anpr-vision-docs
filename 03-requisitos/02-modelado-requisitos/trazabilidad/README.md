# 📊 Trazabilidad — ANPR VISION

Este módulo contiene los documentos que garantizan la **trazabilidad de los requerimientos** del proyecto **ANPR VISION**, asegurando la relación entre los **Requerimientos Funcionales (RF)**, **No Funcionales (RNF)**, **Historias de Usuario (HU)** y **Casos de Uso (UC)**.  

El propósito principal es verificar que cada requerimiento esté cubierto, implementado y probado dentro del ciclo de desarrollo del sistema.

---

## 📁 Estructura de la Carpeta

# 📊 Trazabilidad — ANPR VISION

Este módulo contiene los documentos que garantizan la **trazabilidad de los requerimientos** del proyecto **ANPR VISION**, asegurando la relación entre los **Requerimientos Funcionales (RF)**, **No Funcionales (RNF)**, **Historias de Usuario (HU)** y **Casos de Uso (UC)**.  

El propósito principal es verificar que cada requerimiento esté cubierto, implementado y probado dentro del ciclo de desarrollo del sistema.

---

## 📁 Estructura de la Carpeta

trazabilidad/
├── matriz-trazabilidad_RF-HU-Casos.xlsx
├── especificaciones-RF-RNF.xlsx
└── README.md


---

## 📘 1. matriz-trazabilidad_RF-HU-Casos.xlsx

Este documento muestra la **correspondencia entre los requerimientos, las historias de usuario y los casos de uso**.  
Permite validar que cada requisito funcional tenga al menos una historia y un caso que lo implemente o pruebe.

### Contenido principal:
| Columna | Descripción |
|----------|--------------|
| **ID HU** | Identificador único de la historia de usuario (HU01, HU02, …). |
| **Historia de Usuario** | Descripción en formato “Como [rol], quiero [acción], para [beneficio]”. |
| **Requerimientos Asociados** | RF o RNF relacionados con esa historia. |
| **ID UC** | Código del caso de uso que implementa el requerimiento. |
| **Caso de Uso Relacionado** | Nombre o función principal del caso de uso. |
| **Prioridad / Estado** | Nivel de importancia (Alta, Media, Baja) y avance actual. |
| **Observaciones** | Comentarios sobre validaciones, pruebas o dependencias. |

### Ejemplo:
| ID HU | Historia de Usuario | RF Asociados | ID UC | Caso de Uso Relacionado | Prioridad | Estado |
|-------|---------------------|--------------|-------|--------------------------|------------|---------|
| HU01 | Iniciar sesión en el sistema | RF01. Autenticación y autorización | UC-010 | Gestionar Usuarios y Roles | Alta | Validado |
| HU03 | Gestionar tarifas según tipo de vehículo | RF06. Gestión de tarifas, RF07. Cálculo automático del precio | UC-007 | Gestionar Tarifas y Tiempos | Alta | En desarrollo |

📈 Esta matriz permite rastrear la evolución de los requerimientos y su implementación dentro del sistema.

---

## ⚙️ 2. especificaciones-RF-RNF.xlsx

Contiene el **detalle técnico y descriptivo** de todos los requerimientos del sistema, separados por tipo.

### Hojas del archivo:
1. **Requerimientos Funcionales (RF)**  
   - Describen las funcionalidades que el sistema debe cumplir.  
   - Ejemplo: *RF06 – Gestión de tarifas* → "El sistema debe permitir configurar tarifas por tipo de vehículo, horario y duración."

2. **Requerimientos No Funcionales (RNF)**  
   - Definen las características de calidad del sistema.  
   - Ejemplo: *RNF01 – Latencia del procesamiento* → "El sistema debe detectar matrículas en menos de 200 ms por frame."

3. **Resumen General (opcional)**  
   - Tabla con totales de requerimientos por estado (en desarrollo, validado, pendiente).

### Columnas principales:
| Columna | Descripción |
|----------|--------------|
| **ID** | Identificador único (RF01, RNF01, etc.). |
| **Nombre del Requerimiento** | Título corto del requisito. |
| **Descripción** | Explicación detallada de la funcionalidad o restricción. |
| **Prioridad / Estado** | Nivel de importancia y grado de avance. |
| **HU Asociadas** | Historias de usuario vinculadas a ese requerimiento. |
| **Observaciones** | Notas técnicas, dependencias o pruebas relacionadas. |

---

## 🧠 3. Propósito General de la Trazabilidad

El objetivo de mantener esta documentación es asegurar que:

- Todos los **requerimientos funcionales** estén implementados en el sistema.  
- Todos los **requerimientos no funcionales** sean medibles y comprobables.  
- Cada **historia de usuario** tenga al menos un **caso de uso** asociado.  
- Exista **coherencia y seguimiento** entre análisis, diseño, desarrollo y pruebas.  

---

## ✅ Buenas Prácticas

- Actualiza la matriz cada vez que se cree o modifique una HU, RF o UC.  
- Usa colores o filtros en Excel para identificar requerimientos **pendientes o validados**.  
- Mantén los identificadores (HU, RF, UC) consistentes entre todos los documentos.  
- Revisa la trazabilidad antes de cada entrega o evaluación de avance.

---

## 🧩 Autores y Control de Versión

| Rol | Nombre | Responsabilidad |
|------|---------|----------------|
| Líder de desarrollo | **Karol Natalia Osorio Poveda** | Coordinación, documentación y revisión. |
| Backend & Microservicios | **Aníbal Alvarado Andrade** | Implementación y validación técnica. |
| Frontend & QA | **Yerson Stiven Cuéllar Rubiano** | Validación funcional y pruebas de interfaz. |

📅 **Última actualización:** _[coloca la fecha actual]_  
📄 **Versión:** 1.0  
🧾 **Proyecto:** ANPR VISION — Sistema de Reconocimiento Automático de Matrículas

---

> “Un sistema bien trazado es un sistema que puede crecer sin perder su rumbo.”
