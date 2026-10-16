# Plan de controles y decisiones

| Prioridad | Riesgo | Acción concreta en el laboratorio | Verificación | Responsable sugerido |
|---|---|---|---|---|
| 1 | R1 credencial literal | Dejar solo `password_env: PLC_PASSWORD` y revisar con Gitleaks | Workflow `seguridad-planta` | Desarrollo + revisor |
| 2 | R2 cambio no validado | Añadir tests de lectura y Pull Requests revisados | Workflow `integracion-planta` | Desarrollo + revisor |
| 3 | R3 dependencias | Ejecutar Semgrep, Trivy y OSV; generar SBOM de la aplicación de prueba | `controles-complementarios` y archivo SBOM | Seguridad del software |
| 4 | R4 logs sensibles | Mantener registro con correlación aleatoria no identificatoria | Test del sector salud | Auditoría |
| 5 | R5 panel abierto | Usar solo rango documental de ejemplo, sin infraestructura desplegable | Test del sector transporte | Auditoría |
| 6 | R6 propuesta IA | Rechazar parche no revisado y justificar cada señal | Documento de veredicto | Equipo completo |

**Decisión de tratamiento:** corregir ahora los defectos que se pueden demostrar en el repositorio; documentar como pendientes los riesgos de operación industrial que exceden el laboratorio. No se elimina ninguna prueba para simular que un riesgo desapareció.
