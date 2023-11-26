import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

datos = pd.read_csv('Kobe_shots_cleanData.csv')

def prediccion():

    c1 = datos["matchup"] == 'Visitante'
    c2 = datos["game_date"] > '2013-04-12'
    c3 = datos["game_date"] < '2016-04-13'
    c4 = datos["shot_made_flag"] == 1
    dfGroup = datos.where(c1 & c2 & c3 & c4)
    db = dfGroup.groupby("game_date").agg({"shot_type": "sum"})
    db.reset_index(inplace=True)

    model = smf.ols('shot_type ~ game_date', db)
    results = model.fit()
    alpha = .05
    predictions = results.get_prediction(db).summary_frame(alpha)

    plt.scatter(db['game_date'], db['shot_type'])
    plt.plot(db['game_date'], predictions['mean'], color='red')
    plt.fill_between(db['game_date'], predictions['obs_ci_lower'], predictions['obs_ci_upper'], alpha=.1)
    plt.xlabel('Fecha')
    plt.ylabel('Total Puntos')
    plt.title('Prediccion de puntos')
    plt.show()
    plt.savefig("Graficas_P9/Prediccion_Puntos_Lesion.png")

prediccion()