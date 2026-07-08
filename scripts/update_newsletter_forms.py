#!/usr/bin/env python3
"""
Actualiza todos los formularios de newsletter en el repo de decodifica.net
para usar el endpoint embed oficial de Buttondown.

Cambios:
  1. action="https://buttondown.email/decodifica" method="post" target="_blank"
     -> action="https://buttondown.com/api/emails/embed-subscribe/decodifica" method="post"
  2. Inserta <input type="hidden" name="embed" value="1" /> después del label sr-only
     y antes del <input type="email" ...>.

Idempotente: si el archivo ya está actualizado, sale sin tocarlo.
"""
import re
import sys
from pathlib import Path

REPO = Path(r"C:\Users\jordi\Documents\GitHub\decodifica.net")
TARGETS = [
    "src/pages/blog/index.astro",
    "src/pages/blog/ia-organiza-pendientes.astro",
    "src/pages/blog/ia-crea-presentaciones-completas.astro",
    "src/pages/blog/odysseus-pewdiepie-ia-gratis.astro",
    "src/pages/blog/ia-mejora-excel.astro",
    "src/pages/blog/notebooklm-guia-2026.astro",
    "src/pages/blog/crear-agente-voz-ia-sin-programar.astro",
    "src/pages/blog/claude-emails-sonar-humanos.astro",
    "src/pages/blog/claude-skills-desde-cero.astro",
    "src/pages/blog/ia-gratis-silicon-valley.astro",
    "src/pages/blog/alternativas-gratis-chatgpt-2026.astro",
    "src/pages/recursos.astro",
]

OLD_ACTION = 'action="https://buttondown.email/decodifica" method="post" target="_blank"'
NEW_ACTION = 'action="https://buttondown.com/api/emails/embed-subscribe/decodifica" method="post"'

# Patrón para encontrar el label sr-only del email + input email siguiente
# Captura el id para mantenerlo en el hidden
HIDDEN_LABEL = '\n        <input type="hidden" name="embed" value="1" />\n        '
LABEL_RE = re.compile(
    r'(<label for="([^"]+)" class="sr-only">Email</label>\s*\n\s*)<input id="\2" type="email"',
    flags=re.MULTILINE
)


def update_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    original = text

    action_replaced = NEW_ACTION in text and OLD_ACTION not in text
    if OLD_ACTION in text:
        text = text.replace(OLD_ACTION, NEW_ACTION)
        action_replaced = True

    hidden_present = 'name="embed" value="1"' in text
    if not hidden_present:
        text, n_hidden = LABEL_RE.subn(
            lambda m: m.group(1) + HIDDEN_LABEL + f'<input id="{m.group(2)}" type="email"',
            text,
        )
        if n_hidden == 0:
            return f"[warn] {path.name}: no se encontró el patrón label/input. Revisar manualmente."

    if text == original:
        return f"[skip] {path.name}: ya estaba actualizado."

    path.write_text(text, encoding="utf-8")
    return f"[ok]   {path.name}: action actualizado, {n_hidden if not hidden_present else 0} hidden input(s) añadidos."


def main():
    for rel in TARGETS:
        path = REPO / rel
        if not path.exists():
            print(f"[err] {rel} no existe", file=sys.stderr)
            continue
        print(update_file(path))


if __name__ == "__main__":
    main()