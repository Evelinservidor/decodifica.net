"""
Lead Magnet Decodifica #2 - Claude Skills desde cero
Contenido resumido de /blog/claude-skills-1000-gratis/ (fuentes oficiales consultadas el 06-10-2026).
Regenerar: python lead-magnets/gen_claude_skills_pdf.py
Reutiliza el mismo template visual que 50-prompts-ia.pdf (A4, dark mode, paleta cyan/white/green).
"""
import os
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
)

CYAN = HexColor('#06b6d4')
WHITE = HexColor('#ffffff')
DARK_BG = HexColor('#0a0a0a')
GRAY = HexColor('#9ca3af')
GREEN = HexColor('#10b981')

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'public', 'lead-magnets', 'claude-skills-desde-cero.pdf')

styles = getSampleStyleSheet()

def make_style(name, **kwargs):
    base = styles.get(kwargs.pop('parent', 'Normal'), styles['Normal'])
    return ParagraphStyle(name=name, parent=base, **kwargs)

cover_h = make_style('CoverH', fontSize=44, leading=52, textColor=CYAN, alignment=TA_CENTER, fontName='Helvetica-Bold', spaceAfter=20)
cover_sub = make_style('CoverSub', fontSize=18, leading=24, textColor=WHITE, alignment=TA_CENTER, fontName='Helvetica-Bold', spaceAfter=10)
cover_desc = make_style('CoverDesc', fontSize=12, leading=18, textColor=GRAY, alignment=TA_CENTER, fontName='Helvetica-Oblique')
h1 = make_style('H1', fontSize=24, leading=30, textColor=CYAN, fontName='Helvetica-Bold', spaceBefore=20, spaceAfter=14)
h2 = make_style('H2', fontSize=16, leading=20, textColor=WHITE, fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=8)
h3 = make_style('H3', fontSize=12, leading=16, textColor=CYAN, fontName='Helvetica-Bold', spaceBefore=10, spaceAfter=4)
body = make_style('Body', fontSize=10, leading=14, textColor=WHITE, alignment=TA_JUSTIFY, spaceAfter=6)
intro = make_style('Intro', fontSize=11, leading=15, textColor=GRAY, alignment=TA_LEFT, spaceAfter=8)
code_style = make_style('Code', fontSize=8.5, leading=11, textColor=GREEN, fontName='Courier', leftIndent=12, rightIndent=12, spaceBefore=4, spaceAfter=8)
footer_style = make_style('Footer', fontSize=8, leading=10, textColor=GRAY, alignment=TA_CENTER)

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, A4[1] - 0.4*cm, A4[0], 0.4*cm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString(A4[0]/2, A4[1] - 0.7*cm, 'Decodifica · Claude Skills desde cero · decodifica.net')
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(GRAY)
    canvas.drawCentredString(A4[0]/2, 0.6*cm, f'Página {doc.page} · decodifica.net')
    canvas.setFillColor(CYAN)
    canvas.rect(0, 0, A4[0], 0.3*cm, fill=1, stroke=0)
    canvas.restoreState()

def on_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, 0, A4[0], 0.5*cm, fill=1, stroke=0)
    canvas.rect(0, A4[1] - 0.5*cm, A4[0], 0.5*cm, fill=1, stroke=0)
    canvas.restoreState()



