export type PracticalWorkflow = {
  slug: string;
  title: string;
  description: string;
  task: string;
  tools: string[];
  steps: string[];
  prompt: string;
  test: string[];
  success: string[];
  doNotDelegate: string;
  evidence: string;
};

export const practicalWorkflows: PracticalWorkflow[] = [
  {
    slug: 'reunion-a-decisiones-y-tareas', title: 'Convertir una reunión en decisiones y tareas revisables', description: 'Workflow para transformar una transcripción en acuerdos, responsables y fechas sin inventar lo que no se dijo.', task: 'Reuniones', tools: ['granola','fathom','notebooklm','chatgpt'],
    steps: ['Avisa a los participantes y confirma que puedes grabar o transcribir.', 'Conserva la transcripción original como fuente.', 'Pide que se separen decisiones, acciones, responsables, fechas y dudas.', 'Contrasta cada elemento con el fragmento exacto de la transcripción.', 'Envía el borrador a una persona responsable antes de crear tareas o avisos.'],
    prompt: 'Usa únicamente esta transcripción. Devuelve cinco apartados: decisiones, acciones, responsable mencionado, fecha mencionada y dudas. Añade para cada elemento una cita breve o marca “no consta”. No asignes responsables ni fechas por inferencia.',
    test: ['Usa una reunión cerrada cuyo acta ya conozcas.', 'Incluye una frase ambigua sin responsable.', 'Comprueba que la salida conserva la duda en vez de completarla.'], success: ['No inventa acuerdos, responsables ni fechas.', 'Cada elemento puede volver a la transcripción.', 'La revisión humana ocurre antes de enviar o crear tareas.'], doNotDelegate: 'Consentimiento, aprobación del acta, asignación final de responsables y envío automático.', evidence: 'Plantilla editorial basada en trazabilidad; debe probarse con la política y la herramienta de cada organización.',
  },
  {
    slug: 'verificar-formula-hoja-calculo', title: 'Verificar una fórmula de hoja de cálculo con IA', description: 'Proceso para explicar o corregir una fórmula sin permitir que una respuesta plausible altere tus resultados.', task: 'Hojas de cálculo', tools: ['microsoft-copilot','gemini','quadratic','chatgpt'],
    steps: ['Trabaja en una copia con resultados conocidos.', 'Describe columnas, objetivo y tres filas de ejemplo anonimizadas.', 'Pide fórmula, explicación y casos límite por separado.', 'Prueba la fórmula en celdas nuevas y compara con el resultado conocido.', 'Documenta herramienta, versión, input y corrección manual.'],
    prompt: 'Propón una fórmula para el objetivo indicado. Explica cada parte, marca los supuestos y crea tres casos de prueba, incluido un valor vacío y un error. No cambies datos ni des por correcta la fórmula hasta que los casos coincidan.',
    test: ['Elige una fórmula ya resuelta.', 'Oculta la solución a la herramienta.', 'Compara resultado, explicación y casos límite.'], success: ['Resultado correcto en todos los casos.', 'Explicación comprensible.', 'No modifica rangos ni supuestos sin avisar.'], doNotDelegate: 'La aprobación de cifras financieras, pagos o cierres.', evidence: 'Plantilla de prueba local; todavía no implica rendimiento universal de ninguna herramienta.',
  },
  {
    slug: 'investigar-con-fuentes', title: 'Investigar un tema sin perder las fuentes', description: 'Workflow para separar descubrimiento, selección, análisis y redacción con herramientas distintas.', task: 'Investigación', tools: ['perplexity','notebooklm','gemini','kimi'],
    steps: ['Formula una pregunta que pueda responderse con evidencia.', 'Busca documentos primarios y descarta resúmenes que no sostienen el claim.', 'Crea un corpus pequeño con las fuentes aceptadas.', 'Extrae hechos, declaraciones e inferencias en columnas separadas.', 'Redacta la conclusión enlazando cada claim importante.'],
    prompt: 'Analiza únicamente las fuentes proporcionadas. Devuelve una tabla con claim, tipo de claim, fuente exacta, fragmento que lo sostiene, fecha y duda pendiente. Si una fuente no permite afirmar algo, escribe “no demostrado”.',
    test: ['Incluye una fuente que no apoye el claim.', 'Comprueba si la salida la rechaza.', 'Abre manualmente todas las URLs conservadas.'], success: ['Cada claim apunta a su fuente.', 'Las dudas permanecen visibles.', 'No usa una fuente sobre un producto para validar otro.'], doNotDelegate: 'La decisión final de publicar un claim factual.', evidence: 'Basado en la jerarquía editorial de fuentes de Decodifica; debe probarse con cada investigación.',
  },
  {
    slug: 'prototipo-app-revisable', title: 'Crear un prototipo de app que puedas revisar', description: 'Proceso corto para pasar de idea a prototipo sin confundir una demo generada con un producto seguro.', task: 'Creación de aplicaciones', tools: ['emergent','cursor','github-copilot','qwen-code'],
    steps: ['Define un usuario, un problema y una acción principal.', 'Limita el prototipo a tres pantallas y datos ficticios.', 'Pide primero estructura y criterios de terminado.', 'Genera en una rama o entorno aislado.', 'Prueba errores, permisos, móvil y recuperación antes de compartir.'],
    prompt: 'Crea un plan para un prototipo con máximo tres pantallas. Usa datos ficticios, no añadas autenticación ni pagos reales y separa requisitos, archivos, riesgos y pruebas. Espera confirmación antes de modificar código.',
    test: ['Usa datos de ejemplo.', 'Prueba el camino feliz y tres errores.', 'Revisa diff, dependencias y llamadas externas.'], success: ['El prototipo resuelve una acción.', 'Los errores son visibles y recuperables.', 'No contiene secretos ni permisos innecesarios.'], doNotDelegate: 'Seguridad, autenticación, pagos, migraciones y despliegue.', evidence: 'Plantilla de prototipo controlado; no valida producción ni seguridad por sí sola.',
  },
  {
    slug: 'planificar-semana-sin-ceder-prioridades', title: 'Planificar la semana sin ceder tus prioridades', description: 'Workflow para convertir tareas y calendario en un borrador semanal que sigue requiriendo decisión humana.', task: 'Planificación', tools: ['reclaim','motion','notion-ai','microsoft-copilot'],
    steps: ['Reúne compromisos fijos y tareas con plazo.', 'Marca impacto, duración aproximada y energía requerida.', 'Pide un borrador con márgenes y bloques de concentración.', 'Revisa conflictos, descansos y compromisos externos.', 'Cierra el plan y registra qué se reprogramó realmente.'],
    prompt: 'Propón un plan semanal sin mover compromisos fijos. Prioriza por plazo e impacto, reserva márgenes y marca cualquier conflicto. No aceptes nuevas reuniones ni cambies fechas externas. Devuelve tabla por día y lista de decisiones pendientes.',
    test: ['Usa una semana ya terminada.', 'Compara el plan con lo que ocurrió.', 'Mide tareas completadas y reprogramaciones.'], success: ['Respeta compromisos fijos.', 'No sobrecarga todos los huecos.', 'Las prioridades importantes aparecen antes que tareas pequeñas.'], doNotDelegate: 'Aceptar reuniones, prometer fechas o cambiar prioridades personales.', evidence: 'Plantilla de planificación; debe adaptarse a calendario y carga reales.',
  },
];
