export type ToolUseCase = {
  slug: string;
  title: string;
  h1: string;
  description: string;
  intro: string;
  tools: string[];
  comparisons: { label: string; href: string; description: string }[];
  decisionRules: string[];
  risks: string[];
};

export const toolUseCases: ToolUseCase[] = [
  {
    slug: 'para-estudiar',
    title: 'Herramientas IA para estudiar',
    h1: 'Herramientas IA para estudiar sin perderte entre apps',
    description: 'Guía evergreen de herramientas IA para estudiar: NotebookLM, Perplexity, ChatGPT y Claude según fuentes, resúmenes, apuntes y privacidad.',
    intro: 'Para estudiar, la decisión importante no es qué IA parece más potente, sino si necesitas trabajar con tus propios apuntes, buscar fuentes nuevas o convertir material largo en algo repasable.',
    tools: ['notebooklm', 'perplexity', 'chatgpt', 'claude'],
    comparisons: [
      { label: 'NotebookLM vs Perplexity', href: '/herramientas/notebooklm-vs-perplexity/', description: 'La comparativa clave si dudas entre fuentes propias y búsqueda web.' },
      { label: 'Mapa de herramientas IA', href: '/recursos/mapa-herramientas-ia/', description: 'El mapa rápido para elegir la primera app según la tarea.' },
    ],
    decisionRules: [
      'Usa NotebookLM si ya tienes apuntes, PDFs, webs o vídeos concretos.',
      'Usa Perplexity si todavía necesitas encontrar fuentes y contexto.',
      'Usa ChatGPT o Claude para convertir el material en esquemas, preguntas o simulacros.',
    ],
    risks: [
      'No estudies solo desde una respuesta sin volver a la fuente.',
      'No subas datos sensibles de clase, empresa o clientes sin revisar privacidad.',
      'No confundas resumen rápido con comprensión real: valida con preguntas propias.',
    ],
  },
  {
    slug: 'para-crear-contenido',
    title: 'Herramientas IA para crear contenido',
    h1: 'Herramientas IA para crear contenido con más criterio',
    description: 'Herramientas IA para crear contenido: ChatGPT, Claude, Canva AI, Gamma y ElevenLabs según guion, diseño, presentación, voz y riesgo.',
    intro: 'Crear contenido con IA funciona mejor cuando separas el trabajo: idea, guion, pieza visual, voz y revisión. Una sola app rara vez es la mejor para todo.',
    tools: ['chatgpt', 'claude', 'canva-ai', 'gamma', 'elevenlabs'],
    comparisons: [
      { label: 'ChatGPT vs Claude', href: '/herramientas/chatgpt-vs-claude/', description: 'Para decidir qué usar al escribir guiones, emails o piezas largas.' },
      { label: 'Gamma vs Canva AI', href: '/herramientas/gamma-vs-canva-ai/', description: 'Para separar estructura de presentación y producción visual.' },
      { label: 'Alternativas a ElevenLabs', href: '/herramientas/alternativas-elevenlabs/', description: 'Para elegir voz IA sin ignorar permisos y uso comercial.' },
    ],
    decisionRules: [
      'Empieza en ChatGPT si la idea todavía está desordenada.',
      'Pasa a Claude si el texto necesita tono, matiz o contexto largo.',
      'Usa Canva AI o Gamma para convertir la idea en material visual.',
      'Usa ElevenLabs solo cuando tengas claro permiso, guion y uso de la voz.',
    ],
    risks: [
      'No publiques datos, voces o imágenes sin derechos claros.',
      'No aceptes claims generados sin fuentes.',
      'No automatices una pieza final sin revisión humana de tono y datos.',
    ],
  },
  {
    slug: 'para-programar',
    title: 'Herramientas IA para programar',
    h1: 'Herramientas IA para programar con control de cambios',
    description: 'Herramientas IA para programar: Qwen Code, ChatGPT, Claude y DeepSeek según terminal, código, coste, privacidad y revisión.',
    intro: 'Para programar con IA, la diferencia no está solo en el modelo. Importa si trabaja dentro del repo, si puedes revisar el diff y si los cambios pasan tests.',
    tools: ['qwen-code', 'chatgpt', 'claude', 'deepseek'],
    comparisons: [
      { label: 'ChatGPT vs Claude', href: '/herramientas/chatgpt-vs-claude/', description: 'Útil para decidir entre ayuda general, explicación y escritura de código.' },
      { label: 'Qwen Code en terminal', href: '/blog/qwen-code-agent-terminal/', description: 'La guía para entender cuándo un agente de terminal tiene sentido.' },
    ],
    decisionRules: [
      'Usa Qwen Code si trabajas con repositorios, terminal y revisión de diff.',
      'Usa ChatGPT para explicar errores, plantear enfoques y desbloquear tareas.',
      'Usa Claude si el cambio depende de leer mucho contexto o documentación.',
      'Usa DeepSeek como segunda opinión o alternativa de coste bajo.',
    ],
    risks: [
      'No aceptes cambios sin revisar diff, dependencias y permisos.',
      'No ejecutes agentes sobre producción sin rama, backup o tests.',
      'No subas código privado a servicios externos sin revisar condiciones.',
    ],
  },
  {
    slug: 'para-presentaciones',
    title: 'Herramientas IA para presentaciones',
    h1: 'Herramientas IA para presentaciones: estructura, diseño y revisión',
    description: 'Herramientas IA para presentaciones: Gamma, Canva AI, ChatGPT y Claude según estructura, diseño, marca, exportación y privacidad.',
    intro: 'Una buena presentación no sale de un prompt largo. Primero necesitas estructura y decisión; después diseño, marca y revisión final.',
    tools: ['gamma', 'canva-ai', 'chatgpt', 'claude'],
    comparisons: [
      { label: 'Gamma vs Canva AI', href: '/herramientas/gamma-vs-canva-ai/', description: 'La decisión central entre generar estructura y producir piezas visuales.' },
      { label: 'IA para presentaciones completas', href: '/blog/ia-crea-presentaciones-completas/', description: 'Guía de contexto para crear presentaciones con IA sin delegar la revisión.' },
    ],
    decisionRules: [
      'Usa ChatGPT o Claude para definir objetivo, público y estructura.',
      'Usa Gamma si necesitas un primer deck visual desde una idea.',
      'Usa Canva AI si necesitas adaptar la pieza a marca, redes o formatos finales.',
    ],
    risks: [
      'No subas información comercial sensible si no puedes compartirla con terceros.',
      'No publiques datos o gráficos generados sin comprobarlos.',
      'No confundas diseño rápido con claridad: revisa la historia slide por slide.',
    ],
  },
  {
    slug: 'para-excel-hojas-calculo',
    title: 'Herramientas IA para Excel y hojas de cálculo',
    h1: 'Herramientas IA para Excel sin perder el control de los datos',
    description: 'Guía práctica para elegir IA en Excel y hojas de cálculo: Copilot, Gemini, Quadratic y ChatGPT según tarea, verificación y privacidad.',
    intro: 'Una fórmula plausible también puede estar mal. La herramienta correcta depende de si necesitas explicar, transformar, analizar o automatizar una hoja y de cómo vas a verificar el resultado.',
    tools: ['microsoft-copilot', 'gemini', 'quadratic', 'chatgpt'],
    comparisons: [{ label: 'Evaluador de resultados', href: '/herramientas/evaluador/', description: 'Puntúa exactitud, edición y repetibilidad antes de conservar el flujo.' }],
    decisionRules: ['Usa Copilot cuando el trabajo ya vive en Excel y el plan lo permite.', 'Usa Gemini si el flujo está en Google Sheets.', 'Usa Quadratic si necesitas cuadrícula, Python o SQL.', 'Usa ChatGPT para explicar fórmulas con una copia no sensible.'],
    risks: ['Trabaja sobre una copia.', 'Contrasta con resultados conocidos.', 'No permitas que una fórmula generada sustituya controles financieros.'],
  },
  {
    slug: 'para-reuniones',
    title: 'Herramientas IA para reuniones',
    h1: 'Herramientas IA para convertir reuniones en decisiones revisables',
    description: 'Herramientas IA para reuniones: Granola, Fathom, NotebookLM y Claude según consentimiento, notas, transcripción y seguimiento.',
    intro: 'El valor no está en resumir más, sino en separar decisiones, acciones, responsables y fechas sin inventar lo que no se dijo.',
    tools: ['granola', 'fathom', 'notebooklm', 'claude'],
    comparisons: [{ label: 'Granola vs Fathom', href: '/herramientas/comparativas/granola-vs-fathom/', description: 'Decide entre notas humanas enriquecidas y captura automatizada.' }, { label: 'Workflow probado de reuniones', href: '/blog/ia-resumir-reuniones-tareas-revisables/', description: 'Proceso de cinco pasos con revisión explícita.' }],
    decisionRules: ['Usa Granola si quieres conservar tus propias notas como base.', 'Usa Fathom si necesitas grabación y resumen de videollamadas con consentimiento.', 'Usa NotebookLM para trabajar después con transcripciones propias.', 'Usa Claude para dar forma al documento final, no para inventar acuerdos.'],
    risks: ['Confirma consentimiento y política.', 'No atribuyas responsables ausentes.', 'No envíes tareas sin revisar la fuente.'],
  },
  {
    slug: 'para-organizar-trabajo',
    title: 'Herramientas IA para organizar el trabajo',
    h1: 'Herramientas IA para organizar correo, calendario y pendientes',
    description: 'Guía para organizar trabajo con Notion AI, Reclaim, Motion y Microsoft Copilot sin delegar prioridades importantes.',
    intro: 'Organizar no consiste en llenar el calendario. Primero hay que distinguir información, compromiso, prioridad y bloque de tiempo.',
    tools: ['notion-ai', 'reclaim', 'motion', 'microsoft-copilot'],
    comparisons: [{ label: 'Reclaim vs Motion', href: '/herramientas/comparativas/reclaim-vs-motion/', description: 'Compara protección flexible de tiempo y planificación automática.' }],
    decisionRules: ['Usa Notion AI para encontrar y resumir conocimiento del workspace.', 'Usa Reclaim para proteger hábitos y bloques flexibles.', 'Usa Motion para ordenar tareas con plazo.', 'Usa Copilot cuando correo y documentos viven en Microsoft 365.'],
    risks: ['Un calendario incompleto produce un plan falso.', 'No automatices compromisos externos sin confirmación.', 'Revisa permisos de correo y documentos.'],
  },
  {
    slug: 'para-crear-apps',
    title: 'Herramientas IA para crear aplicaciones',
    h1: 'Herramientas IA para crear una app sin confundir prototipo con producto',
    description: 'Herramientas IA para crear aplicaciones: Emergent, Cursor, GitHub Copilot y Qwen Code según prototipo, código, pruebas y despliegue.',
    intro: 'La IA puede acelerar una primera versión, pero la diferencia entre demo y producto está en datos, autenticación, errores, seguridad y mantenimiento.',
    tools: ['emergent', 'cursor', 'github-copilot', 'qwen-code'],
    comparisons: [{ label: 'Cursor vs GitHub Copilot', href: '/herramientas/comparativas/cursor-vs-github-copilot/', description: 'Compara editor centrado en IA e integración con GitHub.' }],
    decisionRules: ['Usa Emergent para validar una app pequeña.', 'Usa Cursor para cambios multarchivo en un editor.', 'Usa GitHub Copilot si el repositorio ya vive en GitHub.', 'Usa Qwen Code si trabajas desde terminal y revisas el diff.'],
    risks: ['Usa rama y backup.', 'No expongas secretos.', 'Prueba autenticación, permisos y errores antes de desplegar.'],
  },
  {
    slug: 'para-investigar',
    title: 'Herramientas IA para investigar',
    h1: 'Herramientas IA para investigar sin perder la pista de las fuentes',
    description: 'Guía de investigación con Perplexity, NotebookLM, Gemini y Kimi según búsqueda web, fuentes propias, contexto y verificación.',
    intro: 'Investigar bien separa descubrimiento, selección de fuentes, análisis y redacción. Una sola respuesta no debería cubrir las cuatro fases.',
    tools: ['perplexity', 'notebooklm', 'gemini', 'kimi'],
    comparisons: [{ label: 'NotebookLM vs Perplexity', href: '/herramientas/notebooklm-vs-perplexity/', description: 'Diferencia búsqueda web y análisis de fuentes propias.' }],
    decisionRules: ['Usa Perplexity para descubrir fuentes.', 'Usa NotebookLM cuando ya tienes el corpus.', 'Usa Gemini para material multimodal del ecosistema Google.', 'Usa Kimi como comparación, no como única fuente.'],
    risks: ['Abre siempre la fuente.', 'No uses una URL para validar otro producto.', 'Separa hechos, declaraciones e inferencias.'],
  },
  {
    slug: 'para-agentes-automatizaciones',
    title: 'Herramientas IA para agentes y automatizaciones',
    h1: 'Herramientas IA para automatizar sin entregar las llaves',
    description: 'Guía práctica de agentes con Manus, Zapier, Hermes Agent y Qwen Code según permisos, trazabilidad, reversibilidad y revisión.',
    intro: 'Un agente útil no es el que hace más cosas, sino el que actúa dentro de límites claros, deja evidencia y permite recuperar el estado anterior.',
    tools: ['manus', 'zapier', 'hermes-agent', 'qwen-code'],
    comparisons: [{ label: 'Manus vs ChatGPT Apps', href: '/herramientas/comparativas/manus-vs-chatgpt-apps/', description: 'Compara agente de varias etapas y trabajo dentro de ChatGPT.' }],
    decisionRules: ['Usa Zapier para reglas entre aplicaciones.', 'Usa Manus para una tarea de varias etapas supervisada.', 'Usa Hermes Agent para experimentar con código abierto y aislamiento.', 'Usa Qwen Code para repositorios y terminal.'],
    risks: ['Mínimo privilegio.', 'Nada irreversible sin confirmación.', 'Logs, límites y recuperación obligatorios.'],
  },
  {
    slug: 'para-documentos-pdf',
    title: 'Herramientas IA para documentos y PDF',
    h1: 'Herramientas IA para trabajar con documentos largos y PDF',
    description: 'Guía para elegir Claude, NotebookLM, ChatGPT o Notion AI según documentos largos, citas, redacción y conocimiento interno.',
    intro: 'Antes de elegir herramienta decide si necesitas localizar una cita, comprender un documento, cruzar fuentes o redactar un entregable nuevo.',
    tools: ['claude', 'notebooklm', 'chatgpt', 'notion-ai'],
    comparisons: [{ label: 'ChatGPT vs Claude', href: '/herramientas/chatgpt-vs-claude/', description: 'Compara asistente general y trabajo textual con contexto.' }],
    decisionRules: ['Usa NotebookLM si la respuesta debe volver a una fuente.', 'Usa Claude para transformar textos largos.', 'Usa ChatGPT para formatos y entregables variados.', 'Usa Notion AI si el material ya está en el workspace.'],
    risks: ['Anonimiza información identificable.', 'Comprueba citas.', 'No confundas un resumen con una revisión experta.'],
  },
  {
    slug: 'para-ia-local-abierta',
    title: 'Herramientas IA locales y abiertas',
    h1: 'Herramientas IA locales y abiertas: control antes que comodidad',
    description: 'Guía de herramientas IA locales y abiertas con Ollama, Hermes Agent, Qwen Code y modelos abiertos según privacidad, hardware y dificultad.',
    intro: 'Ejecutar en local puede dar más control, pero también traslada a tu equipo la seguridad, las actualizaciones, el hardware y la calidad de cada modelo.',
    tools: ['ollama', 'hermes-agent', 'qwen-code', 'huggingchat'],
    comparisons: [{ label: 'Preflight de datos', href: '/herramientas/preflight-datos/', description: 'Decide si realmente necesitas un flujo local antes de instalar nada.' }],
    decisionRules: ['Usa Ollama para ejecutar modelos compatibles en tu equipo.', 'Usa Hermes Agent solo en un entorno aislado.', 'Usa Qwen Code para terminal y repositorios.', 'Usa HuggingChat para explorar modelos antes de instalar.'],
    risks: ['Local no significa seguro por defecto.', 'Actualiza dependencias.', 'Mide calidad y hardware con tu tarea real.'],
  },
];

export function getToolUseCase(slug: string): ToolUseCase | undefined {
  return toolUseCases.find((useCase) => useCase.slug === slug);
}