# SECTIONS - (title, intro, [(subtitle, content), ...]). Todo sale de la guía web verificada.
SECTIONS = [
    {
        'title': '1. Qué es una Skill de Claude',
        'intro': 'Anthropic las llama Agent Skills: carpetas con instrucciones, scripts y recursos que Claude descubre y carga solo cuando tu petición encaja con su descripción. Las presentó el 16 de octubre de 2025 y en diciembre de 2025 publicó el formato como estándar abierto en agentskills.io.',
        'items': [
            ('Carga progresiva en tres niveles',
             'Metadatos (siempre cargados): solo name y description, unos 100 tokens por Skill. Instrucciones (al activarse): el cuerpo de SKILL.md, que Anthropic recomienda mantener por debajo de 5.000 tokens. Recursos y código (cuando se necesitan): de los scripts solo entra en el contexto su salida, no el código.'),
            ('Frente a otras funciones de Claude',
             'Las instrucciones personalizadas se aplican a todas las conversaciones; los Proyectos dan conocimiento de fondo dentro de ese espacio; MCP conecta Claude con servicios externos; las Skills aportan procedimientos que se activan solo cuando son relevantes. Una Skill y un conector MCP pueden usarse juntos.'),
        ],
    },
    {
        'title': '2. Dónde funcionan y qué plan necesitas',
        'intro': 'Claude.ai (web y apps), Claude Code y la API admiten Skills, pero no se sincronizan entre sí: hay que instalarlas en cada sitio donde las quieras usar.',
        'items': [
            ('Claude.ai',
             'Incluye las Skills de Anthropic para Word, Excel, PowerPoint y PDF. Las propias se suben en un ZIP y son solo para tu usuario. Requiere activar "Code execution and file creation".'),
            ('Claude Code',
             'Las de documentos no vienen incluidas, pero se pueden instalar desde el repositorio oficial. Las propias van como carpetas en tu equipo o mediante plugins.'),
            ('API',
             'Las de Anthropic se usan con los identificadores pptx, xlsx, docx y pdf; las propias se suben con los endpoints /v1/skills y se comparten con todo el espacio de trabajo.'),
            ('Planes',
             'El centro de ayuda de Anthropic indica Free, Pro, Max, Team y Enterprise, con la ejecución de código activada. La documentación para desarrolladores menciona solo Pro, Max, Team y Enterprise para subir Skills propias en Claude.ai. Si en el plan gratuito no ves la opción de subir, esa es la razón probable.'),
        ],
    },
    {
        'title': '3. Dónde conseguir Skills gratis',
        'intro': 'Empieza por el repositorio oficial. Las colecciones de la comunidad sirven para buscar ideas, no para instalar sin revisar.',
        'items': [
            ('github.com/anthropics/skills',
             'Mantenido por Anthropic. A 6 de octubre de 2026 contiene 19 Skills, entre ellas docx, xlsx, pptx, pdf y skill-creator (ayuda a crear Skills nuevas). La mayoría tienen licencia Apache 2.0; las de documentos son source-available. El propio repositorio avisa de que son ejemplos con fines de demostración y educativos.'),
            ('Colecciones de la comunidad',
             'sickn33/antigravity-awesome-skills (licencia MIT) declara más de 2.658 Skills para varias herramientas; SkillsMP es un buscador que afirma indexar más de 3.000.000. Son cifras que declaran sus responsables, sin relación con Anthropic, e incluyen duplicados y Skills abandonadas.'),
        ],
    },
    {
        'title': '4. Cómo instalar una Skill',
        'intro': 'No hace falta invocarla: Claude la usa cuando la petición encaja con su descripción.',
        'items': [
            ('En Claude.ai',
             'Settings > Capabilities: activa "Code execution and file creation". Después Customize > Skills: activa o desactiva cada una, o pulsa + > Create skill > Upload a skill y sube un ZIP. El ZIP debe contener la carpeta de la Skill, con el mismo nombre que la Skill. En Team y Enterprise, un administrador debe habilitarlo antes.'),
            ('En Claude Code',
             'Personales: ~/.claude/skills/nombre-de-la-skill/SKILL.md. Compartidas en un repositorio: .claude/skills/nombre-de-la-skill/. Las oficiales como plugin: /plugin marketplace add anthropics/skills y después /plugin install document-skills@anthropic-agent-skills. También puedes llamarla escribiendo /nombre-de-la-skill.'),
        ],
    },
    {
        'title': '5. Crea tu primera Skill',
        'intro': 'Merece la pena cuando repites la misma tarea con el mismo formato de salida. Lo único obligatorio es el archivo SKILL.md.',
        'items': [
            ('El encabezado',
             'name: máximo 64 caracteres, solo minúsculas, números y guiones, sin las palabras "anthropic" ni "claude". description: qué hace y cuándo usarla; es lo que Claude compara con tu petición. La API admite 1.024 caracteres, pero Claude.ai fija 200: no pases de 200.'),
            ('Plantilla mínima (email-triage/SKILL.md)',
             """---
name: email-triage
description: Extrae remitente, petición, fecha límite y siguiente
  acción de un email. Úsala cuando el usuario pegue un correo.
---
# Email Triage
Cuando recibas un email, devuelve una tabla con: resumen,
persona, petición, fecha límite (o "sin fecha clara"),
urgencia (baja/media/alta) y siguiente acción.

## Reglas
- No inventes datos que no estén en el email.
- Si es ambiguo, propone una pregunta de aclaración.
- Responde en español claro y directo."""),
            ('Si no se activa o falla',
             'Casi siempre es la description: di qué hace y en qué situación usarla. Si el formato es inestable, añade un ejemplo de entrada y salida. La guía de Claude Code recomienda que SKILL.md no pase de 500 líneas. La Skill skill-creator del repositorio oficial ayuda a redactar una nueva.'),
        ],
    },
    {
        'title': '6. Seguridad: antes de instalar una de terceros',
        'intro': 'La documentación de Anthropic recomienda usar solo Skills de fuentes de confianza: las tuyas o las de Anthropic. Una Skill da a Claude instrucciones y código; una maliciosa puede provocar robo de datos o accesos no autorizados.',
        'items': [
            ('Revisión mínima',
             'Lee todos los archivos, no solo SKILL.md. Busca llamadas de red o accesos a archivos que no tengan que ver con lo que dice hacer. Desconfía de las que descargan contenido de URLs externas. Prueba primero con datos poco sensibles. En Claude Code el código corre en tu propio equipo, con tus archivos y tu red.'),
            ('Cuándo no merece la pena',
             'Preguntas sueltas: un prompt normal. Preferencias de tono o idioma: instrucciones personalizadas. Material fijo de un trabajo: un Proyecto. Conectar otro servicio: un conector MCP.'),
        ],
    },
]

