# 📗 Especificación de Requerimientos de Software (SRS)
### Proyecto: **ANPR VISION – Sistema de Reconocimiento Automático de Matrículas**
**Versión:** 1.0  
**Fecha:** 29/10/2025 
**Autores:**  
- Karol Natalia Osorio Poveda – Líder de desarrollo y programadora  
- Aníbal Alvarado Andrade – Programador Fullstack  
- Yerson Stiven Cuellar Rubiano – Desarrollador  
**Centro de Formación:** Centro de la industria la empresa y lo servicios  
**Regional:** Huila  

---

## 📘 1. Marco Conceptual y Organización

### 1.1 Introducción
El sistema **ANPR VISION** combina inteligencia artificial y visión por computadora para reconocer matrículas vehiculares de manera automática.  
Su propósito es optimizar el control de accesos y la gestión de parqueaderos mediante la automatización del registro y monitoreo de vehículos en tiempo real.

---

### 1.2 Abstract
**ANPR VISION** is an AI-powered software for automatic number plate recognition.  
It uses deep learning and OCR to identify and log vehicle plates in real time, providing integration with a .NET backend and a PostgreSQL database for centralized management.

---

### 1.3 Resumen
El sistema **ANPR VISION** detecta y reconoce placas vehiculares a través de cámaras IP, analizando imágenes con redes neuronales y algoritmos OCR.  
Se busca lograr precisión, eficiencia y escalabilidad sin depender de hardware costoso.

---

### 1.4 Planteamiento del problema
Los sistemas de reconocimiento actuales presentan problemas de precisión bajo condiciones variables (iluminación, movimiento, formatos).  
Además, las soluciones propietarias tienen altos costos.  
Este proyecto busca desarrollar una alternativa **escalable, accesible y confiable**.

---

### 1.5 Propósito
Desarrollar un sistema de reconocimiento de matrículas **preciso y eficiente** basado en IA y visión por computadora, aplicable en parqueaderos y entornos de control vehicular.

---

### 1.6 Justificación
La automatización del control vehicular contribuye a la seguridad y eficiencia de operaciones urbanas.  
ANPR VISION proporciona una solución accesible sin licencias propietarias, adaptable a entornos reales.

---

### 1.7 Objetivo general
Optimizar la gestión vehicular mediante un sistema de reconocimiento de matrículas **en tiempo real** usando inteligencia artificial y visión por computadora.

---

### 1.8 Objetivos específicos
- Analizar sistemas ANPR existentes y sus limitaciones.  
- Desarrollar un modelo IA con detección precisa de placas.  
- Implementar backend con autenticación, reportes y gestión.  
- Integrar interfaz web/móvil intuitiva y en tiempo real.  
- Validar el rendimiento con pruebas en escenarios reales.

---

### 1.9 Alcance
El sistema cubrirá:  
- Reconocimiento de matrículas mediante cámaras IP (RTSP).  
- Gestión de parqueaderos (cupos, membresías, tarifas).  
- Dashboards administrativo y de empleados.  
- Aplicación móvil para usuarios finales con alertas y pagos.  
- Extensible a peajes, zonas de control o seguridad vial.

---

### 1.10 Personal involucrado
| Nombre | Rol | Categoría | Responsabilidad | Contacto |
|---------|-----|------------|----------------|-----------|
| Karol Natalia Osorio Poveda | Líder de desarrollo | Desarrolladora | Frontend Web / Coordinación | 305 476 4359 |
| Aníbal Alvarado Andrade | Programador Fullstack | Desarrollador | Backend / Microservicio ANPR | 312 345 5867 |
| Yerson Stiven Cuellar Rubiano | Programador | Desarrollador | Frontend móvil / API | 302 575 0939 |

---

### 1.11 Definiciones, acrónimos y abreviaturas
| Acrónimo | Significado |
|-----------|-------------|
| RF | Requerimiento Funcional |
| RNF | Requerimiento No Funcional |
| ANPR | Automatic Number Plate Recognition |
| OCR | Optical Character Recognition |
| API | Application Programming Interface |
| RTSP | Real-Time Streaming Protocol |

---

