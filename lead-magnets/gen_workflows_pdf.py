"""Lead Magnet Decodifica #3 - 5 workflows con IA en tu día a día
Reutiliza el template visual de 50-prompts-ia.pdf. Carga los prompts desde archivo .md.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
)
import os

CYAN = HexColor('#06b6d4')
WHITE = HexColor('#ffffff')
DARK_BG = HexColor('#0a0a0a')
GRAY = HexColor('#9ca3af')
GREEN = HexColor('#10b981')

OUTPUT = r'C:\Users\jordi\Documents\GitHub\decodifica.net\lead-magnets\workflows-ia-dia-a-dia.pdf'
PROMPTS_DIR = r'C:\Users\jordi\Documents\GitHub\decodifica.net\lead-magnets\prompts'
VERSION = '1.1'
UPDATED = '10 de julio de 2026'
UPDATED_SHORT = '10/07/2026'
CANONICAL_URL = 'https://decodifica.net/lead-magnets/workflows-ia-dia-a-dia.pdf'

styles = getSampleStyleSheet()

def make_style(name, **kwargs):
    base = styles.get(kwargs.pop('parent', 'Normal'), styles['Normal'])
    return ParagraphStyle(name=name, parent=base, **kwargs)

cover_h = make_style('CoverH', fontSize=42, leading=50, textColor=CYAN, alignment=TA_CENTER, fontName='Helvetica-Bold', spaceAfter=20)
cover_sub = make_style('CoverSub', fontSize=18, leading=24, textColor=WHITE, alignment=TA_CENTER, fontName='Helvetica-Bold', spaceAfter=10)
cover_desc = make_style('CoverDesc', fontSize=12, leading=18, textColor=GRAY, alignment=TA_CENTER, fontName='Helvetica-Oblique')
h1 = make_style('H1', fontSize=24, leading=30, textColor=CYAN, fontName='Helvetica-Bold', spaceBefore=20, spaceAfter=14)
h2 = make_style('H2', fontSize=16, leading=20, textColor=WHITE, fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=8)
h3 = make_style('H3', fontSize=12, leading=16, textColor=CYAN, fontName='Helvetica-Bold', spaceBefore=10, spaceAfter=4)
body = make_style('Body', fontSize=10, leading=14, textColor=WHITE, alignment=TA_JUSTIFY, spaceAfter=6)
intro = make_style('Intro', fontSize=11, leading=15, textColor=GRAY, alignment=TA_LEFT, spaceAfter=8)
prompt_style = make_style('Prompt', fontSize=8.5, leading=11, textColor=GREEN, fontName='Courier', leftIndent=12, rightIndent=12, spaceBefore=4, spaceAfter=8)

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, A4[1] - 0.4*cm, A4[0], 0.4*cm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString(A4[0]/2, A4[1] - 0.7*cm, 'Decodifica · 5 Workflows con IA · decodifica.net')
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(GRAY)
    canvas.drawCentredString(A4[0]/2, 0.6*cm, f'Página {doc.page} · v{VERSION} · {UPDATED_SHORT} · decodifica.net/recursos')
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


# WORKFLOWS - prompts loaded from external .md files to avoid string-quote hell
WORKFLOWS = [
    {
        'title': 'Workflow 1: Escribir emails que suenan a ti',
        'problem': 'Tienes que escribir un email difícil, no tienes tiempo para pulirlo 20 min, y el tono Claude por defecto suena a robot. Resultado: emails que no suenan a ti, o tardas una hora.',
        'solucion': 'Claude con tu voz + estructura de 5 párrafos. 5 min de email bien escrito.',
        'pasos': [
            'Crea un voice sample: escribe 3-5 emails reales tuyos (los que mejor suenan) y pégalos en el prompt.',
            'Pega el email que tienes que responder.',
            'Indica objetivo: mantener relación, cerrar tema, conseguir X.',
            'Pide 3 versiones con tono distinto (asertivo, diplomático, firme) y elige la que más te suene.',
            'Edita solo el 5% (quita muletillas, ajusta una frase), envia.',
        ],
        'prompt_file': 'workflow-1-emails.md',
    },
    {
        'title': 'Workflow 2: Resumir PDFs largos (sin que suba a la nube)',
        'problem': 'Tienes un PDF de 80 páginas que necesitas entender HOY. Subirlo a ChatGPT/Claude puede exponer información confidencial. No subirlo significa renunciar a usar IA.',
        'solucion': 'Pipeline local: extraer texto con pypdf + chunking + map-reduce. El PDF nunca sale de tu máquina.',
        'pasos': [
            'Instala pypdf: pip install pypdf',
            'Extrae el texto: from pypdf import PdfReader; ...',
            'Si es escaneo, aplica OCR local con Tesseract. Si usas un OCR en la nube, revisa antes la privacidad del documento.',
            'Chunking semántico: divide por secciones (no por páginas), bloques de 10-15 páginas.',
            'Resume cada chunk por separado con el mismo prompt.',
            'Resume todos los resúmenes parciales en uno ejecutivo de 400-600 palabras.',
        ],
        'prompts': [
            ('Prompt resumen parcial', 'workflow-2-prompt-parcial.md'),
            ('Prompt resumen final', 'workflow-2-prompt-final.md'),
        ],
    },
    {
        'title': 'Workflow 3: Analizar datos en CSV/Excel (sin programar)',
        'problem': 'Tienes un CSV con 10K filas, necesitas insights pero no quieres abrir Tableau ni aprender pandas.',
        'solucion': 'Code Interpreter (ChatGPT Plus) o Claude con capacidad de código, análisis estructurado en pasos.',
        'pasos': [
            'Sube el CSV a ChatGPT con Code Interpreter o a Claude.',
            'Pide resumen estadístico (count, mean, std, top) PRIMERO. Valida que entendió el schema.',
            'Después pide insights específicos: outliers, comparativas, tendencias.',
            'Pide gráficos específicos. Claude puede generar código Python que tú ejecutas en local.',
            'Verifica: ¿los números de la IA coinciden con cálculos manuales sobre 5-10 filas?',
        ],
        'prompt_file': 'workflow-3-csv.md',
    },
    {
        'title': 'Workflow 4: Planificar tu semana (sin sobreoptimizar)',
        'problem': 'Tienes 47 cosas que hacer, 3 deadlines urgentes, no sabes por dónde empezar.',
        'solucion': 'Claude con tu contexto real (horas, deadlines, energía) + output accionable, no motivacional.',
        'pasos': [
            'Lista TODO lo pendiente, sin filtrar.',
            'Para cada item: deadline, urgencia, tiempo estimado realista.',
            'Indica capacidad REAL: horas/día, días de foco vs reuniones, energía.',
            'Pide el plan priorizado, NO la lista completa. La IA decide el 20% que haras.',
            'Añade un parking lot para lo que no entra, visible pero sin culpa.',
        ],
        'prompt_file': 'workflow-4-semana.md',
    },
    {
        'title': 'Workflow 5: Aprender un tema nuevo (sin tutoriales de 2h)',
        'problem': 'Quieres aprender X. Tutoriales de 2 h, documentación de 300 páginas, cursos de 20 h. No tienes 20 h.',
        'solucion': 'Explain like I am 12 + 3 ejercicios prácticos. 1-2 horas, nivel funcional.',
        'pasos': [
            'Prompt 1: Explícame X como si tuviera 12 años, con analogía.',
            'Prompt 2: Ahora técnicamente, asumiendo que sé programar pero no X.',
            'Prompt 3: Dame 3 problemas pequeños progresivos.',
            'Resuelve los 3 TÚ. Cuando te atasques, pregunta.',
            'Prompt 4: 2 contraargumentos o limitaciones de X.',
        ],
        'prompt_file': 'workflow-5-aprender.md',
    },
]


def load_prompt_file(filename):
    path = os.path.join(PROMPTS_DIR, filename)
    if not os.path.exists(path):
        return f'[Prompt file not found: {filename}]'
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()


intro_text = """
Cinco workflows para convertir tareas repetidas en procesos más claros. Cada
uno incluye el problema, los pasos y un prompt inicial. Adapta el contexto,
comprueba los datos y revisa siempre el resultado antes de utilizarlo.
"""

cta_text = """
¿TE HA GUSTADO ESTE PDF?

