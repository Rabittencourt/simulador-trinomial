# 🎲 Simulador de Processo Trinomial

Uma aplicação interativa para simular e visualizar Passeios Aleatórios Trinomiais (Trinomial Random Walks). O projeto modela decisões estocásticas (Boas, Neutras, Ruins) em uma rede temporal, calculando estatísticas via simulação de Monte Carlo.

🔗 **[Acesse o App Online Aqui](https://LINK_DO_SEU_APP.streamlit.app)**

## 📊 Funcionalidades

- **Rede de Decisão 2D:** Visualização gráfica do caminho em um grid triangular/hexagonal.
- **Simulação de Monte Carlo:** Gera milhares de cenários para projetar a tendência futura.
- **Análise Estatística:** Compara a distribuição empírica (realizada) com a curva Normal teórica (Gaussiana).
- **Parâmetros Customizáveis:** Ajuste de probabilidades (Up/Neutral/Down) e horizonte de tempo.

## 🛠️ Instalação e Uso Local

Se quiser rodar na sua máquina:

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o app:
   ```bash
   streamlit run app.py
   ```

## 📂 Estrutura do Projeto

- `app.py`: Interface do usuário (Frontend Streamlit).
- `src/engine.py`: Motor matemático e lógica de simulação.
- `src/plots.py`: Geração de gráficos com Matplotlib.

---
Desenvolvido com Python 🐍 e Streamlit 🎈
