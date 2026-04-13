import streamlit as st
from datetime import date

# --- CLÁUSULA DE SEGURIDAD: PERÍODO DE PRUEBA ---
# El sistema se bloqueará automáticamente después de esta fecha
FECHA_LIMITE = date(2026, 4, 20) 

if date.today() > FECHA_LIMITE:
    st.error("⚠️ El período de prueba de 7 días ha finalizado.")
    st.info("Para renovar el acceso o adquirir la licencia permanente, contacte a Enrique Conte Mac Donell.")
    st.stop() 
# -----------------------------------------------

import streamlit as st
import time
from datetime import datetime
import requests

# ==========================================
# 1. MOTOR SOBERANO (CONFIGURACIÓN)
# ==========================================
MODELO_LOCAL = "llama3"

def llamar_experto_local(perfil, problema, historial):
    """Comunicación privada con el cerebro local y memoria compartida"""
    url = "http://localhost:11434/api/generate"
    
    # Construcción de la mesa redonda (Memoria)
    memoria_contexto = ""
    if historial:
        memoria_contexto = "\n\n--- REGISTRO DE LA MESA DE EXPERTOS ---\n"
        for msg in historial:
            memoria_contexto += f"{msg['nombre']}: {msg['texto']}\n"
        memoria_contexto += "--------------------------------------\n"
        memoria_contexto += "INSTRUCCIÓN: Evalúa los argumentos anteriores y responde desde tu especialidad."

    prompt_final = f"{perfil}\n\nDESAFÍO ACTUAL: {problema}{memoria_contexto}"
    
    payload = {
        "model": MODELO_LOCAL,
        "prompt": prompt_final,
        "stream": False
    }
    
    try:
        respuesta = requests.post(url, json=payload)
        if respuesta.status_code == 200:
            return respuesta.json().get("response", "")
        else:
            return "⚠️ El motor está procesando otra orden. Reintente en un instante."
    except:
        return "⚠️ Error de conexión: Asegúrese de que Ollama esté encendido."

# ==========================================
# 2. ARQUITECTURA VISUAL (REALEZA Y PODER)
# ==========================================
st.set_page_config(page_title="Solución", layout="wide", initial_sidebar_state="expanded")

