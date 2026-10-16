"""Prueba funcional; no muestra el secreto ni se conecta a nada."""
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lector_cloro import leer_cloro_simulado

resultado = leer_cloro_simulado()
assert resultado['cloro_mg_l'] == 0.7
print('PRUEBA OK: lectura ficticia recibida; secreto no mostrado')
