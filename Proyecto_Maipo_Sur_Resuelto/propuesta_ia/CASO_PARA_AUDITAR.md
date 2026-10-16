# Propuesta #7 — parche de IA (NO EJECUTAR / NO FUSIONAR)

Material de análisis solamente. Reproduce el fragmento inseguro de la presentación.

```python
import subprocess
import requests
from plc_helper_utils import leer_registro  # procedencia no comprobada

def leer_cloro(host, registro):
    cmd = "modpoll -r " + registro + " " + host
    salida = subprocess.run(cmd, shell=True, capture_output=True)
    requests.post(TELEMETRIA, verify=False, data=salida.stdout)
    return salida.stdout
```

**Decisión preliminar:** RECHAZAR; no se debe fusionar ni ejecutar este código.

1. Paquete sin procedencia verificada: `plc_helper_utils` requiere validación en PyPI, control de versiones y revisión de mantenedor.
2. Entradas: concatena `registro` y `host` en un comando que usa `shell=True`.
3. Protecciones: `verify=False` desactiva verificación TLS.
4. Datos: envía la salida a `TELEMETRIA` sin autorización, minimización ni destino identificado.
