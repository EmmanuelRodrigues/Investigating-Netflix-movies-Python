import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("netflix_data.csv", index_col=0)

# Filtrando os dados para remover programas de TV e armazenar como netflix_subset.
netflix_subset = dataframe[dataframe['type'] == "Movie"]

# Subdividir os dados de filmes, mantendo apenas as colunas "título", "país", "gênero", "ano_de lançamento", "duração" e salvando-os em um novo DataFrame chamado netflix_movies.
netflix_movies = netflix_subset.loc[["title","country","genre" ,"release_year","duration"]]

# Filtrando netflix_movies para encontrar os filmes com menos de 60 minutos, salvando o DataFrame resultante como short_movies; inspecionando o resultado para encontrar possíveis fatores contribuintes.
short_movies = netflix_movies[netflix_movies.duration < 60]
ou: short_movies = netflix_movies[netflix_movies["duration"] < 60]

# Parece que muitos dos filmes com menos de 60 minutos se enquadram em gêneros como "Crianças", "Stand-Up" e "Documentários". Este é um resultado lógico, já que esses tipos de filmes são provavelmente mais curtos do que os blockbusters de Hollywood de 90 minutos. Poderíamos eliminar essas linhas do nosso DataFrame e plotar os valores novamente. Mas outra forma interessante de explorar o efeito destes géneros nos nossos dados seria plotá-los, mas marcá-los com uma cor diferente.
# Usando um loop para percorrer as linhas de netflix_movies e atribuir cores para quatro grupos de gênero ("Crianças", "Documentários", "Stand-Up" e "Outros".
colors = []
for label, row in netflix_movies.iterrows() :
    if row["genre"] == "Children" :
        colors.append("red")
elif row["genre"] == "Documentaries" :
        colors.append("blue")
    elif row["genre"] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# Inicialize um plot de figura no matplotlib e criando gráfico de dispersão para a duração do filme por ano de lançamento, usando a lista de cores para colorir os pontos.
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c = colors)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')
plt.show()

# Calculando a duração média dos filmes por ano para definir a tendência da duração dos filmes ao longo dos anos
average_duration_by_year = netflix_movies.groupby('release_year')['duration'].mean()

# Traçando a duração média do filme ao longo dos anos em gráfico x/y
fig, ax = plt.subplots(figsize=(12, 8))
average_duration_by_year.plot(kind='line',ax=ax,color='purple')

ax.set_xlabel('Release Year', fontsize=12)
ax.set_ylabel('Average Duration (min)', fontsize=12)
ax.set_title('Average Movie Duration by Release Year', fontsize=14)

plt.grid(True)
plt.show()

# É possível observar uma tendência de queda entre os períodos de 2000 a 2020, se aproximando mais da faixa de média de 75 minutos, enquanto de 1965 a 2000 os filmes se mantinham entre 100 e 125 minutos. Ao analisar as oscilações de 1960 a 2000, não é possível definir uma tendência clara para a duração dos filmes.