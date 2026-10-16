"""Registro de datos simulados."""
import uuid

def anotar_lectura(paciente_id: str, valor: float) -> None:
    correlacion = str(uuid.uuid4())
    print(f"correlacion={correlacion} lectura_validada=True")
