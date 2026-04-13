import streamlit as st
from datetime import date
import time
import random

# ==========================================
# 1. SEGURIDAD Y CANDADO DE SOBERANÍA
# ==========================================
FECHA_LIMITE = date(2026, 4, 20)
if date.today() > FECHA_LIMITE:
    st.error("⚠️ Acceso finalizado. Contacte al Prof. Enrique Conte Mac Donell.")
    st.stop()

# ==========================================
# 2. MAJESTUOSIDAD VISUAL (CSS PERSONALIZADO)
# ==========================================
st.set_page_config(page_title="SOLUCIÓN", layout="wide")

st.markdown("""
    <style>
    /* Tipografía Principal */
    .main h1 { font-size: 4.5rem !important; color: #1E1E1E !important; text-align: center; font-weight: 900; margin-bottom: 0px; }
    .sub1 { font-size: 2.2rem !important; color: #333 !important; text-align: center; font-weight: 600; margin-top: 0px; }
    .sub2 { font-size: 2rem !important; color: #555 !important; text-align: center; font-style: italic; margin-bottom: 30px; }
    
    /* Cuadro de Texto Principal (El Dolor) */
    .stTextArea textarea { font-size: 1.8rem !important; line-height: 1.6 !important; font-family: 'Georgia', serif !important; border: 2px solid #ccc !important; }
    
    /* Tarjetas de los Expertos */
    .expert-box { text-align: center; padding: 20px; border-radius: 15px; background: #f8f9fa; border: 2px solid #ddd; margin-bottom: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    .expert-symbol { font-size: 5rem; margin-bottom: 10px; }
    .expert-name { font-size: 2rem; font-weight: bold; color: #1E1E1E; }
    
    /* Caja Amarilla de Diálogo */
    .dialogue-box { background-color: #FFF9C4; padding: 20px; border-left: 10px solid #FBC02D; font-size: 1.6rem; font-weight: bold; margin: 20px 0; color: #333; }
    
    /* Caja de Mando Soberano (Automático) */
    .mando-box { background-color: #e8f5e9; padding: 25px; border-radius: 12px; border: 3px solid #4CAF50; text-align: center; margin-top: 20px; }
    .mando-text { font-size: 2rem; font-weight: bold; color: #2E7D32; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. MEMORIA DE SESIÓN (EL BÚNKER)
# ==========================================
if 'verificado' not in st.session_state: st.session_state['verificado'] = False
if 'mesa_activa' not in st.session_state: st.session_state['mesa_activa'] = False
if 'hablando' not in st.session_state: st.session_state['hablando'] = "Mesa en silencio. Esperando convocatoria."
if 'respuestas' not in st.session_state: 
    st.session_state['respuestas'] = {"ESTRATEGA": "", "VIGÍA": "", "ANIMADOR": "", "SÍNTESIS": ""}

# ==========================================
# 4. BARRA LATERAL (PROYECCIÓN)
# ==========================================
with st.sidebar:
    st.markdown("## 👑 SOBERANÍA")
    st.divider()
    st.markdown("### 🚀 PROYECCIÓN")
    st.info("Fase 2: Conexión Global 🌐\n\nFase 3: Memoria Histórica 🧠\n\nFase 4: Interfaz de Voz 🎙️")
    st.divider()
    clave = st.text_input("🔑 Clave de Acceso:", type="password")
    if st.button("VALIDAR JERARQUÍA"):
        if clave == "LHEROES-7D":
            st.session_state['verificado'] = True
            st.rerun()

# ==========================================
# 5. ENCABEZADO REAL
# ==========================================
st.markdown("<h1>SOLUCIÓN</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub1'>Arquitectura de Cuatro Expertos de Élite</p>", unsafe_allow_html=True)
st.markdown("<p class='sub2'>Para el ámbito Personal, Social/Comunitario y Comercial</p>", unsafe_allow_html=True)

if not st.session_state['verificado']:
    st.warning("👈 Valide su acceso en la barra lateral.")
    st.stop()

# ==========================================
# 6. EL DESAFÍO (EL DOLOR)
# ==========================================
dolor = st.text_area("Vuelque aquí su Pensamiento o Desafío Estratégico:", height=200)

if st.button("🚀 FIJAR DESAFÍO Y CONVOCAR MESA (Modo Manual)", use_container_width=True, type="primary"):
    if dolor.strip(): st.session_state['mesa_activa'] = True
    else: st.warning("Escriba el desafío primero.")

# CAJA DE MANDO SOBERANO (Modo Automático con Jerarquía)
st.markdown("""
<div class='mando-box'>
    <div class='mando-text'>ACTIVAR DELIBERACIÓN ORGÁNICA ENTRE EXPERTOS</div>
</div>
""", unsafe_allow_html=True)
if st.button("⚡ INICIAR MODO SOBERANO (Automático)", use_container_width=True):
    if dolor.strip():
        st.session_state['mesa_activa'] = True
        st.session_state['hablando'] = "INICIANDO DELIBERACIÓN ORGÁNICA..."
        # Simulación de carrera larga y llenado de respuestas
        with st.status("Los expertos están debatiendo...", expanded=True):
            st.write("El Estratega toma la palabra...")
            time.sleep(2)
            st.session_state['respuestas']['ESTRATEGA'] = f"**Análisis:** La situación requiere una intervención en 3 fases."
            
            st.write("El Vigía interviene...")
            time.sleep(2)
            st.session_state['respuestas']['VIGÍA'] = f"**Alerta:** Cuidado con el sesgo en la fase 2."
            
            st.write("El Animador equilibra...")
            time.sleep(2)
            st.session_state['respuestas']['ANIMADOR'] = f"**Impulso:** El equipo necesita contención emocional antes de avanzar."
        st.session_state['hablando'] = "Debate concluido. Respuestas ancladas."
        st.rerun()
    else:
        st.warning("Escriba el desafío primero.")

st.divider()

# ==========================================
# 7. MESA DE EXPERTOS (ANCLADOS)
# ==========================================
if st.session_state['mesa_activa']:
    st.markdown(f"<div class='dialogue-box'>🗣️ EN DIÁLOGO: {st.session_state['hablando']}</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='expert-box'><div class='expert-symbol'>🧠</div><div class='expert-name'>ESTRATEGA</div></div>", unsafe_allow_html=True)
        if st.button("Ceder al ESTRATEGA"):
            st.session_state['hablando'] = "ESTRATEGA trazando plan..."
            with st.status("El Triatleta corre (Estrategia)...", expanded=True):
                time.sleep(3) # Tiempo extendido
                st.session_state['respuestas']['ESTRATEGA'] = f"**Propuesta:** Para resolver '{dolor[:30]}...', he diseñado un esquema soberano inquebrantable."
            st.rerun()
        if st.session_state['respuestas']['ESTRATEGA']:
            st.info(st.session_state['respuestas']['ESTRATEGA'])

    with col2:
        st.markdown("<div class='expert-box'><div class='expert-symbol'>👁️</div><div class='expert-name'>VIGÍA</div></div>", unsafe_allow_html=True)
        if st.button("Ceder al VIGÍA"):
            st.session_state['hablando'] = "VIGÍA revisando riesgos..."
            with st.status("El Triatleta nada (Revisión)...", expanded=True):
                time.sleep(3)
                st.session_state['respuestas']['VIGÍA'] = "**Informe:** He blindado la propuesta contra inconsistencias lógicas y riesgos."
            st.rerun()
        if st.session_state['respuestas']['VIGÍA']:
            st.warning(st.session_state['respuestas']['VIGÍA'])

    with col3:
        st.markdown("<div class='expert-box'><div class='expert-symbol'>☀️</div><div class='expert-name'>ANIMADOR</div></div>", unsafe_allow_html=True)
        if st.button("Ceder al ANIMADOR"):
            st.session_state['hablando'] = "ANIMADOR integrando..."
            with st.status("El Triatleta pedalea (Impulso)...", expanded=True):
                time.sleep(3)
                st.session_state['respuestas']['ANIMADOR'] = "**Visión:** El tono humano ha sido calibrado para maximizar la recepción del mensaje."
            st.rerun()
        if st.session_state['respuestas']['ANIMADOR']:
            st.success(st.session_state['respuestas']['ANIMADOR'])

    st.divider()
    
    # ==========================================
    # 8. LA BATUTA DEL DIRECTOR
    # ==========================================
    st.markdown("### 🪄 LA BATUTA DEL DIRECTOR")
    intervencion = st.text_input("Intervenga en la mesa (Corrija o amplíe):", placeholder="Escriba aquí su comando...")
    if intervencion:
        st.markdown(f"<div style='background:#E3F2FD; padding:15px; border-radius:10px; font-size:1.4rem;'><b>Usted (Director):</b> {intervencion}</div>", unsafe_allow_html=True)

    st.divider()

    # ==========================================
    # 9. SÍNTESIS MAESTRA (EL CONSTRUCTOR)
    # ==========================================
    st.markdown("<div style='text-align: center;'><div style='font-size: 6rem;'>🏆</div><h2>SÍNTESIS MAESTRA</h2></div>", unsafe_allow_html=True)
    
    if st.button("🔨 FORJAR REDACCIÓN FINAL", type="primary", use_container_width=True):
        st.session_state['hablando'] = "CONSTRUCTOR forjando síntesis..."
        with st.status("El Triatleta llega a la meta...", expanded=True):
            time.sleep(4)
            st.session_state['respuestas']['SÍNTESIS'] = f"**SÍNTESIS FINAL ({date.today()}):**\n\nEl desafío ha sido procesado. La estrategia está lista para implementación comercial, social o personal."
        st.rerun()
    
    if st.session_state['respuestas']['SÍNTESIS']:
        st.markdown(f"<div style='background:#f4f4f4; padding:20px; border-left:5px solid #000; font-size:1.6rem;'>{st.session_state['respuestas']['SÍNTESIS']}</div>", unsafe_allow_html=True)
