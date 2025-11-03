# ADR-002 — Adopción de Arquitectura Onion en el Backend

## 📅 Fecha
2025-06-10

## 🧠 Contexto
El sistema requiere un backend modular y mantenible que permita:
- Alta **separación de responsabilidades**.
- Facilidad para realizar **pruebas unitarias**.
- Independencia de frameworks externos.  

El diseño inicial acoplaba la lógica de negocio directamente a los controladores y repositorios, lo que dificultaba su evolución y testing.

## 🎯 Decisión
Se adopta la **Arquitectura Onion** (en capas concéntricas), aplicando el principio de **dependencia hacia el núcleo del dominio**.

### 🧩 Capas definidas:
1. **Domain** → Entidades, interfaces, enums, value objects.  
2. **Application** → Casos de uso y lógica de negocio (servicios, validaciones, managers).  
3. **Infrastructure** → Acceso a datos (EF Core), Kafka, repositorios, SignalR, etc.  
4. **Web** → Controladores, endpoints, middleware, configuración de dependencias.

## ⚙️ Implementación
Cada capa se implementa como un proyecto independiente dentro de la solución `.NET`:


ANPR.Vision.Domain/
ANPR.Vision.Application/
ANPR.Vision.Infrastructure/
ANPR.Vision.Web/


El flujo principal sigue este esquema:
Controller → Service / Use Case → Repository → Database

con inyección de dependencias y uso de interfaces para mantener el bajo acoplamiento.

## 🧩 Consecuencias

### Ventajas ✅
- Código **más limpio, testable y desacoplado**.  
- Facilita la **sustitución de tecnologías** sin afectar el dominio.  
- Mayor mantenibilidad y claridad estructural.

### Desventajas ⚠️
- Curva de aprendizaje moderada.  
- Más archivos y proyectos dentro de la solución.  

## 🔍 Alternativas Consideradas
| Alternativa | Motivo de descarte |
|--------------|--------------------|
| Arquitectura MVC tradicional | Acoplamiento alto entre capas. |
| Clean Architecture | Muy similar, pero más compleja para el alcance actual. |
| Monolito con módulos | Menor flexibilidad y pruebas más difíciles. |

## 🔗 Estado
✅ **Implementado parcialmente en backend**  
🔜 Integración final con microservicio ANPR y módulo de notificaciones.
