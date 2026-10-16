# Cuatro variantes ficticias para el ejercicio 2

**AGUA:** `config.yaml`. La credencial de demostración debe dejar de aparecer como valor. El archivo corregido referencia `password_env: PLC_PASSWORD`.

**ENERGÍA:** `escenarios/energia/requirements.in`. La dependencia no está fijada. Identificar qué significa una versión abierta y sustituirla por una versión exacta **previamente verificada**. El comprobador del taller revisa la fijación, no certifica ausencia de vulnerabilidades.

**SALUD:** `escenarios/salud/registro.py`. Un identificador de paciente totalmente ficticio se imprime en los registros. Mantener la trazabilidad con un identificador de correlación de laboratorio, sin datos sensibles.

**TRANSPORTE:** `escenarios/transporte/infra/panel.tf`. Permite conexiones de origen abierto. Cambiar el valor por un rango de documentación previamente aprobado para el ejercicio; no emplear una red real.

Cada equipo describe tres amenazas, el impacto físico, un control asociado, el resultado observable y una decisión argumentada.
