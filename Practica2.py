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

                    nombreColumna = False
                    
                else:

                    if(((str(row[15]).find('2PT Field Goal') > -1) and ((int(row[13]) < 25)))
                       or ((str(row[15]).find('3PT Field Goal') > -1) and (int(row[13]) > 20))):

                        if(str(row[14]) == ''):

                            row[14] = 0.0
                        
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

                        if(row[16].find('(R)') != -1):

                            zonaTiro = 'Right Side'

                        elif(row[16].find('(L)') != -1):

                            zonaTiro = 'Left Side'

                        elif(row[16].find('(LC)') != -1):

                            zonaTiro = 'Left Side Center'

                        elif(row[16].find('(RC)') != -1):

                            zonaTiro = 'Right Side Center'

                        elif(row[16].find('(C)') != -1):

                            zonaTiro = 'Center'

                        elif(row[16].find('(BC)') != -1):

                            zonaTiro = 'Back Court'

                        else:

                            zonaTiro = 'Indefinido'                        

                        data.append([int(row[13]), float(row[8] + '.' + row[12]), tipoTiro, row[21], lugar, row[23], row[0], zonaTiro, row[9], row[14]])

    return(data)

df = pd.DataFrame(limpieza_de_datos(), columns=('shot_distance','minutes_remaining','shot_type','game_date','matchup','opponent', 'action_type', 'shot_zone_area', 'period', 'shot_made_flag'))
df.to_csv("Kobe_shots_cleanData.csv", index=False)

print(df)