export type ToolLink = {
  label: string;
  href: string;
};

export type ToolSource = {
  label: string;
  href: string;
};

export type ToolDetail = {
  verdict: string;
  idealFor: string[];
  notFor: string[];
  workflow: string[];
  privacyNotes: string[];
  priceNotes: string[];
  alternatives: string[];
  sources: ToolSource[];
};

export type Tool = {
  slug: string;
  name: string;
  summary: string;
  metaDescription: string;
  useCase: string;
  price: string;
  privacy: string;
  difficulty: string;
  bestFor: string;
  avoidIf: string;
  tags: string[];
  officialUrl: string;
  relatedLinks: ToolLink[];
  hasDetailPage: boolean;
  detail?: ToolDetail;
};

export const tools: Tool[] = [
  {
    slug: 'chatgpt',
    name: 'ChatGPT',
    summary: 'Asistente general para escribir, idear, resumir, programar y convertir tareas abiertas en borradores accionables.',
    metaDescription: 'Ficha practica de ChatGPT: cuando usarlo, cuando evitarlo, precio por categoria, privacidad, dificultad y alternativas.',
    useCase: 'Asistente general',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Baja',
    bestFor: 'Cuando necesitas pensar, escribir o desbloquear una tarea sin montar un sistema complejo.',
    avoidIf: 'Vas a subir datos sensibles sin revisar ajustes, permisos o plan de empresa.',
    tags: ['escritura', 'productividad', 'codigo', 'analisis'],
    officialUrl: 'https://openai.com/chatgpt/pricing/',
    relatedLinks: [
      { label: 'Como elegir una herramienta IA', href: '/blog/como-elegir-herramienta-ia/' },
      { label: 'Alternativas gratis a ChatGPT', href: '/blog/alternativas-gratis-chatgpt-2026/' },
      { label: 'Recursos IA', href: '/recursos/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'ChatGPT es la opcion mas versatil para empezar: sirve para escribir, razonar, resumir, programar y convertir ideas sueltas en borradores. Su valor esta en la amplitud, no en ser siempre la mejor herramienta especializada.',
      idealFor: [
        'Primer borrador de emails, articulos, guiones, planes o documentos.',
        'Analisis rapido de una decision cuando aun no sabes que herramienta concreta usar.',
        'Ayuda con codigo, depuracion y explicacion de errores.',
        'Reformular informacion en formatos utiles: tabla, lista, resumen ejecutivo o checklist.',
      ],
      notFor: [
        'Trabajar con datos sensibles sin revisar configuracion, plan y politica de privacidad.',
        'Aceptar respuestas factuales sin fuentes cuando la decision tiene riesgo legal, medico o financiero.',
        'Automatizar procesos criticos sin supervision humana.',
      ],
      workflow: [
        'Define la tarea en una frase y el resultado esperado.',
        'Pide una primera version corta, no una respuesta definitiva.',
        'Anade contexto, restricciones y ejemplos reales.',
        'Usa una segunda pasada para revisar errores, omisiones y pasos accionables.',
      ],
      privacyNotes: [
        'Tratalo como una herramienta de terceros: no subas informacion sensible sin revisar el plan y la configuracion de datos.',
        'Para equipos, conviene separar cuenta personal, cuenta de trabajo y datos de clientes.',
      ],
      priceNotes: [
        'Tiene plan gratuito y planes de pago por usuario o equipo.',
        'Los limites, modelos y funciones cambian; confirma siempre el plan actual antes de pagar.',
      ],
      alternatives: ['Claude para escritura larga', 'NotebookLM para fuentes propias', 'DeepSeek para probar modelos alternativos', 'Qwen Code para terminal'],
      sources: [
        { label: 'Planes oficiales de ChatGPT', href: 'https://openai.com/chatgpt/pricing/' },
        { label: 'Centro de ayuda de OpenAI', href: 'https://help.openai.com/' },
      ],
    },
  },
  {
    slug: 'claude',
    name: 'Claude',
    summary: 'Modelo conversacional fuerte para documentos largos, escritura cuidada, razonamiento y trabajo con instrucciones reutilizables.',
    metaDescription: 'Ficha practica de Claude: cuando usarlo para documentos, escritura, prompts reutilizables y trabajo con contexto.',
    useCase: 'Escritura y documentos',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Baja',
    bestFor: 'Cuando necesitas transformar textos largos, preparar documentos o crear sistemas de prompts mas estables.',
    avoidIf: 'Solo quieres respuestas cortas y no vas a aprovechar contexto, archivos o instrucciones.',
    tags: ['documentos', 'escritura', 'prompts', 'contexto'],
    officialUrl: 'https://claude.com/pricing',
    relatedLinks: [
      { label: 'Claude Skills desde cero', href: '/blog/claude-skills-desde-cero/' },
      { label: 'Emails con Claude sin sonar a robot', href: '/blog/claude-emails-sonar-humanos/' },
      { label: 'Alternativas gratis a ChatGPT', href: '/blog/alternativas-gratis-chatgpt-2026/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'Claude destaca cuando el trabajo es textual, largo o con mucho contexto. Es buena eleccion para documentos, emails, instrucciones reutilizables y decisiones que requieren matiz.',
      idealFor: [
        'Reescribir documentos sin perder tono ni estructura.',
        'Preparar emails, propuestas y textos profesionales con contexto humano.',
        'Crear instrucciones reutilizables para tareas repetidas.',
        'Analizar textos largos y convertirlos en decisiones claras.',
      ],
      notFor: [
        'Tareas donde solo necesitas una respuesta corta y rapida.',
        'Flujos donde la prioridad absoluta sea integracion tecnica o automatizacion desde terminal.',
        'Subir informacion sensible sin revisar plan, privacidad y retencion.',
      ],
      workflow: [
        'Empieza dando rol, objetivo, publico y criterio de calidad.',
        'Incluye ejemplos de tono o una version anterior que quieras mejorar.',
        'Pide primero estructura y luego redaccion final.',
        'Guarda las mejores instrucciones como plantilla reutilizable.',
      ],
      privacyNotes: [
        'La sensibilidad de los datos importa mas que la comodidad del chat.',
        'Para documentos de clientes, separa material anonimo de material identificable.',
      ],
      priceNotes: [
        'Tiene plan gratuito y planes de pago para uso mas intensivo.',
        'La disponibilidad por region, limites y precios pueden variar.',
      ],
      alternatives: ['ChatGPT para uso general', 'NotebookLM para documentos con citas', 'Gemini para ecosistema Google'],
      sources: [
        { label: 'Planes oficiales de Claude', href: 'https://claude.com/pricing' },
        { label: 'Guia de planes de Anthropic', href: 'https://support.anthropic.com/en/articles/11049762-choosing-a-claude-plan' },
      ],
    },
  },
  {
    slug: 'notebooklm',
    name: 'NotebookLM',
    summary: 'Herramienta de Google para trabajar con fuentes propias: PDFs, webs, videos, notas y materiales de estudio.',
    metaDescription: 'Ficha practica de NotebookLM: cuando usarlo con fuentes propias, privacidad, dificultad, limites y alternativas.',
    useCase: 'Investigacion',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Baja',
    bestFor: 'Cuando quieres preguntar a tus propias fuentes y mantener la respuesta anclada al material que has subido.',
    avoidIf: 'Necesitas automatizar acciones fuera del cuaderno o trabajar con informacion muy confidencial sin revisar condiciones.',
    tags: ['fuentes', 'investigacion', 'estudio', 'resumen'],
    officialUrl: 'https://notebooklm.google/',
    relatedLinks: [
      { label: 'Guia NotebookLM', href: '/blog/notebooklm-guia-2026/' },
      { label: 'NotebookLM frente a Google y OpenAI', href: '/blog/notebooklm-google-openai/' },
      { label: 'Como elegir herramienta IA', href: '/blog/como-elegir-herramienta-ia/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'NotebookLM no es un chat generalista. Es una herramienta para trabajar con tus fuentes: documentos, notas, webs o videos. Gana cuando necesitas claridad, citas y menos invencion.',
      idealFor: [
        'Preparar reuniones con documentos, briefs y notas previas.',
        'Estudiar materiales largos sin perder la relacion con la fuente.',
        'Cruzar varias fuentes antes de escribir un articulo, guion o informe.',
        'Convertir un video o documento en preguntas, resumen y puntos clave.',
      ],
      notFor: [
        'Buscar respuestas abiertas en internet sin aportar fuentes.',
        'Automatizar acciones fuera del entorno de NotebookLM.',
        'Subir material altamente confidencial sin revisar politicas y cuenta usada.',
      ],
      workflow: [
        'Crea un cuaderno por proyecto, no uno gigante para todo.',
        'Sube fuentes relevantes y elimina las que no aportan.',
        'Pregunta primero por estructura, acuerdos y contradicciones.',
        'Usa las citas para volver a la fuente antes de publicar o decidir.',
      ],
      privacyNotes: [
        'La privacidad depende de la cuenta, configuracion y tipo de material subido.',
        'Anonimiza documentos cuando el valor esta en el contenido y no en los datos personales.',
      ],
      priceNotes: [
        'La herramienta tiene acceso gratuito y opciones ampliadas segun el ecosistema de Google.',
        'Los limites de cuadernos, fuentes y funciones pueden cambiar.',
      ],
      alternatives: ['Perplexity para investigar en web', 'Claude para redactar con contexto', 'ChatGPT para uso general'],
      sources: [
        { label: 'Web oficial de NotebookLM', href: 'https://notebooklm.google/' },
        { label: 'NotebookLM para estudiantes', href: 'https://notebooklm.google/students' },
      ],
    },
  },
  {
    slug: 'perplexity',
    name: 'Perplexity',
    summary: 'Buscador con IA para explorar temas, encontrar fuentes y arrancar una investigacion sin partir de una pagina en blanco.',
    metaDescription: 'Ficha de Perplexity para investigar con IA, buscar fuentes y comparar informacion antes de decidir.',
    useCase: 'Investigacion',
    price: 'Freemium',
    privacy: 'Baja',
    difficulty: 'Baja',
    bestFor: 'Cuando necesitas contexto rapido, fuentes y una primera comparacion antes de decidir que leer a fondo.',
    avoidIf: 'Vas a aceptar la respuesta sin abrir fuentes o necesitas una verificacion legal, medica o financiera.',
    tags: ['busqueda', 'fuentes', 'comparacion', 'contexto'],
    officialUrl: 'https://www.perplexity.ai/pro',
    relatedLinks: [
      { label: 'Metodo de evaluacion', href: '/blog/como-elegir-herramienta-ia/' },
    ],
    hasDetailPage: false,
  },
  {
    slug: 'gamma',
    name: 'Gamma',
    summary: 'Creador de presentaciones, documentos y paginas visuales a partir de una idea o estructura inicial.',
    metaDescription: 'Ficha de Gamma para crear presentaciones y documentos visuales con IA.',
    useCase: 'Presentaciones',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Baja',
    bestFor: 'Cuando necesitas un primer borrador visual rapido para ordenar una presentacion o propuesta.',
    avoidIf: 'La pieza final exige identidad visual muy estricta o datos corporativos que no puedes subir a terceros.',
    tags: ['presentaciones', 'diseno', 'propuestas', 'borradores'],
    officialUrl: 'https://gamma.app/pricing',
    relatedLinks: [
      { label: 'IA para presentaciones', href: '/blog/ia-crea-presentaciones-completas/' },
    ],
    hasDetailPage: false,
  },
  {
    slug: 'canva-ai',
    name: 'Canva AI',
    summary: 'Suite visual con funciones de IA para crear piezas graficas, editar disenos y producir materiales de comunicacion.',
    metaDescription: 'Ficha de Canva AI para crear y editar piezas visuales con funciones de inteligencia artificial.',
    useCase: 'Diseno',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Baja',
    bestFor: 'Cuando necesitas publicar una pieza visual decente sin abrir una herramienta profesional de diseno.',
    avoidIf: 'Necesitas control fino de marca, trazabilidad completa o archivos de produccion complejos.',
    tags: ['diseno', 'redes', 'presentaciones', 'marca'],
    officialUrl: 'https://www.canva.com/en/pricing/',
    relatedLinks: [
      { label: 'Recursos IA', href: '/recursos/' },
    ],
    hasDetailPage: false,
  },
  {
    slug: 'elevenlabs',
    name: 'ElevenLabs',
    summary: 'Herramienta de voz IA para generar locuciones, doblaje y audio sintetico con control de voces e idiomas.',
    metaDescription: 'Ficha de ElevenLabs para voz IA, doblaje, narracion y audio sintetico.',
    useCase: 'Audio y voz',
    price: 'Freemium',
    privacy: 'Alta',
    difficulty: 'Media',
    bestFor: 'Cuando necesitas probar voces, doblajes o narraciones con calidad suficiente para piezas publicas.',
    avoidIf: 'No tienes claro el permiso de una voz, el uso comercial o la politica de datos del proyecto.',
    tags: ['voz', 'audio', 'doblaje', 'video'],
    officialUrl: 'https://elevenlabs.io/pricing',
    relatedLinks: [
      { label: 'Agentes de voz IA', href: '/blog/crear-agente-voz-ia-sin-programar/' },
    ],
    hasDetailPage: false,
  },
  {
    slug: 'qwen-code',
    name: 'Qwen Code',
    summary: 'Agente de codigo abierto para trabajar desde terminal con bases de codigo y tareas tecnicas.',
    metaDescription: 'Ficha practica de Qwen Code: agente open source de terminal, dificultad, privacidad y cuando usarlo.',
    useCase: 'Codigo',
    price: 'Open source',
    privacy: 'Alta',
    difficulty: 'Alta',
    bestFor: 'Cuando sabes trabajar en terminal y quieres automatizar tareas tecnicas dentro de un proyecto real.',
    avoidIf: 'Buscas una app visual sencilla o no puedes revisar lo que un agente cambia en tu codigo.',
    tags: ['codigo', 'terminal', 'agentes', 'open source'],
    officialUrl: 'https://qwen.ai/qwencode',
    relatedLinks: [
      { label: 'Qwen Code en terminal', href: '/blog/qwen-code-agent-terminal/' },
      { label: 'Crear app web con IAs chinas open source', href: '/blog/crear-app-web-ias-chinas-open-source/' },
      { label: 'Alternativas Fable 5', href: '/blog/alternativas-fable-5/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'Qwen Code tiene sentido si ya trabajas con repositorios, terminal y control de cambios. No es la mejor puerta de entrada a la IA, pero si una pieza potente para tareas tecnicas supervisadas.',
      idealFor: [
        'Explorar una base de codigo y pedir cambios acotados.',
        'Automatizar tareas tecnicas repetitivas desde terminal.',
        'Probar agentes open source sin depender solo de herramientas cerradas.',
        'Combinar IA con git, tests y revision humana.',
      ],
      notFor: [
        'Usuarios que buscan una interfaz visual sencilla.',
        'Cambios en produccion sin pruebas, diff y control de version.',
        'Proyectos donde no puedes revisar lo que el agente modifica.',
      ],
      workflow: [
        'Empieza en una rama limpia o con un diff controlado.',
        'Pide una tarea pequena y verificable.',
        'Ejecuta tests o build antes de aceptar el resultado.',
        'Revisa manualmente cambios de seguridad, datos y dependencias.',
      ],
      privacyNotes: [
        'La privacidad depende del modelo, proveedor y entorno donde lo ejecutes.',
        'No confundas open source con privado automaticamente: revisa configuracion y llamadas externas.',
      ],
      priceNotes: [
        'La herramienta es open source, pero el coste real depende del modelo o API que uses detras.',
        'Si lo conectas a servicios de pago, controla consumo y limites.',
      ],
      alternatives: ['Cursor para experiencia integrada', 'Codex para flujos agenticos', 'Claude Code si priorizas ecosistema Anthropic'],
      sources: [
        { label: 'Web oficial de Qwen Code', href: 'https://qwen.ai/qwencode' },
        { label: 'Repositorio oficial Qwen Code', href: 'https://github.com/QwenLM/qwen-code' },
        { label: 'Documentacion de Qwen Code', href: 'https://qwenlm.github.io/qwen-code-docs/en/users/overview/' },
      ],
    },
  },
  {
    slug: 'deepseek',
    name: 'DeepSeek',
    summary: 'Asistente y modelos de IA con foco en coste bajo, razonamiento y opciones para uso por app o API.',
    metaDescription: 'Ficha practica de DeepSeek: cuando usarlo, privacidad, precio por categoria, API y alternativas.',
    useCase: 'Asistente general',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Media',
    bestFor: 'Cuando quieres comparar respuestas, probar modelos alternativos o explorar opciones de bajo coste.',
    avoidIf: 'La prioridad es cumplimiento corporativo estricto o no puedes revisar donde procesas los datos.',
    tags: ['modelos', 'asistente', 'api', 'coste'],
    officialUrl: 'https://www.deepseek.com/en/',
    relatedLinks: [
      { label: 'DeepSeek en espanol', href: '/blog/deepseek-app-oficial-espanol/' },
      { label: 'Alternativas gratis a ChatGPT', href: '/blog/alternativas-gratis-chatgpt-2026/' },
      { label: 'Alternativas Fable 5', href: '/blog/alternativas-fable-5/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'DeepSeek es interesante cuando quieres comparar modelos, probar costes bajos o usar una alternativa potente para codigo y razonamiento. La decision no es solo calidad: tambien importa privacidad, proveedor y contexto de uso.',
      idealFor: [
        'Comparar respuestas frente a ChatGPT, Claude o Gemini.',
        'Probar tareas de codigo, razonamiento y analisis con bajo coste.',
        'Explorar API para prototipos donde el precio importa.',
        'Tener una segunda opinion antes de cerrar una decision.',
      ],
      notFor: [
        'Datos sensibles o regulados sin revision legal, tecnica y de privacidad.',
        'Equipos que necesitan cumplimiento corporativo muy estricto desde el primer dia.',
        'Usuarios que no van a contrastar respuestas con fuentes o pruebas.',
      ],
      workflow: [
        'Usalo como comparador, no como unica fuente de verdad.',
        'Prueba una tarea real y mide calidad, coste y tiempo ahorrado.',
        'Si usas API, empieza con limites bajos y logs claros.',
        'Contrasta los resultados importantes con fuentes primarias o tests.',
      ],
      privacyNotes: [
        'Antes de subir datos internos, revisa terminos, ubicacion, retencion y politica aplicable.',
        'Para datos sensibles, considera anonimizar o usar alternativas con controles empresariales claros.',
      ],
      priceNotes: [
        'El chat tiene acceso gratuito y la API publica precios por tokens.',
        'Los precios y modelos pueden cambiar; revisa la pagina oficial antes de integrar.',
      ],
      alternatives: ['ChatGPT para uso general', 'Claude para texto largo', 'Qwen Code para terminal', 'Modelos locales si priorizas control'],
      sources: [
        { label: 'Web oficial de DeepSeek', href: 'https://www.deepseek.com/en/' },
        { label: 'Precios oficiales de la API DeepSeek', href: 'https://api-docs.deepseek.com/quick_start/pricing' },
      ],
    },
  },
];

export const detailedTools = tools.filter((tool) => tool.hasDetailPage && tool.detail);

export function getToolBySlug(slug: string): Tool | undefined {
  return tools.find((tool) => tool.slug === slug);
}
