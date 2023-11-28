import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Kobe_shots_cleanData.csv')

def boxplot_Shot_Distance_Opponent():
        
    sns.boxplot(x="shot_distance", y="opponent", data=df)

    plt.savefig("Graficas_P4/Bp_Opponent_ShotDistance.png")

def pie_Opponent():

    datos = df[(df["game_date"] >= '1999-12-01') & (df["game_date"] < '2002-10-29')]
    df_aux = datos.groupby('action_type').size()
    df_aux.plot.pie(figsize=(10, 10), autopct="%1.0f%%")
    plt.title("Distribucion de Tipos de tiros en 3 temporadas")
    plt.savefig("Graficas_P4/p_ActionType_Date.png")


def pie_ZonaTiro():
    
    grouped = df.groupby(['shot_zone_area', 'shot_type']).size().unstack()

    grouped.plot(kind='barh', stacked=True, figsize=(10, 8))
    plt.xlabel('Cantidad')
    plt.ylabel('Zona de tiro')
    plt.title('Distribucion de los tiros de acuerdo a la zona')
    
    plt.savefig("Graficas_P4/p_ZonaTiro.png")

boxplot_Shot_Distance_Opponent()
plt.gcf().clear()
pie_Opponent()
plt.gcf().clear()
pie_ZonaTiro()