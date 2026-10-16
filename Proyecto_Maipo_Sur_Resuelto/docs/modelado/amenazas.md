# Modelo de amenazas STRIDE — Maipo Sur

**Autores de esta ficha:** Daniel Silva, Allen Ramirez y Antonella Mancilla.

## Alcance y supuestos

Sistema ficticio con un lector local sin dispositivos conectados. El modelado analiza qué podría importar **si** un sistema semejante se implementara en un servicio esencial, sin suponer que exista una conexión operativa real. Diagrama: [arquitectura](../arquitectura/maipo-sur.svg).

| Código | Amenaza | STRIDE | Impacto potencial sobre el servicio | Prioridad | Control de software propuesto | Evidencia planeada |
|---|---|---|---|---|---|---|
| R1 | Credencial expuesta en configuración o historial | Filtración, suplantación | Persona no autorizada podría intentar acceder a la supervisión | Alta | Gitleaks, secretos de entorno, revocación de credenciales reales | Log de Gitleaks y configuración revisada |
| R2 | Cambio inseguro de parámetros o instrucciones | Manipulación | Lecturas o indicaciones erróneas para decisiones humanas | Alta | Revisión de Pull Requests, validaciones, aprobación externa | Tests, aprobación de cambios |
| R3 | Dependencia vulnerable o de procedencia dudosa | Manipulación, denegación | Fallo o indisponibilidad del programa de supervisión | Alta | Semgrep, Trivy, OSV y versiones fijas | Log de herramientas, inventario SBOM |
| R4 | Salida sensible escrita en el log | Filtración | Exposición de un identificador en contexto hospitalario (simulado) | Media | Revisión de logs, prueba negativa | Test sector salud |
| R5 | Configuración con origen de red demasiado amplio | Elevación, denegación | Acceso no autorizado a un panel de transporte hipotético | Alta | Analizador de configuración y política de acceso | Test sector transporte |
| R6 | Parche propuesto por IA con conexiones no autorizadas | Manipulación, filtración | Envío involuntario de datos fuera del sistema y pérdida de control | Alta | Revisión de dependencias, comandos, certificados y destino | Veredicto de auditoría |

### Las tres amenazas elegidas para la ficha

R1, R2 y R3 concentran la discusión del caso de agua. La severidad expresa una **estimación cualitativa**, no una medición de una planta real.

### Riesgo residual

Incluso si el pipeline termina correctamente, quedan riesgos que un escáner de repositorio no cubre: identidad de operadores, segmentación TI/TO, seguridad funcional, procedimientos de emergencia, mantenimiento y disponibilidad en terreno.
