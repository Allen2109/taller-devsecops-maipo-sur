"""Crea un paquete fuente de la aplicación de laboratorio, sin artefactos secretos."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED

ROOT=Path(__file__).resolve().parents[1]
TARGET=ROOT/'dist'/'maipo-sur-simulador.zip'
INCLUDES=['lector_cloro.py','config.yaml','README.md','docs/arquitectura/sistema.md']

def main():
    TARGET.parent.mkdir(parents=True,exist_ok=True)
    with ZipFile(TARGET,'w',ZIP_DEFLATED) as z:
        for path in INCLUDES:
            z.write(ROOT/path,path)
    print(f'Paquete de laboratorio creado: {TARGET.relative_to(ROOT)}')

if __name__=='__main__':main()
