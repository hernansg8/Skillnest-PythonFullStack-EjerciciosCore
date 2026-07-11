#########################
#|  PYTHON FULL STACK   |
#| CORE 2               |
#| Hernán Soto          |
#########################

#1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]

print("")
print("-[1]--------------------------")

matriz[1][0] = 6
print(matriz)

cantantes[0]["nombre"]="Enrique Martin Morales"
print(cantantes)

ciudades["México"][2]="Monterrey"
print(ciudades)

coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

#2. Iterar a través de una lista de diccionarios

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

def iterarDiccionario(list):
    for item in list:
        cantante = ""
        for clave in item:
            cantante += clave + " - " + item[clave]
            if clave == "nombre" :
                cantante += ", "
        print(cantante)

print("")
print("-[2]--------------------------")

iterarDiccionario(cantantes)


#3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(key,list):
    for item in list :
        print(item[key])

print("")
print("-[3]--------------------------")

iterarDiccionario2("nombre",cantantes)
iterarDiccionario2("pais", cantantes)

#4. Iterar a través de un diccionario con valores de lista

costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def imprimirInformacion(diccionario):
    for key in diccionario:
        print(key, "(", len(diccionario[key]), ")")
        for item in diccionario[key]:
            print(item)

print("")
print("-[4]--------------------------")

imprimirInformacion(costa_rica)

print("")