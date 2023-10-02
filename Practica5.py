import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('Kobe_shots_cleanData.csv')

def anova(df_aux: pd.DataFrame, str_ols: str):

    modl = ols(str_ols, data=df_aux).fit()
    anova_df = sm.stats.anova_lm(modl, typ=2)

    if anova_df["PR(>F)"][0] < 0.005:

        print("Hay diferencias")
        print(anova_df)

    else:
        
        print("No hay diferencias")


def anova_1():

    df_aux = df.groupby(["matchup", "opponent"]).agg({"shot_distance": "count"})
    df_aux.reset_index(inplace=True)
    anova(df_aux, "shot_distance ~ opponent + matchup")

#ANOVA ENTRE OPONENTES Y EMPAREJAMIENTO DE ACUERDO A LA DISTANCIA CADA TIRO
anova_1()