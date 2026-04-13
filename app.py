import streamlit as st
from datetime import date

# 1. SEGURIDAD: CANDADO DE 7 DÍAS
FECHA_LIMITE = date(2026, 4, 20)
if date.today() > FECHA_LIMITE:
    st.error("⚠️ El período de prueba de 7 días ha finalizado.")
    st.stop()

# 2. BARRA LATERAL (SOBERANÍA)
st.set_page_config(page_title="SOLUCIÓN", layout="wide")
with st.sidebar:
    st.title("🚀 Próximas Fases")
    st.write("🧠 **Motor Soberano:** Llama3")
    st.divider()
    st.checkbox("Fase 2: Conexión al Mundo", disabled=True)
    st.checkbox("Fase 3: Memoria Histórica", disabled=True)
    st.checkbox("Fase 4: Interfaz de Voz", disabled=True)
    st.divider()
    clave = st.text_input("🔑 Ingrese Clave de Acceso:", type="password")
    if clave == "Heroes2026":
        st.success("Acceso Validado")
    else:
        st.caption("La clave activa el motor de los expertos.")

# 3. CUERPO PRINCIPAL
st.title("Solución")
st.subheader("Arquitectura de Cuatro Expertos")

if clave != "Heroes2026":
    st.warning("Por favor, valide su clave en la barra lateral para comenzar.")
    st.stop()

dolor = st.text_area("Describa aquí la situación o el conflicto a resolver:", height=150)

if st.button("🚀 FIJAR DESAFÍO Y CONVOCAR MESA"):
    st.session_state['mesa_activa'] = True

st.divider()

if st.session_state.get('mesa_activa'):
    st.write("### ⚙️ Panel de Dirección Estratégica")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🧠 Ceder al ESTRATEGA"):
            st.info("**Estratega:** Diseñando arquitectura...")
    with col2:
        if st.button("👁️ Ceder al VIGÍA"):
            st.warning("**Vigía:** Verificando coherencia...")
    with col3:
        if st.button("✨ Ceder al ANIMADOR"):
            st.success("**Animador:** Infundiendo propósito...")
    st.divider()
    if st.button("🔥 TRABAJO EN CONJUNTO (Modo Automático)", type="primary", use_container_width=True):
        with st.status("Deliberando..."):
            st.write("✅ Integrando visiones.")
        st.success("### 🏆 SÍNTESIS FINAL (CONSTRUCTOR)")
        st.write("El Prompt Maestro ha sido generado.")
