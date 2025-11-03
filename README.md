<!-- ===================== ENCABEZADO CON LOGO ===================== -->
<div align="center" style="background: linear-gradient(135deg, #288992ef, #227c9cff); padding: 25px; border-radius: 15px; color: white; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
  <img src="assets/logoSolo.png" alt="ANPRVision Logo" width="150" style="margin-bottom: 10px;" />
  <h1 style="margin: 10px 0;">🚘 ANPR-VISION</h1>
  <p><b>Sistema de Reconocimiento Automático de Matrículas</b><br>
  <i>Proyecto de software para la gestión inteligente de parqueaderos</i></p>
  <a href="https://6908da95978cb100082b47fc--courageous-salamander-30e352.netlify.app/" 
     style="color: #fff; text-decoration: underline;" 
     target="_blank">
     Pagina Web🚀
  </a>
  <hr style="width: 60%; border: 1px solid rgba(255,255,255,0.3);">
  <p><b>Servicio Nacional de Aprendizaje (SENA)</b><br>
  Tecnólogo en Análisis y Desarrollo de Software · 2025</p>
</div>

---

<div style="background:#f9f9fb; border: 1px solid #ddd; border-radius: 12px; padding: 25px; margin-top: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">

## 🧩 Descripción del Proyecto
**ANPR-VISION** (Automatic Number Plate Recognition Vision) es un sistema inteligente que permite **reconocer automáticamente las matrículas vehiculares** mediante técnicas de visión artificial y OCR.  
Su propósito es **automatizar la gestión de parqueaderos**, registrando entradas, salidas, cobros y reportes de forma eficiente y sin intervención manual.

---

## 🎯 Objetivos
- Automatizar el registro de ingreso y salida de vehículos.  
- Reconocer matrículas en tiempo real mediante OCR.  
- Controlar disponibilidad de cupos.  
- Calcular cobros y tiempos de permanencia automáticamente.  
- Generar reportes y estadísticas.  
- Mejorar la experiencia del usuario final y la eficiencia administrativa.  

---

## ⚙️ Tecnologías Utilizadas
| 🧱 **Categoría** | 💡 **Tecnologías** |
|------------------|-------------------|
| **Backend** | .NET Core · C# · Entity Framework |
| **Frontend / App** | Angular · Ionic |
| **Base de Datos** | SQL Server / MySQL / PostgreSQL |
| **OCR / IA** | OpenCV · EasyOCR · YOLOv5 · ByteTracker · Python |
| **Arquitectura** | N-Capas · Microservicios |
| **Mensajería y Comunicación** | Apache Kafka · SignalR · WebSockets |
| **Documentación** | Markdown · PlantUML · Mermaid · Swagger |
| **DevOps / Despliegue** | Docker · Docker Compose · GitHub Actions · Nginx |
| **Pruebas y Calidad** | xUnit · NUnit · Jest · Jasmine · Cypress · Moq · SonarQube · Postman Tests · Load Testing (k6 / JMeter) |
| **Control de Versiones** | Git · GitHub |
| **Entorno de Desarrollo** | Visual Studio · VS Code · Postman · DBeaver · Docker Desktop · pgAdmin |
| **Gestión de Tareas y Proyectos** | ClickUp |

---

## 🧠 Arquitectura del Sistema
El sistema **ANPR-VISION** se construye bajo una **arquitectura en N-capas**, complementada por un **microservicio externo de visión artificial (ANPR-VISION-MICROSERVICE)**.  
Esta estructura garantiza **modularidad, mantenibilidad y escalabilidad**, separando claramente las responsabilidades entre backend, frontend y microservicios.

### 🧩 Capas Principales
-  **Capa Web / API (Presentación y Exposición)**  
  Desarrollada en **ASP.NET Core Web API**, expone servicios hacia el frontend (**Angular / Ionic**) y otros módulos del sistema.  

-  **Capa de Negocio (Business Layer)**  
  Contiene la **lógica de negocio y reglas del dominio**, aplicando principios **SOLID**, **POO** y **patrones de diseño**.  

-  **Capa de Datos (Data Layer)**  
  Encargada del **acceso y persistencia de información** mediante **Entity Framework Core** y repositorios genéricos.  

-  **Capa de Entidades (Entity Layer)**  
  Define los **modelos del dominio**, sus relaciones y los **DTOs** utilizados entre las capas.  

---

### 🤖 Microservicio de Visión (ANPR-VISION-MICROSERVICE)
Microservicio **independiente**, desarrollado en **Python**, responsable del procesamiento de video e imágenes para el **reconocimiento automático de matrículas (ANPR)**.  
Utiliza **OpenCV**, **YOLOv5**, **EasyOCR** y **ByteTrack**, y se comunica con el backend mediante **Apache Kafka**.

