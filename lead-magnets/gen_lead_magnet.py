"""
Lead Magnet Decodifica - 50 prompts para IA
Genera PDF profesional con ReportLab
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    PageTemplate, Frame, NextPageTemplate
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

CYAN = HexColor('#06b6d4')
WHITE = HexColor('#ffffff')
DARK_BG = HexColor('#0a0a0a')
GRAY = HexColor('#9ca3af')
GREEN = HexColor('#10b981')
DARK_GRAY = HexColor('#374151')

OUTPUT = r'C:\Users\jordi\Documents\GitHub\decodifica.net\lead-magnets\50-prompts-ia.pdf'

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
prompt_style = make_style('Prompt', fontSize=8.5, leading=11, textColor=GREEN, fontName='Courier', leftIndent=12, rightIndent=12, spaceBefore=4, spaceAfter=8)
footer_style = make_style('Footer', fontSize=8, leading=10, textColor=GRAY, alignment=TA_CENTER)

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, A4[1] - 0.4*cm, A4[0], 0.4*cm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString(A4[0]/2, A4[1] - 0.7*cm, 'Decodifica · 50 Prompts para IA · decodifica.net')
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

# PROMPTS CONTENT
PROMPTS = {
    'Productividad y trabajo': [
        ('Email difícil de responder', 'Eres un asistente de comunicación profesional. Tengo que responder a este email que me incomoda: [PEGAR EMAIL]. Mi objetivo: [mantener relación / cerrar tema / conseguir X]. Reescribe el email en tono [asertivo/diplomático/firme], con máximo 5 párrafos, sin palabras pasivo-agresivas. Termina con pregunta que fuerce respuesta.'),
        ('Reunión que preparo en 5 min', 'Voy a una reunión sobre [tema] con [perfiles]. Duración: [X min]. Mis objetivos: [X, Y, Z]. Mis preocupaciones: [A, B]. Genera: 1) agenda de 3-5 puntos priorizados, 2) preguntas clave que debo hacer, 3) posibles objeciones y respuestas, 4) cómo cerrar la reunión con un siguiente paso concreto.'),
        ('Reunión que he tenido', 'Toma estas notas de mi reunión con [nombre] sobre [tema]: [PEGAR NOTAS]. Genera: 1) resumen ejecutivo de 3 líneas, 2) decisiones tomadas, 3) acciones con responsable y fecha, 4) temas abiertos para próxima reunión, 5) email de seguimiento profesional de 5 párrafos.'),
        ('Decisión entre opciones', 'Tengo que decidir entre [OPCIÓN A] y [OPCIÓN B]. Contexto: [describir situación]. Criterios que importan: [lista]. Mi intuición actual: [X]. Haz: 1) tabla comparativa con pros/contras por criterio, 2) qué información me falta, 3) qué pasaría si elijo cada una, 4) tu recomendación razonada.'),
        ('Bloqueo creativo / no sé por dónde empezar', 'Quiero conseguir [objetivo] pero no sé por dónde empezar. Mi situación: [contexto]. Genera: 1) las 3 preguntas más importantes que debería responder primero, 2) el primer paso concreto de 15 minutos que puedo hacer HOY, 3) recursos gratuitos para aprender lo básico, 4) plan de 7 días para arrancar.'),
        ('Reuniones 1:1 con mi jefe', 'Tengo un 1:1 con mi jefe. Quiero hablar de: [X]. Mi frustración: [Y]. Lo que quiero conseguir: [Z]. Ayúdame con: 1) cómo plantear el tema sin sonar quejica, 2) datos/ejemplos que debería llevar preparados, 3) cómo pedir lo que quiero sin parecer exigente, 4) señales de que la conversación va bien o mal.'),
        ('Priorizar mi backlog de tareas', 'Mi lista de tareas pendientes: [PEGAR LISTA]. Mi deadline más urgente: [fecha]. Mi capacidad real: [X horas/día]. Energía: [alta/media/baja]. Ayúdame a: 1) ordenar por impacto/urgencia, 2) agrupar en bloques de trabajo, 3) decidir qué NO voy a hacer esta semana, 4) sugerir la primera tarea para hacer AHORA.'),
        ('Email de "no puedo"', 'Tengo que rechazar [X: una reunión / un favor / un proyecto]. Mi relación con la persona: [jefe/cliente/igual]. Mi razón real: [X]. Redacta un email breve, profesional, que no cierre puertas, que no se extienda en disculpas, y que ofrezca alternativa concreta si la tengo.'),
        ('Pedir feedback honesto', 'Quiero pedirle a [persona: jefe, mentor, cliente] feedback honesto sobre [mi trabajo / mi forma de comunicar / etc]. No quiero respuestas genéricas. Dame 5 preguntas específicas que maximicen la probabilidad de recibir crítica constructiva honesta, en un tono que invite a abrirse.'),
        ('Resumen semanal (Friday Review)', 'Esta semana hice: [LISTA DE COSAS]. Aprendí: [X]. Fracasos: [Y]. Mi objetivo del mes: [Z]. Mi estado de energía: [X]. Genera: 1) wins reales vs tareas completadas (no todo vale), 2) qué NO funcionó y por qué, 3) qué cambiar la semana que viene, 4) una pregunta para mí mismo que me obligue a pensar profundo.'),
    ],
    'Escritura y contenido': [
        ('Hook que no sea clickbait', 'Escribe 5 versiones de hook (primeras 2 líneas) para un post sobre [TEMA]. Audiencia: [QUIÉN]. Objetivo: que abran el post, no que sientan que les han engañado. Cada hook debe: 1) plantear una tensión o pregunta real, 2) prometer valor concreto, 3) sonar como humano, no como SEO.'),
        ('Post de LinkedIn que genere conversación', 'Tema: [TEMA]. Mi punto de vista único: [X]. Mi experiencia: [Y]. Genera un post de LinkedIn: 1) primera línea que pare la scroll (sin clickbait), 2) historia o ejemplo concreto, 3) insight no obvio, 4) pregunta que invite a comentar, 5) formato con saltos de línea cortos, máximo 1300 caracteres.'),
        ('Reescribir email corporativo para sonar humano', 'Reescribe este email corporativo para que suene como una persona real y no como plantilla: [PEGAR EMAIL]. Quita: palabras vacías, formalismo excesivo, frases hechas. Añade: una frase específica que muestre que te importa el tema. Mantén profesional pero quita la máscara.'),
        ('Tweet / post X que aporta valor', 'Sobre [TEMA], dame 5 versiones de tweet (≤280 chars) que: 1) enseñen algo útil, 2) NO sean frases vacías de LinkedIn, 3) generen al menos un "save" o un reply, 4) se puedan defender si alguien te llama la atención por imprecisos.'),
        ('Newsletter intro (primer párrafo)', 'Newsletter semanal sobre [TEMA]. Tono: [profesional/casual/técnico]. Apertura debe: 1) hacer sentir al lector que se perdió algo, 2) prometer 1-3 ideas concretas que se lleva hoy, 3) no ser genérica. Genera 3 versiones de apertura (2-3 frases cada una).'),
        ('Título que NO sea clickbait', 'Tema del post: [TEMA]. Ángulo: [X]. Audiencia: [QUIÉN]. Genera 8 títulos que: 1) prometan valor real, 2) no usen "esto cambiará tu vida", 3) tengan entre 40-60 chars para SEO, 4) generen curiosidad legítima. Si usas números, que sean honestos.'),
        ('Comentario inteligente en post ajeno', 'Voy a comentar este post de LinkedIn/Twitter/HN: [PEGAR POST O LINK]. Quiero: 1) añadir valor, no solo "great post!", 2) no quedar como pelota, 3) posiblemente iniciar conversación con el autor, 4) que mi comentario aporte insight que otros no vean. Genera 3 versiones con distinto ángulo.'),
        ('Texto de bio / about me creíble', 'Necesito una bio para [perfil: LinkedIn/Twitter/Newsletter/about de la web]. Datos: trabajo en [X], me importa [Y], creo que [Z]. Genera 3 versiones (corta, media, larga) que: 1) no suenen a CV inflado, 2) tengan al menos un detalle específico, 3) inviten a conectar/contactar, 4) sean honestas, no aspiracionales.'),
        ('Argumento contra posición popular', 'Quiero反驳 la idea popular de que [POSICIÓN POPULAR]. Mis razones: [X, Y, Z]. Genera un argumento de 200-300 palabras que: 1) reconozca la parte de razón de la otra postura, 2) presente mi反驳 sin sonar borde, 3) use un ejemplo o dato concreto, 4) cierre con una pregunta que abra diálogo, no que cierre.'),
        ('Newsletter body (cuerpo del email)', 'Tema: [TEMA]. Estructura: 1) apertura personal corta (1-2 frases), 2) 3 ideas principales con ejemplos, 3) "1 prompt que probé esta semana" (opcional, original), 4) cierre con pregunta o call to action. Tono: como si le escribieras a un amigo que sabe poco. Máximo 600 palabras.'),
    ],
    'Programación y código': [
        ('Refactorizar función legacy', 'Refactoriza esta función legacy para que sea legible y testeable, sin cambiar el comportamiento externo: [PEGAR CÓDIGO]. Requisitos: 1) nombres de variables claros, 2) separar concerns, 3) añadir type hints, 4) tests unitarios de los casos principales, 5) maneja errores explícitamente.'),
        ('Explicar código a un junior', 'Explica este código como si se lo explicaras a un developer junior con 6 meses de experiencia: [PEGAR CÓDIGO]. Estructura: 1) qué hace en una frase, 2) el flujo paso a paso, 3) por qué se hizo así, 4) qué mejoraría, 5) un ejemplo de uso real.'),
        ('Code review honesto', 'Review honesto de este PR/diff: [PEGAR DIFF]. No me ahorres críticas. Dame: 1) qué está bien, 2) qué está mal o se puede mejorar, 3) bugs potenciales, 4) problemas de seguridad, 5) problemas de performance, 6) tests que faltan, 7) cambios de naming/estructura.'),
        ('Debugging misterioso', 'Bug: [DESCRIPCIÓN]. Lo que he probado: [LISTA]. Lo que esperaba: [X]. Lo que pasa: [Y]. Logs relevantes: [PEGAR]. Genera: 1) hipótesis ordenadas por probabilidad, 2) tests específicos para cada una, 3) lugares donde mirar primero, 4) preguntas que me ayudarían a descartarlas.'),
        ('Migración de framework X a Y', 'Tengo un proyecto en [X] que quiero migrar a [Y]. Stack: [X con versiones]. Restricciones: [NO romper API / mantener backwards compat / etc]. Genera plan de migración: 1) orden de cambios, 2) cosas que se rompen seguro, 3) cómo hacerlo incrementalmente, 4) tests críticos, 5) rollback plan.'),
        ('Optimizar query lenta', 'Esta query tarda [X segundos / Y ms]: [PEGAR SQL]. Schema: [PEGAR SCHEMA]. Cardinalidad: [tabla tiene N filas, etc]. Genera: 1) análisis de qué la hace lenta, 2) índices que añadiría, 3) reformulación de la query, 4) si necesita particionado, 5) cómo medir el speedup.'),
        ('Naming things (variables, funciones, clases)', 'Nombra mejor esto: [PEGAR CÓDIGO]. Reglas: 1) nombres que describan intención, no implementación, 2) consistencia con el resto del codebase, 3) evitar abreviaciones, 4) si es función, debe leerse como verbo, 5) si es booleano, debe leerse como pregunta (isX, hasY).'),
        ('Diseño de API REST', 'Diseña los endpoints REST para [RECURSO: usuarios/productos/posts]. Casos de uso: [LISTAR]. Genera: 1) tabla de endpoints con método, path, propósito, 2) schemas JSON de request/response, 3) códigos HTTP y cuándo se devuelven, 4) paginación, 5) versionado, 6) autenticación y rate limiting.'),
        ('Tests que sí valen la pena', 'Tengo este código: [PEGAR]. ¿Qué tests SÍ aportan valor vs cuáles son ceremony? Dame: 1) los 5-7 tests críticos que sí escribiría, 2) qué cubre cada uno, 3) el código del test, 4) tests que NO haría y por qué.'),
        ('Setup de proyecto nuevo', 'Voy a empezar un proyecto [tipo: API/script/webapp] con [stack]. Genera: 1) estructura de directorios, 2) qué archivos de config crear primero, 3) dependencias iniciales con justificación, 4) setup de CI/tests, 5) convenciones que voy a seguir.'),
    ],
    'Análisis y decisión': [
        ('Trade-off técnico con tiempo limitado', 'Tengo que decidir entre [A] y [B] para [proyecto]. Pros/contras que conozco: [X]. Tiempo disponible: [X días]. Equipo: [X]. Recomiéndame con justificación qué elegir, asumiendo que no hay opción perfecta y que tengo que avanzar.'),
        ('Evaluar herramienta nueva', 'Estoy evaluando usar [HERRAMIENTA] para [CASO DE USO]. Alternativas que ya uso: [X, Y]. Dame: 1) qué problema real me resuelve, 2) qué me cuesta aprender/integrar, 3) riesgo de vendor lock-in, 4) si tiene alternativa open source seria, 5) tu recomendación: adoptar / probar / ignorar.'),
        ('Vale la pena aprender [Tecnología]?', '¿Vale la pena aprender [TECNOLOGÍA] en 2026? Mi perfil: [DESCRIBIR]. Mi tiempo: [X horas/semana]. Contexto: [TRABAJO/PROYECTO]. Dame: 1) demanda real del mercado, 2) curva de aprendizaje, 3) transferibilidad a otras tech, 4) recursos para empezar, 5) veredicto.'),
        ('Análisis de competencia', 'Estos son mis competidores en [NICHO]: [LISTAR]. Dame: 1) qué están haciendo bien, 2) qué están haciendo mal, 3) dónde hay hueco para diferenciarme, 4) ideas concretas de ángulos que ellos no cubren, 5) tu opinión sobre cuál es la mejor estrategia para destacar.'),
        ('Cuándo dejar un proyecto', 'Llevo [X meses] con [PROYECTO]. Avances: [LISTA]. Ingresos: [X]. Mi compromiso: [X horas/sem]. Mi nivel de burnout: [X]. Dame criterios objetivos para decidir si seguir o parar, y aplica el test a mi caso.'),
        ('Pricing de producto digital', 'Quiero vender [PRODUCTO] a [PRECIO]. Competencia vende: [LISTA con precios]. Mi coste marginal: [X]. Mi audiencia: [DESCRIBIR]. Recomiéndame precio óptimo considerando: 1) poder adquisitivo, 2) valor percibido, 3) competencia, 4) modelo de suscripción vs pago único.'),
        ('SWOT honesto', 'Estoy lanzando [PROYECTO]. Hazme un SWOT brutalmente honesto: 1) Strengths (no inventes), 2) Weaknesses (incluye las que no quiero ver), 3) Opportunities (reales, no wishful thinking), 4) Threats (incluye las que me autoengaño creyendo que no existen).'),
        ('Hire vs. no hire', 'Estoy dudando si contratar a [PERFIL: VA/dev/diseñador/marketing] o seguir haciéndolo yo. Coste: [X/mes]. Tiempo que gano: [estimar]. Ingresos actuales: [X]. Ayúdame con: 1) análisis de cuándo contratar, 2) si lo hago, qué tareas delego primero, 3) si no lo hago, qué tareas SÍ debería automatizar.'),
        ('Evaluar copy antes de publicar', 'Voy a publicar este copy: [PEGAR COPY]. Audiencia: [X]. Objetivo: [Y]. Dame: 1) qué funciona, 2) qué confunde o repele, 3) la versión mejorada, 4) tests A/B que haría, 5) dónde poner CTAs.'),
        ('Comparar dos ofertas/trabajos', 'Tengo dos ofertas: [A] y [B]. Datos: [salario, beneficios, equipo, tech, etc]. Mis prioridades: [LISTA]. Ayúdame a: 1) tabla comparativa con scoring por prioridad, 2) cuál encaja mejor con mis objetivos de 3-5 años, 3) qué preguntar en la siguiente entrevista, 4) tu recomendación razonada.'),
    ],
    'Aprendizaje y estudio': [
        ('Aprender [TEMA] desde cero', 'Quiero aprender [TEMA] desde cero. Mi background: [X]. Mi objetivo: [saber usar / certificarme / hacer proyecto / etc]. Tiempo: [X horas/sem]. Dame: 1) roadmap de 4 semanas, 2) recursos ordenados por dificultad, 3) proyecto práctico para cada semana, 4) cómo saber si avanzo bien.'),
        ('Resumir artículo denso', 'Lee este artículo/ensayo: [PEGAR TEXTO O URL]. Genera: 1) tesis principal en 1 frase, 2) 5 ideas clave con números/datos, 3) 1-2 contraargumentos que el autor no menciona, 4) cómo aplicar a mi vida/trabajo, 5) lecturas siguientes si quiero profundizar.'),
        ('Explicar concepto complejo simple', 'Explícame [CONCEPTO] como si tuviera 12 años y luego otra vez como si fuera experto. 1) versión simple con analogía, 2) versión técnica con el modelo mental correcto, 3) ejemplo concreto, 4) errores comunes que la gente comete, 5) cómo profundizar.'),
        ('Comparar dos frameworks/tecnologías', 'Compara [A] vs [B] para [CASO DE USO]. Tabla con: 1) curva de aprendizaje, 2) ecosistema, 3) demanda laboral, 4) casos donde A gana, 5) casos donde B gana, 6) tu recomendación según mi perfil.'),
        ('Hacer un curso mejor', 'Estoy tomando un curso sobre [TEMA]. Quiero aprender mejor: 1) cómo tomar notas activas, 2) cómo practicar efectivamente, 3) cómo conectar conceptos, 4) cómo aplicar a mi trabajo, 5) cómo saber si avanzo.'),
        ('Explicar diferencia entre X e Y', 'Explícame la diferencia real entre [X] e [Y]. No la definición de manual. 1) cuándo usar uno vs otro, 2) ejemplos concretos, 3) la confusión típica entre ambos, 4) el matiz que casi nadie explica.'),
        ('Generar preguntas de entrevista', 'Voy a una entrevista para [PUESTO]. Genera: 1) las 10 preguntas más probables con respuesta sugerida, 2) 5 preguntas trampa con cómo responder, 3) 3 preguntas que YO debería hacer al entrevistador, 4) cómo negociar el sueldo si me lo ofrecen.'),
        ('Crear un cheat sheet personal', 'Necesito un cheat sheet de [TEMA] para tener siempre a mano. Haz: 1) los 5-7 conceptos mínimos, 2) los comandos/snippets esenciales, 3) los 3 errores típicos, 4) el árbol de decisión de cuándo usar qué, 5) recursos para profundizar.'),
        ('Generar ejercicios para practicar', 'Quiero practicar [HABILIDAD]. Dame: 1) 5 ejercicios progresivos (de fácil a difícil), 2) criterios para saber si los resuelvo bien, 3) trampa típica en cada uno, 4) tiempo estimado por ejercicio, 5) el orden en que hacerlos.'),
        ('Encontrar recursos confiables', 'Quiero aprender sobre [TEMA] con recursos de calidad. Filtra: 1) los 3 mejores libros (con por qué), 2) los 3 mejores canales de YouTube, 3) las 3 mejores newsletters, 4) los 2 mejores cursos (gratuitos primero), 5) personas a seguir en Twitter/LinkedIn.'),
    ],
}

intro_text = """
Este PDF es el lead magnet de Decodifica, una curacion semanal de herramientas de IA
y trucos de productividad. Son prompts que yo (Jordi) uso a diario para trabajar,
escribir, programar y tomar decisiones. Todos los prompts se han probado con
ChatGPT, Claude y Gemini. Funcionan tal cual. Copia, pega, adapta.
"""

cta_text = """
¿TE HA GUSTADO ESTE PDF?

