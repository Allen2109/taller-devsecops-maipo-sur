import os
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lector_cloro import leer_cloro_simulado

class PruebaLector(unittest.TestCase):
    def test_sin_credencial_la_simulacion_falla(self):
        anterior = os.environ.pop('PLC_PASSWORD', None)
        try:
            with self.assertRaises(RuntimeError):
                leer_cloro_simulado()
        finally:
            if anterior is not None: os.environ['PLC_PASSWORD'] = anterior

    def test_lectura_no_divulga_clave(self):
        anterior = os.environ.get('PLC_PASSWORD')
        os.environ['PLC_PASSWORD']='VALOR-FICTICIO-DE-PRUEBA'
        try:
            lectura=leer_cloro_simulado()
            self.assertEqual(lectura['cloro_mg_l'], 0.7)
            self.assertNotIn('VALOR-FICTICIO-DE-PRUEBA', str(lectura))
        finally:
            if anterior is None: os.environ.pop('PLC_PASSWORD',None)
            else: os.environ['PLC_PASSWORD']=anterior

if __name__=='__main__': unittest.main()
