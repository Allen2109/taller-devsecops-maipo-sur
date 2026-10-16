# Verificación local reproducible

**Equipo:** Daniel Silva, Allen Ramirez y Antonella Mancilla.

## Pruebas de Python

**Resultado:** correcto (código 0)

```text
test_detecta_credencial_literal_en_fixtura_aislada (test_laboratorio.TestControles.test_detecta_credencial_literal_en_fixtura_aislada) ... ok
test_detecta_dependencia_sin_version (test_laboratorio.TestControles.test_detecta_dependencia_sin_version) ... ok
test_detecta_log_con_id_en_ejemplo (test_laboratorio.TestControles.test_detecta_log_con_id_en_ejemplo) ... ok
test_detecta_rango_abierto_en_ejemplo (test_laboratorio.TestControles.test_detecta_rango_abierto_en_ejemplo) ... ok
test_todos_los_casos_corregidos (test_laboratorio.TestControles.test_todos_los_casos_corregidos) ... ok
test_devuelve_lectura_fija_y_no_secreto (test_laboratorio.TestLectorLocal.test_devuelve_lectura_fija_y_no_secreto) ... ok
test_exige_variable_de_entorno (test_laboratorio.TestLectorLocal.test_exige_variable_de_entorno) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.007s

OK
```

## Revisión sectorial

**Resultado:** correcto (código 0)

```text
OK: AGUA: configuración referencia el nombre del secreto, sin valor expuesto.
OK: ENERGÍA: las dependencias del ejercicio tienen versiones exactas (no implica que no tengan CVE).
OK: SALUD: no se detecta el patrón didáctico de identificación de paciente en logs.
OK: TRANSPORTE: no se detecta el rango totalmente abierto (requiere validación de red autorizada).
```

## Generación SBOM

**Resultado:** correcto (código 0)

```text
SBOM académica generada: evidencias/sbom-local.cdx.json (aplicación base sin paquetes externos)
```

## Empaquetado

**Resultado:** correcto (código 0)

```text
Paquete de laboratorio creado: dist/maipo-sur-simulador.zip
```

Los resultados corresponden a una ejecución en este entorno de preparación, NO a GitHub Actions ni a un entorno de producción.
