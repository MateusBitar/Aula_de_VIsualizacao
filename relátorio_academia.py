import pandas as pd
import streamlit as st
import altair as alt

# Carregar Base de dados do Kaggle
df = pd.read_csv('gym_members_exercise_tracking.csv')

# Subtítulo
st.subheader('Pessoas que frequentam academia divididas por genero')

# criar Dataframe com informações que serão utilizadas no gráfico para incluir a frequência
sexo = pd.DataFrame({
    'genero' : df['Gender'].unique(),
    'freq' :df['Gender'].value_counts()
    })

st.bar_chart(sexo,x = 'genero',y = 'freq', color = '#bb781c')



# Subtítulo
st.title('Quantidade de caloria queimada por tempo de treino')

# Selecionar os tipos de treino para análise
workout_types = df['Workout_Type'].unique()
selected_workout = st.multiselect('Selecione o(s) tipo(s) de treino:', workout_types, default=workout_types)

# Filtrar dados com base no tipo de treino selecionado
filtered_df = df[df['Workout_Type'].isin(selected_workout)]

st.scatter_chart(filtered_df,y = 'Calories_Burned',x = 'Session_Duration (hours)', color = '#bb781c')


# subtítulo
st.subheader('Média de Calorias Queimadas por Nível de Experiência')


genero = st.radio("Selecione o Gênero" ,
                  ["Male", "Female", "Ambos"]
    )



teste = pd.DataFrame({
    'Calories_Burned': df['Calories_Burned'],
    'Experience_Level': df['Experience_Level'],
    'Gender': df['Gender']
})
if genero != "Ambos":
    teste = teste[teste['Gender'] == genero]

# Calcular a média de calorias queimadas por nível de experiência e gênero
media_calorias = teste.groupby(['Experience_Level', 'Gender'])['Calories_Burned'].mean().reset_index()

color_scale = alt.Scale(domain=['Male', 'Female'], range=['#7f1734', '#ff7f0e'])

bar_chart = alt.Chart(media_calorias).mark_bar().encode(
    x='Experience_Level:N',
    y='Calories_Burned:Q',
    color=alt.Color('Gender:N', scale=color_scale),  # Diferenciar as barras por gênero
    tooltip=['Experience_Level:N', 'Gender:N', 'Calories_Burned:Q']  # Exibir informações ao passar o mouse
).properties(
    title=f' Gênero: {genero}'
)

# Exibir o gráfico no Streamlit
st.altair_chart(bar_chart, use_container_width=True)




#st.bar_chart(teste, y = 'Calories_Burned', x = 'Experience_Level',color = "Gender", stack=False)
