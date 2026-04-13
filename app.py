# --- BARRA LATERAL (SOBERANÍA Y FUTURO) ---
with st.sidebar:
    st.markdown("## 👑 Soberanía")
    st.write("Motor: **Llama3 (Independiente)**")
    st.divider()
    
    # RECUPERAMOS LOS ADELANTOS A FUTURO
    st.markdown("### 🚀 Próximas Fases")
    st.info("Fase 2: Conexión al Mundo 🌐")
    st.info("Fase 3: Memoria Histórica 🧠")
    st.info("Fase 4: Interfaz de Voz 🎙️")
    
    st.divider()
    
    # VALIDACIÓN DE ACCESO
    clave_ingresada = st.text_input("🔑 Clave de Acceso:", type="password")
    if st.button("Validar Entrada"):
        if clave_ingresada == "LHEROES-7D":
            st.session_state['verificado'] = True
            st.rerun()
        else:
            st.error("Acceso denegado")
