import streamlit as st
from datetime import datetime

# CONFIGURACIÓN DE PÁGINA (Priorizando espacio de lectura)
st.set_page_config(page_title="SOLUCIÓN - Arquitectura de Expertos", layout="wide")

# --- LÓGICA DE ACCESO Y SEGURIDAD ---
def validar_acceso(clave):
    # 1. Clave Maestra Permanente
    if clave == "SABIO-PRO":
        return True, "Acceso Total Maestro"
    
    # 2. Clave de Cortesía (España) - Extendida hasta el 23 de Abril
    if clave == "LHEROES-7D":
        fecha_limite = datetime(2026, 4, 23)
        if datetime.now() <= fecha_limite:
            return True, "Acceso Institucional (Cortesía)"
        else:
            return False, "La clave de cortesía ha expirado."
            
    # 3. Claves Únicas de Imprenta (SOLUCIÓN 001 al 020)
    if clave.startswith("SOLUCIÓN "):
        try:
            numero = int(clave.split(" ")[1])
            if 1 <= numero <= 20:
                return True, f"Acceso Individual (Tarjeta {numero:03d})"
        except:
            pass
            
    return False, "Clave no válida"

# --- INTERFAZ LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("👑 SOBERANÍA")
    st.subheader("Acceso al Sistema")
    clave_input = st.text_input("Ingrese su Clave de Acceso:", type="password")
    boton_validar = st.button("VALIDAR JERARQUÍA")

# --- CUERPO PRINCIPAL ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if boton_validar:
    es_valida, mensaje = validar_acceso(clave_input)
    if es_valida:
        st.session_state.autenticado = True
        st.success(f"✅ {mensaje}")
    else:
        st.error(f"❌ {mensaje}")

if st.session_state.autenticado:
    st.title("SOLUCIÓN")
    st.header("Arquitectura de Cuatro Expertos de Élite")
    st.write("---")
    
    # ENTRADA DEL DESAFÍO
    dolor = st.text_area("Describa aquí la situación o el conflicto a resolver:", height=200)
    
    if st.button("🚀 FIJAR DESAFÍO Y CONVOCAR MESA"):
        if dolor.strip():
            with st.spinner("Los 4 Expertos están deliberando..."):
                # Aquí se integrará la llamada a la API de Google en el siguiente paso
                st.info("La Mesa de Expertos está analizando su desafío. (Conexión establecida)")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("🕵️ El Vigía")
                    st.write("Analizando riesgos y puntos ciegos...")
                with col2:
                    st.subheader("📐 El Estratega")
                    st.write("Diseñando la ruta de menor resistencia...")
                
                col3, col4 = st.columns(2)
                with col3:
                    st.subheader("🎭 El Animador")
                    st.write("Evaluando el impacto humano y emocional...")
                with col4:
                    st.subheader("🏗️ El Constructor")
                    st.write("Estructurando la respuesta técnica final...")
        else:
            st.warning("Por favor, describa el conflicto antes de convocar a la mesa.")

    # --- SECCIÓN TÉCNICA (PUNTO 7 DEL MANUAL MAESTRO) ---
    with st.expander("🛠️ Instrucciones Técnicas (Anexo Referencial)"):
        st.markdown("""
        **Nota:** Esta sección es estrictamente informativa para auditorías técnicas.
        
        Para garantizar la compatibilidad con los modelos de última generación, el entorno requiere obligatoriamente:
        `pip install -q -U google-generativeai`
        
        Arquitectura modular preparada para integración de **Ollama** en despliegues locales.
        """)
else:
    st.warning("⚠️ Valide su acceso en la barra lateral para comenzar a trabajar.")