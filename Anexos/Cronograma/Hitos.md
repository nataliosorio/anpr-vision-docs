# 📅 Cronograma del Proyecto ANPR-VISION  
**Periodo:** Marzo – Octubre 2025  
**Equipo:**  
- 🧠 Karol Natalia Osorio Poveda — Frontend Web y Backend  
- ⚙️ Aníbal Alvarado Andrade — Microservicio y Backend  
- 📱 Yerson Stiven Cuéllar Rubiano — Frontend Móvil y Validaciones  

---

## 🧩 Fase 1. Análisis y Planeación  
**Duración:** 1 – 31 de marzo 2025  

| Nº | Actividad | Subactividad | Inicio | Fin | Responsable | Entregable |
|----|------------|--------------|---------|------|--------------|-------------|
| 1.1 | Reunión inicial y levantamiento | Reunión con el cliente y definición de requerimientos | 01/03/2025 | 03/03/2025 | Karol Natalia | Acta de acercamiento |
| 1.2 | Análisis de procesos | Levantamiento de procesos actuales del parqueadero | 04/03/2025 | 07/03/2025 | Yerson | Documento de análisis |
| 1.3 | Definición de alcance | Identificación de requerimientos funcionales y no funcionales | 08/03/2025 | 10/03/2025 | Karol Natalia | Documento de alcance |
| 1.4 | Elaboración del anteproyecto | Redacción de objetivos, justificación y entregables | 11/03/2025 | 14/03/2025 | Yerson | Anteproyecto.pdf |
| 1.5 | Diseño de instrumentos | Creación de instrumentos de recolección de información | 15/03/2025 | 17/03/2025 | Karol Natalia | Formatos de recolección |
| 1.6 | Aplicación de instrumentos | Ejecución de encuestas y entrevistas | 18/03/2025 | 22/03/2025 | Yerson | Informe de resultados |
| 1.7 | Documento SRS | Redacción del Documento de Requerimientos | 23/03/2025 | 28/03/2025 | Karol Natalia | SRS.md |
| 1.8 | Planificación final | Elaboración del mapa de procesos y cronograma | 29/03/2025 | 31/03/2025 | Yerson | MapaProcesos.png / Cronograma.xlsx |

---

## 🧱 Fase 2. Diseño de Arquitectura y Base de Datos  
**Duración:** 1 – 30 de abril 2025  

| Nº | Actividad | Subactividad | Inicio | Fin | Responsable | Entregable |
|----|------------|--------------|---------|------|--------------|-------------|
| 2.1 | Diseño de arquitectura | Diagrama general del sistema | 01/04/2025 | 05/04/2025 | Aníbal | Arquitectura.md |
| 2.2 | Comunicación interna | Flujo de datos Backend–Microservicio | 06/04/2025 | 10/04/2025 | Aníbal | Diagrama de comunicación |
| 2.3 | Modelo de datos | Creación del modelo entidad–relación (ERD) | 11/04/2025 | 14/04/2025 | Karol Natalia | ERD.png |
| 2.4 | Normalización | Ajuste de relaciones y claves foráneas | 15/04/2025 | 18/04/2025 | Karol Natalia | Script SQL inicial |
| 2.5 | Seguridad | Definición de roles, permisos y auditoría | 19/04/2025 | 22/04/2025 | Yerson | PoliticaSeguridadDB.md |
| 2.6 | API REST | Definición de endpoints y contratos DTO | 23/04/2025 | 26/04/2025 | Aníbal | ApiEndpoints.md |
| 2.7 | Diagramas UML | Casos de uso y diagramas de secuencia | 27/04/2025 | 30/04/2025 | Todos | Diagramas UML completos |

---

## ⚙️ Fase 3. Desarrollo Backend y Microservicio  
**Duración:** 1 de mayo – 30 de junio 2025  

