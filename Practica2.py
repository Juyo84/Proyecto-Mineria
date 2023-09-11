import csv
import pandas as pd

def limpieza_de_datos():

    nombreColumna = True

    data = []

    with open('kobe_shots.csv', 'rt') as f:
      
        reader = csv.reader(f)

        for row in reader:
            
            if(len(row) > 0):
                
                if(nombreColumna == True):

                    data.append([row[13], row[8], row[15], row[21], row[22], row[23]])
                    nombreColumna = False
                    
                else:

                    if(str(row[15]).find('3PT Field Goal') > -1):

                        tipoTiro = 3

                    elif(str(row[15]).find('2PT Field Goal') > -1):

                        tipoTiro = 2

                    else:

                        tipoTiro = 0
                    
                    if(str(row[22]).find('@') > -1):

                        lugar = 'Visitante'

                    elif(str(row[22]).find('vs.') > -1):

                        lugar = 'Casa'

                    else:

                        lugar = 'Indefinido'

                    data.append([int(row[13]), str(row[8] + ':' + row[12]), tipoTiro, row[21], lugar, row[23]])

    return(data)

df = pd.DataFrame(limpieza_de_datos())
df.to_csv("Kobe_shots_cleanData.csv", index=False, header=False)

print(limpieza_de_datos())