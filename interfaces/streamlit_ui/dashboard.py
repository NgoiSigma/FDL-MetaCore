# interfaces/streamlit_ui/dashboard.py

import streamlit as st
from sigma_avatarus import SigmaAvatarus
from fdl_agent_kernel.logic_core import FDLKernel
from modules.Δψ_monitor.lie_tension_analyzer import analyze_tension

st.set_page_config(page_title="FDL-MetaCore Dashboard", layout="centered")

avatar = SigmaAvatarus()
kernel = FDLKernel()

st.title("Σ-FDL :: Resonance Dashboard")
st.subheader("Наблюдение напряжения лжи и резонансного состояния")

user_input = st.text_input("🔍 Введите новостной фрагмент или противоречивое утверждение:")

if user_input:
    resonance = avatar.resonate(user_input)
    synthesis = kernel.analyze(user_input, resonance)
    tension_score = analyze_tension(user_input)

    st.markdown("### 📡 Результаты анализа")
    st.write(f"🧠 Семантический отклик: `{resonance}`")
    st.write(f"⚙️ Синтез противоречий: `{synthesis}`")
    st.write(f"💥 Напряжение лжи: `{tension_score}/10`")

    if tension_score >= 7:
        st.warning("❗ Высокий уровень противоречий. Возможна ложь или дезинформация.")
    elif tension_score >= 4:
        st.info("⚠️ Средний уровень напряжения. Требуется внимательный анализ.")
    else:
        st.success("✅ Низкое напряжение. Информация логически устойчива.")

st.markdown("---")
st.caption("Powered by NOVEYA AI · SVET-obolochka · GPT-4o Kernel")
