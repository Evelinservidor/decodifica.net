import type { ToolFaq, ToolLink, ToolSource } from './tools';

export type ToolComparison = {
  slug: string;
  title: string;
  seoTitle?: string;
  description: string;
  modifiedDate?: string; // AAAA-MM-DD: solo cuando se han vuelto a comprobar los datos
  faq?: ToolFaq[];
  relatedLinks?: ToolLink[];
  sources?: ToolSource[];
  left: string;
  right: string;
  verdict: string;
  chooseLeft: string[];
  chooseRight: string[];
  sharedRisks: string[];
};

export const toolComparisons: ToolComparison[] = [
  { slug: 'chatgpt-vs-gemini', title: 'ChatGPT vs Gemini', description: 'Compara ChatGPT y Gemini por tipo de tarea, ecosistema, trabajo con archivos, privacidad y revisión antes de elegir un asistente de IA.', left: 'chatgpt', right: 'gemini', verdict: 'ChatGPT es una entrada versátil para entregables variados; Gemini gana sentido cuando el trabajo ya vive en Google o depende de material multimodal.', chooseLeft: ['Necesitas formatos y tareas muy variados.', 'Quieres separar el trabajo del ecosistema Google.', 'Ya tienes workflows documentados en ChatGPT.'], chooseRight: ['Trabajas con Google Workspace.', 'Necesitas combinar texto, imágenes y archivos.', 'Quieres contrastar una respuesta con búsqueda y fuentes.'], sharedRisks: ['No subas datos sensibles sin revisar el plan.', 'Comprueba fuentes y datos.', 'Mide la edición necesaria con la misma tarea.'] },
  { slug: 'cursor-vs-github-copilot', title: 'Cursor vs GitHub Copilot', description: 'Compara Cursor y GitHub Copilot para programar con IA dentro del editor, trabajar con repositorios y elegir según integración, control y adopción.', left: 'cursor', right: 'github-copilot', verdict: 'Cursor centra el editor completo en flujos de IA; GitHub Copilot encaja mejor cuando la integración con GitHub y editores existentes pesa más.', chooseLeft: ['Quieres un editor diseñado alrededor de agentes.', 'Necesitas cambios multarchivo frecuentes.', 'Puedes adoptar un editor nuevo.'], chooseRight: ['Tu equipo ya usa GitHub.', 'Quieres conservar el editor actual.', 'Necesitas una adopción más gradual.'], sharedRisks: ['Rama, diff y tests obligatorios.', 'No expongas secretos.', 'Revisa dependencias y licencias.'] },
  {
    slug: 'manus-vs-chatgpt-apps',
    title: 'Manus vs ChatGPT',
    seoTitle: 'Manus vs ChatGPT: cuál es mejor y cuánto cuesta Manus',
    description: 'Manus o ChatGPT para tareas de varios pasos: en qué se diferencian, cuándo conviene cada uno, cuánto cuesta Manus (tiene plan gratis) y qué revisar antes de delegar.',
    modifiedDate: '2026-10-22',
    left: 'manus',
    right: 'chatgpt',
    verdict: 'Manus está pensado para encargarle una tarea de varias etapas y recibir el resultado terminado (un informe, una web, unas diapositivas), trabajando por su cuenta en un entorno en la nube. ChatGPT encaja mejor cuando quieres ir paso a paso en una conversación, con tus archivos y apps dentro de un asistente general; para pedirle un entregable completo tiene el modo Work. Manus tiene plan gratis con 300 créditos al día y sus planes de pago empiezan en 20 $ al mes (consultado el 22-10-2026).',
    chooseLeft: ['La tarea tiene etapas y un entregable claro (informe, web, presentación).', 'Puedes revisar el plan y las acciones antes de dar el resultado por bueno.', 'Necesitas que investigue muchas fuentes a la vez o que siga trabajando sin ti.'],
    chooseRight: ['Ya pagas y trabajas en ChatGPT.', 'Prefieres ir paso a paso y corregir sobre la marcha.', 'Quieres más control de la conversación.'],
    sharedRisks: ['Concede el mínimo acceso.', 'Nada irreversible sin confirmación.', 'Revisa fuentes y acciones.'],
    relatedLinks: [
      { label: 'ChatGPT Work: cuándo usarlo en lugar del chat normal', href: '/blog/chatgpt-work-archivos-a-entregables/' },
      { label: 'Ficha de Manus', href: '/herramientas/manus/' },
      { label: 'Alternativas gratis a ChatGPT', href: '/blog/alternativas-gratis-chatgpt-2026/' },
      { label: 'ChatGPT vs Claude', href: '/herramientas/chatgpt-vs-claude/' },
    ],
    sources: [
      { label: 'Planes de Manus', href: 'https://manus.im/pricing' },
      { label: 'Manus: precios de cada plan (centro de ayuda)', href: 'https://help.manus.im/en/articles/11711111-what-is-the-current-membership-pricing-for-manus' },
      { label: 'Manus: créditos gratis al registrarse y cada día (centro de ayuda)', href: 'https://help.manus.im/en/articles/11813668-are-there-any-discounts-or-special-offers' },
      { label: 'Manus vs ChatGPT, según Manus', href: 'https://manus.im/compare/vs-chatgpt' },
      { label: 'Manus Joins Meta for Next Era of Innovation (blog de Manus)', href: 'https://manus.im/blog/manus-joins-meta-for-next-era-of-innovation' },
      { label: 'ChatGPT Work (OpenAI)', href: 'https://openai.com/chatgpt-work/' },
    ],
    faq: [
      {
        q: '¿Manus es gratis?',
        a: 'Tiene un plan gratis: incluye el modo chat y Manus 2.0 Lite en modo agente, 300 créditos que se recargan cada día, una tarea a la vez y 2 tareas programadas; al registrarte te dan además 1.000 créditos. Los planes de pago cuestan 20 $ al mes (4.000 créditos), 40 $ (8.000) y 200 $ (40.000), con un 17 % menos si pagas el año. Consultado el 22-10-2026 en su web y su centro de ayuda.',
      },
      {
        q: '¿Qué es mejor, Manus o ChatGPT?',
        a: 'Depende de la tarea. Según la propia Manus, trabaja como agente en su propio entorno en la nube (con archivos y terminal) y está pensado para entregar el trabajo terminado. ChatGPT es un asistente general en el que tú guías cada paso; para entregables completos a partir de tus archivos tiene <a href="/blog/chatgpt-work-archivos-a-entregables/">ChatGPT Work</a>. La forma justa de decidir es darles a los dos la misma tarea pequeña y comparar cuánto tienes que corregir.',
      },
      {
        q: '¿Manus es de Meta?',
        a: 'Sí. Manus anunció el 29 de diciembre de 2025 que se une a Meta. En ese mismo anuncio dijo que seguiría vendiendo y gestionando sus suscripciones desde su web y su app.',
      },
      {
        q: '¿Manus está en español?',
        a: 'Su web y su página de planes tienen versión en español (de España y de Latinoamérica). Lo que no detalla es en qué idiomas trabaja mejor el agente: si lo vas a usar en español, pruébalo primero con una tarea pequeña en el plan gratis.',
      },
    ],
  },
  { slug: 'kimi-vs-glm', title: 'Kimi vs GLM', seoTitle: 'Kimi vs GLM: documentos, código y agentes', description: 'Compara Kimi y GLM por documentos, contexto largo, razonamiento, código, agentes, privacidad y disponibilidad antes de elegir cuál probar.', left: 'kimi', right: 'glm', verdict: 'Kimi suele tener sentido en documentos y contexto largo; GLM merece la prueba cuando el foco está en razonamiento, código o agentes. La disponibilidad cambia y debe verificarse.', chooseLeft: ['Trabajas con material largo.', 'Quieres una segunda lectura documental.', 'La tarea es fácil de contrastar.'], chooseRight: ['La tarea incluye código o razonamiento.', 'Quieres comparar familias de modelos chinos.', 'Puedes registrar versión y fecha.'], sharedRisks: ['No introduzcas datos sensibles.', 'Registra modelo y región.', 'Usa el mismo input y criterio.'] },
  { slug: 'microsoft-copilot-vs-gemini-workspace', title: 'Microsoft Copilot vs Gemini Workspace', description: 'Compara Microsoft Copilot y Gemini para Workspace según dónde viven tus documentos, correo, calendario, permisos y suite de oficina habitual.', left: 'microsoft-copilot', right: 'gemini', verdict: 'La decisión principal no es el modelo: es dónde viven los documentos y qué permisos tiene cada cuenta. Copilot encaja en Microsoft 365; Gemini, en Google Workspace.', chooseLeft: ['Usas Outlook, Teams, Word y Excel.', 'Tus permisos ya se gobiernan en Microsoft.', 'Necesitas ayuda dentro de Office.'], chooseRight: ['Usas Gmail, Drive, Docs y Sheets.', 'Trabajas con archivos multimodales de Google.', 'Quieres mantener el flujo en Workspace.'], sharedRisks: ['Audita permisos heredados.', 'Contrasta documentos originales.', 'No automatices compromisos externos.'] },
  { slug: 'gamma-vs-beautiful-ai', title: 'Gamma vs Beautiful.ai', description: 'Compara Gamma y Beautiful.ai para crear presentaciones: primer borrador, diseño automático, consistencia visual, edición y trabajo en equipo.', left: 'gamma', right: 'beautiful-ai', verdict: 'Gamma ayuda a pasar de idea a primer deck; Beautiful.ai encaja mejor cuando el contenido ya existe y el problema es mantener el diseño.', chooseLeft: ['Empiezas desde una idea o esquema.', 'Necesitas una primera versión rápida.', 'Quieres probar narrativa y formato.'], chooseRight: ['Ya tienes el contenido.', 'La consistencia visual es prioritaria.', 'Trabajas con presentaciones de equipo.'], sharedRisks: ['Revisa cada dato.', 'Comprueba exportación.', 'No subas estrategia sensible sin política.'] },
  { slug: 'reclaim-vs-motion', title: 'Reclaim vs Motion', description: 'Compara Reclaim y Motion para proteger tiempo, planificar tareas automáticamente y elegir según calendario, hábitos, prioridades y carga diaria.', left: 'reclaim', right: 'motion', verdict: 'Reclaim protege hábitos y bloques alrededor de tu calendario; Motion intenta construir el plan completo a partir de tareas y plazos.', chooseLeft: ['Quieres proteger concentración y hábitos.', 'Prefieres reglas flexibles.', 'Tu calendario ya está bastante ordenado.'], chooseRight: ['Tienes muchas tareas con fecha.', 'Quieres una propuesta diaria completa.', 'Puedes mantener prioridades actualizadas.'], sharedRisks: ['Un calendario incompleto engaña.', 'Revisa compromisos externos.', 'Prueba una semana antes de migrar.'] },
  { slug: 'granola-vs-fathom', title: 'Granola vs Fathom', description: 'Compara Granola y Fathom para reuniones: notas humanas enriquecidas, grabación, transcripción, resúmenes, consentimiento y seguimiento.', left: 'granola', right: 'fathom', verdict: 'Granola conserva tus notas como parte central; Fathom prioriza grabar, transcribir y compartir una videollamada. Consentimiento y política deciden antes que las funciones.', chooseLeft: ['Quieres tomar notas propias.', 'Prefieres enriquecer un registro humano.', 'No necesitas automatizar todo el seguimiento.'], chooseRight: ['Necesitas grabación de videollamadas.', 'Quieres compartir resúmenes y momentos.', 'El equipo acepta el flujo de consentimiento.'], sharedRisks: ['Confirma consentimiento.', 'Revisa responsables y fechas.', 'No envíes tareas automáticamente.'] },
];

export function getToolComparison(slug: string): ToolComparison | undefined {
  return toolComparisons.find((comparison) => comparison.slug === slug);
}
