"""Pruebas unitarias sin PLC, red ni sistemas externos."""
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from lector_cloro import leer_cloro_simulado
from scripts import revisar_sector

class TestLectorLocal(unittest.TestCase):
    def test_exige_variable_de_entorno(self):
        with mock.patch.dict(os.environ,{},clear=True):
            with self.assertRaises(RuntimeError):
                leer_cloro_simulado()

    def test_devuelve_lectura_fija_y_no_secreto(self):
        with mock.patch.dict(os.environ, {'PLC_PASSWORD':'FICTICIO'}, clear=True):
            salida=leer_cloro_simulado()
        self.assertEqual(salida['cloro_mg_l'],0.7)
        self.assertNotIn('FICTICIO',str(salida))

class TestControles(unittest.TestCase):
    def test_todos_los_casos_corregidos(self):
        for sector in ('agua','energia','salud','transporte'):
            with self.subTest(sector=sector):
                ok,detalles=revisar_sector.comprobar(sector)
                self.assertTrue(ok,detalles)

    def test_detecta_credencial_literal_en_fixtura_aislada(self):
        with tempfile.TemporaryDirectory() as td:
            raiz=Path(td)
            (raiz/'config.yaml').write_text('planta: demo\npassword: VALOR_DE_PRUEBA\n',encoding='utf8')
            with mock.patch.object(revisar_sector,'ROOT',raiz):
                ok,msg=revisar_sector.comprobar('agua')
            self.assertFalse(ok)
            self.assertIn('credencial',msg)

    def test_detecta_dependencia_sin_version(self):
        with tempfile.TemporaryDirectory() as td:
            raiz=Path(td);(raiz/'escenarios/energia').mkdir(parents=True)
            (raiz/'escenarios/energia/requirements.in').write_text('requests\n',encoding='utf8')
            with mock.patch.object(revisar_sector,'ROOT',raiz):
                ok,msg=revisar_sector.comprobar('energia')
            self.assertFalse(ok)

    def test_detecta_log_con_id_en_ejemplo(self):
        with tempfile.TemporaryDirectory() as td:
            raiz=Path(td);(raiz/'escenarios/salud').mkdir(parents=True)
            (raiz/'escenarios/salud/registro.py').write_text('print(paciente_id)\n',encoding='utf8')
            with mock.patch.object(revisar_sector,'ROOT',raiz):
                ok,msg=revisar_sector.comprobar('salud')
            self.assertFalse(ok)

    def test_detecta_rango_abierto_en_ejemplo(self):
        with tempfile.TemporaryDirectory() as td:
            raiz=Path(td);(raiz/'escenarios/transporte/infra').mkdir(parents=True)
            (raiz/'escenarios/transporte/infra/panel.tf').write_text('cidr = "0.0.0.0/0"\n',encoding='utf8')
            with mock.patch.object(revisar_sector,'ROOT',raiz):
                ok,msg=revisar_sector.comprobar('transporte')
            self.assertFalse(ok)

if __name__ == '__main__':unittest.main()
