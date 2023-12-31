import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

datos = pd.read_csv('Kobe_shots_cleanData.csv')

def prediccion_tirosAnotados_PreLesion():

    datos['game_date'] = pd.to_datetime(datos['game_date']).dt.year

    c1 = datos["shot_made_flag"] == 1
    c2 = datos["game_date"] >= 2006
    c3 = datos["game_date"] <= 2013

    dfGroup = datos[c1 & c2 & c3]
    
    db = dfGroup.groupby(datos["game_date"]).agg({"shot_type": "sum"})
    db.reset_index(inplace=True)

    model = smf.ols('shot_type ~ game_date', db)
    results = model.fit()
    alpha = .1
    predictions = results.get_prediction(db).summary_frame(alpha)

    plt.scatter(db['game_date'], db['shot_type'])
    plt.plot(db['game_date'], predictions['mean'], color='purple')
    plt.fill_between(db['game_date'], predictions['obs_ci_lower'], predictions['obs_ci_upper'], alpha=.1)
    
    plt.xlabel('Fecha')
    plt.ylabel('Total Puntos')
    plt.title('Prediccion de puntos por temporada')
    plt.savefig("Graficas_P9/Prediccion_Puntos_Temporada.png")

prediccion_tirosAnotados_PreLesion()