# CSS para Presencia Imponente y Simetría Absoluta
st.markdown("""
    <style>
    /* Tipografía Masiva y Títulos Reales */
    .titulo-principal {
        font-size: 85px !important;
        font-weight: 900 !important;
        color: #1a2a6c; /* Azul Profundo de Autoridad */
        margin-bottom: 0px;
        text-align: left;
    }
    .subtitulo-royal {
        font-size: 32px !important;
        font-weight: 700 !important;
        color: #b8860b; /* Oro Viejo / Realeza */
        margin-top: -10px;
    }
    .descripcion-universal {
        font-size: 22px !important;
        font-style: italic;
        color: #444;
        margin-bottom: 30px;
    }
    
    /* Caja de Desafío (Resaltado del Dolor) */
    .stTextArea textarea {
        font-size: 20px !important;
        border: 2px solid #1a2a6c !important;
        border-radius: 12px !important;
    }
    
    /* Pizarra Dinámica (Status Box) */
    .pizarra-viva {
        background-color: #fdf2d0;
        border: 3px solid #d4af37;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 26px !important;
        font-weight: bold;
        color: #856404;
        margin-bottom: 25px;
    }

    /* Botones de Expertos (Simetría de Director) */
    div.stButton > button {
        height: 70px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: 2px solid #1a2a6c !important;
    }
    
    /* Botón del Constructor (Diferenciado) */
    .stButton button[kind="primary"] {
        background-color: #1a2a6c !important;
        color: white !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Memoria de Sesión
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "historial" not in st.session_state:
    st.session_state.historial = []
if "problema" not in st.session_state:
    st.session_state.problema = ""

# Códigos de Acceso Institucional
CODIGOS = {"LHEROES-7D": "2026-04-20", "EDUCACION-AR": "2026-12-31", "SABIO-PRO": "2030-01-01"}

def pantalla_login():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align:center;'>🛡️ Acceso Institucional</h1>", unsafe_allow_html=True)
        codigo = st.text_input("Ingrese su Código de Autoridad:", type="password")
        if st.button("Activar Solución", use_container_width=True):
            if codigo in CODIGOS:
                st.session_state.autenticado = True
                st.rerun()

# ==========================================
# 3. INTERFAZ DE SOLUCIÓN (MODO DIRECTOR)
# ==========================================
if not st.session_state.autenticado:
    pantalla_login()
else:
    with st.sidebar:
        st.markdown("### 🚀 Próximas Fases")
        st.caption(f"🧠 Motor Soberano: {MODELO_LOCAL}")
        st.markdown("---")
        st.toggle("🌐 Fase 2: Mundo", disabled=True)
        st.toggle("🧠 Fase 3: Memoria", disabled=True)
        st.toggle("🎙️ Fase 4: Voz", disabled=True)
        st.markdown("---")
        if st.button("🗑️ Reiniciar Sesión"):
            st.session_state.historial = []
            st.session_state.problema = ""
            st.rerun()

    # Títulos con Presencia Universal
    st.markdown('<p class="titulo-principal">Solución</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo-royal">El recurso definitivo para la resolución de problemas.</p>', unsafe_allow_html=True)
    st.markdown('<p class="descripcion-universal">Una mesa de expertos para sus decisiones vitales, institucionales y comerciales.</p>', unsafe_allow_html=True)
    
    st.markdown("---")

    # Entrada del Desafío
    desafio_input = st.text_area("Describa aquí la situación o el conflicto a resolver:", 
                                 value=st.session_state.problema, height=150)
    
    if st.button("Fijar Desafío y Convocar Mesa", type="primary"):
        st.session_state.problema = desafio_input
        st.rerun()

    if st.session_state.problema:
        st.markdown("### ⚙️ Panel de Dirección")
        st.caption("Usted es el Director. Ceda la palabra a sus expertos. Ellos se escuchan y responden entre sí.")
        
        # Pizarra Dinámica (La Pizarra Viva)
        pizarra = st.empty()
        pizarra.markdown('<div class="pizarra-viva">Estado: Mesa lista. Esperando su directiva...</div>', unsafe_allow_html=True)

        def ceder_palabra(perfil, nombre, frase_pizarra):
            pizarra.markdown(f'<div class="pizarra-viva">⏳ {nombre}: "{frase_pizarra}"</div>', unsafe_allow_html=True)
            respuesta = llamar_experto_local(perfil, st.session_state.problema, st.session_state.historial)
            st.session_state.historial.append({"nombre": nombre, "texto": respuesta})
            st.rerun()

        # Botones Simétricos de Expertos
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("🧠 Ceder al ESTRATEGA", use_container_width=True):
                ceder_palabra("Eres El Estratega. Analiza el problema y propone un plan de acción frío y efectivo.", 
                              "EL ESTRATEGA", "Diseñando la arquitectura del plan...")
        with c2:
            if st.button("👁️ Ceder al VIGÍA", use_container_width=True):
                ceder_palabra("Eres El Vigía. Detecta riesgos ocultos y puntos débiles en las ideas planteadas.", 
                              "EL VIGÍA", "Identificando barreras y riesgos críticos...")
        with c3:
            if st.button("✨ Ceder al ANIMADOR", use_container_width=True):
                ceder_palabra("Eres El Animador. Enfócate en el factor humano, la motivación y la empatía.", 
                              "EL ANIMADOR", "Equilibrando el impacto emocional...")

        st.markdown("<br>", unsafe_allow_html=True)

        # Botón de Cierre (EL CONSTRUCTOR)
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            if st.button("🛠️ SÍNTESIS FINAL (CONSTRUCTOR)", type="primary", use_container_width=True):
                ceder_palabra("Eres El Constructor. Resume todo el debate y redacta un veredicto final con excelencia y síntesis.", 
                              "EL CONSTRUCTOR", "Redactando el documento de solución definitiva...")

        st.divider()
        
        # Área de Lectura (Limpia y Amplia)
        for m in st.session_state.historial:
            with st.chat_message("assistant"):
                st.markdown(f"### {m['nombre']}")
                st.write(m['texto'])