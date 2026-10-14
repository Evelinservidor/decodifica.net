// Temas para navegar por las guías. Cada artículo declara `const tema = "<clave>";`.
// El color es uno de los fondos de las portadas (scripts/imagenes/comun.py).
export const temas = {
  chatbots: { nombre: 'Chatbots y asistentes', color: 'indigo' },
  local: { nombre: 'IA en tu ordenador', color: 'verde' },
  automatizar: { nombre: 'Agentes y automatización', color: 'rosa' },
  oficina: { nombre: 'Trabajo y día a día', color: 'azul' },
  crear: { nombre: 'Imagen, vídeo y webs', color: 'naranja' },
} as const;

export type Tema = keyof typeof temas;

export function esTema(valor: string | null | undefined): valor is Tema {
  return Boolean(valor && valor in temas);
}

export function nombreTema(valor: string | null | undefined): string {
  return esTema(valor) ? temas[valor].nombre : 'Guías';
}