| Nº | Actividad | Subactividad | Inicio | Fin | Responsable | Entregable |
|----|------------|--------------|---------|------|--------------|-------------|
| 3.1 | Proyecto base | Configuración inicial del backend (ASP.NET Core) | 01/05/2025 | 04/05/2025 | Karol Natalia | Estructura API |
| 3.2 | Módulo Vehículos | CRUD y validaciones | 05/05/2025 | 10/05/2025 | Karol Natalia | Vehículos funcional |
| 3.3 | Módulo Tarifas | CRUD y lógica de cálculo | 11/05/2025 | 15/05/2025 | Karol Natalia | Tarifas configuradas |
| 3.4 | Microservicio base | Configuración Python + YOLOv5 | 01/05/2025 | 07/05/2025 | Aníbal | anpr-vision-microservice |
| 3.5 | Kafka | Implementación de Producer/Consumer | 08/05/2025 | 15/05/2025 | Aníbal | Comunicación Kafka |
| 3.6 | Notificaciones | SignalR y persistencia | 16/05/2025 | 25/05/2025 | Karol Natalia | Sistema de notificaciones |
| 3.7 | Control de acceso | Registro de entradas/salidas | 26/05/2025 | 31/05/2025 | Karol Natalia | API ParkingEntradas |
| 3.8 | OCR y detección | Entrenamiento YOLO y pruebas de detección | 01/06/2025 | 10/06/2025 | Aníbal | Modelo funcional |
| 3.9 | Integración | Backend ↔ Microservicio | 11/06/2025 | 18/06/2025 | Aníbal / Karol | Integración validada |
| 3.10 | Pruebas unitarias | Creación de tests automáticos | 19/06/2025 | 23/06/2025 | Karol Natalia | Reporte de pruebas |
| 3.11 | Optimización | Refactor de servicios | 24/06/2025 | 28/06/2025 | Karol Natalia | Código optimizado |
| 3.12 | Documentación | Informe técnico parcial | 29/06/2025 | 30/06/2025 | Todos | Informe parcial |

---

## 💻 Fase 4. Desarrollo Frontend Web y Móvil  
**Duración:** 1 – 31 de julio 2025  

| Nº | Actividad | Subactividad | Inicio | Fin | Responsable | Entregable |
|----|------------|--------------|---------|------|--------------|-------------|
| 4.1 | Proyecto Angular | Creación de estructura base | 01/07/2025 | 04/07/2025 | Karol Natalia | Base Angular |
| 4.2 | Autenticación web | Login, roles y permisos | 05/07/2025 | 10/07/2025 | Karol Natalia | Login funcional |
| 4.3 | Dashboard | Panel de control y reportes | 11/07/2025 | 20/07/2025 | Karol Natalia | Panel administrativo |
| 4.4 | Proyecto Ionic | Estructura base móvil | 01/07/2025 | 05/07/2025 | Yerson | Base Ionic |
| 4.5 | Login móvil | Verificación de código | 06/07/2025 | 10/07/2025 | Yerson | Login móvil |
| 4.6 | Notificaciones | UI de notificaciones y QR | 11/07/2025 | 18/07/2025 | Yerson | Interfaz notificaciones |
| 4.7 | Integración | Conexión SignalR y API | 19/07/2025 | 25/07/2025 | Yerson / Karol | Comunicación tiempo real |
| 4.8 | Pruebas UX | Validación con usuarios | 26/07/2025 | 31/07/2025 | Yerson / Karol | Informe UX |

---

## 🚀 Fase 5. Pruebas, Despliegue y Documentación Final  
**Duración:** 1 – 31 de agosto 2025  

| Nº | Actividad | Subactividad | Inicio | Fin | Responsable | Entregable |
|----|------------|--------------|---------|------|--------------|-------------|
| 5.1 | Pruebas funcionales | Backend y microservicio | 01/08/2025 | 08/08/2025 | Aníbal / Karol | Reporte QA |
| 5.2 | Pruebas integradas | Web y móvil | 09/08/2025 | 15/08/2025 | Yerson / Karol | Validación completa |
| 5.3 | CI/CD | Configuración Docker y Jenkins | 16/08/2025 | 22/08/2025 | Aníbal | Pipeline operativo |
| 5.4 | Despliegue | Pruebas locales y nube | 23/08/2025 | 28/08/2025 | Aníbal | Deploy exitoso |
| 5.5 | Documentación | Manual técnico y de usuario | 29/08/2025 | 31/08/2025 | Karol / Yerson | Manuales listos |

---

## 🏁 Fase 6. Cierre y Evaluación  
**Duración:** 16 de septiembre – 5 de octubre 2025  

| Nº | Actividad | Subactividad | Inicio | Fin | Responsable | Entregable |
|----|------------|--------------|---------|------|--------------|-------------|
| 6.1 | Sustentación / presentación | Entrega cliente / jurado | 16/09/2025 | 25/09/2025 | Todos | Video y presentación final |
| 6.2 | Cierre y retroalimentación | Acta de cierre | 26/09/2025 | 05/10/2025 | Todos | Acta de cierre |

---

📘 **Notas finales:**  
- Las fechas son tentativas y pueden ajustarse según el avance real del proyecto.  
- Cada entregable será respaldado en el repositorio de documentación dentro de su carpeta correspondiente.  
- Este cronograma es parte del entregable `02-cronograma` del proyecto ANPR-VISION.