---

#### 🌐 Frontend / Aplicación Híbrida
Desarrollado con **Angular** e **Ionic**, provee una interfaz moderna, responsiva y multiplataforma (web y móvil).

---

## 👥 Roles de Usuario
| Rol | Descripción |
|------|--------------|
| **Administrador** | Configura tarifas, usuarios, reportes y alertas. |
| **Trabajador** | Supervisa vehículos, pagos e infracciones. |
| **Usuario Final** | Consulta historial, pagos y alertas. |

---

## 🚗 Funcionalidades Principales
-  Reconocimiento automático de placas.  
-  Registro manual en caso de error.  
-  Control de cupos en tiempo real.  
-  Gestión de membresías y usuarios.  
-  Tarifas configurables.  
-  Dashboard con métricas e informes.  
-  Notificaciones automáticas y alertas.  

---

## 🧾 Requisitos Clave
| Código | Descripción |
|---------|--------------|
| **RF01** | Autenticación y autorización basada en roles (Administrador, Operador, Usuario Final). |
| **RF02** | Reconocimiento automático de matrículas mediante el microservicio de visión (OCR). |
| **RF03** | Registro manual de vehículos en caso de fallo del OCR. |
| **RF04** | Gestión de vehículos registrados: consulta, listado y actualización. |
| **RF05** | Control de disponibilidad en tiempo real, actualizando cupos al detectar entradas y salidas. |
| **RF06** | Gestión de tarifas dinámicas según tipo de vehículo. |
| **RF07** | Cálculo automático del precio de parqueo según permanencia y tarifa vigente. |
| **RF08** | Generación de historial de parqueo (ingresos, salidas, fechas y usuarios asociados). |
| **RF10** | Consulta del historial y estado del vehículo por parte del usuario final. |
| **RF11** | Gestión de listas negras: bloqueo de vehículos y registro de motivos. |
| **RF12** | Emisión de alertas automáticas ante incidencias (tiempo excedido, ingreso restringido, etc.). |
| **RF13** | Generación de reportes (ocupación, ingresos, tiempos promedio, etc.). |
| **RF14** | Gestión de usuarios del sistema (creación, edición, eliminación). |
| **RF15** | Asignación de roles y permisos diferenciados por usuario y parqueadero. |
| **RF16** | Validación de formato de placas antes del registro. |
| **RF19** | Panel de control administrativo con métricas en tiempo real. |
| **RF20** | Envío de notificaciones automáticas a los usuarios. |

---

## 👨‍💻 Equipo de Desarrollo
| Integrante | Rol / Responsabilidades |
|-------------|--------------------------|
| **Karol Natalia Osorio Poveda** |  **Líder del Proyecto** · Desarrollo **Backend**, **Frontend** y **Aplicación Móvil** · Coordinación general del sistema ANPR-VISION. |
| **Yerson Stiven Cuellar Rubiano** |  **Desarrollador Frontend y Móvil** |
| **Aníbal Alvarado** |  **Especialista en IA / OCR y Backend** · Desarrollo del **microservicio ANPR-VISION-MICROSERVICE** basado en **OpenCV**, **YOLO** y **EasyOCR** · Integración con **Kafka** y soporte backend. |


---

## 🧱 Repositorios del Proyecto
| Módulo | Descripción | Repositorio |
|---------|--------------|-------------|
|  **Apr-Vision-Backend** | API REST desarrollada en **.NET Core**, encargada de la lógica de negocio, seguridad y comunicación con el microservicio OCR. | [🔗 Ir al repositorio](https://github.com/nataliosorio/anpr-vision-api) |
|  **Apr-Vision-Frontend** | Aplicación **Angular** para la interfaz web administrativa y de usuario final. Incluye dashboard, reportes y gestión general. | [🔗 Ir al repositorio](https://github.com/nataliosorio/anpr-vision-portal) |
|  **Apr-Vision-Mobile** | Aplicación móvil híbrida desarrollada con **Ionic**, orientada al uso para usuarios finales. | [🔗 Ir al repositorio](https://github.com/nataliosorio/anpr-vision-app) |
|  **Apr-Vision-Microservice** | Microservicio independiente en **Python**, con **OpenCV**, **EasyOCR**, **YOLOv5** y **ByteTrack** para detección y reconocimiento de matrículas. | [🔗 Ir al repositorio](https://github.com/nataliosorio/anpr-vision-microservice) |
|  **Apr-Vision-db** | Base de datos | [🔗 Ir al repositorio](https://github.com/nataliosorio/anpr-vision-db) |

</div>
