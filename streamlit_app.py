import streamlit as st
import numpy as np

from src.optimizer import otimizar_energia
from src.rl_agent import politica_otima

# ============================
# TÍTULO
# ============================
st.title("🚢 Sistema Inteligente de Propulsão Naval")

st.markdown("""
Aplicação de Inteligência Artificial para otimização energética
em sistemas híbridos diesel-elétricos.
""")

# ============================
# ENTRADAS
# ============================
velocidade = st.slider("Velocidade do Navio", 0, 30, 15)
carga = st.slider("Carga Operacional (%)", 0, 100, 70)
soc = st.slider("Estado de Carga da Bateria (%)", 0, 100, 60)
temperatura = st.slider("Temperatura (°C)", 0, 50, 25)

# ============================
# DEMANDA SIMULADA
# ============================
demanda = velocidade * carga * 0.25

# ============================
# OTIMIZAÇÃO
# ============================
diesel, bateria = otimizar_energia(demanda, soc)

# RL
acao_rl = politica_otima(soc, demanda)

# ============================
# RESULTADOS
# ============================
st.subheader("📊 Resultados")

st.write(f"Demanda estimada: {demanda:.2f} kW")
st.write(f"Potência Diesel: {diesel:.2f} kW")
st.write(f"Potência Bateria: {bateria:.2f} kW")

st.write(f"Uso ótimo bateria (RL): {acao_rl*100:.1f}%")

# ============================
# GRÁFICO
# ============================
st.bar_chart({
    "Diesel": [diesel],
    "Bateria": [bateria]
})