import assemblyai as aai

# Configure la clave de API (almacénela de forma segura en producción)
aai.settings.api_key = "c8db1e04148d42998ffaac7062a28e1e"

# URL del archivo de la reunión
MEETING_URL = "https://storage.googleapis.com/aai-web-samples/meeting.mp3"

# Paso 1: Transcribir el archivo de audio
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(MEETING_URL)

# Paso 2: Definir un prompt detallado para generar las actas de la reunión
prompt = """
Analice esta transcripción de la reunión y proporcione un resumen estructurado con lo siguiente:

1.  **Visión General de la Reunión**
    *   Fecha y duración de la reunión
    *   Lista de participantes (si se mencionan)
    *   Objetivos principales discutidos

2.  **Decisiones Clave**
    *   Documente todas las decisiones finales tomadas
    *   Incluya cualquier plazo o cronograma establecido
    *   Anote cualquier presupuesto o recurso asignado

3.  **Elementos de Acción**
    *   Enumere cada elemento de acción con:
        *   Propietario asignado
        *   Fecha de vencimiento (si se especifica)
        *   Dependencias o requisitos previos

4.  **Temas de Discusión**
    *   Resuma los puntos principales de cada tema
    *   Destaque cualquier desafío o riesgo identificado
    *   Anote cualquier pregunta no resuelta que requiera seguimiento

ROL: Usted es un analista de reuniones profesional centrado en extraer información procesable.
FORMATO: Presente la información en secciones claras con viñetas para facilitar la lectura.
""".strip()

# Paso 3: Enviar el prompt a LeMUR
llm_output = transcript.lemur.task(
    prompt,
    final_model=aai.LemurModel.claude3_5_sonnet
)

# Imprimir las actas de la reunión generadas
print(llm_output.response)