# Subir esta versión a la raíz de tu GitHub

Repo destino: https://github.com/Allen2109/taller-devsecops-maipo-sur

**Importante:** no subir toda esta carpeta dentro de otra carpeta. Las rutas `.github/workflows/*.yml` tienen que quedar en la raíz para que GitHub Actions las detecte.

## Opción sin consola

1. Descomprime `Proyecto_Maipo_Sur_MEJORADO.zip` en Windows.
2. Abre la página principal del repositorio en GitHub y elige `Code` → `Add file` → `Upload files`.
3. Arrastra **el contenido** del proyecto (archivos y carpetas, incluida `.github`). Si GitHub se niega a reemplazar un archivo existente, abre ese archivo y edítalo directamente o utiliza GitHub Desktop.
4. Finaliza con `Commit changes`. Revisa que `.github` aparezca directamente en la página principal del repositorio.
5. Abre `Actions`: los workflows `integracion-planta`, `seguridad-planta` y `controles-complementarios` deberían aparecer. Ejecuta los dos primeros y anota la URL real en `evidencias/VALIDACION.md`.

**Subcarpeta anterior:** `Proyecto_Maipo_Sur_Resuelto` puede seguir como copia antigua, pero no es la carpeta que ejecuta Actions. Para evitar confusiones, déjala explícitamente como respaldo o elimínala después de verificar que este proyecto nuevo funciona en la raíz.

## Opción con Git para Windows

Si tienes Git instalado, puedes usar el script independiente [`ACTUALIZAR_GITHUB.ps1`](../ACTUALIZAR_GITHUB.ps1) incluido en el ZIP. Pide confirmación antes de hacer `push` y no solicita tokens ni contraseñas dentro del script.

## Comprobación antes de exponer

- [ ] Los tres nombres aparecen en `README.md` y `ENTREGABLE.md`.
- [ ] `.github/workflows` está en la raíz.
- [ ] `integracion-planta` muestra ejecución propia y los tests terminan.
- [ ] `seguridad-planta` muestra ejecución propia y Gitleaks informa resultados.
- [ ] `controles-complementarios` se probó o sus problemas se registraron, sin inventar un éxito.
- [ ] Se registraron enlaces reales de GitHub en `evidencias/VALIDACION.md`.
