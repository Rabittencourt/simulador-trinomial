import numpy as np
from scipy.stats import norm
from typing import Tuple, List

class TrinomialSimulator:
    """
    Responsável pela lógica matemática da simulação de Passeio Aleatório Trinomial.
    """

    def __init__(self, n_steps: int, probs: List[float]):
        """
        Inicializa o simulador.
        :param n_steps: Número de passos temporais.
        :param probs: Lista com probabilidades [P_up, P_neutral, P_down].
        """
        self.n_steps = n_steps
        self.probs = probs

    def generate_paths(self, n_simulations: int) -> np.ndarray:
        """
        Gera caminhos estocásticos usando álgebra linear (vetorização).
        :return: Array numpy (n_simulations, n_steps + 1) com os caminhos acumulados.
        """
        # Escolhas: +1 (Sobe), 0 (Mantém), -1 (Desce)
        choices = np.random.choice([1, 0, -1], size=(n_simulations, self.n_steps), p=self.probs)
        
        # Caminho acumulado
        paths = np.cumsum(choices, axis=1)
        
        # Adiciona a origem (0) no início de todos os caminhos
        zeros = np.zeros((n_simulations, 1))
        return np.hstack((zeros, paths))

    def get_theoretical_stats(self) -> Tuple[float, float]:
        """
        Calcula a Média e o Desvio Padrão teóricos finais.
        :return: (mu_total, sigma_total)
        """
        # Esperança matemática de um único passo
        # E[X] = 1*p_up + 0*p_neu + (-1)*p_down
        mu_step = 1 * self.probs[0] + 0 * self.probs[1] + (-1) * self.probs[2]
        
        # Variância de um passo: E[X^2] - (E[X])^2
        var_step = (self.probs[0] * (1 - mu_step)**2) + \
                   (self.probs[1] * (0 - mu_step)**2) + \
                   (self.probs[2] * (-1 - mu_step)**2)
        
        # Totais para N passos
        mu_total = self.n_steps * mu_step
        sigma_total = np.sqrt(self.n_steps * var_step)
        
        return mu_total, sigma_total