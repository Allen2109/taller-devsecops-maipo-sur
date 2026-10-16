# Maipo Sur — Taller DevSecOps de infraestructura crítica

![Integración](https://github.com/Allen2109/taller-devsecops-maipo-sur/actions/workflows/ci.yml/badge.svg?branch=main)
![Seguridad](https://github.com/Allen2109/taller-devsecops-maipo-sur/actions/workflows/seguridad.yml/badge.svg?branch=main)

**Universidad Bernardo O'Higgins · SIST AUTO DEVSECOPS · Octubre de 2026**

**Integrantes: Daniel Silva · Allen Ramirez · Antonella Mancilla**

> Proyecto académico original de laboratorio, inspirado por los contenidos del taller y el repositorio de referencia citado en [`docs/REFERENCIAS_Y_AUTORIA.md`](docs/REFERENCIAS_Y_AUTORIA.md). **No existe una planta conectada**: toda operación es local, simulada y con datos inventados.

## Resumen

Estudiamos cómo prevenir que errores de software afecten servicios esenciales. En nuestro caso, Maipo Sur representa una planta de agua potable ficticia. Un lector devuelve un valor inventado de `0.7 mg/L` que **no representa una recomendación sanitaria**; no hay PLC, red industrial ni dosificación real. El proyecto integra controles de secretos, patrones de código, dependencias y configuración, además de un modelo de amenazas y una revisión crítica de código propuesto por IA.

## Accesos rápidos a la entrega

| Evidencia | Documento |
|---|---|
| Ficha principal del equipo | [ENTREGABLE.md](ENTREGABLE.md) |
| Diagrama de flujo de datos | [Arquitectura SVG](docs/arquitectura/maipo-sur.svg) |
| Modelado de amenazas STRIDE | [Amenazas y riesgos](docs/modelado/amenazas.md) |
| Medidas y controles | [Plan de mejora](docs/modelado/plan-controles.md) |
| Auditoría de propuesta de IA | [Veredicto](docs/auditoria-ia/veredicto.md) |
| Política del repositorio | [POLITICA_SEGURIDAD.md](POLITICA_SEGURIDAD.md) |
| Matriz de rúbrica | [docs/evaluacion/rubrica.md](docs/evaluacion/rubrica.md) |
| Ejecuciones reales (una vez que GitHub Actions corra) | [Integración](https://github.com/Allen2109/taller-devsecops-maipo-sur/actions/workflows/ci.yml) · [Seguridad](https://github.com/Allen2109/taller-devsecops-maipo-sur/actions/workflows/seguridad.yml) |
| Registro de lo verificado y lo pendiente | [evidencias/VALIDACION.md](evidencias/VALIDACION.md) |
| Guion de presentación | [docs/presentacion/guion_90_segundos.md](docs/presentacion/guion_90_segundos.md) |

## Estructura del proyecto

```text
.github/workflows/           # Integración continua y revisiones de seguridad
lector_cloro.py              # Lector local ficticio
config.yaml                  # Configuración: referencia PLC_PASSWORD, nunca su valor
tests/                       # Tests unitarios y pruebas de detección
scripts/                     # Validaciones, demostración y empaquetado
escenarios/                  # Casos simulados de energía, salud y transporte
docs/arquitectura/           # Diagrama de flujo de datos y alcance
docs/modelado/               # Matriz STRIDE y controles
docs/auditoria-ia/           # Evaluación humana del parche de IA
docs/evaluacion/             # Rúbrica y trazabilidad
evidencias/                  # Resultados observados o pendientes (no inventados)
ENTREGABLE.md                # Ficha para calificación
```

## Ejecutar las pruebas localmente

Requiere Python 3.10 o superior, sin instalar paquetes adicionales:

```bash
python -m unittest discover -s tests -v
python scripts/revisar_sector.py todos
python scripts/generar_sbom.py
```

La ejecución funcional opcional requiere una variable **solo de demostración** (no usar credenciales reales):

```bash
# Windows PowerShell
$env:PLC_PASSWORD='FICTICIO_SOLO_PRUEBA'
python scripts/prueba_funcional.py
```

## GitHub Actions (la carpeta `.github` debe estar en la raíz)

- **`integracion-planta`**: prueba todos los casos con Python y construye una entrega ZIP como artefacto.
- **`seguridad-planta`**: ejecuta Gitleaks sobre archivos actuales, valida los cuatro escenarios y realiza una prueba funcional. Detectar un fallo produce un resultado rojo, **no se apagan reglas**.
- **`controles-complementarios`**: incorpora Semgrep, Trivy y OSV-Scanner (este último revisa el archivo de dependencias del escenario de energía) para análisis externo. Debe validarse tras subir a GitHub (requiere descargas de herramientas de terceros).

Importante: el escaneo pedagógico de Gitleaks se limita a los archivos actuales. No certifica que no existan secretos en commits históricos. En una operación real se requerirían rotación de claves, análisis del historial y revisión profesional, además de controles del entorno operacional.

## Ejercicio reproducible de 15 minutos

1. En Actions ejecuta `seguridad-planta` con sector `todos` y observa el resultado sobre el proyecto corregido.
2. Para demostrar la detección inicial, utiliza **una copia aparte del laboratorio** y cambia `config.yaml` únicamente con un valor de prueba definido por la guía, nunca uno real.
3. Ejecuta la revisión; lee qué control falla y registra el motivo.
4. En la copia, elimina el valor literal y usa `password_env: PLC_PASSWORD`. El secreto se configura en **Settings → Secrets and variables → Actions**.
5. Ejecuta de nuevo y registra los enlaces reales de GitHub Actions. **No se debe confundir un resultado verde con garantía total de seguridad.**

## Evidencia y autoría

El modelo, la explicación de riesgos y los tests de esta versión fueron preparados para **Daniel Silva, Allen Ramirez y Antonella Mancilla**. El repositorio de Miguel Briceño se consultó como referencia de estructura y buenas prácticas; no se presenta su trabajo como autoría del equipo. No se han copiado sus capturas ni resultados de ejecución. Los enlaces a comprobaciones de esta cuenta deben completarse **solo después de ejecutarlas**.
