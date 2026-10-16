"""Prueba local sin servicio externo."""
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lector_cloro import leer_cloro_simulado

os.environ.setdefault("PLC_PASSWORD", "VALOR-FICTICIO-DE-PRUEBA")
lectura = leer_cloro_simulado()
assert lectura["cloro_mg_l"] == 0.7
assert "PLC_PASSWORD" not in lectura
print("OK: lectura ficticia, sin mostrar secretos")
