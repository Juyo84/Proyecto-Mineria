import pandas as pd

df = pd.read_csv('Kobe_shots_cleanData.csv')

def cantidad_Tiros_Por_Oponente():

    resultado = df.groupby('opponent')['shot_type'].count()
    print(resultado)

def cantidad_Tiros_Por_Partido():

    resultado = df.groupby('game_date')['shot_type'].count()
    print(resultado)

def mayor_Distancia_Tiro_Por_Oponente():

    resultado = df.groupby('opponent')['shot_distance'].max()
    print(resultado)

def cantidad_Partidos_Por_Emparejamiento():

    resultado = df.groupby('matchup')['game_date'].count()
    print(resultado)

def mayor_Distancia_Tiro_Por_Partido():

    resultado = df.groupby('game_date')['shot_distance'].max()
    print(resultado)
    
def minima_Distancia_Tiro_Por_Partido():

    resultado = df.groupby('game_date')['shot_distance'].min()
    print(resultado)

def Cantidad_Tiros_Por_Tiempo_Juego():

    resultado = df.groupby('minutes_remaining')['shot_type'].count()
    print(resultado)