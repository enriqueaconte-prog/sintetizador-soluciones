import streamlit as st
from datetime import date

# 1. CLÁUSULA DE SEGURIDAD (CANDADO)
FECHA_LIMITE = date(2026, 4, 20)
if date.today() > FECHA_LIMITE:
    st.error("⚠️ El período de prueba de 7 días ha finalizado.")
    st.info("Para renovar el acceso, contacte a Enrique Conte Mac Donell.")
    st.stop()

# 2. INICIALIZACIÓN DEL ESTADO (EL MOTOR)
if 'mesa_activa' not in st.session_state:
    st.session_state['mesa_activa'] = False

# 3. INTERFAZ
st.set_page_config(page_title="SOLUCIÓN", layout="wide")
st.title("Solución")
st.subheader("Arquitectura de Cuatro Expertos")

dolor = st.text_area("Describa aquí la situación o el conflicto a resolver:", height=150)

if st.button("🚀 FIJAR DESAFÍO Y CONVOCAR MESA"):
    if dolor.strip():
        st.session_state['mesa_activa'] = True
    else:
        st.warning("Por favor, describa el problema antes de convocar a los expertos.")

st.divider()

# 4. PANEL DE LOS EXPERTOS (SOLO APARECE SI SE FIJA EL DESAFÍO)
if st.session_state['mesa_activa']:
    st.write("### ⚙️ Panel de Dirección Estratégica")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🧠 Ceder al ESTRATEGA"):
            st.info(f"**Estratega:** Analizando la ruta crítica para: {dolor[:50]}...")
            
    with col2:
        if st.button("👁️ Ceder al VIGÍA"):
            st.warning(f"**Vigía:** Supervisando riesgos en: {dolor[:50]}...")
            
    with col3:
        if st.button("✨ Ceder al ANIMADOR"):
            st.success(f"**Animador:** Ajustando el tono humano para: {dolor[:50]}...")

    st.divider()
    
    # EL BOTÓN DE AUTOMATIZACIÓN
    if st.button("🔥 TRABAJO EN CONJUNTO (Modo Automático)", type="primary", use_container_width=True):
        with st.spinner("Los expertos están deliberando en conjunto..."):
            st.write("✅ Estrategia definida.")
            st.write("✅ Coherencia validada.")
            st.write("✅ Tono humanizado.")
        st.success("### 🏆 SÍNTESIS FINAL (CONSTRUCTOR)")
        st.write("El Prompt Maestro ha sido generado con éxito.")
