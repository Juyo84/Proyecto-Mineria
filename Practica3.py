import pandas as pd

df = pd.read_csv('Kobe_shots_cleanData.csv')

def Oponente_TipoTiro():

    resultado = df.groupby('opponent')['shot_type'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.to_csv('CSV_P3/Kobe_shots_TipoTiro_Oponente.csv')

def Fecha_TipoTiro():

    resultado = df.groupby('game_date')['shot_type'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.to_csv('CSV_P3/Kobe_shots_Fecha_TipoTiro.csv')

def Minutos_TipoTiro():

    resultado = df.groupby('minutes_remaining')['shot_type'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.to_csv('CSV_P3/Kobe_shots_Minutos_TipoTiro.csv')

def Minutos_DistanciaTiro():

    resultado = df.groupby('minutes_remaining')['shot_distance'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.to_csv('CSV_P3/Kobe_shots_Minutos_DistanciaTiro.csv')

def Fecha_DistanciaTiro():

    resultado = df.groupby('game_date')['shot_distance'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.to_csv('CSV_P3/Kobe_shots_Fecha_DistanciaTiro.csv')

def Oponente_DistanciaTiro():

    resultado = df.groupby('opponent')['shot_distance'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.to_csv('CSV_P3/Kobe_shots_Oponente_DistanciaTiro.csv')

Oponente_DistanciaTiro()
Oponente_TipoTiro()
Fecha_TipoTiro()
Fecha_DistanciaTiro()
Minutos_TipoTiro()
Minutos_DistanciaTiro()