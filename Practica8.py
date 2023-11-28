import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

datos = pd.read_csv('Kobe_shots_cleanData.csv')
datos_aux = datos[(datos["shot_type"] == 3)]
df = datos_aux[["shot_distance", "minutes_remaining"]]

def Kmeans1():

    for i in range(1,6):

        kmeans = KMeans(n_clusters=i, random_state=0, n_init=5)
        kmeans.fit_predict(df)
        plt.scatter(x=df["shot_distance"], y=df["minutes_remaining"], c=kmeans.labels_)
        plt.xlabel('Distancia de tiro')
        plt.ylabel('Minutos restantes')
        plt.title("Tiros de 3 puntos\nK = " + str(i))
        plt.savefig("Graficas_P8/K = " + str(i) + ".png")
        plt.clf()

Kmeans1()