Si quieres recibir uno nuevo cada sábado, con prompts actualizados y los
mejores trucos de la semana, suscribete a la newsletter:

    https://buttondown.com/decodifica

Si un prompt te ha ahorrado tiempo, escribeme por Twitter y lo cuento:
@decodificaia
"""

# Build PDF
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=1.5*cm, bottomMargin=1.5*cm,
    title='50 Prompts para IA - Decodifica',
    author='Decodifica',
    subject='Lead magnet Decodifica'
)

story = []

# COVER
story.append(Spacer(1, 6*cm))
story.append(Paragraph('50 Prompts', cover_h))
story.append(Paragraph('para IA', cover_h))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph('Productividad, escritura, código, análisis y aprendizaje', cover_sub))
story.append(Spacer(1, 1*cm))
story.append(Paragraph('Una curacion de Decodifica · decodifica.net', cover_desc))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph('Por Jordi · @decodificaia', cover_desc))
story.append(PageBreak())

# TOC
story.append(Paragraph('Indice', h1))
toc_data = [['#', 'Categoria', 'Prompts']]
for idx, (cat, prompts) in enumerate(PROMPTS.items(), 1):
    toc_data.append([str(idx), cat, str(len(prompts))])
t = Table(toc_data, colWidths=[1*cm, 10*cm, 2*cm])
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
for category, prompts in PROMPTS.items():
    story.append(Paragraph(category, h1))
    story.append(Paragraph(f'{len(prompts)} prompts en esta seccion', intro))
    story.append(Spacer(1, 0.3*cm))
    for idx, (title, prompt_text) in enumerate(prompts, 1):
        story.append(Paragraph(f'{idx}. {title}', h2))
        # Escape for ReportLab
        safe = prompt_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        # Use courier style for the prompt itself
        story.append(Paragraph(safe, prompt_style))
    story.append(PageBreak())

# CTA
story.append(Spacer(1, 3*cm))
story.append(Paragraph('Gracias por leer', h1))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph(cta_text.replace('\n', '<br/>'), body))

# Build with two page templates: cover (no header/footer) + content
doc.build(story, onFirstPage=on_cover, onLaterPages=on_page)

print(f'OK: {OUTPUT}')
print(f'Size: {os.path.getsize(OUTPUT) / 1024:.1f} KB')
