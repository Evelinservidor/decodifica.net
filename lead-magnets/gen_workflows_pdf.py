"""Lead Magnet Decodifica #3 - 5 Workflows con IA en tu dia a dia
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


# WORKFLOWS - prompts loaded from external .md files to avoid string-quote hell
WORKFLOWS = [
    {
        'title': 'Workflow 1: Escribir emails que suenan a ti',
        'problem': 'Tienes que escribir un email difícil, no tienes tiempo para pulirlo 20 min, y el tono Claude por defecto suena a robot. Resultado: emails que no suenan a ti, o tardas una hora.',
        'solucion': 'Claude con tu voz + estructura de 5 parrafos. 5 min de email bien escrito.',
        'pasos': [
            'Crea un voice sample: escribe 3-5 emails reales tuyos (los que mejor suenan) y pegalos en el prompt.',
            'Pega el email que tienes que responder.',
            'Indica objetivo: mantener relacion, cerrar tema, conseguir X.',
            'Pide 3 versiones con tono distinto (asertivo, diplomatico, firme) y elige la que mas te suene.',
            'Edita solo el 5% (quita muletillas, ajusta una frase), envia.',
        ],
        'prompt_file': 'workflow-1-emails.md',
    },
    {
        'title': 'Workflow 2: Resumir PDFs largos (sin que suba a la nube)',
        'problem': 'Tienes un PDF de 80 paginas que necesitas entender HOY. Subirlo a ChatGPT/Claude = cede confidencialidad. No subirlo = no usas IA.',
        'solucion': 'Pipeline local: extraer texto con pypdf + chunking + map-reduce. El PDF nunca sale de tu maquina.',
        'pasos': [
            'Instala pypdf: pip install pypdf',
            'Extrae el texto: from pypdf import PdfReader; ...',
            'Si es escaneo, OCR previo con Tesseract o Mistral OCR local.',
            'Chunking semantico: divide por secciones (no por paginas), bloques de 10-15 paginas.',
            'Resume cada chunk por separado con el mismo prompt.',
            'Resume todos los resumenes parciales en uno ejecutivo de 400-600 palabras.',
        ],
        'prompts': [
            ('Prompt resumen parcial', 'workflow-2-prompt-parcial.md'),
            ('Prompt resumen final', 'workflow-2-prompt-final.md'),
        ],
    },
    {
        'title': 'Workflow 3: Analizar datos en CSV/Excel (sin programar)',
        'problem': 'Tienes un CSV con 10K filas, necesitas insights pero no quieres abrir Tableau ni aprender pandas.',
        'solucion': 'Code Interpreter (ChatGPT Plus) o Claude con capacidad de codigo, analisis estructurado en pasos.',
        'pasos': [
            'Sube el CSV a ChatGPT con Code Interpreter o a Claude.',
            'Pide resumen estadistico (count, mean, std, top) PRIMERO. Valida que entendio el schema.',
            'Despues pide insights especificos: outliers, comparativas, tendencias.',
            'Pide graficos especificos. Claude puede generar codigo Python que tu ejecutas en local.',
            'Verifica: los numeros de la IA, coinciden con calculos manuales sobre 5-10 filas?',
        ],
        'prompt_file': 'workflow-3-csv.md',
    },
    {
        'title': 'Workflow 4: Planificar tu semana (sin sobreoptimizar)',
        'problem': 'Tienes 47 cosas que hacer, 3 deadlines urgentes, no sabes por donde empezar.',
        'solucion': 'Claude con tu contexto real (horas, deadlines, energia) + output accionable, no motivacional.',
        'pasos': [
            'Lista TODO lo pendiente, sin filtrar.',
            'Para cada item: deadline, urgencia, tiempo estimado realista.',
            'Indica capacidad REAL: horas/dia, dias de foco vs reuniones, energia.',
            'Pide el plan priorizado, NO la lista completa. La IA decide el 20% que haras.',
            'Anade un parking lot para lo que no entra, visible pero sin culpa.',
        ],
        'prompt_file': 'workflow-4-semana.md',
    },
    {
        'title': 'Workflow 5: Aprender un tema nuevo (sin tutoriales de 2h)',
        'problem': 'Quieres aprender X. Tutoriales 2h, docs 300 paginas, cursos 20h. No tienes 20h.',
        'solucion': 'Explain like I am 12 + 3 ejercicios practicos. 1-2 horas, nivel funcional.',
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
Este es el tercer lead magnet de Decodifica. 5 workflows que uso yo cada
semana con IA. Cada uno incluye el problema, los pasos exactos y el prompt
literal que uso (copia y pega). Funcionan con ChatGPT, Claude y Gemini.
"""

cta_text = """
¿TE HA GUSTADO ESTE PDF?

Si quieres uno nuevo cada sabado, suscribete:
    https://buttondown.com/decodifica

Para mas tutoriales sobre IA aplicada al trabajo:
    https://decodifica.net/blog

¿Adaptas alguno de estos workflows a tu trabajo? Mandamelo y lo publico.
"""

# Build PDF
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=1.5*cm, bottomMargin=1.5*cm,
    title='5 Workflows con IA en tu dia a dia - Decodifica',
    author='Decodifica',
    subject='Lead magnet Decodifica #3'
)

story = []

# COVER
story.append(Spacer(1, 5*cm))
story.append(Paragraph('5 Workflows', cover_h))
story.append(Paragraph('con IA en tu', cover_h))
story.append(Paragraph('dia a dia', cover_h))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph('Emails, PDFs, datos, planificacion, aprendizaje', cover_sub))
story.append(Spacer(1, 1*cm))
story.append(Paragraph('Una guia practica de Decodifica · decodifica.net', cover_desc))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph('Por Jordi · @decodificaia', cover_desc))
story.append(PageBreak())

# TOC
story.append(Paragraph('Indice', h1))
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

    story.append(Paragraph('La solucion', h2))
    story.append(Paragraph(wf['solucion'], body))

    story.append(Paragraph('Pasos', h2))
    for i, paso in enumerate(wf['pasos'], 1):
        story.append(Paragraph(str(i) + '. ' + paso, body))

    story.append(Paragraph('Prompt(s) que uso', h2))
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
