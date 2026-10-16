# Evidencias y estado de validación

**Equipo:** Daniel Silva, Allen Ramirez y Antonella Mancilla.

## Resultados locales de esta entrega

Se ejecutaron las comprobaciones locales definidas en `tests/` y `scripts/revisar_sector.py`. Los resultados y fecha se registran en [PRUEBAS_LOCALES.md](PRUEBAS_LOCALES.md). Las herramientas Python no requieren internet.

## GitHub Actions — todavía pendiente de comprobar en la cuenta

| Comprobación | URL real de la ejecución | Estado |
|---|---|---|
| `integracion-planta` | PENDIENTE | No ejecutado/verificado desde este entorno |
| `seguridad-planta` | PENDIENTE | No ejecutado/verificado desde este entorno |
| `controles-complementarios` | PENDIENTE | No ejecutado/verificado desde este entorno |
| SBOM adjunta a Actions | PENDIENTE | El generador local es independiente del informe externo |

Para añadir una evidencia verdadera: GitHub → Actions → elegir workflow → abrir su ejecución → copiar URL. Indicar si terminó verde o rojo, qué control lo causó y cómo se gestionó. **No usar enlaces ni capturas de otros repositorios como resultados propios.**

## Límites

El proyecto solo evalúa una muestra local y patrones determinados; no sustituye una auditoría externa, pruebas de seguridad industrial, ni revisión del historial y rotación de secretos reales.
