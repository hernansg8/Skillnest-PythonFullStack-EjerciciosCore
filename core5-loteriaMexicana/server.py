#########################
#|  PYTHON FULL STACK   |
#| CORE 5               |
#| Hernán Soto          |
#########################


from flask import Flask, render_template
import random

app = Flask(__name__)

colors = ['pink', 'blue', 'yellow'] #Colores disponibles

cards = [                           #Totalidad de cartas disponibles
    "1  El Gallo",
    "2  El Diablito",
    "3  La Dama",
    "4  El catrín",
    "5  El paraguas",
    "6  La sirena",
    "7  La escalera",
    "8  La botella",
    "9  El barril",
    "10 El árbol",
    "11 El melón",
    "12 El valiente",
    "13 El gorrito",
    "14 La muerte",
    "15 La pera",
    "16 La bandera",
    "17 El bandolón",
    "18 El violoncello",
    "19 La garza",
    "20 El pájaro",
    "21 La mano",
    "22 La bota",
    "23 La luna",
    "24 El cotorro",
    "25 El borracho",
    "26 El negrito",
    "27 El corazón",
    "28 La sandía",
    "29 El tambor",
    "30 El camarón",
    "31 Las jaras",
    "32 El músico",
    "33 La araña",
    "34 El soldado",
    "35 La estrella",
    "36 El cazo",
    "37 El mundo",
    "38 El apache",
    "39 El nopal",
    "40 El alacrán",
    "41 La rosa",
    "42 La calavera",
    "43 La campana",
    "44 El cantarito",
    "45 El venado",
    "46 El sol",
    "47 La corona",
    "48 La chalupa",
    "49 El pino",
    "50 El pescado",
    "51 La palma",
    "52 La maceta",
    "53 El arpa",
    "54 La rana"]

def getColor(index):                #Función para obtener el color correspondiente
    global colors                   #Acceder a la variable global de colores

    if index >= len(colors):        #Comprobar final del arreglo
        index = index%len(colors)   #volover y no repetir colores
    color = colors[index]

    return (color)

def fillDek(row,col):               #Función para llenar un mazo de RxC (row - col)
    global cards                    #Acceder a la variable global de cartas y hacer la seleccion
    selectedCards = random.sample(cards, row*col)
    index = 0
    r = []                          #variable para guardar la matriz de colores (RxC)

    for x in range(row):
        c = []
        for y in range(col):        #asignamos un color y una carta
            c.append({"color": getColor(x+y),"card": selectedCards[index]})
            index += 1
        r.append(c)

    return r

@app.route('/loteria')
def loteria():
    return render_template(
        'index.html',
        dek = fillDek(4,4),         #Llenamos el mazo de cartas (4x4)
        row = 4,                    #Filas
        col = 4                     #Columnas
        )

@app.route('/loteria/<int:row>')
def loteria_x(row):
    return render_template(
        'index.html',
        dek = fillDek(row,4),       #Llenamos el mazo de cartas (filas x 4)
        row = row,                  #Filas
        col = 4                     #Columnas
        )

@app.route('/loteria/<int:row>/<int:col>')
def loteria_xy(row, col):
    return render_template(
        'index.html',
        dek = fillDek(row,col),     #Llenamos el mazo de cartas (filas x columnas)
        row = row,                  #Filas
        col = col                   #Columnas
        )

if __name__=="__main__":
    app.run(debug=True)  