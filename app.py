import streamlit as st
import requests
import google.generativeai as genai
import json

# =================================================================
# 1. CONFIGURACIÓN VISUAL Y JERARQUÍA DE TAMAÑOS
# =================================================================
st.set_page_config(page_title="Sintetizador de Soluciones", page_icon="🏛️", layout="wide")

st.markdown("""
    <style>
    .titulo-maestro { font-size: 4.5rem !important; font-weight: 800; color: #1a1a1a; margin-bottom: 0px; line-height: 1.2; }
    .etiqueta-fuerte { font-size: 1.8rem !important; font-weight: 700; color: #2c3e50; margin-top: 20px; margin-bottom: 10px; }
    textarea { font-size: 1.3rem !important; }
    .stButton > button { height: 70px; font-size: 1.3rem !important; font-weight: bold; border-radius: 10px; }
    .stChatMessage { font-size: 1.3rem !important; background-color: #f8f9fa; border-radius: 10px; border: 1px solid #e0e0e0; }
    .indicador-activo { font-size: 2rem !important; font-weight: 800; color: #d35400; background-color: #fcf3cf; padding: 10px 20px; border-radius: 10px; text-align: center;}
    </style>
""", unsafe_allow_html=True)

# =================================================================
# 1.5 PANEL LATERAL - EL HORIZONTE EVOLUTIVO
# =================================================================
with st.sidebar:
    st.markdown('### 🚀 Próximas Fases')
    st.caption("Arquitectura en desarrollo para expansión universal.")
    st.divider()
    st.markdown('**🌐 Fase 2: Conexión al Mundo**')
    st.toggle("Internet en Tiempo Real", disabled=True, help="Próximamente: Análisis fundamentado con datos actualizados al segundo.")
    st.markdown('**🧠 Fase 3: Memoria Histórica**')
    st.toggle("Bóveda de Memoria Colectiva", disabled=True, help="Próximamente: Asimilación de casos de éxito mundiales para un progreso continuo.")
    st.markdown('**🎙️ Fase 4: Interfaz de Voz**')
    st.toggle("Diálogo Bidireccional", disabled=True, help="Próximamente: Diálogo natural por voz generada localmente con el panel de expertos.")

st.markdown('<p class="titulo-maestro">Sintetizador de Soluciones</p>', unsafe_allow_html=True)
st.divider()

# =================================================================
# 2. CONEXIÓN BLINDADA E INTELIGENTE
# =================================================================
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

nombre_rescate = 'gemini-pro'
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods and 'gemini' in m.name:
            nombre_rescate = m.name
            break
except Exception:
    pass
modelo_respaldo = genai.GenerativeModel(nombre_rescate)

# =================================================================
# 3. LA HERIDA ABIERTA
# =================================================================
st.markdown('<p class="etiqueta-fuerte">🎯 1. La Herida Abierta (Dolor o Desafío)</p>', unsafe_allow_html=True)
desafio = st.text_area("Describa detalladamente el contexto, dolor o desafío institucional/personal a resolver:", height=130)
st.divider()

# =================================================================
# 4. LA BATUTA Y EL PANEL DE ESTADO VIVO
# =================================================================
st.markdown('<p class="etiqueta-fuerte">⚙️ 2. Panel de Control de los 4 Expertos</p>', unsafe_allow_html=True)

comando_automatico = None
rol_seleccionado = None

# PRIMER RENGLÓN: Los 4 Expertos
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🧠 EL ESTRATEGA", use_container_width=True):
        comando_automatico, rol_seleccionado = "Inicia tu análisis estratégico.", "🧠 EL ESTRATEGA"
with col2:
    if st.button("✨ EL ANIMADOR", use_container_width=True):
        comando_automatico, rol_seleccionado = "Danos tu perspectiva humana.", "✨ EL ANIMADOR"
with col3:
    if st.button("👁️ EL VIGÍA", use_container_width=True):
        comando_automatico, rol_seleccionado = "Evalúa los riesgos técnicos y éticos.", "👁️ EL VIGÍA"
with col4:
    if st.button("🛠️ EL CONSTRUCTOR", use_container_width=True):
        comando_automatico, rol_seleccionado = "Haz el cierre y redacta el Plan de Acción Definitivo.", "🛠️ EL CONSTRUCTOR"

