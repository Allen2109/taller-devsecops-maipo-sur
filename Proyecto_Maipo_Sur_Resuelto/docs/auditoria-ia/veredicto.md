# Auditoría de la propuesta de IA n.º 7

**Equipo:** Daniel Silva, Allen Ramirez y Antonella Mancilla.  
**Resultado:** **RECHAZAR** el cambio propuesto **en su estado actual** y solicitar una versión corregida para revisión humana.

## Cuatro preguntas exigidas por la guía

| Pregunta | Evidencia encontrada en el texto didáctico | Decisión |
|---|---|---|
| ¿El paquete existe y está verificado? | Se menciona `plc_helper_utils` sin fuente, responsable ni verificación trazable. | No incorporar una dependencia no acreditada. No afirmamos que el paquete no exista; no se verificó contra un registro en vivo. |
| ¿Cómo se procesan las entradas? | Se construye una orden juntando cadenas y se usa `shell=True`. | Rechazar: las entradas requieren validación y separación de argumentos. |
| ¿Se desactiva alguna protección? | Se utiliza `verify=False`. | Rechazar: no se justifica eludir validación TLS. |
| ¿Qué ocurre con los datos? | Se envía una respuesta al destino `TELEMETRIA` sin autorización acreditada. | Rechazar cualquier salida no aprobada. |

## Consecuencias sobre el caso hipotético

Un cambio que ejecuta comandos no validados o comparte lecturas sin autorización podría comprometer la confidencialidad, exactitud o disponibilidad de un sistema de supervisión. En una planta real, eso exigiría revisión prioritaria antes de permitir un despliegue.

## Criterios para presentar un parche aceptable

Mantener un proceso local sin conectividad industrial, usar bibliotecas documentadas, no ejecutar shell a partir de entradas, conservar la validación TLS y no añadir destinos externos. El equipo exige tests automatizados y revisión por otra persona antes de aceptar un cambio.

**Importante:** el código inseguro solo figura descrito como evidencia de auditoría; no se ejecuta ni se ofrece como software operable.
