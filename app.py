import streamlit as st
from datetime import date

# 1. SEGURIDAD: CANDADO DE 7 DÍAS (20 de abril de 2026)
FECHA_LIMITE = date(2026, 4, 20)
if date.today() > FECHA_LIMITE:
    st.error("⚠️ El período de prueba de 7 días ha finalizado.")
    st.stop()

# 2. CONFIGURACIÓN Y MAJESTUOSIDAD VISUAL (CSS)
st.set_page_config(page_title="SOLUCIÓN", layout="wide")

st.markdown("""
    <style>
    .main h1 { font-size: 3.8rem !important; color: #1E1E1E !important; text-align: center; font-weight: 800; margin-bottom: 0px; }
    .main h3 { font-size: 1.8rem !important; color: #4A4A4A !important; text-align: center; margin-bottom: 30px; }
    .stTextArea textarea {
        font-size: 1.65rem !important;
        line-height: 1.6 !important;
        color: #000000 !important;
        font-family: 'Georgia', serif !important;
        background-color: #fcfcfc !important;
    }
    .stTextArea label { font-size: 1.4rem !important; font-weight: bold !important; color: #1E1E1E !important; }
    div[data-testid="stExpander"] { font-size: 1.2rem !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. ESTADO DE LA SESIÓN
if 'verificado' not in st.session_state: st.session_state['verificado'] = False
if 'mesa_activa' not in st.session_state: st.session_state['mesa_activa'] = False

# 4. BARRA LATERAL (SOBERANÍA Y PROYECCIÓN FUTURA)
with st.sidebar:
    st.markdown("## 👑 Soberanía")
    st.write("Motor: **Llama3 (Independiente)**")
    st.divider()
    
    st.markdown("### 🚀 Próximas Fases")
    st.info("Fase 2: Conexión Global 🌐")
    st.info("Fase 3: Memoria Histórica 🧠")
    st.info("Fase 4: Interfaz de Voz 🎙️")
    st.divider()
    
    clave_ingresada = st.text_input("🔑 Clave de Acceso:", type="password")
    if st.button("Validar Entrada"):
        if clave_ingresada == "LHEROES-7D":
            st.session_state['verificado'] = True
            st.rerun()
        else:
            st.error("Acceso denegado")

# 5. CUERPO PRINCIPAL
st.title("SOLUCIÓN")
st.subheader("Arquitectura de Cuatro Expertos de Élite")

if not st.session_state['verificado']:
    st.warning("👈 Por favor, valide su jerarquía de acceso en la barra lateral.")
    st.stop()

# ÁREA DEL PENSAMIENTO
dolor = st.text_area("Vuelque aquí su Pensamiento o Desafío Estratégico:", height=280)

if st.button("🚀 FIJAR DESAFÍO Y CONVOCAR MESA", use_container_width=True):
    if dolor.strip():
        st.session_state['mesa_activa'] = True
    else:
        st.warning("Debe escribir su desafío primero.")

st.divider()

# 6. PANEL DE EXPERTOS
if st.session_state['mesa_activa']:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🧠 ESTRATEGA", use_container_width=True):
            st.info("### El Estratega:\nAnalizando la arquitectura de su solución...")
    with col2:
        if st.button("👁️ VIGÍA", use_container_width=True):
            st.warning("### El Vigía:\nBlindando la coherencia y el riesgo...")
    with col3:
        if st.button("✨ ANIMADOR", use_container_width=True):
            st.success("### El Animador:\nInfundiendo propósito y tono humano...")
    
    st.divider()
    if st.button("🔥 TRABAJO EN CONJUNTO (SÍNTESIS MAESTRA)", type="primary", use_container_width=True):
        st.success("### 🏆 SÍNTESIS FINAL DEL CONSTRUCTOR\nSu Prompt Maestro de Soberanía Tecnológica ha sido forjado con éxito.")
