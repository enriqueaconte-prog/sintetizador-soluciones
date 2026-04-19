import streamlit as st
import google.generativeai as genai
import PyPDF2
import docx
import re
from datetime import datetime

# =========================================================
# 1. IDENTIDAD VISUAL Y SOBERANÍA TIPOGRÁFICA
# =========================================================
st.set_page_config(page_title="SOLUCIÓN", layout="wide", initial_sidebar_state="expanded")

# --- LLAVE DE ENERGÍA ---
LLAVE_GOOGLE_DIRECTOR = "AIzaSyCnDEMYn-fnoAy3STKS9bjIo5nJj5nc35c"

# --- BÓVEDA DE CORTESÍA ---
BOVEDA_VIP = {
    "LHEROES-7D": {"nombre": "España - Learning Heroes", "vence": datetime(2026, 4, 26)},
}

# --- CSS: EL TÉRMINO MEDIO PERFECTO CON REALCE DE ETIQUETAS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@400;700&display=swap');
    
    .stApp { background-color: #fafaf8; }

    /* Títulos Principales */
    .main-title { 
        font-family: 'Playfair Display', serif !important; 
        color: #1a237e; 
        text-align: center; 
        font-size: 3.8rem !important; 
        margin-top: -40px;
        margin-bottom: 5px;
    }
    .resaltado-sub { 
        font-family: 'Lato', sans-serif !important; 
        color: #1a237e; 
        text-align: center; 
        font-size: 1.25rem !important; 
        background-color: #fcf3cf; 
        padding: 10px 20px; 
        border-radius: 8px; 
        width: fit-content; 
        margin: 0 auto 30px auto;
        border-bottom: 3px solid #b8860b;
        font-weight: bold;
    }
    
    /* REALCE DE ETIQUETAS (Texto minúsculo corregido definitivamente) */
    .stTextArea label, .stTextArea label p, 
    .stFileUploader label, .stFileUploader label p, 
    .stSelectbox label, .stSelectbox label p {
        font-size: 1.25rem !important;
        font-weight: bold !important;
        color: #1a237e !important;
        font-family: 'Lato', sans-serif !important;
    }

    /* ZONA DE PROTAGONISMO: El Desafío y las Respuestas */
    .stTextArea textarea { font-size: 1.25rem !important; line-height: 1.5; font-family: 'Lato', sans-serif !important; }
    div[data-testid="stChatMessageContent"] p { font-size: 1.25rem !important; line-height: 1.6; color: #1a237e; font-family: 'Lato', sans-serif !important; }
    
    /* BARRA LATERAL Y MANUAL: El término medio exacto */
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] li { 
        font-size: 1.15rem !important; 
        line-height: 1.5; 
        color: #1a237e; 
        font-family: 'Lato', sans-serif !important;
    }

    /* Tarjetas de Expertos */
    .expert-card { 
        border: 2px solid #b8860b; 
        padding: 20px; 
        border-radius: 15px; 
        background: white; 
        text-align: center; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        height: 100%;
    }
    .expert-icon { font-size: 3rem !important; margin-bottom: 10px; }
    .expert-title { font-family: 'Playfair Display', serif !important; font-size: 1.5rem !important; font-weight: bold; color: #1a237e; }
    .expert-desc { font-family: 'Lato', sans-serif !important; font-size: 1rem !important; color: #555; }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# 2. COLUMNA IZQUIERDA: PORTAL DEL DIRECTOR Y HOJA DE RUTA
# =========================================================
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; margin-bottom: 15px;'>
            <span style='font-size: 3.5rem;'>🏰</span><br>
            <span style='font-family: "Playfair Display", serif; font-size: 1.8rem; font-weight: bold; color: #1a237e;'>Portal del Director</span>
        </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    st.markdown("### Próximas fases:")
    st.markdown("🌐 **Fase 2:** Conexión Global")
    st.markdown("🧠 **Fase 3:** Memoria de Largo Plazo")
    st.markdown("🎙️ **Fase 4:** Interfaz de Voz")
    st.divider()
    
    st.markdown("### 📖 Manual de Usuario")
    with st.expander("Instrucciones de Excelencia"):
        st.write("**1. Redacción del Desafío:**")
        st.write("Para un análisis de élite, procure que su descripción sea detallada y rica en contexto.")
        st.write("**2. Respaldo Documental:**")
        st.write("Adjunte archivos PDF o Word si desea que los expertos consideren datos técnicos.")
        st.write("**3. Ejecución:**")
        st.write("Seleccione al experto y autorice su intervención.")

# =========================================================
# 3. CONTROL DE ACCESO
# =========================================================
if 'auth' not in st.session_state: st.session_state.auth = False
if 'api_key_ok' not in st.session_state: st.session_state.api_key_ok = ""
if "messages" not in st.session_state: st.session_state.messages = []

id_url = st.query_params.get("id", "").upper()

if not st.session_state.auth:
    st.markdown("<div class='main-title'>SOLUCIÓN</div>", unsafe_allow_html=True)
    st.markdown("<div class='resaltado-sub'>Una mesa de expertos para resolver tus desafíos</div>", unsafe_allow_html=True)
    
    _, col_login, _ = st.columns([1, 1.5, 1])
    with col_login:
        st.markdown("<div class='expert-card'>", unsafe_allow_html=True)
        if id_url in BOVEDA_VIP and datetime.now() < BOVEDA_VIP[id_url]["vence"]:
            st.success(f"Acceso Autorizado: {BOVEDA_VIP[id_url]['nombre']}")
            if st.button("INGRESAR A LA MESA", use_container_width=True):
                st.session_state.auth = True
                st.session_state.api_key_ok = LLAVE_GOOGLE_DIRECTOR
                st.rerun()
        else:
            clave = st.text_input("Identificador de Acceso:", type="password")
            if st.button("VALIDAR", use_container_width=True):
                if clave.upper() in BOVEDA_VIP and datetime.now() < BOVEDA_VIP[clave.upper()]["vence"]:
                    st.session_state.auth = True
                    st.session_state.api_key_ok = LLAVE_GOOGLE_DIRECTOR
                    st.rerun()
                else:
                    st.error("Credencial inválida.")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# =========================================================
# 4. ESCÁNER IMPLACABLE DE MOTORES
# =========================================================
try:
    genai.configure(api_key=st.session_state.api_key_ok)
    motores = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    motor_final = None
    for pref in ['gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-1.0-pro']:
        for m in motores:
            if pref in m:
                motor_final = m
                break
        if motor_final: break
    
    if not motor_final and motores: motor_final = motores[0]
    model = genai.GenerativeModel(motor_final)
except Exception as e:
    st.error("Error en la conexión con Google AI. Verifique su Llave de Energía.")
    st.stop()

# =========================================================
# 5. EL SALÓN DE LOS EXPERTOS
# =========================================================
st.markdown("<div class='main-title'>SOLUCIÓN</div>", unsafe_allow_html=True)
st.markdown("<div class='resaltado-sub'>Una mesa de expertos para resolver tus desafíos</div>", unsafe_allow_html=True)

col_e1, col_e2, col_e3, col_e4 = st.columns(4)
config_expertos = [
    ("🧠", "El Estratega", "Arquitectura y visión de conjunto."),
    ("🚨", "El Vigía", "Detección de riesgos y blindaje."),
    ("❤️", "El Animador", "Impacto humano y comunicación."),
    ("🏛️", "El Constructor", "Cierre, veredicto y síntesis.")
]

for col, (icon, name, desc) in zip([col_e1, col_e2, col_e3, col_e4], config_expertos):
    with col:
        st.markdown(f"""<div class='expert-card'>
        <div class='expert-icon'>{icon}</div>
        <div class='expert-title'>{name}</div>
        <div class='expert-desc'>{desc}</div>
        </div>""", unsafe_allow_html=True)

# =========================================================
# 6. PANEL DE TRABAJO (CON ETIQUETAS REALZADAS)
# =========================================================
st.divider()
desafio = st.text_area("Describa su situación estratégica:", height=200, placeholder="Redacte aquí su directiva...")
archivo = st.file_uploader("Respaldo Documental (Opcional):", type=['pdf', 'docx'])

st.markdown("### Ceder la Palabra")
col_sel, col_btn = st.columns([3, 1])

with col_sel:
    rol = st.selectbox("Seleccione quién debe intervenir en esta fase:", ["El Estratega", "El Vigía", "El Animador", "El Constructor"])
with col_btn:
    st.write("")
    if st.button("ORDENAR INTERVENCIÓN", type="primary", use_container_width=True):
        if desafio:
            txt_doc = ""
            if archivo:
                if archivo.name.endswith('.pdf'):
                    reader = PyPDF2.PdfReader(archivo)
                    txt_doc = "".join(p.extract_text() for p in reader.pages)
                else:
                    doc = docx.Document(archivo)
                    txt_doc = "".join(p.text + "\n" for p in doc.paragraphs)

            prompt_maestro = f"""
            DIRECTIVA ÉTICA: Eres un consultor de élite. Tu respuesta debe ser profunda, honesta y ética.
            REGLA DE ORO: Tienes terminantemente PROHIBIDO repetir o resumir el problema del usuario. 
            Entra DIRECTAMENTE al análisis crítico y a las propuestas de solución.
            TU ROL ACTUAL: {rol}
            SITUACIÓN: {desafio}
            DOCS: {txt_doc}
            """
            
            st.session_state.messages.append({"role": "Director", "content": desafio})
            with st.spinner(f"{rol} está analizando el escenario..."):
                try:
                    response = model.generate_content(prompt_maestro)
                    st.session_state.messages.append({"role": rol, "content": response.text})
                    st.rerun()
                except Exception as e:
                    st.error(f"Interrupción técnica: {str(e)}")
        else:
            st.warning("Escriba su desafío antes de solicitar la intervención.")

# DIÁLOGO DE LA MESA
st.divider()
for m in st.session_state.messages:
    if m["role"] == "Director":
        st.markdown(f"**👑 {m['role']}:** {m['content']}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"**🏛️ {m['role']}:**\n{m['content']}")