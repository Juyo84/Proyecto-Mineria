import pandas as pd
import matplotlib.pyplot as plt
 
datos = pd.read_csv('Kobe_shots_cleanData.csv')

def Distancia_Minutos_Clutch_Prime():

    datos1 = datos[(datos["minutes_remaining"] <= 2) & (datos["period"] == 4) & (datos['shot_made_flag'] == 0.0)
               & ((datos['game_date'] >= '2005-11-01') & (datos['game_date'] < '2006-04-19'))]
    datos2 = datos[(datos["minutes_remaining"] <= 2) & (datos["period"] == 4) & (datos['shot_made_flag'] == 1.0)
               & ((datos['game_date'] >= '2005-11-01') & (datos['game_date'] < '2006-04-19'))]

    plt.scatter(pd.to_datetime(datos1["game_date"]), datos1["shot_distance"], marker="x", s=30, color="red")
    plt.scatter(pd.to_datetime(datos2["game_date"]), datos2["shot_distance"], marker="o", s=30, color="green")

    plt.xlabel("Fecha")
    plt.ylabel("Distancia")
    plt.title('Tiros realizados de los ultimos 2 minutos de cada partido\nde la temporada 2005/2006')
    plt.legend(bbox_to_anchor=(1,0.2))
    plt.savefig("Graficas_P7/Distancia_Minutos_Clutch_Prime.png")


Distancia_Minutos_Clutch_Prime()