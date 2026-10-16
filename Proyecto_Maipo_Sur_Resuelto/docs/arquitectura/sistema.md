# Arquitectura y límites de confianza

El modelo usa tres niveles conceptuales: **operador**, **HMI/servicio ficticio**, y **proceso industrial conceptual**. Las flechas no representan conexiones operativas reales. `lector_cloro.py` devuelve un valor de muestra sin abrir sockets.

- El operador puede consultar una lectura ficticia.
- El programa verifica únicamente que la variable de entorno `PLC_PASSWORD` exista, pero **no autentica** con un dispositivo.
- El pipeline automatizado valida código y configuración del repositorio antes de una eventual publicación.
- En el límite entre desarrollo y operación deben existir aprobaciones, pruebas y medidas de segmentación que no se implementan en este laboratorio.

Diagrama: [maipo-sur.svg](maipo-sur.svg). Esta figura es un diseño digital de referencia; no es una fotografía de un trabajo presencial.
