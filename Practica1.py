import pandas as pd
import requests
import io

def get_csv_from_url(url: str) -> pd.DataFrame:

    s = requests.get(url).content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))

df = get_csv_from_url("https://raw.githubusercontent.com/Worm4047/kobe-bryant-shot-selection/master/data.csv")

df.to_csv("kobe_shots.csv", index=False)

print("DataSet Descargado")