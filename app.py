import streamlit as st
import numpy as np
from src.engine import TrinomialSimulator
from src.plots import TrinomialPlotter

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Trinomial Random Walk",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("🎲 Simulador de Processo Trinomial")
    st.markdown("""
    Modelagem estocástica de escolhas (Boas, Neutras, Ruins) visualizada em uma rede temporal 2D.
    """)

    # --- SIDEBAR: INPUTS ---
    with st.sidebar:
        st.header("⚙️ Parâmetros")
        
        n_steps = st.slider("Horizonte de Tempo (Passos)", 5, 100, 20)
        
        st.subheader("Probabilidades de Transição")
        p_up = st.slider("Prob. Escolha Boa (X) %", 0, 100, 33)
        
        remaining = 100 - p_up
        p_neutral = st.slider("Prob. Escolha Neutra (Y) %", 0, remaining, 33)
        
        p_down = 100 - p_up - p_neutral
        st.metric("Prob. Escolha Ruim (Z) %", f"{p_down}%")
        
        if (p_up + p_neutral + p_down) != 100:
            st.error("Erro de arredondamento: ajustando para 100%")
        
        # Converter para formato 0-1
        probs = [p_up/100, p_neutral/100, p_down/100]

    # --- INSTANCIAÇÃO DO MOTOR ---
    simulator = TrinomialSimulator(n_steps=n_steps, probs=probs)

    # --- SEÇÃO 1: CAMINHO ÚNICO ---
    st.header("1. Visualização da Rede")
    col_btn, _ = st.columns([1, 4])
    
    if col_btn.button("🔄 Gerar Novo Caminho"):
        # Hack para forçar re-execução do script e gerar novo random
        pass 

    # Gera 1 caminho
    single_path = simulator.generate_paths(n_simulations=1)[0]
    fig_network = TrinomialPlotter.plot_lattice_network(single_path, n_steps)
    st.pyplot(fig_network)

    st.divider()

    # --- SEÇÃO 2: MONTE CARLO ---
    st.header("2. Análise Estatística (Monte Carlo)")
    
    n_sims = st.slider("Quantidade de Simulações", 100, 10000, 1000)
    
    # Processamento
    with st.spinner('Simulando caminhos...'):
        all_paths = simulator.generate_paths(n_simulations=n_sims)
        mu_theo, sigma_theo = simulator.get_theoretical_stats()
        
        # Plotagem
        fig_mc = TrinomialPlotter.plot_monte_carlo_analysis(all_paths, mu_theo, sigma_theo)
        st.pyplot(fig_mc)

    # Métricas Finais
    final_values = all_paths[:, -1]
    
    st.subheader("Resultados Consolidados")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    kpi1.metric("Média Realizada", f"{np.mean(final_values):.2f}")
    kpi2.metric("Média Teórica", f"{mu_theo:.2f}")
    kpi3.metric("Desvio Padrão (Vol)", f"{np.std(final_values):.2f}")
    kpi4.metric("Valor Máximo Atingido", f"{np.max(final_values):.0f}")

if __name__ == "__main__":
    main()