Cada semana compartimos una tarea real, varias herramientas, un proceso práctico
y el fallo que conviene evitar. Suscríbete:
    https://buttondown.com/decodifica

Versión {version} · Actualizada el {updated}
Recurso canónico: {canonical_url}
"""
cta_text = cta_text.format(version=VERSION, updated=UPDATED, canonical_url=CANONICAL_URL)

# Build PDF
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=1.5*cm, bottomMargin=1.5*cm,
    title='5 workflows con IA en tu día a día - Decodifica',
    author='Decodifica',
    subject=f'Lead magnet Decodifica #3 · versión {VERSION} · {UPDATED}'
)

story = []

# COVER
story.append(Spacer(1, 5*cm))
story.append(Paragraph('5 Workflows', cover_h))
story.append(Paragraph('con IA en tu', cover_h))
story.append(Paragraph('día a día', cover_h))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph('Emails, PDFs, datos, planificación, aprendizaje', cover_sub))
story.append(Spacer(1, 1*cm))
story.append(Paragraph('Una guía práctica de Decodifica · decodifica.net', cover_desc))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph(f'Versión {VERSION} · Actualizada el {UPDATED}', cover_desc))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Por Jordi · Decodifica', cover_desc))
story.append(PageBreak())

# TOC
story.append(Paragraph('Índice', h1))
toc_data = [['#', 'Workflow', 'Tiempo']]
for idx, wf in enumerate(WORKFLOWS, 1):
    title = wf['title'].split(': ', 1)[1] if ': ' in wf['title'] else wf['title']
    toc_data.append([str(idx), title, '5-10 min'])
t = Table(toc_data, colWidths=[1*cm, 11*cm, 2.5*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), CYAN),
    ('TEXTCOLOR', (0, 0), (-1, 0), DARK_BG),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('TEXTCOLOR', (0, 1), (-1, -1), WHITE),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('ALIGN', (-1, 1), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [DARK_BG, HexColor('#1f2937')]),
]))
story.append(t)
story.append(Spacer(1, 1*cm))
story.append(Paragraph(intro_text.replace('\n', '<br/>'), intro))
story.append(PageBreak())

# CONTENT
for wf in WORKFLOWS:
    story.append(Paragraph(wf['title'], h1))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph('El problema', h2))
    story.append(Paragraph(wf['problem'], body))

    story.append(Paragraph('La solución', h2))
    story.append(Paragraph(wf['solucion'], body))

    story.append(Paragraph('Pasos', h2))
    for i, paso in enumerate(wf['pasos'], 1):
        story.append(Paragraph(str(i) + '. ' + paso, body))

    story.append(Paragraph('Prompt(s) iniciales', h2))
    if 'prompt_file' in wf:
        prompt_text = load_prompt_file(wf['prompt_file'])
        safe = prompt_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        story.append(Paragraph(safe.replace('\n', '<br/>'), prompt_style))
    if 'prompts' in wf:
        for subtitle, filename in wf['prompts']:
            story.append(Paragraph(subtitle, h3))
            prompt_text = load_prompt_file(filename)
            safe = prompt_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            story.append(Paragraph(safe.replace('\n', '<br/>'), prompt_style))

    story.append(PageBreak())

# CTA
story.append(Spacer(1, 3*cm))
story.append(Paragraph('Gracias por leer', h1))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph(cta_text.replace('\n', '<br/>'), body))

doc.build(story, onFirstPage=on_cover, onLaterPages=on_page)

print(f'OK: {OUTPUT}')
print(f'Size: {os.path.getsize(OUTPUT) / 1024:.1f} KB')
print(f'Workflows: {len(WORKFLOWS)}')