st.markdown("<br>", unsafe_allow_html=True)

# SEGUNDO RENGLÓN: Trabajo en equipo
col_auto, col_estado = st.columns([1, 1])

with col_auto:
    if st.button("🗣️ TRABAJO EN CONJUNTO (Modo Automático)", use_container_width=True, type="primary"):
        comando_automatico, rol_seleccionado = "Inicien el debate orgánico. Dialoguen entre ustedes.", "PANEL DE EXPERTOS"

with col_estado:
    espacio_estado = st.empty()
    espacio_estado.markdown('<p class="indicador-activo">Esperando directiva...</p>', unsafe_allow_html=True)

st.divider()

# =================================================================
# 5. EL CEREBRO Y LOS PERFILES MAESTROS UNIVERSALES
# =================================================================
def configurar_prompt(rol):
    base = "Eres el 'Sintetizador de Soluciones', un ecosistema de inteligencia colectiva. Priorizas la soberanía tecnológica, la evolución humana y la economía circular."
    
    if rol == "PANEL DE EXPERTOS":
        instruccion = "Tienen libre albedrío para debatir. REGLA OBLIGATORIA: Cada vez que un experto habla, debe poner su etiqueta exacta: [ESTRATEGA], [ANIMADOR], [VIGIA], o [CONSTRUCTOR] al inicio de su intervención."
    elif rol == "🧠 EL ESTRATEGA":
        instruccion = "Como Experto Estratega, tu labor es convertir el dolor planteado en un plan estratégico robusto que priorice la planificación y la eficiencia. Evalúa el diagnóstico con una mirada de alto nivel, define visión, alcance y fases, y diseña una arquitectura de capacidades que sustente la ejecución. Mapea procesos clave, establece indicadores de desempeño y puntos de control. Delimita responsabilidades, anticipa dependencias críticas y presenta un marco claro de decisiones que permitan avanzar de forma escalonada y sostenible."
    elif rol == "✨ EL ANIMADOR":
        instruccion = "Como Experto Animador, analiza el problema desde la psicología humana, la empatía, la motivación y el impacto emocional. Identifica barreras psicológicas al cambio y diseña una estrategia de comunicación que fomente la seguridad, la confianza y la cohesión. Propone intervenciones para motivar y alinear a las personas, y establece mecanismos de resolución de conflictos. Traduce las necesidades emocionales en requisitos prácticos, generando un marco que construya resiliencia y un compromiso sostenido con la evolución."
    elif rol == "👁️ EL VIGÍA":
        instruccion = "Como Experto Vigía, aplica una mirada rigurosa para identificar riesgos ocultos, fallas lógicas, problemas éticos o técnicos. Examina supuestos, dependencias no evidentes y posibles efectos secundarios. Realiza un análisis de riesgo exhaustivo, propone mitigaciones y planes de contingencia. Verifica la viabilidad operativa. Documenta tus hallazgos de forma clara y accionable para que el Constructor pueda integrarlos con precisión, manteniendo un foco constante en la protección de la integridad del proyecto."
    elif rol == "🛠️ EL CONSTRUCTOR":
        instruccion = "Como Experto Constructor, no debes debatir. Tu única misión es escuchar atentamente a los tres expertos anteriores y redactar el 'Plan de Acción Definitivo' en perfecto español, de forma objetiva, concisa y profundamente humana. Integra las perspectivas del Estratega, del Animador y del Vigía en un documento estructurado: 1. Diagnóstico Profundo, 2. Estrategia de Resolución, 3. Acciones Inmediatas (Paso a Paso), y 4. Prevención de Riesgos. Tu resultado no es un código de programación ni un comando de IA, sino una hoja de ruta autosuficiente, pragmática y empática. Debe estar redactada para que cualquier ser humano pueda aplicarla directamente para transformar su realidad, sanar su dolor y generar progreso."

    return f"{base}\n\nINSTRUCCIÓN: {instruccion}"

