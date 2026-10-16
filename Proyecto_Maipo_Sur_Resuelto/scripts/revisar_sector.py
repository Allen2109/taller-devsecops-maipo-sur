"""Validaciones didácticas y deliberadamente acotadas; NO equivalen a un escáner de producción."""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

def comprobar(sector):
    if sector == 'agua':
        contenido = (ROOT / 'config.yaml').read_text(encoding='utf-8')
        if re.search(r'(?m)^password\s*:', contenido):
            return False, 'AGUA: credencial almacenada directamente en config.yaml. Sustituir por password_env: PLC_PASSWORD.'
        if 'password_env: PLC_PASSWORD' not in contenido:
            return False, 'AGUA: falta la referencia password_env: PLC_PASSWORD en config.yaml.'
        return True, 'AGUA: configuración referencia el nombre del secreto, sin valor expuesto.'
    if sector == 'energia':
        contenido = (ROOT / 'escenarios/energia/requirements.in').read_text(encoding='utf-8')
        lineas = [ln.strip() for ln in contenido.splitlines() if ln.strip() and not ln.lstrip().startswith('#')]
        if not lineas or any(not re.fullmatch(r'[a-zA-Z0-9_.-]+==[0-9][a-zA-Z0-9_.+!-]*',ln) for ln in lineas):
            return False, 'ENERGÍA: dependencia sin versión exacta en escenarios/energia/requirements.in.'
        return True, 'ENERGÍA: las dependencias del ejercicio tienen versiones exactas (no implica que no tengan CVE).'
    if sector == 'salud':
        contenido = (ROOT / 'escenarios/salud/registro.py').read_text(encoding='utf-8')
        if re.search(r'(?m)^\s*print\(.*paciente_id', contenido):
            return False, 'SALUD: el registro imprime un identificador de paciente (ficticio). Retirar ese campo del log.'
        return True, 'SALUD: no se detecta el patrón didáctico de identificación de paciente en logs.'
    if sector == 'transporte':
        contenido = (ROOT / 'escenarios/transporte/infra/panel.tf').read_text(encoding='utf-8')
        if '0.0.0.0/0' in contenido:
            return False, 'TRANSPORTE: rango de origen abierto a internet en configuración simulada.'
        return True, 'TRANSPORTE: no se detecta el rango totalmente abierto (requiere validación de red autorizada).'
    return False, 'Sector inválido'

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('sector',choices=['agua','energia','salud','transporte','todos'],nargs='?',default='agua')
    args=p.parse_args()
    sectores=['agua','energia','salud','transporte'] if args.sector == 'todos' else [args.sector]
    resultados=[comprobar(sec) for sec in sectores]
    for ok,mensaje in resultados:
        print(('OK: ' if ok else 'HALLAZGO: ')+mensaje)
    sys.exit(0 if all(ok for ok,_ in resultados) else 1)