### 1.12 Referencias
| Fuente | Descripción |
|--------|--------------|
| IBM – *Computer Vision Overview* | https://www.ibm.com/es-es/topics/computer-vision |
| Shaip – *Automatic Number Plate Recognition (ANPR)* | https://es.shaip.com/blog/automatic-number-plate-recognition-anpr/ |
| OMES – *Reconocimiento de matrículas vehiculares con OpenCV y Python* | https://omes-va.com/reconocimiento-de-matriculas-vehiculares-opencv-pytesseract-ocr-python/ |

---

## 📘 2. Descripción General

### 2.1 Perspectivas del producto
El sistema combina un **microservicio de IA en Python** con un **backend en .NET** y una **interfaz Angular/Ionic**.  
Procesa video en tiempo real, detecta placas y actualiza dashboards mediante WebSockets (SignalR).  
La arquitectura es modular y escalable, compatible con cámaras RTSP y PostgreSQL.

---

### 2.2 Características de los usuarios

| Tipo de usuario | Descripción | Funciones principales |
|------------------|--------------|------------------------|
| **Administrador** | Supervisa toda la operación | Dashboard, reportes, roles, tarifas, cámaras, membresías |
| **Empleado** | Operador de parqueadero | Registros, alertas, pagos, historial de placas |
| **Usuario Final** | Cliente con vehículo | Consulta de disponibilidad, historial, notificaciones y pagos |

---

### 2.3 Restricciones

#### Técnicas
- Cámaras IP 1080p con RTSP.  
- Servidor recomendado con GPU (NVIDIA GTX 1650 o superior).  
- Latencia menor a 100 ms por frame.  
- Comunicación en tiempo real mediante WebSockets.

#### Operativas
- Solo administradores pueden cambiar cámaras o configuraciones.  
- Acceso a información restringido por roles.  
- Capacidad de almacenamiento limitada según BD.

#### De seguridad
- Cifrado de contraseñas y tokens JWT.  
- Validación de roles y auditoría de acciones.

#### Legales
- Cumplimiento de Ley 1581 de 2012 (Habeas Data).  
- Uso exclusivo para control vehicular autorizado.

---

## 📘 3. Requerimientos Específicos

### 3.1 Requisitos Comunes de las Interfaces
- Interfaz web administrativa (Angular).  
- Interfaz operativa para empleados (Ionic).  
- App móvil para usuario final (Ionic + Capacitor).  
- Comunicación API REST + SignalR.  
- BD PostgreSQL.  

---

### 3.2 Requerimientos Funcionales

| ID | Nombre | Descripción resumida | Relación HU |
|----|----------|----------------------|--------------|
| RF-01 | Registro Automático de Vehículos | Registro automático por cámara y ANPR. | HU-11 |
| RF-02 | Consulta de Disponibilidad | Consulta en tiempo real de cupos. | HU-08, HU-12 |
| RF-03 | Registro Manual de Vehículos | Registro manual en caso de falla del ANPR. | HU-11 |
| RF-04 | Historial de Placas | Muestra entradas, salidas y pagos. | HU-10, HU-15 |
| RF-05 | Alertas de Infracciones | Notifica y registra infracciones. | HU-05, HU-09, HU-14 |
| RF-07 | Lista Negra de Vehículos | Bloquea o alerta sobre vehículos restringidos. | HU-05, HU-09 |
| RF-08 | Reportes y Estadísticas | Genera informes y gráficos de uso. | HU-02, HU-06 |
| RF-09 | Gestión de Tarifas | Configura tarifas por vehículo, hora o tipo. | HU-03 |
| RF-10 | Autenticación y Autorización | Login seguro con roles. | HU-01, HU-13 |
| RF-11 | Dashboard Administrativo | Vista de métricas y reportes globales. | HU-02 |
| RF-12 | Dashboard de Empleados | Panel de control operativo. | HU-02 |
| RF-13 | Consulta de Pagos e Información | Muestra estado, membresía y cobros. | HU-10, HU-15 |
| RF-14 | Consulta de Pagos (Empleado) | Verificación de deudas y membresías. | HU-03 |
| RF-15 | Asignación de Roles y Permisos | Administración de accesos. | HU-07 |
| RF-16 | Gestión de Usuarios | Creación, edición y eliminación de usuarios. | HU-07 |
| RF-17 | Reconocimiento Automático (ANPR) | Detección IA de matrículas. | HU-11 |
| RF-18 | Notificaciones al Usuario | Envío de alertas y notificaciones. | HU-14 |

