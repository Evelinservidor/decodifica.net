import { expandedTools } from './tools-expanded';
import autoPublishedToolsData from './tools-auto-published.json';
import reviewLedger from './tool-review-ledger.json';

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
  publishedAt?: string;
  verifiedAt?: string;
  nextReviewAt?: string;
  reviewCadenceDays?: number;
  reviewedFields?: string[];
  freshnessStatus?: 'current' | 'due-soon' | 'review-due';
  status?: 'active' | 'changed' | 'review' | 'archived';
  evidenceLevel?: 'official' | 'controlled-test' | 'decodifica-test';
  platforms?: string[];
  language?: string;
  detail?: ToolDetail;
};

const coreTools: Tool[] = [
  {
    slug: 'chatgpt',
    name: 'ChatGPT',
    summary: 'Asistente general para escribir, idear, resumir, programar y convertir tareas abiertas en borradores accionables.',
    metaDescription: 'Ficha práctica de ChatGPT: cuando usarlo, cuando evitarlo, precio por categoría, privacidad, dificultad y alternativas.',
    useCase: 'Asistente general',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Baja',
    bestFor: 'Cuando necesitas pensar, escribir o desbloquear una tarea sin montar un sistema complejo.',
    avoidIf: 'Vas a subir datos sensibles sin revisar ajustes, permisos o plan de empresa.',
    tags: ['escritura', 'productividad', 'código', 'análisis'],
    officialUrl: 'https://openai.com/chatgpt/pricing/',
    relatedLinks: [
      { label: 'ChatGPT vs Claude', href: '/herramientas/chatgpt-vs-claude/' },
      { label: 'ChatGPT vs Gemini', href: '/herramientas/comparativas/chatgpt-vs-gemini/' },
      { label: 'Herramientas IA para crear contenido', href: '/herramientas/para-crear-contenido/' },
      { label: 'Herramientas IA para programar', href: '/herramientas/para-programar/' },
      { label: 'Cómo elegir una herramienta IA', href: '/blog/como-elegir-herramienta-ia/' },
      { label: 'Alternativas gratis a ChatGPT', href: '/blog/alternativas-gratis-chatgpt-2026/' },
      { label: 'Recursos IA', href: '/recursos/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'ChatGPT es la opción más versátil para empezar: sirve para escribir, razonar, resumir, programar y convertir ideas sueltas en borradores. Su valor esta en la amplitud, no en ser siempre la mejor herramienta especializada.',
      idealFor: [
        'Primer borrador de emails, artículos, guiones, planes o documentos.',
        'Análisis rápido de una decisión cuando aun no sabes que herramienta concreta usar.',
        'Ayuda con código, depuración y explicación de errores.',
        'Reformular información en formatos útiles: tabla, lista, resumen ejecutivo o checklist.',
      ],
      notFor: [
        'Trabajar con datos sensibles sin revisar configuración, plan y política de privacidad.',
        'Aceptar respuestas factuales sin fuentes cuando la decisión tiene riesgo legal, médico o financiero.',
        'Automatizar procesos críticos sin supervisión humana.',
      ],
      workflow: [
        'Define la tarea en una frase y el resultado esperado.',
        'Pide una primera versión corta, no una respuesta definitiva.',
        'Anade contexto, restricciones y ejemplos reales.',
        'Usa una segunda pasada para revisar errores, omisiones y pasos accionables.',
      ],
      privacyNotes: [
        'Trátalo como una herramienta de terceros: no subas información sensible sin revisar el plan y la configuración de datos.',
        'Para equipos, conviene separar cuenta personal, cuenta de trabajo y datos de clientes.',
      ],
      priceNotes: [
        'Tiene plan gratuito y planes de pago por usuario o equipo.',
        'Los límites, modelos y funciones cambian; confirma siempre el plan actual antes de pagar.',
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
    metaDescription: 'Ficha práctica de Claude: cuando usarlo para documentos, escritura, prompts reutilizables y trabajo con contexto.',
    useCase: 'Escritura y documentos',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Baja',
    bestFor: 'Cuando necesitas transformar textos largos, preparar documentos o crear sistemas de prompts más estables.',
    avoidIf: 'Solo quieres respuestas cortas y no vas a aprovechar contexto, archivos o instrucciones.',
    tags: ['documentos', 'escritura', 'prompts', 'contexto'],
    officialUrl: 'https://claude.com/pricing',
    relatedLinks: [
      { label: 'ChatGPT vs Claude', href: '/herramientas/chatgpt-vs-claude/' },
      { label: 'Herramientas IA para crear contenido', href: '/herramientas/para-crear-contenido/' },
      { label: 'Guía de Claude Skills', href: '/blog/claude-skills-1000-gratis/' },
      { label: 'Emails con Claude sin sonar a robot', href: '/blog/claude-emails-sonar-humanos/' },
      { label: 'Alternativas gratis a ChatGPT', href: '/blog/alternativas-gratis-chatgpt-2026/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'Claude destaca cuando el trabajo es textual, largo o con mucho contexto. Es buena elección para documentos, emails, instrucciones reutilizables y decisiones que requieren matiz.',
      idealFor: [
        'Reescribir documentos sin perder tono ni estructura.',
        'Preparar emails, propuestas y textos profesionales con contexto humano.',
        'Crear instrucciones reutilizables para tareas repetidas.',
        'Analizar textos largos y convertirlos en decisiones claras.',
      ],
      notFor: [
        'Tareas donde solo necesitas una respuesta corta y rápida.',
        'Flujos donde la prioridad absoluta sea integración técnica o automatización desde terminal.',
        'Subir información sensible sin revisar plan, privacidad y retención.',
      ],
      workflow: [
        'Empieza dando rol, objetivo, publico y criterio de calidad.',
        'Incluye ejemplos de tono o una versión anterior que quieras mejorar.',
        'Pide primero estructura y luego redacción final.',
        'Guarda las mejores instrucciones como plantilla reutilizable.',
      ],
      privacyNotes: [
        'La sensibilidad de los datos importa más que la comodidad del chat.',
        'Para documentos de clientes, separa material anónimo de material identificable.',
      ],
      priceNotes: [
        'Tiene plan gratuito y planes de pago para uso más intensivo.',
        'La disponibilidad por región, límites y precios pueden variar.',
      ],
      alternatives: ['ChatGPT para uso general', 'NotebookLM para documentos con citas', 'Gemini para ecosistema Google'],
      sources: [
        { label: 'Planes oficiales de Claude', href: 'https://claude.com/pricing' },
        { label: 'Guía de planes de Anthropic', href: 'https://support.anthropic.com/en/articles/11049762-choosing-a-claude-plan' },
      ],
    },
  },
  {
    slug: 'notebooklm',
    name: 'NotebookLM',
    summary: 'Herramienta de Google para trabajar con fuentes propias: PDFs, webs, vídeos, notas y materiales de estudio.',
    metaDescription: 'Ficha práctica de NotebookLM: cuando usarlo con fuentes propias, privacidad, dificultad, límites y alternativas.',
    useCase: 'Investigación',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Baja',
    bestFor: 'Cuando quieres preguntar a tus propias fuentes y mantener la respuesta anclada al material que has subido.',
    avoidIf: 'Necesitas automatizar acciones fuera del cuaderno o trabajar con información muy confidencial sin revisar condiciones.',
    tags: ['fuentes', 'investigación', 'estudio', 'resumen'],
    officialUrl: 'https://notebooklm.google/',
    relatedLinks: [
      { label: 'NotebookLM vs Perplexity', href: '/herramientas/notebooklm-vs-perplexity/' },
      { label: 'Herramientas para investigar con fuentes', href: '/herramientas/casos/para-investigar/' },
      { label: 'Herramientas IA para estudiar', href: '/herramientas/para-estudiar/' },
      { label: 'Guía NotebookLM', href: '/blog/notebooklm-guia-2026/' },
      { label: 'Cómo elegir herramienta IA', href: '/blog/como-elegir-herramienta-ia/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'NotebookLM no es un chat generalista. Es una herramienta para trabajar con tus fuentes: documentos, notas, webs o vídeos. Gana cuando necesitas claridad, citas y menos invención.',
      idealFor: [
        'Preparar reuniones con documentos, briefs y notas previas.',
        'Estudiar materiales largos sin perder la relación con la fuente.',
        'Cruzar varias fuentes antes de escribir un artículo, guion o informe.',
        'Convertir un vídeo o documento en preguntas, resumen y puntos clave.',
      ],
      notFor: [
        'Buscar respuestas abiertas en internet sin aportar fuentes.',
        'Automatizar acciones fuera del entorno de NotebookLM.',
        'Subir material altamente confidencial sin revisar políticas y cuenta usada.',
      ],
      workflow: [
        'Crea un cuaderno por proyecto, no uno gigante para todo.',
        'Sube fuentes relevantes y elimina las que no aportan.',
        'Pregunta primero por estructura, acuerdos y contradicciones.',
        'Usa las citas para volver a la fuente antes de publicar o decidir.',
      ],
      privacyNotes: [
        'La privacidad depende de la cuenta, configuración y tipo de material subido.',
        'Anonimiza documentos cuando el valor esta en el contenido y no en los datos personales.',
      ],
      priceNotes: [
        'La herramienta tiene acceso gratuito y opciones ampliadas según el ecosistema de Google.',
        'Los límites de cuadernos, fuentes y funciones pueden cambiar.',
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
    summary: 'Buscador con IA para explorar temas, encontrar fuentes y arrancar una investigación sin partir de una página en blanco.',
    metaDescription: 'Ficha de Perplexity para investigar con IA, buscar fuentes y comparar información antes de decidir.',
    useCase: 'Investigación',
    price: 'Freemium',
    privacy: 'Baja',
    difficulty: 'Baja',
    bestFor: 'Cuando necesitas contexto rápido, fuentes y una primera comparación antes de decidir que leer a fondo.',
    avoidIf: 'Vas a aceptar la respuesta sin abrir fuentes o necesitas una verificación legal, médica o financiera.',
    tags: ['búsqueda', 'fuentes', 'comparación', 'contexto'],
    officialUrl: 'https://www.perplexity.ai/pro',
    relatedLinks: [
      { label: 'NotebookLM vs Perplexity', href: '/herramientas/notebooklm-vs-perplexity/' },
      { label: 'Herramientas para investigar con fuentes', href: '/herramientas/casos/para-investigar/' },
      { label: 'Herramientas IA para estudiar', href: '/herramientas/para-estudiar/' },
      { label: 'Método de evaluación', href: '/blog/como-elegir-herramienta-ia/' },
      { label: 'Alternativas gratis a ChatGPT', href: '/blog/alternativas-gratis-chatgpt-2026/' },
      { label: 'Guía NotebookLM', href: '/blog/notebooklm-guia-2026/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'Perplexity es útil cuando necesitas orientarte rápido, encontrar fuentes y decidir que merece una lectura más seria. No sustituye la verificación: su valor esta en acelerar la primera fase de investigación.',
      idealFor: [
        'Explorar un tema nuevo y sacar fuentes iniciales.',
        'Comparar puntos de vista antes de escribir un artículo, guion o informe.',
        'Encontrar documentos, páginas oficiales y contexto reciente.',
        'Preparar una lista de lectura antes de tomar una decisión.',
      ],
      notFor: [
        'Aceptar una respuesta sin abrir y revisar las fuentes enlazadas.',
        'Decisiones legales, médicas o financieras sin verificación experta.',
        'Trabajar con información privada cuando solo necesitas buscar en la web publica.',
      ],
      workflow: [
        'Empieza con una pregunta concreta y pide fuentes primarias cuando existan.',
        'Abre las fuentes importantes y descarta las que no validen el claim.',
        'Pide una tabla de diferencias, dudas abiertas y términos a revisar.',
        'Lleva el material final a una herramienta de escritura o a NotebookLM si vas a trabajar con fuentes propias.',
      ],
      privacyNotes: [
        'Funciona como buscador con IA: evita introducir datos privados si la tarea puede resolverse con información publica.',
        'Para investigación sensible, separa búsqueda de contexto publico y análisis de documentos internos.',
      ],
      priceNotes: [
        'Tiene plan gratuito y planes Pro/Max para uso más intensivo.',
        'Los planes de empresa tienen precios por asiento y controles adicionales; revisa la página oficial antes de contratar.',
      ],
      alternatives: ['NotebookLM para fuentes propias', 'ChatGPT para sintetizar y escribir', 'Claude para documentos largos', 'Google para búsqueda manual'],
      sources: [
        { label: 'Planes oficiales de Perplexity', href: 'https://www.perplexity.ai/enterprise/pricing' },
        { label: 'Perplexity Pro', href: 'https://www.perplexity.ai/pro' },
        { label: 'FAQ de precios Enterprise', href: 'https://www.perplexity.ai/help-center/en/articles/10352986-enterprise-pricing-and-billing-frequently-asked-questions.html' },
      ],
    },
  },
  {
    slug: 'gamma',
    name: 'Gamma',
    summary: 'Creador de presentaciones, documentos y páginas visuales a partir de una idea o estructura inicial.',
    metaDescription: 'Ficha práctica de Gamma para crear presentaciones y documentos visuales con IA: cuándo usarla, límites, privacidad, dificultad y alternativas.',
    useCase: 'Presentaciones',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Baja',
    bestFor: 'Cuando necesitas un primer borrador visual rápido para ordenar una presentación o propuesta.',
    avoidIf: 'La pieza final exige identidad visual muy estricta o datos corporativos que no puedes subir a terceros.',
    tags: ['presentaciones', 'diseno', 'propuestas', 'borradores'],
    officialUrl: 'https://gamma.app/pricing',
    relatedLinks: [
      { label: 'Gamma vs Canva AI', href: '/herramientas/gamma-vs-canva-ai/' },
      { label: 'Gamma vs Beautiful.ai', href: '/herramientas/comparativas/gamma-vs-beautiful-ai/' },
      { label: 'Herramientas IA para presentaciones', href: '/herramientas/para-presentaciones/' },
      { label: 'IA para presentaciones', href: '/blog/ia-crea-presentaciones-completas/' },
      { label: 'Cómo elegir herramienta IA', href: '/blog/como-elegir-herramienta-ia/' },
      { label: 'Recursos IA', href: '/recursos/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'Gamma es buena para convertir una idea o esquema en una primera presentación visual. Su mejor uso no es reemplazar el criterio, sino desbloquear estructura, narrativa y borrador rápido.',
      idealFor: [
        'Preparar una presentación inicial para ordenar una propuesta.',
        'Transformar notas en una estructura visual que puedas revisar.',
        'Crear documentos, páginas o decks internos sin empezar desde cero.',
        'Probar varios enfoques de una misma idea antes de disenar a mano.',
      ],
      notFor: [
        'Presentaciones finales con identidad visual muy estricta.',
        'Material corporativo sensible que no puedes subir a una herramienta externa.',
        'Decks donde cada gráfico, dato y estilo debe estar auditado manualmente.',
      ],
      workflow: [
        'Escribe primero el objetivo, publico y decisión que quieres provocar.',
        'Pide un esquema antes de generar el deck completo.',
        'Edita titulares y orden de ideas antes de tocar colores o imágenes.',
        'Exporta y revisa manualmente datos, claims y consistencia visual.',
      ],
      privacyNotes: [
        'No subas información confidencial de clientes o estrategia sin revisar plan, permisos y políticas.',
        'Para propuestas sensibles, usa datos anonimizados en el borrador y completa detalles fuera de la herramienta.',
      ],
      priceNotes: [
        'Tiene plan gratuito y planes de pago para más tarjetas por prompt, menos marca y funciones avanzadas.',
        'Los límites de generación, exportación y modelos pueden cambiar según el plan.',
      ],
      alternatives: ['Canva AI para piezas visuales y marca', 'PowerPoint o Google Slides para control final', 'ChatGPT o Claude para preparar el guion'],
      sources: [
        { label: 'Precios oficiales de Gamma', href: 'https://gamma.app/pricing' },
      ],
    },
  },
  {
    slug: 'canva-ai',
    name: 'Canva AI',
    summary: 'Suite visual con funciones de IA para crear piezas graficas, editar disenos y producir materiales de comunicación.',
    metaDescription: 'Ficha de Canva AI para crear y editar piezas visuales con funciones de inteligencia artificial.',
    useCase: 'Diseno',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Baja',
    bestFor: 'Cuando necesitas publicar una pieza visual decente sin abrir una herramienta profesional de diseno.',
    avoidIf: 'Necesitas control fino de marca, trazabilidad completa o archivos de producción complejos.',
    tags: ['diseno', 'redes', 'presentaciones', 'marca'],
    officialUrl: 'https://www.canva.com/en/pricing/',
    relatedLinks: [
      { label: 'Gamma vs Canva AI', href: '/herramientas/gamma-vs-canva-ai/' },
      { label: 'Herramientas IA para presentaciones', href: '/herramientas/para-presentaciones/' },
      { label: 'Herramientas IA para crear contenido', href: '/herramientas/para-crear-contenido/' },
      { label: 'Recursos IA', href: '/recursos/' },
      { label: 'IA para presentaciones', href: '/blog/ia-crea-presentaciones-completas/' },
      { label: 'Cómo elegir herramienta IA', href: '/blog/como-elegir-herramienta-ia/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'Canva AI encaja cuando necesitas producir piezas visuales publicables con rapidez: posts, presentaciones, banners, miniaturas sencillas o materiales de marca. No sustituye a un sistema de diseno profesional cuando el control fino importa.',
      idealFor: [
        'Crear piezas de redes, presentaciones y materiales simples de comunicación.',
        'Probar variantes visuales antes de encargar o construir una versión final.',
        'Editar disenos existentes con ayuda de IA sin entrar en herramientas complejas.',
        'Trabajar con plantillas, marca y formatos frecuentes de marketing.',
      ],
      notFor: [
        'Producción visual compleja donde necesitas archivos, capas y control profesional completo.',
        'Material con datos o activos de marca que no puedes subir a terceros.',
        'Piezas donde la originalidad visual es más importante que la velocidad.',
      ],
      workflow: [
        'Empieza desde una plantilla cercana al formato final.',
        'Usa IA para generar variantes, no para cerrar la pieza sin revisión.',
        'Aplica colores, tipografía y assets de marca antes de exportar.',
        'Comprueba legibilidad en móvil y derechos de los recursos usados.',
      ],
      privacyNotes: [
        'Revisa que imágenes, logos y materiales de clientes puedan subirse a Canva.',
        'En equipos, usa espacios y permisos separados para no mezclar marcas o clientes.',
      ],
      priceNotes: [
        'Canva mantiene plan gratuito y planes de pago para funciones Pro, Business o Enterprise.',
        'Las funciones de IA usan allowances o límites según plan; confirma el plan actual antes de depender de volumen.',
      ],
      alternatives: ['Gamma para decks generados desde texto', 'Adobe Express para piezas visuales rápidas', 'Figma para diseno colaborativo con más control'],
      sources: [
        { label: 'Precios oficiales de Canva', href: 'https://www.canva.com/en/pricing/' },
        { label: 'Canva Business', href: 'https://www.canva.com/newsroom/news/introducing-canva-business/' },
      ],
    },
  },
  {
    slug: 'elevenlabs',
    name: 'ElevenLabs',
    summary: 'Herramienta de voz IA para generar locuciones, doblaje y audio sintético con control de voces e idiomas.',
    metaDescription: 'Ficha práctica de ElevenLabs para voz IA, doblaje, narración y audio sintético: cuándo usarla, privacidad, dificultad, límites y alternativas.',
    useCase: 'Audio y voz',
    price: 'Freemium',
    privacy: 'Alta',
    difficulty: 'Media',
    bestFor: 'Cuando necesitas probar voces, doblajes o narraciones con calidad suficiente para piezas públicas.',
    avoidIf: 'No tienes claro el permiso de una voz, el uso comercial o la política de datos del proyecto.',
    tags: ['voz', 'audio', 'doblaje', 'vídeo'],
    officialUrl: 'https://elevenlabs.io/pricing',
    relatedLinks: [
      { label: 'Alternativas a ElevenLabs', href: '/herramientas/alternativas-elevenlabs/' },
      { label: 'Herramientas IA para crear contenido', href: '/herramientas/para-crear-contenido/' },
      { label: 'Agentes de voz IA', href: '/blog/crear-agente-voz-ia-sin-programar/' },
      { label: 'Recursos IA', href: '/recursos/' },
      { label: 'Cómo elegir herramienta IA', href: '/blog/como-elegir-herramienta-ia/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'ElevenLabs es una de las opciones fuertes para voz IA, locuciones y doblaje. Es potente, pero exige más cuidado que una herramienta de texto: permisos de voz, uso comercial y contexto legal importan mucho.',
      idealFor: [
        'Probar locuciones para vídeos, demos, cursos o piezas internas.',
        'Crear doblajes y versiones de audio con calidad suficiente para publicar.',
        'Experimentar con voces, idiomas y estilos antes de producir a escala.',
        'Construir prototipos de agentes de voz o productos con audio sintético.',
      ],
      notFor: [
        'Clonar o imitar voces sin permiso claro.',
        'Publicar audio comercial sin revisar licencias, términos y derechos.',
        'Producciones masivas sin calcular créditos, coste por minuto y revisión humana.',
      ],
      workflow: [
        'Define primero el uso: prueba interna, vídeo publico, doblaje o API.',
        'Elige una voz con permisos adecuados y guarda el criterio de selección.',
        'Genera una muestra corta y revisa naturalidad, ritmo y pronunciación.',
        'Antes de escalar, calcula créditos, derechos y proceso de aprobación.',
      ],
      privacyNotes: [
        'La voz es dato sensible: no uses voces reales sin consentimiento y documentación.',
        'Evita subir guiones privados o datos personales si no son necesarios para la locución.',
      ],
      priceNotes: [
        'Tiene plan gratuito y planes de pago basados en créditos incluidos.',
        'El coste real depende del producto usado, modelo, volumen y posibles excedentes.',
      ],
      alternatives: ['OpenAI para voz integrada en flujos propios', 'PlayHT o Resemble AI para comparativas de voz', 'TTS local si priorizas control'],
      sources: [
        { label: 'Precios oficiales de ElevenLabs', href: 'https://elevenlabs.io/pricing' },
        { label: 'Precios API de ElevenLabs', href: 'https://elevenlabs.io/pricing/api' },
      ],
    },
  },
  {
    slug: 'qwen-code',
    name: 'Qwen Code',
    summary: 'Agente de código abierto para trabajar desde terminal con bases de código y tareas técnicas.',
    metaDescription: 'Ficha práctica de Qwen Code: agente open source de terminal, dificultad, privacidad y cuando usarlo.',
    useCase: 'Código',
    price: 'Open source',
    privacy: 'Alta',
    difficulty: 'Alta',
    bestFor: 'Cuando sabes trabajar en terminal y quieres automatizar tareas técnicas dentro de un proyecto real.',
    avoidIf: 'Buscas una app visual sencilla o no puedes revisar lo que un agente cambia en tu código.',
    tags: ['código', 'terminal', 'agentes', 'open source'],
    officialUrl: 'https://qwen.ai/qwencode',
    relatedLinks: [
      { label: 'Qwen Code en terminal', href: '/blog/qwen-code-agent-terminal/' },
      { label: 'Herramientas IA para programar', href: '/herramientas/para-programar/' },
      { label: 'Crear app web con IAs chinas open source', href: '/blog/crear-app-web-ias-chinas-open-source/' },
      { label: 'Alternativas Fable 5', href: '/blog/alternativas-fable-5/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'Qwen Code tiene sentido si ya trabajas con repositorios, terminal y control de cambios. No es la mejor puerta de entrada a la IA, pero si una pieza potente para tareas técnicas supervisadas.',
      idealFor: [
        'Explorar una base de código y pedir cambios acotados.',
        'Automatizar tareas técnicas repetitivas desde terminal.',
        'Probar agentes open source sin depender solo de herramientas cerradas.',
        'Combinar IA con git, tests y revisión humana.',
      ],
      notFor: [
        'Usuarios que buscan una interfaz visual sencilla.',
        'Cambios en producción sin pruebas, diff y control de versión.',
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
        'No confundas open source con privado automáticamente: revisa configuración y llamadas externas.',
      ],
      priceNotes: [
        'La herramienta es open source, pero el coste real depende del modelo o API que uses detrás.',
        'Si lo conectas a servicios de pago, controla consumo y límites.',
      ],
      alternatives: ['Cursor para experiencia integrada', 'Codex para flujos agenticos', 'Claude Code si priorizas ecosistema Anthropic'],
      sources: [
        { label: 'Web oficial de Qwen Code', href: 'https://qwen.ai/qwencode' },
        { label: 'Repositorio oficial Qwen Code', href: 'https://github.com/QwenLM/qwen-code' },
        { label: 'Documentación de Qwen Code', href: 'https://qwenlm.github.io/qwen-code-docs/en/users/overview/' },
      ],
    },
  },
  {
    slug: 'deepseek',
    name: 'DeepSeek',
    summary: 'Asistente y modelos de IA con foco en coste bajo, razonamiento y opciones para uso por app o API.',
    metaDescription: 'Ficha práctica de DeepSeek: cuando usarlo, privacidad, precio por categoría, API y alternativas.',
    useCase: 'Asistente general',
    price: 'Freemium',
    privacy: 'Media',
    difficulty: 'Media',
    bestFor: 'Cuando quieres comparar respuestas, probar modelos alternativos o explorar opciones de bajo coste.',
    avoidIf: 'La prioridad es cumplimiento corporativo estricto o no puedes revisar donde procesas los datos.',
    tags: ['modelos', 'asistente', 'api', 'coste'],
    officialUrl: 'https://www.deepseek.com/en/',
    relatedLinks: [
      { label: 'DeepSeek en español', href: '/blog/deepseek-app-oficial-espanol/' },
      { label: 'Herramientas IA para programar', href: '/herramientas/para-programar/' },
      { label: 'Alternativas gratis a ChatGPT', href: '/blog/alternativas-gratis-chatgpt-2026/' },
      { label: 'Alternativas Fable 5', href: '/blog/alternativas-fable-5/' },
    ],
    hasDetailPage: true,
    detail: {
      verdict: 'DeepSeek es interesante cuando quieres comparar modelos, probar costes bajos o usar una alternativa potente para código y razonamiento. La decisión no es solo calidad: también importa privacidad, proveedor y contexto de uso.',
      idealFor: [
        'Comparar respuestas frente a ChatGPT, Claude o Gemini.',
        'Probar tareas de código, razonamiento y análisis con bajo coste.',
        'Explorar API para prototipos donde el precio importa.',
        'Tener una segunda opinión antes de cerrar una decisión.',
      ],
      notFor: [
        'Datos sensibles o regulados sin revisión legal, técnica y de privacidad.',
        'Equipos que necesitan cumplimiento corporativo muy estricto desde el primer día.',
        'Usuarios que no van a contrastar respuestas con fuentes o pruebas.',
      ],
      workflow: [
        'Úsalo como comparador, no como única fuente de verdad.',
        'Prueba una tarea real y mide calidad, coste y tiempo ahorrado.',
        'Si usas API, empieza con límites bajos y logs claros.',
        'Contrasta los resultados importantes con fuentes primarias o tests.',
      ],
      privacyNotes: [
        'Antes de subir datos internos, revisa términos, ubicación, retención y política aplicable.',
        'Para datos sensibles, considera anonimizar o usar alternativas con controles empresariales claros.',
      ],
      priceNotes: [
        'El chat tiene acceso gratuito y la API publica precios por tokens.',
        'Los precios y modelos pueden cambiar; revisa la página oficial antes de integrar.',
      ],
      alternatives: ['ChatGPT para uso general', 'Claude para texto largo', 'Qwen Code para terminal', 'Modelos locales si priorizas control'],
      sources: [
        { label: 'Web oficial de DeepSeek', href: 'https://www.deepseek.com/en/' },
        { label: 'Precios oficiales de la API DeepSeek', href: 'https://api-docs.deepseek.com/quick_start/pricing' },
      ],
    },
  },
];

const defaultReviewedFields = ['status', 'officialUrl', 'price', 'privacy', 'platforms', 'bestFor', 'avoidIf'];

function addDays(date: string, days: number): string {
  const value = new Date(`${date}T00:00:00Z`);
  value.setUTCDate(value.getUTCDate() + days);
  return value.toISOString().slice(0, 10);
}

function freshnessStatus(nextReviewAt: string): Tool['freshnessStatus'] {
  const today = new Date().toISOString().slice(0, 10);
  if (nextReviewAt <= today) return 'review-due';
  const dueSoon = addDays(today, 7);
  return nextReviewAt <= dueSoon ? 'due-soon' : 'current';
}

const autoPublishedTools = autoPublishedToolsData as Tool[];

export const tools: Tool[] = [...coreTools, ...expandedTools, ...autoPublishedTools].map((tool) => {
  const review = reviewLedger[tool.slug as keyof typeof reviewLedger];
  const verifiedAt = review?.verifiedAt ?? tool.verifiedAt ?? '2026-07-14';
  const reviewCadenceDays = review?.reviewCadenceDays ?? tool.reviewCadenceDays ?? 30;
  const nextReviewAt = addDays(verifiedAt, reviewCadenceDays);
  return {
    status: tool.status ?? 'active',
    evidenceLevel: tool.evidenceLevel ?? 'official',
    platforms: tool.platforms ?? ['Web'],
    language: tool.language ?? 'Español disponible',
    ...tool,
    verifiedAt,
    reviewCadenceDays,
    nextReviewAt,
    reviewedFields: tool.reviewedFields ?? defaultReviewedFields,
    freshnessStatus: freshnessStatus(nextReviewAt),
  };
});

export const detailedTools = tools.filter((tool) => tool.hasDetailPage && tool.detail);

export function getToolBySlug(slug: string): Tool | undefined {
  return tools.find((tool) => tool.slug === slug);
}
