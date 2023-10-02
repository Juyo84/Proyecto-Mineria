import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Kobe_shots_cleanData.csv')

#Tabla de Bigotes entre tiro de distancia y oponente
def boxplot_Shot_Distance_Opponent():
        
    sns.boxplot(x="shot_distance", y="opponent", data=df)

    plt.savefig("Graficas_P4/Bp_Opponent_ShotDistance.png")

#Grafica de pastel de los oponentes
def pie_Opponent():
    
    df_aux = df.groupby('opponent')['opponent'].value_counts()
    df_aux.plot.pie(y='opponent', figsize=(10,10), autopct="%1.0f%%")

    plt.savefig("Graficas_P4/p_Opponent.png")

boxplot_Shot_Distance_Opponent()
plt.gcf().clear()
pie_Opponent()
plt.gcf().clear()