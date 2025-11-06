# ADR-001 — Uso de Apache Kafka para Comunicación Asíncrona

## 📅 Fecha
2025-06-10

## 🧠 Contexto
El sistema **ANPR-VISION** requiere procesar información en tiempo real proveniente de las cámaras ANPR y del microservicio de visión artificial.  
Inicialmente, se consideró usar peticiones **HTTP síncronas** para la comunicación entre servicios, pero este enfoque no garantizaba la **entrega confiable**, generaba **cuellos de botella** y dificultaba la **escalabilidad horizontal**.

## 🎯 Decisión
Se adopta el uso de **Apache Kafka** como **middleware de mensajería** para la transmisión de eventos entre los módulos del sistema, permitiendo comunicación **asíncrona, escalable y tolerante a fallos**.

### 📦 Componentes involucrados:
- **Microservicio ANPR (Python)** → Publica eventos con la placa detectada.  
- **Backend ASP.NET Core** → Consume eventos y orquesta acciones (notificaciones, registro de vehículo).  
- **Servicio de Notificaciones (SignalR)** → Emite alertas en tiempo real a los usuarios.  
- **Base de Datos (PostgreSQL)** → Almacena registros procesados.

## ⚙️ Implementación
Kafka se desplegará en un contenedor Docker junto con **Zookeeper**.  
El backend y el microservicio usarán **producers y consumers** configurados mediante tópicos específicos:
- `plates.detected`
- `notifications.new`
- `vehicles.registered`

## 🧩 Consecuencias

### Ventajas ✅
- Comunicación **asíncrona y no bloqueante** entre microservicios.  
- Mejora el **rendimiento** y la **resiliencia** ante fallos temporales.  
- Facilita la **escalabilidad horizontal** del sistema.  

### Desventajas ⚠️
- Incrementa la **complejidad operativa** (configuración y monitoreo de brokers).  
- Requiere gestión de **tópicos, offsets y particiones**.  

## 🔍 Alternativas Consideradas
| Alternativa | Motivo de descarte |
|--------------|--------------------|
| WebSockets directos entre servicios | No garantizan entrega ni persistencia. |
| RabbitMQ | Buena opción, pero Kafka ofrece mejor rendimiento y particionado nativo. |
| REST API síncrona | Limitaciones de latencia y escalabilidad. |

## 🔗 Estado
✅ **Implementado en entorno de desarrollo**  
🛠️ En pruebas de rendimiento y optimización de offsets.
