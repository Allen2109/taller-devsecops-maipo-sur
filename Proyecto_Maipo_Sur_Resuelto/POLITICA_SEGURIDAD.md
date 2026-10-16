# Política del repositorio — Maipo Sur

**Equipo:** Daniel Silva · Allen Ramirez · Antonella Mancilla

1. **Laboratorio aislado.** Prohibido conectar este ejemplo a PLC, HMI, SCADA, redes industriales o servicios reales.
2. **Cambios revisados.** Documentar el propósito de cada cambio y revisarlo mediante Pull Request cuando sea viable.
3. **Sin secretos reales.** Credenciales auténticas nunca se publican. `PLC_PASSWORD` se proporciona por entorno en ejecución; para tests locales se utilizan únicamente valores ficticios.
4. **Menor privilegio.** Los workflows usan permisos de lectura y no incorporan despliegues automáticos de infraestructura.
5. **Resultados verificables.** Los enlaces a ejecuciones se registran después de ejecutarlas. El resultado de una simulación no equivale a una certificación de seguridad.
6. **Dependencias auditables.** Para aplicaciones reales exigir versiones fijadas y acciones externas ancladas a SHA completo verificado.
7. **Cambios de IA.** No fusionar propuestas de IA sin comprobar procedencia, tratamiento de entradas, validaciones y destinos de datos.
8. **Tratamiento de hallazgos.** Documentar gravedad, decisión, justificación, responsable y fecha. Nunca desactivar una regla para fabricar un resultado verde.

La protección de `main` mediante reglas de ramas y revisores debe configurarse en el sitio web de GitHub. Los nombres del equipo no equivalen a nombres de usuario de GitHub; por eso no se configura un `CODEOWNERS` inventado.
