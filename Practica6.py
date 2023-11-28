import pandas as pd
import statsmodels.api as sm
import numbers
import matplotlib.pyplot as plt

df = pd.read_csv('Kobe_shots_cleanData.csv')
df = df[df["shot_made_flag"] == 1]
df_aux = df.groupby("opponent").agg({"shot_type": "sum"})
df_aux.reset_index(inplace=True)

def transform_variable(df: pd.DataFrame, x: str) -> pd.Series:

    if isinstance(df[x][0], numbers.Number):

        return df[x]
    
    else:

        return pd.Series([i for i in range(0, len(df[x]))])


def progresion_lineal(df: pd.DataFrame, x: str, y:str) -> None:

    fixed_x = transform_variable(df, x)
    model = sm.OLS(df[y], sm.add_constant(fixed_x)).fit()
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]['coef']
    
    df.plot(x=x, y=y, kind='scatter')
    plt.plot(df_aux[x], [coef.values[1] + x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.title('Puntos totales contra cada equipo')
    plt.savefig('Graficas_P6/PL_Oponente_PuntosTotales.png')
    plt.close()

#PROGESION LINEAL ENTRE OPONENTE Y LA DISTANCIA DE TIRO
progresion_lineal(df_aux, "opponent", "shot_type")