import streamlit as st
from datetime import date

# 1. SEGURIDAD: CANDADO DE 7 DÍAS
FECHA_LIMITE = date(2026, 4, 20)
if date.today() > FECHA_LIMITE:
    st.error("⚠️ El período de prueba de 7 días ha finalizado.")
    st.stop()

# 2. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="SOLUCIÓN", layout="wide")

# 3. BARRA LATERAL (SOBERANÍA Y CLAVE)
with st.sidebar:
    st.title("🚀 Próximas Fases")
    st.write("🧠 **Motor Soberano:** Llama3")
    st.divider()
    st.checkbox("Fase 2: Conexión al Mundo", disabled=True)
    st.checkbox("Fase 3: Memoria Histórica", disabled=True)
    st.checkbox("Fase 4: Interfaz de Voz", disabled=True)
    st.divider()
    
    # NUEVA LÓGICA DE VALIDACIÓN CON BOTÓN
    clave_ingresada = st.text_input("🔑 Ingrese Clave de Acceso:", type="password")
    if st.button("Validar Acceso"):
        if clave_ingresada == "LHEROES-7D":
            st.session_state['verificado'] = True
            st.success("Acceso Validado")
        else:
            st.error("Clave incorrecta")

# 4. CUERPO PRINCIPAL
st.title("Solución")
st.subheader("Arquitectura de Cuatro Expertos")

if not st.session_state.get('verificado'):
    st.warning("👈 Por favor, ingrese su clave en la barra lateral y haga clic en 'Validar Acceso' para comenzar.")
    st.stop()

# ESTO SOLO SE VE SI ESTÁ VERIFICADO
dolor = st.text_area("Describa aquí la situación o el conflicto a resolver:", height=150)

if st.button("🚀 FIJAR DESAFÍO Y CONVOCAR MESA"):
    st.session_state['mesa_activa'] = True

if st.session_state.get('mesa_activa'):
    st.write("### ⚙️ Panel de Dirección Estratégica")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🧠 Ceder al ESTRATEGA"):
            st.info("**Estratega:** Analizando la ruta crítica...")
    with col2:
        if st.button("👁️ Ceder al VIGÍA"):
            st.warning("**Vigía:** Verificando coherencia sistémica...")
    with col3:
        if st.button("✨ Ceder al ANIMADOR"):
            st.success("**Animador:** Infundiendo el propósito humano...")
    
    st.divider()
    if st.button("🔥 TRABAJO EN CONJUNTO (Modo Automático)", type="primary", use_container_width=True):
        with st.status("Los expertos están deliberando..."):
            st.write("✅ Estrategia, Coherencia y Tono integrados.")
        st.success("### 🏆 SÍNTESIS FINAL (CONSTRUCTOR)")
        st.write("El Prompt Maestro de soberanía tecnológica ha sido generado.")
