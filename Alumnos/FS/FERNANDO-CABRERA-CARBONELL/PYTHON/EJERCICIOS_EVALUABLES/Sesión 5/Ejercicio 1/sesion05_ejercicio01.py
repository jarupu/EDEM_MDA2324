import pandas as pd

file_path = '/Users/fernandocabreracarbonell/Documents/GitHub/EDEM_MDA2324/Alumnos/FS/FERNANDO-CABRERA-CARBONELL/PYTHON/EJERCICIOS_EVALUABLES/Sesión 5/pokemon_data.csv'
df = pd.read_csv(file_path)

# IMPRIMIR TODOS LOS VALORES
print(df)

# IMPRIMIR LOS PRIMEROS 5
print(df.head(5))

# IMPRIMIR LOS ÚLTIMOS 5
print (df.tail(5))

# OBTENER NOMBRES DE LAS COLUMNAS
print(df.columns)

#- OBTENER TODOS LOS NOMBRES
print(df['Name'])

#- OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print(df[['Name', 'Speed']])

# - LOS PRIMEROS 5 NOMBRES USANDO [::]
print(df['Name'][:5])

# - OBTENER TODAS LAS FILAS
print(df[:])

# - OBTENER UN RANGO DE FILAS
print(df[1:11]) #cojo de la 1 a la 10

# - OBTENER EL NOMBRE DE LA FILA 10
print(df.loc[10,'Name'])

# - ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
for index, row in df.iterrows():
    print(f"Índice: {index}, Nombre: {row['Name']}")

# - POKEMONS DE TIPO 1 == WATER
agua_pokemon = df[df['Type 1'] == 'Water']
print(agua_pokemon)

# - ESTADÍSTICAS (usando Describe del DafaFrame)
print(df.describe())

# - ORDENACIÓN POR NOMBRE ASCENDENTE
print(df.sort_values('Name', ascending=True))

 #- CREAR UNA COLUMNA EXTRA CALCULADA
 #   - La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
 #   - La columna debe llamarse TOTAL

df['TOTAL'] = df['HP']+df['Attack']+df['Defense']+df['Speed']
print(df)

# - ELIMINAR LA COLUMNA TOTAL
df.drop('TOTAL', axis=1, inplace=True)
print(df)

# - FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
grass_poison_pokemon = df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') | (df['Type 2'] == 'Grass') & (df['Type 1'] == 'Poison')]
print(grass_poison_pokemon) # creo que no hay de tipo1 poison y tipo2 grass, pero he probado por si acaso, y salen 800

# - FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
fire_poison_pokemon = df[(df['Type 1'] == 'Fire') | (df['Type 2'] == 'Poison') | (df['Type 2'] == 'Fire') | (df['Type 1'] == 'Poison')]
print(fire_poison_pokemon) # aquí sí que he cogido todos los que sean tipo1 o tipo2 fire, y tipo1 o tipo2 poison, y salen 126

# - FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
filtro_tipo_pokemon = df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') | (df['Type 2'] == 'Grass')& (df['Type 1'] == 'Poison')]
filtro_hp_pokemon = filtro_tipo_pokemon[filtro_tipo_pokemon['HP'] >= 70]
print(filtro_hp_pokemon)

# - FILTRAR POKEMONS CON NOMBRE "MEGA"
mega_pokemon = df[df['Name'] == 'MEGA'] # se pide esto, pero no da resultados. Entiendo que queremos que el nombre contenga "Mega"
mega_pokemon = df[df['Name'].str.contains('Mega')] #así sí, y salen 
print(mega_pokemon)

# - FILTRAR POKEMONS SIN NOMBRE "MEGA"
no_mega_pokemon = df[~df['Name'].str.contains('Mega')] 
print(no_mega_pokemon)

# - FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
pi_pokemon = df[df['Name'].str.startswith('Pi')]
print(pi_pokemon)

# - RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
df['Type 1'] = df['Type 1'].replace('Fire', 'Flame') # no hay columnas que se llame FIRE o Fire
df['Type 2'] = df['Type 2'].replace('Fire', 'Flame') # ntiendo que queremos cambiar todos los que tengan de type 1 o Type 2 Fire, por Flame
print(df) # lo pruebo y funciona

# - RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
df['Type 1'] = df['Type 1'].replace('Flame', 'Fire') 
df['Type 2'] = df['Type 2'].replace('Flame', 'Fire') 
print(df)

# si queremos cambiar nombres de columna, por ejemplos Type 1 a Tipo 1, sería
df.rename(columns={'Type 1': 'Tipo 1'}, inplace=True)
print(df)

# y volvemos a dejarlo como estaba
df.rename(columns={'Tipo 1': 'Type 1'}, inplace=True)
print(df)

# - CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
df.loc[df['Legendary'] == True, ['Type 1']] = 'Fire' # Les ponemos tipo1 Fuego, pero tipo 2 ninguno. En este caso NaN
df.loc[df['Legendary'] == True, ['Type 1']] = 'NaN'
print(df)

#- (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
groupby_tipo_orden_defensa = df.groupby('Type 1')['Defense'].mean().sort_values(ascending=False)
print(groupby_tipo_orden_defensa)

#- (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
groupby_tipo_orden_ataque = df.groupby('Type 1')['Attack'].mean().sort_values(ascending=False)
print(groupby_tipo_orden_ataque)

# - (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
groupby_tipo_orden_hp = df.groupby('Type 1')['HP'].mean().sort_values(ascending=False)
print(groupby_tipo_orden_hp)

# - (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
suma_tipo_pokemon = df.groupby('Type 1')[['Attack', 'Defense']].sum() # sumamos por ejemplo, ataque y defensa
print(suma_tipo_pokemon)

# - (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
num_tipo_pokemon = df['Type 1'].value_counts().reset_index()
num_tipo_pokemon.columns = ['Tipo de Pokémon', 'Número de Pokémons']
print(num_tipo_pokemon)

# - (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
num_tipo1_tipo2_pokemon = df.groupby(['Type 1', 'Type 2']).size().sort_values(ascending=False)
print(num_tipo1_tipo2_pokemon)

#SI TENEMOS ARCHIVOS ENORMES (1TB) PODEMOS LEERLOS POR PARTES 
#Cada fila podría estar acumulando cerca de 20 bytes, por lo que podríamos estar trabajando con cantidades enormes

#- LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE  (chunksize=5)
#- ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA

chunksize = 5
for chunk in pd.read_csv(file_path, chunksize=chunksize):
    print(chunk)











