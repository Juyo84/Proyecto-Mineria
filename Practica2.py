import csv

datos = []

def limpieza_de_datos():
   
    distancia = []
    acierto = []
    tipoTiro = []
    fechaJuego = []
    lugar = []
    rival = []

    with open('kobe_shots.csv', 'rt') as f:
      
        reader = csv.reader(f)

        for row in reader:
      
            if(len(row)>0):
      
                if(row[0] != '' and row[1] != ''):
                    
                    distancia.append(row[0])
                    
                    acierto.append(row[1])
                    
                    if(row[2] == '2PT Field Goal'):

                        tipoTiro.append('2')

                    if(row[2] == '3PT Field Goal'):

                        tipoTiro.append('3')

                    fechaJuego.append(row[3])
                    
                    if(row[4].find(' @ ')):

                        lugar.append('Visitante')
          
                    if(row[4].find(' vs. ')):

                        lugar.append('Casa')

                    rival.append(row[5])

    return(list([distancia, acierto, tipoTiro, fechaJuego, lugar, rival]))