SOURCES = [
    'platform.claude.com/docs/en/agents-and-tools/agent-skills/overview',
    'support.claude.com: "Using Skills in Claude", "Creating custom Skills", "What are Skills?"',
    'code.claude.com/docs/en/skills',
    'github.com/anthropics/skills',
    'anthropic.com/engineering (anuncio de Agent Skills, 16-10-2025)',
    'github.com/sickn33/antigravity-awesome-skills · skillsmp.com',
]

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm, topMargin=1.5*cm, bottomMargin=1.5*cm,
    title='Claude Skills desde cero - Decodifica', author='Jordi Castañeira · Decodifica',
    subject='Guía práctica de Claude Skills',
)
story = [Spacer(1, 6*cm), Paragraph('Claude Skills', cover_h), Paragraph('desde cero', cover_h), Spacer(1, 0.5*cm),
         Paragraph('Qué son, dónde conseguirlas gratis y cómo crear la tuya', cover_sub), Spacer(1, 1*cm),
         Paragraph('Una guía práctica de Decodifica · decodifica.net', cover_desc), Spacer(1, 0.5*cm),
         Paragraph('Por Jordi Castañeira · Datos consultados el 6 de octubre de 2026', cover_desc), PageBreak()]
story.append(Paragraph('Antes de empezar', h1))
story.append(Paragraph('Esta guía resume la versión web, que se mantiene actualizada en decodifica.net/blog/claude-skills-1000-gratis/. Todos los datos salen de la documentación oficial de Anthropic y de los repositorios citados al final. Las funciones de Claude cambian a menudo: si algo no coincide con lo que ves en tu cuenta, manda la documentación oficial.', intro))
for sec in SECTIONS:
    story.append(Paragraph(sec['title'], h1))
    story.append(Paragraph(escape(sec['intro']), intro))
    for sub, content in sec['items']:
        story.append(Paragraph(escape(sub), h2))
        if content.startswith('---'):
            for line in content.split('\n'):
                story.append(Paragraph(escape(line).replace(' ', '&nbsp;') or '&nbsp;', code_style))
        else:
            story.append(Paragraph(escape(content), body))
story.append(Paragraph('Fuentes', h1))
for src in SOURCES:
    story.append(Paragraph('· ' + escape(src), body))
story.append(Spacer(1, 1*cm))
story.append(Paragraph('Recibe guías como esta por email: decodifica.net/newsletter/', intro))
doc.build(story, onFirstPage=on_cover, onLaterPages=on_page)
print('PDF generado:', os.path.abspath(OUTPUT))
