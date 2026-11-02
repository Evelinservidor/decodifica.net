/**
 * Datos de la herramienta «¿Qué IA local puede mover tu ordenador?» (/herramientas/ia-local-mi-ordenador/).
 *
 * Cada cifra sale de una fuente oficial abierta en la fecha de `consultado`. El repaso mensual (día 20) las vuelve a
 * comprobar y cambia la fecha (docs/AGENTE-SEMANAL.md). Si cambia un tamaño, se cambia aquí y la herramienta lo usa sola.
 *
 * `gb` es la cifra que da la biblioteca de Ollama en su columna «Size / Usage» (un rango cuando hay varias versiones del
 * mismo tamaño). Ollama no dice si es lo que ocupa en disco o la memoria que usa: la herramienta la toma como memoria
 * orientativa y usa siempre la cifra más alta del rango, para no prometer de más.
 */

export const consultado = '2026-11-02';

export interface ModeloLocal {
  familia: 'Gemma 4' | 'Qwen 3.5';
  autor: string;
  tamano: string; // como en la biblioteca de Ollama
  orden: string; // la orden de Ollama para descargarlo
  gb: [number, number]; // mínimo y máximo del rango de la biblioteca de Ollama
}

export const modelos: ModeloLocal[] = [
  { familia: 'Qwen 3.5', autor: 'Alibaba', tamano: '0.8b', orden: 'ollama run qwen3.5:0.8b', gb: [1.2, 1.3] },
  { familia: 'Qwen 3.5', autor: 'Alibaba', tamano: '2b', orden: 'ollama run qwen3.5:2b', gb: [2.7, 3.1] },
  { familia: 'Qwen 3.5', autor: 'Alibaba', tamano: '4b', orden: 'ollama run qwen3.5:4b', gb: [3.3, 4.0] },
  { familia: 'Gemma 4', autor: 'Google', tamano: 'e2b', orden: 'ollama run gemma4:e2b', gb: [4.6, 7.5] },
  { familia: 'Gemma 4', autor: 'Google', tamano: 'e4b', orden: 'ollama run gemma4:e4b', gb: [6.6, 9.5] },
  { familia: 'Qwen 3.5', autor: 'Alibaba', tamano: '9b', orden: 'ollama run qwen3.5:9b', gb: [6.6, 7.6] },
  { familia: 'Gemma 4', autor: 'Google', tamano: '12b', orden: 'ollama run gemma4:12b', gb: [7.7, 8.0] },
  { familia: 'Gemma 4', autor: 'Google', tamano: '26b', orden: 'ollama run gemma4:26b', gb: [16, 19] },
  { familia: 'Qwen 3.5', autor: 'Alibaba', tamano: '27b', orden: 'ollama run qwen3.5:27b', gb: [17, 20] },
  { familia: 'Gemma 4', autor: 'Google', tamano: '31b', orden: 'ollama run gemma4:31b', gb: [19, 20] },
  { familia: 'Qwen 3.5', autor: 'Alibaba', tamano: '35b', orden: 'ollama run qwen3.5:35b', gb: [22, 22] },
  { familia: 'Qwen 3.5', autor: 'Alibaba', tamano: '122b', orden: 'ollama run qwen3.5:122b', gb: [81, 81] },
];

/**
 * Margen que se deja libre para el sistema y los demás programas. NO es una cifra oficial: es la regla prudente de
 * Decodifica, y la página lo dice así. Ninguna fuente oficial da un margen exacto.
 */
export const margenSistemaGb = 4;

export const fuentes = [
  { nombre: 'Biblioteca de Ollama: gemma4 (tamaños y cifra en GB)', url: 'https://ollama.com/library/gemma4/tags' },
  { nombre: 'Biblioteca de Ollama: qwen3.5 (tamaños y cifra en GB)', url: 'https://ollama.com/library/qwen3.5/tags' },
  { nombre: 'LM Studio: System Requirements (memoria, procesador y gráfica recomendados)', url: 'https://lmstudio.ai/docs/app/system-requirements' },
  { nombre: 'Ollama Docs: FAQ (cómo saber si el modelo cabe en la gráfica o pasa al procesador)', url: 'https://docs.ollama.com/faq' },
  { nombre: 'Ollama: Download (los modelos grandes van lentos sin una gráfica potente)', url: 'https://ollama.com/download' },
  { nombre: 'Ollama Docs: Context length (contexto según la memoria de la gráfica)', url: 'https://docs.ollama.com/context-length' },
];
