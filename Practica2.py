import csv

def limpieza_de_datos():
   
    distancia = []
    tiempo = []
    tipoTiro = []
    fechaJuego = []
    lugar = []
    rival = []

    nombreColumna = True

    with open('kobe_shots.csv', 'rt') as f:
      
        reader = csv.reader(f)

        for row in reader:
            
            if(len(row) > 0):
                
                if(nombreColumna == True):

                    distancia.append(row[13])
                    tiempo.append(row[8])
                    tipoTiro.append(row[15])
                    fechaJuego.append(row[21])
                    lugar.append(row[22])
                    rival.append(row[23])
                    nombreColumna = False
   
                else:

                    distancia.append(int(row[13]))
                    tiempo.append(str(row[8] + ':' + row[12]))
                    tipoTiro.append(row[15])
                    fechaJuego.append(row[21])
                    
                    if(str(row[22]).find('@') > 0):

                        lugar.append('Visitante')

                    elif(str(row[22]).find('vs.') > 0):

                        lugar.append('Casa')

                    else:

                        lugar.append('Indefinido')

                    rival.append(row[23])
                    
    return(list([distancia, tiempo, tipoTiro, fechaJuego, lugar, rival]))

print(limpieza_de_datos())