import streamlit as st
from datetime import date

# 1. SEGURIDAD: CANDADO TEMPORAL (HASTA EL 20 DE ABRIL)
FECHA_LIMITE = date(2026, 4, 20)
if date.today() > FECHA_LIMITE:
    st.error("⚠️ El período de prueba ha finalizado. Contacte a Enrique Conte Mac Donell.")
    st.stop()

# 2. INICIALIZACIÓN DEL MOTOR
if 'mesa_activa' not in st.session_state:
    st.session_state['mesa_activa'] = False

# 3. DISEÑO Y ESTILOS (TU INTERFAZ LIMPIA)
st.set_page_config(page_title="SOLUCIÓN", layout="wide")

st.markdown("""
    <style>
    .expert-box { text-align: center; padding: 20px; border-radius: 15px; background: #f8f9fa; margin-bottom: 10px; }
    .expert-symbol { font-size: 3rem; }
    .expert-name { font-size: 1.5rem; font-weight: bold; color: #1E1E1E; }
    .dialogue-box { background-color: #FFF9C4; padding: 20px; border-left: 10px solid #FBC02D; }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL (SOBERANÍA)
with st.sidebar:
    st.markdown("## 👑 SOBERANÍA")
    st.divider()
    st.markdown("### 🚀 PROYECCIÓN")
    st.info("Fase 2: Conexión Global 🌐\n\nFase 3: Memoria Histórica 🧠\n\nFase 4: Interfaz de Voz 🎙️")
    st.divider()
    
    # VALIDACIÓN DE ACCESO
    st.subheader("🔑 Clave de Acceso")
    clave = st.text_input("Ingrese su clave:", type="password")
    if st.button("VALIDAR JERARQUÍA"):
        if clave in ["LHEROES-7D", "SABIO-PRO"]:
            st.success("Acceso Validado")
        else:
            st.error("Clave incorrecta")

# 5. CUERPO PRINCIPAL
st.title("SOLUCIÓN")
st.subheader("Arquitectura de Cuatro Expertos de Élite")

# FILTRO DE SEGURIDAD
if clave not in ["LHEROES-7D", "SABIO-PRO"]:
    st.warning("👉 Valide su acceso en la barra lateral para comenzar.")
    st.stop()

# INTERFAZ OPERATIVA
dolor = st.text_area("Describa aquí la situación o el conflicto a resolver:", height=150)

if st.button("🚀 FIJAR DESAFÍO Y CONVOCAR MESA"):
    if dolor.strip():
        st.session_state['mesa_activa'] = True
    else:
        st.warning("Por favor, describa el problema primero.")

st.divider()

if st.session_state['mesa_activa']:
    st.write("### ⚙️ Panel de Dirección Estratégica")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🧠 ESTRATEGA"):
            st.info(f"**Estratega:** Analizando ruta para: {dolor[:40]}...")
    with col2:
        if st.button("👁️ VIGÍA"):
            st.warning(f"**Vigía:** Supervisando riesgos en: {dolor[:40]}...")
    with col3:
        if st.button("✨ ANIMADOR"):
            st.success(f"**Animador:** Ajustando tono humano para: {dolor[:40]}...")

    st.divider()
    if st.button("🔥 TRABAJO EN CONJUNTO", type="primary", use_container_width=True):
        with st.spinner("Deliberando síntesis..."):
            st.write("✅ Visiones integradas.")
        st.success("### 🏆 SÍNTESIS FINAL (CONSTRUCTOR)")
        st.write("El **Prompt Maestro** ha sido generado.")