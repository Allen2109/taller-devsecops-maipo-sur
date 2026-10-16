"""Puerta de laboratorio: una credencial literal en config.yaml bloquea el cambio."""
from pathlib import Path
import re

contenido=Path(__file__).resolve().parents[1].joinpath('config.yaml').read_text(encoding='utf-8')
assert not re.search(r'(?m)^\s*password\s*:\s*\S+', contenido), (
    'ERROR: config.yaml contiene una credencial en claro; use password_env: PLC_PASSWORD')
assert re.search(r'(?m)^\s*password_env\s*:\s*PLC_PASSWORD\s*$', contenido), (
    'ERROR: la configuracion debe referenciar PLC_PASSWORD')
print('OK: config.yaml no contiene credenciales literales')