def generar_y_escanear_vivo(mensaje, contexto, prompt, contenedor_estado, rol_fijo):
    mensaje_completo = f"[Contexto: {contexto}]\n\n{mensaje}"
    if rol_fijo != "PANEL DE EXPERTOS":
        contenedor_estado.markdown(f'<p class="indicador-activo">Hablando: {rol_fijo}</p>', unsafe_allow_html=True)

    try:
        url_local = "http://localhost:11434/api/chat"
        payload = {"model": "llama3", "messages": [{"role": "system", "content": prompt}, {"role": "user", "content": mensaje_completo}], "stream": True}
        respuesta = requests.post(url_local, json=payload, stream=True, timeout=60)
        respuesta.raise_for_status() 
        
        for linea in respuesta.iter_lines():
            if linea:
                datos = json.loads(linea)
                if 'message' in datos and 'content' in datos['message']:
                    fragmento = datos['message']['content']
                    if rol_fijo == "PANEL DE EXPERTOS":
                        if "[ESTRATEGA]" in fragmento.upper(): contenedor_estado.markdown('<p class="indicador-activo">Hablando: 🧠 EL ESTRATEGA</p>', unsafe_allow_html=True)
                        elif "[ANIMADOR]" in fragmento.upper(): contenedor_estado.markdown('<p class="indicador-activo">Hablando: ✨ EL ANIMADOR</p>', unsafe_allow_html=True)
                        elif "[VIGIA]" in fragmento.upper() or "[VIGÍA]" in fragmento.upper(): contenedor_estado.markdown('<p class="indicador-activo">Hablando: 👁️ EL VIGÍA</p>', unsafe_allow_html=True)
                        elif "[CONSTRUCTOR]" in fragmento.upper(): contenedor_estado.markdown('<p class="indicador-activo">Hablando: 🛠️ EL CONSTRUCTOR</p>', unsafe_allow_html=True)
                    yield fragmento

    except Exception:
        respuesta_google = modelo_respaldo.generate_content(f"{prompt}\n\n{mensaje_completo}", stream=True)
        for fragmento in respuesta_google:
            texto = fragmento.text
            if rol_fijo == "PANEL DE EXPERTOS":
                if "[ESTRATEGA]" in texto.upper(): contenedor_estado.markdown('<p class="indicador-activo">Hablando: 🧠 EL ESTRATEGA</p>', unsafe_allow_html=True)
                elif "[ANIMADOR]" in texto.upper(): contenedor_estado.markdown('<p class="indicador-activo">Hablando: ✨ EL ANIMADOR</p>', unsafe_allow_html=True)
                elif "[VIGIA]" in texto.upper() or "[VIGÍA]" in texto.upper(): contenedor_estado.markdown('<p class="indicador-activo">Hablando: 👁️ EL VIGÍA</p>', unsafe_allow_html=True)
                elif "[CONSTRUCTOR]" in texto.upper(): contenedor_estado.markdown('<p class="indicador-activo">Hablando: 🛠️ EL CONSTRUCTOR</p>', unsafe_allow_html=True)
            yield texto

# =================================================================
# 6. ZONA DE LECTURA
# =================================================================
st.markdown('<p class="etiqueta-fuerte">💬 3. Zona de Resolución</p>', unsafe_allow_html=True)

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

mensaje_chat = st.chat_input("Micrófono abierto: intervenga o guíe a los expertos...")
texto_a_procesar = comando_automatico or mensaje_chat

if texto_a_procesar:
    if not comando_automatico:
        rol_seleccionado = "PANEL DE EXPERTOS"

    st.session_state.mensajes.append({"role": "user", "content": texto_a_procesar if not comando_automatico else f"*(Acción: Da la palabra a {rol_seleccionado})*"})
    with st.chat_message("user"):
        st.markdown(texto_a_procesar if not comando_automatico else f"*(Acción: Da la palabra a {rol_seleccionado})*")
    
    prompt_armado = configurar_prompt(rol_seleccionado)
    with st.chat_message("assistant"):
        respuesta_completa = st.write_stream(generar_y_escanear_vivo(texto_a_procesar, desafio, prompt_armado, espacio_estado, rol_seleccionado))
    
    st.session_state.mensajes.append({"role": "assistant", "content": respuesta_completa})
    espacio_estado.markdown('<p class="indicador-activo">Sesión en pausa. Esperando directiva...</p>', unsafe_allow_html=True)