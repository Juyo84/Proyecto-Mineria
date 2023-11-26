import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

datos = pd.read_csv('Kobe_shots_cleanData.csv')
datos = datos[(datos["shot_type"] == 3)]
df = datos[["shot_distance", "minutes_remaining"]]

def Kmeans():

    for i in range(1,6):

        kmeans = KMeans(n_clusters=i, random_state=0, n_init=5)
        kmeans.fit_predict(df)
        plt.scatter(x=df["shot_distance"], y=df["minutes_remaining"], c=kmeans.labels_)
        plt.xlabel('Distancia de tiro')
        plt.ylabel('Minutos restantes')
        plt.title("K = " + str(i))
        plt.savefig("Graficas_P8/K = " + str(i) + ".png")
        plt.clf()

Kmeans()