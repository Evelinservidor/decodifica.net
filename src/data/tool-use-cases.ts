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
    description: 'Guia evergreen de herramientas IA para estudiar: NotebookLM, Perplexity, ChatGPT y Claude segun fuentes, resumenes, apuntes y privacidad.',
    intro: 'Para estudiar, la decision importante no es que IA parece mas potente, sino si necesitas trabajar con tus propios apuntes, buscar fuentes nuevas o convertir material largo en algo repasable.',
    tools: ['notebooklm', 'perplexity', 'chatgpt', 'claude'],
    comparisons: [
      { label: 'NotebookLM vs Perplexity', href: '/herramientas/notebooklm-vs-perplexity/', description: 'La comparativa clave si dudas entre fuentes propias y busqueda web.' },
      { label: 'Mapa de herramientas IA', href: '/recursos/mapa-herramientas-ia/', description: 'El mapa rapido para elegir la primera app segun la tarea.' },
    ],
    decisionRules: [
      'Usa NotebookLM si ya tienes apuntes, PDFs, webs o videos concretos.',
      'Usa Perplexity si todavia necesitas encontrar fuentes y contexto.',
      'Usa ChatGPT o Claude para convertir el material en esquemas, preguntas o simulacros.',
    ],
    risks: [
      'No estudies solo desde una respuesta sin volver a la fuente.',
      'No subas datos sensibles de clase, empresa o clientes sin revisar privacidad.',
      'No confundas resumen rapido con comprension real: valida con preguntas propias.',
    ],
  },
  {
    slug: 'para-crear-contenido',
    title: 'Herramientas IA para crear contenido',
    h1: 'Herramientas IA para crear contenido con mas criterio',
    description: 'Herramientas IA para crear contenido: ChatGPT, Claude, Canva AI, Gamma y ElevenLabs segun guion, diseno, presentacion, voz y riesgo.',
    intro: 'Crear contenido con IA funciona mejor cuando separas el trabajo: idea, guion, pieza visual, voz y revision. Una sola app rara vez es la mejor para todo.',
    tools: ['chatgpt', 'claude', 'canva-ai', 'gamma', 'elevenlabs'],
    comparisons: [
      { label: 'ChatGPT vs Claude', href: '/herramientas/chatgpt-vs-claude/', description: 'Para decidir que usar al escribir guiones, emails o piezas largas.' },
      { label: 'Gamma vs Canva AI', href: '/herramientas/gamma-vs-canva-ai/', description: 'Para separar estructura de presentacion y produccion visual.' },
      { label: 'Alternativas a ElevenLabs', href: '/herramientas/alternativas-elevenlabs/', description: 'Para elegir voz IA sin ignorar permisos y uso comercial.' },
    ],
    decisionRules: [
      'Empieza en ChatGPT si la idea todavia esta desordenada.',
      'Pasa a Claude si el texto necesita tono, matiz o contexto largo.',
      'Usa Canva AI o Gamma para convertir la idea en material visual.',
      'Usa ElevenLabs solo cuando tengas claro permiso, guion y uso de la voz.',
    ],
    risks: [
      'No publiques datos, voces o imagenes sin derechos claros.',
      'No aceptes claims generados sin fuentes.',
      'No automatices una pieza final sin revision humana de tono y datos.',
    ],
  },
  {
    slug: 'para-programar',
    title: 'Herramientas IA para programar',
    h1: 'Herramientas IA para programar con control de cambios',
    description: 'Herramientas IA para programar: Qwen Code, ChatGPT, Claude y DeepSeek segun terminal, codigo, coste, privacidad y revision.',
    intro: 'Para programar con IA, la diferencia no esta solo en el modelo. Importa si trabaja dentro del repo, si puedes revisar el diff y si los cambios pasan tests.',
    tools: ['qwen-code', 'chatgpt', 'claude', 'deepseek'],
    comparisons: [
      { label: 'ChatGPT vs Claude', href: '/herramientas/chatgpt-vs-claude/', description: 'Util para decidir entre ayuda general, explicacion y escritura de codigo.' },
      { label: 'Qwen Code en terminal', href: '/blog/qwen-code-agent-terminal/', description: 'La guia para entender cuando un agente de terminal tiene sentido.' },
    ],
    decisionRules: [
      'Usa Qwen Code si trabajas con repositorios, terminal y revision de diff.',
      'Usa ChatGPT para explicar errores, plantear enfoques y desbloquear tareas.',
      'Usa Claude si el cambio depende de leer mucho contexto o documentacion.',
      'Usa DeepSeek como segunda opinion o alternativa de coste bajo.',
    ],
    risks: [
      'No aceptes cambios sin revisar diff, dependencias y permisos.',
      'No ejecutes agentes sobre produccion sin rama, backup o tests.',
      'No subas codigo privado a servicios externos sin revisar condiciones.',
    ],
  },
  {
    slug: 'para-presentaciones',
    title: 'Herramientas IA para presentaciones',
    h1: 'Herramientas IA para presentaciones: estructura, diseno y revision',
    description: 'Herramientas IA para presentaciones: Gamma, Canva AI, ChatGPT y Claude segun estructura, diseno, marca, exportacion y privacidad.',
    intro: 'Una buena presentacion no sale de un prompt largo. Primero necesitas estructura y decision; despues diseno, marca y revision final.',
    tools: ['gamma', 'canva-ai', 'chatgpt', 'claude'],
    comparisons: [
      { label: 'Gamma vs Canva AI', href: '/herramientas/gamma-vs-canva-ai/', description: 'La decision central entre generar estructura y producir piezas visuales.' },
      { label: 'IA para presentaciones completas', href: '/blog/ia-crea-presentaciones-completas/', description: 'Guia de contexto para crear presentaciones con IA sin delegar la revision.' },
    ],
    decisionRules: [
      'Usa ChatGPT o Claude para definir objetivo, publico y estructura.',
      'Usa Gamma si necesitas un primer deck visual desde una idea.',
      'Usa Canva AI si necesitas adaptar la pieza a marca, redes o formatos finales.',
    ],
    risks: [
      'No subas informacion comercial sensible si no puedes compartirla con terceros.',
      'No publiques datos o graficos generados sin comprobarlos.',
      'No confundas diseno rapido con claridad: revisa la historia slide por slide.',
    ],
  },
];

export function getToolUseCase(slug: string): ToolUseCase | undefined {
  return toolUseCases.find((useCase) => useCase.slug === slug);
}
