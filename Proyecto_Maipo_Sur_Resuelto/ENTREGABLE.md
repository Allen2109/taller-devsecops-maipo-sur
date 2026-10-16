# Ficha de blindaje — Maipo Sur

**Equipo:** Daniel Silva · Allen Ramirez · Antonella Mancilla  
**Curso:** SIST AUTO DEVSECOPS · Universidad Bernardo O'Higgins  
**Fecha de preparación:** 16 de octubre de 2026  
**Sector principal:** agua potable simulada. Se agregaron casos complementarios de energía, salud y transporte.

> No copiar contraseñas ni inventar resultados de GitHub Actions. Los controles locales y remotos tienen alcances distintos.

## 1. Sistema y equipo

**Sistema:** lector simulado de valores de cloro en una planta ficticia.  
**Objetivo:** impedir que cambios no revisados introduzcan secretos, patrones inseguros o configuraciones abiertas.  
**Integrantes:** Daniel Silva, Allen Ramirez y Antonella Mancilla.  
**Roles:** repartir entre el equipo antes de exponer: operación/impacto, desarrollo/pipeline, y auditoría/relatoría.  
**Diagrama:** [ver diagrama propio](docs/arquitectura/maipo-sur.svg).

## 2. Tres amenazas priorizadas (STRIDE)

| Riesgo | Categoría | Impacto potencial | Control previsto |
|---|---|---|---|
| Credencial del controlador en un archivo público | Filtración / suplantación | Acceso no autorizado al sistema de supervisión, con riesgo de interrupción del servicio | Gitleaks y uso de una variable de entorno; rotación obligatoria en sistema real |
| Cambio no validado en órdenes de la HMI | Manipulación / elevación | Indicaciones incorrectas a un controlador, con riesgo para la continuidad del servicio | Revisión de cambios, mínimo privilegio, tests y validación operacional previa |
| Servicio o componente vulnerable | Denegación / manipulación | Pérdida de disponibilidad y retraso en supervisión | Revisión de dependencias (Trivy, OSV) y pruebas antes del despliegue |

**Alcance:** los controles de GitHub detectan clases de riesgo del software, **no** aseguran una planta física; el enlace entre TI y TO requiere protecciones y aprobaciones externas.

## 3. Controles y evidencia

| Control | Comprobación | Estado |
|---|---|---|
| Tests de Python + revisión sectorial | `python -m unittest discover -s tests -v` | Validar localmente / ver registro en evidencias |
| Gitleaks | Archivos actuales y reglas de laboratorio | Pendiente de ejecución de GitHub Actions |
| Semgrep | Reglas de `shell=True` y validación TLS | Pendiente de ejecución en Actions |
| Trivy | Dependencias e infraestructura simulada | Pendiente de ejecución en Actions |
| OSV-Scanner | Revisión del material de dependencias | Pendiente de ejecución en Actions |

**Enlace integración:** [abrir Actions](https://github.com/Allen2109/taller-devsecops-maipo-sur/actions/workflows/ci.yml) — pegar URL de una ejecución real: `PENDIENTE`.  
**Enlace seguridad:** [abrir Actions](https://github.com/Allen2109/taller-devsecops-maipo-sur/actions/workflows/seguridad.yml) — pegar URL de una ejecución real: `PENDIENTE`.

## 4. Hallazgo, impacto y decisión

**Hallazgo inicial del escenario agua:** una credencial escrita directamente en `config.yaml` (ejercicio ficticio).  
**Gravedad:** alta, si existiera en una instalación real.  
**Decisión:** corregir, referenciando el nombre `PLC_PASSWORD` sin guardar el valor en el repositorio.  
**Responsable:** equipo de desarrollo; **verificación:** equipo de revisión mediante Actions.  
**Estado actual del archivo de ejemplo:** `password_env: PLC_PASSWORD`; esto puede comprobarse inspeccionando el código.  
**Pendiente real:** si hubiera existido una credencial auténtica, sería imprescindible revocarla/rotarla e investigar el historial; este laboratorio no realiza esa operación.

## 5. Auditoría humana del parche escrito por IA

**Veredicto: RECHAZAR la propuesta #7 mientras no sea rediseñada y auditada.**

1. **Paquete:** `plc_helper_utils` carece de verificación acreditada; no se presume legítimo ni se declara inexistente sin consultar un registro real.
2. **Entradas:** la propuesta mezcla datos de entrada en comandos con `shell=True`; peligro de ejecución no prevista.
3. **Protección:** `verify=False` desactiva la comprobación del certificado TLS.
4. **Destino de datos:** `TELEMETRIA` no posee autorización y justificación documentadas.

[Evidencia técnica explicada y requisitos para una alternativa segura](docs/auditoria-ia/veredicto.md).

## 6. Pendientes antes de un despliegue real

La aplicación no tiene conectividad operacional. Faltarían una evaluación industrial específica, gestión de identidades, cambios aprobados, ventanas de mantenimiento, monitoreo, pruebas bajo supervisión y auditoría del historial de secretos.

## 7. Reproducción

```bash
python -m unittest discover -s tests -v
python scripts/revisar_sector.py todos
python scripts/generar_sbom.py
```

**Modalidad del ejemplo:** análisis de archivos actuales; no certifica el historial.  
**Evidencia comprobada y pendiente:** [evidencias/VALIDACION.md](evidencias/VALIDACION.md).
