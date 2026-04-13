import streamlit as st
from datetime import date
import time
import random

# 1. SEGURIDAD: CANDADO DE SOBERANÍA
FECHA_LIMITE = date(2026, 4, 20)
if date.today() > FECHA_LIMITE:
    st.error("⚠️ El período de prueba de 7 días ha finalizado. Contacte al Prof. Enrique Conte Mac Donell.")
    st.stop()

# 2. CONFIGURACIÓN Y MAJESTUOSIDAD VISUAL (CSS PERSONALIZADO)
st.set_page_config(page_title="SOLUCIÓN", layout="wide")

st.markdown("""
    <style>
    .main h1 { font-size: 4.5rem !important; color: #1E1E1E !important; text-align: center; font-weight: 800; margin-bottom: 0px; }
    .sub1 { font-size: 2.2rem !important; color: #333 !important; text-align: center; font-weight: 600; margin-top: 0px; }
    .sub2 { font-size: 2.2rem !important; color: #555 !important; text-align: center; font-style: italic; margin-bottom: 40px; }
    
    .stTextArea textarea {
        font-size: 1.8rem !important;
        line-height: 1.6 !important;
        color: #000 !important;
        font-family: 'Georgia', serif !important;
        background-color: #fcfcfc !important;
        border: 2px solid #ddd !important;
    }
    
    .expert-box { text-align: center; padding: 20px; border-radius: 15px; background: #f0f2f6; border: 1px solid #ccc; }
    .expert-symbol { font-size: 5rem; margin-bottom: 10px; }
    .expert-name { font-size: 1.8rem; font-weight: bold; color: #1E1E1E; }
    
    .dialogue-box { 
        background-color: #FFF9C4; 
        padding: 20px; 
        border-left: 10px solid #FBC02D; 
        font-size: 1.5rem; 
        font-weight: bold;
        margin: 20px 0;
    }
    
    .user-batuta {
        background-color: #E3F2FD;
        border: 2px solid #2196F3;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIALIZACIÓN DE MEMORIA (EL BÚNKER)
if 'verificado' not in st.session_state: st.session_state['verificado'] = False
if 'mesa_activa' not in st.session_state: st.session_state['mesa_activa'] = False
if 'historial_sintesis' not in st.session_state: st.session_state['historial_sintesis'] = []
if 'hablando_ahora' not in st.session_state: st.session_state['hablando_ahora'] = "Esperando inicio..."

# 4. BARRA LATERAL: SOBERANÍA Y PROYECCIÓN
with st.sidebar:
    st.markdown("## 👑 SOBERANÍA")
    st.write("Motor: **Llama3 (Independiente)**")
    st.divider()
    st.markdown("### 🚀 PROYECCIÓN A FUTURO")
    st.info("Fase 2: Conexión Global 🌐")
    st.info("Fase 3: Memoria Histórica 🧠")
    st.info("Fase 4: Interfaz de Voz 🎙️")
    st.divider()
    clave = st.text_input("🔑 Clave de Acceso:", type="password")
    if st.button("VALIDAR JERARQUÍA"):
        if clave == "LHEROES-7D":
            st.session_state['verificado'] = True
            st.rerun()
        else: st.error("Acceso Denegado")

# 5. ENCABEZADO REAL
st.markdown("<h1>SOLUCIÓN</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub1'>Arquitectura de Cuatro Expertos de Élite</p>", unsafe_allow_html=True)
st.markdown("<p class='sub2'>Para el ámbito Personal, Social/Comunitario y Comercial</p>", unsafe_allow_html=True)

if not st.session_state['verificado']:
    st.warning("👈 Por favor, valide su acceso en la barra lateral para convocar a la mesa.")
    st.stop()

# 6. EL DESAFÍO (EL DOLOR)
dolor = st.text_area("Vuelque aquí su Pensamiento o Desafío Estratégico:", height=250)

col_fijar, col_auto = st.columns([2, 1])
with col_fijar:
    btn_fijar = st.button("🚀 FIJAR DESAFÍO Y CONVOCAR MESA DE EXPERTOS", use_container_width=True)
with col_auto:
    modo_auto = st.toggle("🤖 Modo Diálogo Automático")

if btn_fijar:
    if dolor.strip(): st.session_state['mesa_activa'] = True
    else: st.warning("Debe describir el desafío para comenzar.")

st.divider()

# 7. MESA DE EXPERTOS Y DIÁLOGO ACTIVO
if st.session_state['mesa_activa']:
    # Caja Amarilla de Diálogo (Derecha/Arriba)
    st.markdown(f"""<div class='dialogue-box'>🗣️ EN DIÁLOGO: {st.session_state['hablando_ahora']}</div>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='expert-box'><div class='expert-symbol'>🧠</div><div class='expert-name'>ESTRATEGA</div></div>", unsafe_allow_html=True)
        if st.button("La palabra al ESTRATEGA"):
            with st.status("El Triatleta está corriendo..."):
                st.session_state['hablando_ahora'] = "ESTRATEGA (Analizando ruta crítica)"
                time.sleep(2)
            st.info("### Propuesta Estratégica:\nEl plan de acción está trazado sobre bases sólidas.")

    with col2:
        st.markdown("<div class='expert-box'><div class='expert-symbol'>👁️</div><div class='expert-name'>VIGÍA</div></div>", unsafe_allow_html=True)
        if st.button("La palabra al VIGÍA"):
            with st.status("El Triatleta está nadando..."):
                st.session_state['hablando_ahora'] = "VIGÍA (Supervisando coherencia)"
                time.sleep(2)
            st.warning("### Informe del Vigía:\nSe han blindado los riesgos y la coherencia sistémica.")

    with col3:
        st.markdown("<div class='expert-box'><div class='expert-symbol'>☀️</div><div class='expert-name'>ANIMADOR</div></div>", unsafe_allow_html=True)
        if st.button("La palabra al ANIMADOR"):
            with st.status("El Triatleta en bicicleta..."):
                st.session_state['hablando_ahora'] = "ANIMADOR (Infundiendo propósito)"
                time.sleep(2)
            st.success("### Visión del Animador:\nEl tono humano y la energía vital han sido integrados.")

    # MODO AUTOMÁTICO (DIÁLOGO ORGÁNICO)
    if modo_auto and st.button("🔥 INICIAR DELIBERACIÓN AUTOMÁTICA"):
        expertos = ["ESTRATEGA", "VIGÍA", "ANIMADOR"]
        for _ in range(4): # Simula 4 intervenciones aleatorias
            exp = random.choice(expertos)
            st.session_state['hablando_ahora'] = f"{exp} interviniendo..."
            with st.status(f"Mesa en sesión: {exp} hablando"):
                time.sleep(1.5)
        st.session_state['hablando_ahora'] = "SÍNTESIS MAESTRA en proceso..."

    st.divider()

    # 8. LA BATUTA DEL DIRECTOR (INTERVENCIÓN DEL USUARIO)
    st.markdown("### 🪄 LA BATUTA DEL DIRECTOR")
    intervencion = st.text_input("Su intervención en la mesa (Pregunte, corrija o amplíe):", placeholder="Escriba aquí su comando de voz o texto...")
    if intervencion:
        st.markdown(f"<div class='user-batuta'><b>Director:</b> {intervencion}</div>", unsafe_allow_html=True)

    st.divider()

    # 9. CUARTO EXPERTO: SÍNTESIS MAESTRA (EL CONSTRUCTOR)
    st.markdown("<div style='text-align: center;'><div style='font-size: 6rem;'>🏆</div><h2>SÍNTESIS MAESTRA</h2></div>", unsafe_allow_html=True)
    if st.button("🔨 FORJAR REDACCIÓN FINAL", type="primary", use_container_width=True):
        resultado = f"SÍNTESIS FINAL ({date.today()}): El desafío '{dolor[:30]}...' ha sido resuelto mediante soberanía tecnológica."
        st.session_state['historial_sintesis'].append(resultado)
        st.write(resultado)

    # 10. BITÁCORA DE SÍNTESIS (MEMORIA)
    if st.session_state['historial_sintesis']:
        with st.expander("📚 BITÁCORA DE SÍNTESIS (Historial guardado)"):
            for s in st.session_state['historial_sintesis']:
                st.write(s)
                st.divider()