---

### 3.3 Requerimientos No Funcionales

| ID | Nombre | Descripción | Criterio de aceptación |
|----|----------|-------------|------------------------|
| RNF-01 | Latencia del procesamiento | Menor a 200 ms por frame. | Mínimo 10 FPS en hardware recomendado. |
| RNF-02 | Compatibilidad con cámaras RTSP | Cámaras IP 1080p o superior. | Conexión exitosa con cámaras compatibles. |
| RNF-03 | Seguridad y accesos | Roles, permisos y tokens JWT cifrados. | Acceso restringido y autenticado. |
| RNF-04 | Mantenibilidad | Código modular bajo SOLID. | Nuevas funciones sin romper integraciones. |
| RNF-05 | Escalabilidad | Capaz de gestionar múltiples cámaras. | Rendimiento constante en cargas altas. |
| RNF-06 | Disponibilidad | 99% de tiempo operativo. | Monitoreo de uptime activo. |
| RNF-07 | Portabilidad | Despliegue local o en nube (Docker). | Verificación en ambos entornos. |
| RNF-08 | Usabilidad | Interfaz intuitiva y responsiva. | Validada mediante pruebas de usuario. |

---

## 📘 4. Casos de Uso y Diagramas

### 4.1 Principales Casos de Uso

| ID | Nombre | Actor Principal | Descripción |
|----|---------|-----------------|-------------|
| CU-01 | Registrar Vehículo Automáticamente | Sistema ANPR | Detecta y registra el vehículo. |
| CU-02 | Registrar Vehículo Manualmente | Empleado | Entrada o salida manual. |
| CU-03 | Consultar Disponibilidad | Empleado / Usuario Final | Muestra cupos disponibles. |
| CU-04 | Generar Alerta o Infracción | Empleado / Sistema | Crea y envía notificación. |
| CU-05 | Consultar Historial | Empleado / Usuario | Muestra entradas y pagos. |
| CU-06 | Gestionar Tarifas | Administrador | Define tarifas por tipo o tiempo. |
| CU-07 | Visualizar Dashboard | Administrador / Empleado | Muestra métricas y alertas. |
| CU-08 | Asignar Roles y Permisos | Administrador | Gestiona accesos del personal. |
| CU-09 | Generar Reportes | Administrador | Produce reportes exportables. |
| CU-10 | Consultar Notificaciones | Usuario Final | Visualiza alertas y mensajes. |

---

### 4.2 Ejemplo de Caso de Uso (CU-01)

**Nombre:** Registrar Vehículo Automáticamente  
**Actor:** Sistema ANPR  
**Descripción:** Detecta una placa, valida datos y crea el registro.  
**Flujo Normal:**  
1. La cámara detecta el vehículo.  
2. El microservicio procesa el frame.  
3. Se extrae la matrícula.  
4. Se valida en la BD.  
5. Se registra la entrada/salida.  
6. Se notifica al dashboard.  
**Flujo Alternativo:**  
- Si falla la detección, se habilita registro manual.  
**Entradas:** Imagen, ID de cámara, hora.  
**Salidas:** Registro de vehículo.  
**Requerimientos Relacionados:** RF-01, RF-17  

---

## 📘 5. Anexos y Control de Versiones

### 5.1 Anexos
- Diagramas UML (casos de uso, secuencia, componentes).  
- Mockups de interfaz web/móvil.  
- Pruebas de rendimiento.  
- Configuraciones RTSP / API.  

---

### 5.2 Control de Versiones

| Versión | Fecha | Autor(es) | Descripción |
|----------|--------|------------|--------------|
| 1.0 | [dd/mm/aaaa] | Karol N. Osorio P. | Creación inicial del SRS. |
| 1.1 | [dd/mm/aaaa] | Aníbal Alvarado A. | Agregado de RF/RNF detallados. |
| 1.2 | [dd/mm/aaaa] | Yerson S. Cuellar R. | Inclusión de casos de uso y anexos. |
| 1.3 | [dd/mm/aaaa] | Equipo ANPR VISION | Versión final validada para entrega. |

---

> **Nota:** Este documento sigue el estándar IEEE 830 y forma parte del entregable **03-requisitos / 01-SRS** del proyecto ANPR-VISION.  
> Se elaboró en el marco del programa **SENA ADSO 2025**.

---

