Este é um guia para o **Dashboard de Análise de Membros de Academia**, uma aplicação interativa desenvolvida em Python utilizando a biblioteca **Streamlit**.

---

# 🏋️‍♂️ Dashboard de Análise de Membros de Academia

Este projeto apresenta uma análise exploratória de dados (EDA) de uma base de dados de frequentadores de academia. O objetivo é identificar padrões de comportamento físico, progressão de atletas e tendências de saúde por meio de visualizações dinâmicas.

## 📊 Funcionalidades do Dashboard

O relatório interativo está dividido em seis seções principais:

1. **Distribuição por Gênero:** Visualização da quantidade de frequentadores dividida entre masculino e feminino.
2. **Níveis de Experiência:** Gráfico de barras mostrando a quantidade de alunos iniciantes, intermediários e avançados.
3. **Análise Etária:** Identificação da frequência de usuários por idade.
4. **Eficiência de Treino:** Gráfico de dispersão correlacionando calorias queimadas e duração do treino, com filtro por tipo de atividade (Cárdio, HIIT, Força, etc.).
5. **Média de Calorias vs. Experiência:** Gráfico comparativo que utiliza filtros de rádio para segmentar o gasto calórico médio por gênero e nível de experiência.
6. **Perfil Biométrico:** Análise da relação entre Peso, Altura e Idade dos membros, segmentada por gênero.

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem principal.
* **Pandas**: Manipulação e tratamento dos dados.
* **Streamlit**: Criação da interface web e visualizações rápidas.
* **Altair**: Gráficos estatísticos avançados e customização de cores.

## 🚀 Como Executar o Projeto

Para rodar este dashboard localmente, siga os passos abaixo:

1. **Instale as dependências:**
```bash
pip install pandas streamlit altair

```


2. **Certifique-se de ter o arquivo de dados:**
O script espera encontrar o arquivo `gym_members_exercise_tracking.csv` no mesmo diretório.
3. **Execute a aplicação:**
```bash
streamlit run relátorio_academia.py

```



## 📂 Estrutura de Arquivos

* `relátorio_academia.py`: Código-fonte da aplicação Streamlit.
* `gym_members_exercise_tracking.csv`: Base de dados contendo 973 amostras de membros.

## 📝 Conclusão

O painel demonstra a superioridade do uso de dashboards interativos em comparação com planilhas estáticas. A capacidade de filtrar dados em tempo real permite que gestores de academias ou profissionais de saúde identifiquem rapidamente quais tipos de treino são mais eficientes para diferentes perfis de alunos.

---

**Links Externos:**

* [Tabela Dinâmica (Google Sheets)](https://docs.google.com/spreadsheets/d/1hZUH3A9y6sxK08FsfJAZMLgkdtz6uObJEWGmeDk3Czo/edit?usp=sharing)
* [Relatório Completo (Google Docs)](https://docs.google.com/document/d/1xVn0OYwI0I1eOyktmPLT4znazsMWTxqZQANO_oNe1J8/edit?tab=t.0)

---
