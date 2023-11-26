from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv

def lectura():
    
    datos= ""
    info = ""

    with open('Kobe_shots_cleanData.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if(len(row) > 0):
                datos = row[6]
                info = info + datos
                datos = ""
    return(info)

wordCloud = WordCloud().generate(lectura())

plt.imshow(wordCloud, interpolation='bilinear')
plt.axis('off')

image = wordCloud.to_image()
image.save('Graficas_P10/Nombres.png')