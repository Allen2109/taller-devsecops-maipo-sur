# Ficha de blindaje — Equipo 1 (Agua potable)

**Taller:** DevSecOps sobre Infraestructura Crítica · **Fecha de referencia:** 09-10-2026  
**Estado:** solución desarrollada y probada localmente; falta evidencia de GitHub Actions.

## 1. Sistema y equipo
- **Sector:** agua potable, planta simulada «Maipo Sur».
- **Función:** un programa presenta el nivel de cloro ficticio `0.7 mg/L`; no controla dispositivos físicos.
- **Integrantes:** [COMPLETAR NOMBRES].
- **Roles:** operador [NOMBRE], desarrollador [NOMBRE], guardián del pipeline [NOMBRE], auditor de IA [NOMBRE], relator [NOMBRE].

## 2. Diagrama de flujo y frontera de confianza
```text
OPERADOR HUMANO
      | consulta autorizada
      v
HMI / SERVICIO SIMULADO --------> REGISTRO Y MONITOREO
      | lectura (simulada)
      v
PLC FICTICIO -------------------> PROCESO DE CLORACIÓN (FICTICIO)
      ^
      | NO existe conexión física en este repositorio
      |
  Repositorio → revisión CI → autorización humana de despliegue
```
El mayor límite de confianza está entre el software/HMI y el controlador: ningún cambio debería llegar allí sin validación y autorización.

## 3. Tres amenazas priorizadas (STRIDE)
| Prioridad | Amenaza / categoría | Efecto en el mundo físico si fuera real | Control propuesto |
|---|---|---|---|
| 1 · crítica | Uso de una contraseña de fábrica filtrada (**Suplantación** y **Filtración de información**) | Un tercero podría cambiar parámetros y comprometer la dosificación; sería necesario aislar el equipo y validar la calidad del agua. | Gitleaks, secreto fuera del código, rotación real y registro de accesos. |
| 2 · alta | Modificación no autorizada de la orden enviada desde la HMI (**Manipulación / Elevación de privilegios**) | Podría alterarse una consigna o detenerse parte del proceso de tratamiento. | Roles mínimos, validación de parámetros, aprobación humana y revisiones Semgrep/CI. |
| 3 · alta | Interrupción de la lectura del sensor o del servicio (**Denegación de servicio**) | El operador perdería visibilidad del proceso, con riesgo de decisiones tardías. | Pruebas funcionales, monitorización, operación manual validada y continuidad de servicio. |

## 4. Controles preparados y evidencia
| Control | Implementación incluida | Evidencia de ejecución |
|---|---|---|
| Secretos | Gitleaks v3 y regla de laboratorio + `scripts/validar_config.py` | Validación local ejecutada. Resultado real de Gitleaks: **PENDIENTE**. |
| Código propio | Semgrep `.semgrep.yml` (shell y TLS) | **PENDIENTE GitHub Actions**. |
| Dependencias | Trivy `fs` y workflow oficial de OSV-Scanner | **PENDIENTE GitHub Actions**. |
| Infraestructura | Trivy `config`, carpeta `infra/` sin despliegue | **PENDIENTE GitHub Actions**. |
| SBOM | Trivy CycloneDX + upload-artifact | Archivo `sbom.cdx.json` a descargar tras ejecución. |
| Prueba funcional | `scripts/prueba_funcional.py` y `tests/test_lector.py` | **Validado localmente**. |

- **Enlace al repositorio:** [PEGAR URL REAL].
- **Enlace al workflow ejecutado:** [PEGAR URL REAL].
- **Evidencia del fallo inicial con Gitleaks:** [CAPTURA/ENLACE PENDIENTE].
- **Evidencia de ejecución corregida:** [CAPTURA/ENLACE PENDIENTE].
- **Enlace o archivo de SBOM:** [PENDIENTE].

## 5. Hallazgo, valoración y decisión
| Hallazgo | Gravedad | Decisión | Justificación | Responsable y fecha |
|---|---|---|---|---|
| Credencial literal en `config.yaml` inicial | Crítica (escenario de aprendizaje) | **Corregir ahora** | Se reemplaza por `password_env: PLC_PASSWORD`; se usa un secreto ficticio en Actions y nunca se imprime. En un PLC real, también se requeriría rotar la credencial y revisar accesos. | Desarrollador + operador · 09-10-2026 (propuesto) |
| Credencial potencialmente presente en historial | Alta | **Postergar al procedimiento de remediación, con bloqueo de despliegue real** | El taller básico no reescribe historia Git; en un sistema real se revoca primero y se realiza revisión forense controlada. | Responsable de seguridad · [FECHA REAL] |
| Etiquetas de acciones no fijadas a SHA completo | Media | **Postergar con responsable y fecha** | La plantilla se preparó con etiquetas oficiales para poder entenderla; para producción deben fijarse referencias inmutables verificadas. | Guardián CI · [FECHA REAL] |

## 6. Auditoría de la propuesta #7 generada por IA
**Veredicto: RECHAZAR, sin fusionar.** Evidencia de lectura del fragmento proporcionado en la presentación y `propuesta_ia/CASO_PARA_AUDITAR.md`.

1. **¿Existe el paquete?** `plc_helper_utils` está sin procedencia ni versión acreditadas; no se debe añadir hasta verificar registro, mantenedor, origen y hash. La evidencia suficiente para aprobarlo **no está aportada** en el parche.
2. **¿Qué hace con la entrada?** Concatena `host` y `registro` en el comando `modpoll`, luego llama a `subprocess.run(..., shell=True)`. Ese patrón puede interpretar entradas como parte del comando.
3. **¿Apaga protecciones?** `requests.post(..., verify=False)` desactiva la validación del certificado TLS.
4. **¿Dónde envía datos?** Publica la salida del controlador a `TELEMETRIA`, sin destino, política ni autorización documentados.

**Explicación para el operador (dos frases):** El parche propuesto podría permitir instrucciones no autorizadas y enviar información operativa a un destino no aprobado. En una instalación real, eso pondría en riesgo la continuidad y la seguridad del tratamiento de agua, aunque el programa aparentemente funcionara.

**Uso de IA en la explicación:** texto revisado por una persona; aprobación final no delegada a la IA.

## 7. Pendientes antes de utilizarlo en una planta real
- Prohibido implementar esta simulación directamente en una instalación real.
- Autenticación fuerte, credenciales únicas y rotación; acceso segregado a PLC/HMI.
- Validaciones en laboratorio OT, procedimientos de cambio, plan de reversión y ventanas de mantenimiento.
- Control de firmas, fijación de acciones/dependencias por hash y análisis de cadena de suministro.
- Revisar resultados verdaderos de Actions y tratar cualquier hallazgo de severidad alta/crítica.
- Incorporar monitoreo, bitácoras, redundancia y autorización del operador responsable.

## 8. Cómo reproducir
```bash
python scripts/validar_config.py
python scripts/prueba_funcional.py
python -m unittest discover -s tests -v
```
Para controles adicionales, ejecutar en GitHub `seguridad-planta` y `osv-scanner-dependencias`, y adjuntar los enlaces reales. **No se declara CI en verde sin su ejecución.**
