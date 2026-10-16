# Ficha de blindaje — Planta Maipo Sur | Equipo 1: Agua
**Fecha:** 09-10-2026 · **Integrantes y roles:** operador [ ], desarrollador [ ], pipeline [ ], auditor IA [ ], relator [ ].  
**Estado:** pruebas locales aprobadas; enlaces y resultados reales de GitHub Actions pendientes.

## 1. Sistema y diagrama
**Operador → HMI/servicio web → PLC ficticio → cloración ficticia.** La implementación solo devuelve una lectura simulada de 0,7 mg/L; **no controla equipos reales**. El repositorio es revisado por CI y un operador autoriza cualquier cambio.

## 2. Amenazas priorizadas (STRIDE)
| Amenaza | Impacto físico hipotético | Control |
|---|---|---|
| 1. Suplantación / filtración de clave | Alteración de dosificación; se requiere comprobar la calidad del agua. | Gitleaks, secreto fuera del código y rotación. |
| 2. Manipulación / elevación de privilegios | Cambio de parámetros sin autorización. | Mínimo privilegio, validación y revisión humana. |
| 3. Denegación de servicio | Pérdida de visibilidad del tratamiento. | Pruebas, monitoreo y continuidad operativa. |

## 3. Controles y evidencia
**Incluidos:** Gitleaks (secretos), Semgrep (código), Trivy (dependencias/configuración/SBOM), OSV-Scanner (dependencias) y pruebas locales (aprobadas). **GitHub Actions:** [URL REAL PENDIENTE]. **Repositorio:** [URL]. **SBOM CycloneDX:** [ENLACE/ARCHIVO]. **Evidencia del fallo y la corrección:** [CAPTURAS / URL]. No afirmar CI en verde antes de ejecutarla.

## 4. Hallazgo y decisión
| Hallazgo | Gravedad | Decisión justificada | Responsable |
|---|---|---|---|
| Credencial de laboratorio literal en `config.yaml` inicial | Crítica didáctica | **Corregir:** cambiar por `password_env: PLC_PASSWORD`, guardar secreto ficticio en Actions. En una planta real, revocar/rotar y revisar accesos. | Desarrollador + operador · 09-10-2026 (propuesto) |
| Posible exposición histórica | Alta | **Postergar con bloqueo de uso real:** remediar historial solo mediante procedimiento controlado. | Seguridad · [FECHA] |
| Actions fijadas por etiqueta, no SHA | Media | **Postergar con fecha:** verificar y fijar identificadores inmutables antes de producción. | Responsable CI · [FECHA] |

## 5. Auditoría del parche de IA — **RECHAZAR / NO FUSIONAR**
1. **Paquete:** `plc_helper_utils` sin origen y versión acreditados en el parche.
2. **Entradas:** concatena `host`/`registro` en `subprocess.run(..., shell=True)`.
3. **Protección:** `verify=False` elimina validación TLS.
4. **Datos:** `TELEMETRIA` recibe lecturas sin destino/autorización documentados.

**Explicación al operador:** «El parche podría permitir instrucciones no autorizadas y enviar datos operativos a un destino desconocido. En una planta real podría comprometer la continuidad y seguridad del tratamiento». La decisión es humana.

## 6. Pendientes y reproducción
Antes de uso real: validar en laboratorio OT, rotar credenciales, revisar accesos, asegurar zonas de red, aprobar cambios y fijar acciones por SHA. **No desplegar esta simulación.**  
`python scripts/validar_config.py` · `python scripts/prueba_funcional.py` · `python -m unittest discover -s tests -v`
