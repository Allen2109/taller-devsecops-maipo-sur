# Guion breve para exponer (90 segundos aproximados)

**Equipo: Daniel Silva, Allen Ramirez y Antonella Mancilla**

> Buenos días. Somos Daniel Silva, Allen Ramirez y Antonella Mancilla, y presentamos el laboratorio Maipo Sur, un caso ficticio de infraestructura crítica. Imaginamos una planta de agua potable con un programa de supervisión. En un sistema real, un error informático puede afectar un servicio esencial; por eso nuestro enfoque es detectar riesgos antes de usar cambios de software.
>
> Primero modelamos amenazas usando STRIDE. Priorizamos tres: exposición de credenciales, manipulación de instrucciones y dependencias vulnerables. El simulador no está conectado a ninguna máquina; devuelve solamente un dato de ejemplo.
>
> Después integramos controles de DevSecOps en GitHub Actions: pruebas de Python, búsqueda de credenciales y revisiones complementarias del código, las dependencias y la configuración. La idea es que un problema genere una alerta visible y se documente, en lugar de ignorarlo. [Aquí mostramos una ejecución real de nuestra cuenta y contamos su resultado.]
>
> Por último, auditamos un parche propuesto por IA. Lo rechazamos porque planteaba ejecutar comandos con entradas no validadas, desactivar la verificación TLS y enviar información a un destino no autorizado. Nuestra conclusión es que la automatización ayuda a detectar riesgos, pero la decisión de aprobar software sigue siendo humana.

**No leas como logrado lo que esté pendiente:** reemplaza el texto entre corchetes por un resultado comprobado o explica que la ejecución está por completar.
