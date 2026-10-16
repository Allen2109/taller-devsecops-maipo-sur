# Taller DevSecOps — Planta Maipo Sur (solución didáctica)

**Solo entorno simulado.** No se conecta a PLC, HMI, SCADA, redes, sistemas ni pacientes reales.

## Qué incluye
- El lector de cloro simulado que no revela secretos.
- `config.yaml` que referencia `PLC_PASSWORD` sin incrustar su valor.
- Pruebas locales con Python y 2 workflows de Github Actions.
- Reglas de Gitleaks/Semgrep y análisis Trivy/OSV para nube.
- Documento `ENTREGABLE.md` (ficha breve) y `ANALISIS_DETALLADO.md` (respaldo).
- Propuesta de IA para **auditar, nunca ejecutar**.

## Comprobar sin instalar dependencias
Desde la carpeta del proyecto, ejecutar:
```bash
python scripts/validar_config.py
python scripts/prueba_funcional.py
python -m unittest discover -s tests -v
```
Estas comprobaciones **no sustituyen** Gitleaks, Semgrep, Trivy ni OSV.

## Subir y demostrar en GitHub
1. Crear repositorio **privado** y subir estos archivos conservando las carpetas ocultas.
2. En `Settings > Secrets and variables > Actions`, crear un secreto `PLC_PASSWORD` con un valor ficticio diferente al de los ejemplos.
3. Ir a `Actions > seguridad-planta > Run workflow` y revisar cada paso.
4. Ejecutar `osv-scanner-dependencias` y consultar sus resultados.
5. Abrir los detalles de `seguridad-planta` y descargar el artefacto `inventario-sbom-cyclonedx` cuando aparezca.
6. Completar los enlaces reales en `ENTREGABLE.md` y registrar evidencia antes de entregar.

**Atención:** No se ha probado aquí una ejecución en GitHub Actions. La revisión en vivo puede revelar incompatibilidades o nuevos hallazgos. Las referencias `@vN` son etiquetas, no SHA inmutables; se deben reemplazar por SHA completos verificados antes de uso productivo (punto extra de la rúbrica).

## Acerca del historial
Este ejercicio básico mira el estado actual con un `fetch-depth: 1`. En repos reales, borrar un valor no borra su historial: corresponde rotar/revocar la credencial y gestionar limpieza del historial por un procedimiento controlado.
