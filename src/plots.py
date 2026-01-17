import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from typing import Tuple

class TrinomialPlotter:
    """
    Classe utilitária para geração de gráficos do processo trinomial.
    """

    @staticmethod
    def plot_lattice_network(path: np.ndarray, n_steps: int) -> plt.Figure:
        """
        Plota o caminho único sobre uma rede (grid) hexagonal/triangular.
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plotar grid de fundo (Lattice) apenas se não for muito denso
        if n_steps <= 40:
            for i in range(n_steps + 1):
                # Nós possíveis em t=i
                possible_y = np.arange(-i, i + 1)
                ax.scatter([i] * len(possible_y), possible_y, 
                           color='lightgray', s=15, alpha=0.5, marker='H')

        # Plotar o caminho
        x_axis = np.arange(n_steps + 1)
        ax.plot(x_axis, path, color='#FF4B4B', linewidth=2.5, marker='o', markersize=5, label='Caminho Realizado')
        ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
        
        ax.set_title("Caminho na Rede de Decisões")
        ax.set_xlabel("Tempo (Passos)")
        ax.set_ylabel("Nível")
        ax.legend()
        ax.grid(True, linestyle=':', alpha=0.3)
        
        return fig

    @staticmethod
    def plot_monte_carlo_analysis(all_paths: np.ndarray, 
                                  mu_theo: float, 
                                  sigma_theo: float) -> plt.Figure:
        """
        Plota a análise de Monte Carlo: Spaghetti Plot + Histograma de Distribuição.
        """
        n_sims, n_cols = all_paths.shape
        n_steps = n_cols - 1
        x_axis = np.arange(n_steps + 1)
        mean_path = np.mean(all_paths, axis=0)
        final_positions = all_paths[:, -1]

        # Layout com 2 gráficos (Caminhos e Distribuição)
        fig, (ax_path, ax_dist) = plt.subplots(1, 2, figsize=(14, 6), 
                                               gridspec_kw={'width_ratios': [2, 1]})

        # 1. Gráfico de Caminhos (Amostra)
        sample_size = min(n_sims, 150) # Limita para não pesar visualmente
        for i in range(sample_size):
            ax_path.plot(x_axis, all_paths[i], color='steelblue', alpha=0.1)

        ax_path.plot(x_axis, mean_path, color='black', linewidth=2, linestyle='--', label='Média Empírica')
        ax_path.set_title(f"Simulação Monte Carlo ({n_sims} iterações)")
        ax_path.set_ylabel("Nível")
        ax_path.set_xlabel("Passos")
        ax_path.legend(loc='upper left')
        ax_path.grid(alpha=0.3)

        # 2. Histograma Final
        ax_dist.hist(final_positions, bins='auto', density=True, 
                     color='skyblue', edgecolor='white', alpha=0.8, orientation='horizontal')
        
        # Curva Normal Teórica
        y_range = np.linspace(min(final_positions), max(final_positions), 100)
        if sigma_theo > 0:
            pdf = norm.pdf(y_range, mu_theo, sigma_theo)
            ax_dist.plot(pdf, y_range, 'r--', linewidth=2, label='Normal Teórica')

        ax_dist.set_title("Distribuição Final")
        ax_dist.set_xlabel("Densidade")
        ax_dist.legend()
        ax_dist.grid(alpha=0.3)

        plt.tight_layout()
        return fig