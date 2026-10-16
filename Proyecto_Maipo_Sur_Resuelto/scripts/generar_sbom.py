"""Genera una SBOM CycloneDX mínima y honesta para el simulador stdlib.

No representa un análisis de dependencias remotas ni declara ausencia de CVE.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'evidencias'/'sbom-local.cdx.json'

def main():
    doc={
        'bomFormat':'CycloneDX', 'specVersion':'1.5', 'version':1,
        'metadata':{'component':{'type':'application','name':'maipo-sur-simulador','version':'1.0.0',
                                  'description':'Simulador académico sin PLC conectado y sin dependencias de terceros en ejecución.'}},
        'components':[],
        'dependencies':[]
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'SBOM académica generada: {OUT.relative_to(ROOT)} (aplicación base sin paquetes externos)')

if __name__=='__main__':main()
