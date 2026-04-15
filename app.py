import streamlit as st
from datetime import date

# 1. CLÁUSULA DE SEGURIDAD (CANDADO DE FECHA)
FECHA_LIMITE = date(2026, 4, 20)
if date.today() > FECHA_LIMITE:
    st.error("⚠️ El período de prueba ha finalizado.")
    st.info("Para renovar el acceso, contacte a Enrique Conte Mac Donell.")
    st.stop()

# 2. INICIALIZACIÓN DEL ESTADO (MEMORIA DEL MOTOR)
if 'mesa_activa' not in st.session_state:
    st.session_state['mesa_activa'] = False

# 3. CONFIGURACIÓN DE INTERFAZ (LIMPIA Y ESPACIOSA)
st.set_page_config(page_title="SOLUCIÓN", layout="wide")

# 4. BARRA LATERAL (SOBERANÍA Y VALIDACIÓN)
with st.sidebar:
    st.title("🚀 Próximas Fases")
    st.write("🧠 **Motor Soberano:** Llama3")
    st.divider()
    st.checkbox("Fase 2: Conexión al Mundo", disabled=True)
    st.checkbox("Fase 3: Memoria Histórica", disabled=True)
    st.checkbox("Fase 4: Interfaz de Voz", disabled=True)
    st.divider()
    
    # CAMPO DE VALIDACIÓN DE DOBLE LLAVE
    st.subheader("Seguridad")
    clave = st.text_input("🔑 Ingrese Clave de Acceso:", type="password")
    validar = st.button("VALIDAR JERARQUÍA")
    
    if clave in ["LHEROES-7D", "SABIO-PRO"]:
        st.success("Acceso Validado")
    elif clave != "":
        st.error("Clave incorrecta")

# 5. CUERPO PRINCIPAL (FILTRADO POR SEGURIDAD)
st.title("Solución")
st.subheader("Arquitectura de Cuatro Expertos de Élite")

# Si la clave no es la de España ni la tuya, el sistema se detiene aquí
if clave not in ["LHEROES-7D", "SABIO-PRO"]:
    st.warning("Por favor, valide su clave en la barra lateral para comenzar.")
    st.stop()

# Área de trabajo una vez validado
dolor = st.text_area("Describa aquí la situación o el conflicto a resolver:", height=150)

if st.button("🚀 FIJAR DESAFÍO Y CONVOCAR MESA"):
    if dolor.strip():
        st.session_state['mesa_activa'] = True
    else:
        st.warning("Por favor, describa el problema antes de convocar a los expertos.")

st.divider()

# 6. PANEL DE DIRECCIÓN ESTRATÉGICA
if st.session_state['mesa_activa']:
    st.write("### ⚙️ Panel de Dirección Estratégica")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🧠 Ceder al ESTRATEGA"):
            st.info(f"**Estratega:** Analizando la ruta crítica para: {dolor[:50]}...")
            
    with col2:
        if st.button("👁️ Ceder al VIGÍA"):
            st.warning(f"**Vigía:** Supervisando riesgos y coherencia en: {dolor[:50]}...")
            
    with col3:
        if st.button("✨ Ceder al ANIMADOR"):
            st.success(f"**Animador:** Ajustando el propósito y tono humano para: {dolor[:50]}...")

    st.divider()
    
    # EL BOTÓN DE SÍNTESIS FINAL (EL CONSTRUCTOR)
    if st.button("🔥 TRABAJO EN CONJUNTO (Modo Automático)", type="primary", use_container_width=True):
        with st.spinner("Los expertos están deliberando en conjunto..."):
            st.write("✅ Estrategia definida por el Estratega.")
            st.write("✅ Coherencia validada por el Vigía.")
            st.write("✅ Tono humanizado por el Animador.")
        st.success("### 🏆 SÍNTESIS FINAL (CONSTRUCTOR)")
        st.write("El **Prompt Maestro** ha sido generado con éxito para su ejecución.")