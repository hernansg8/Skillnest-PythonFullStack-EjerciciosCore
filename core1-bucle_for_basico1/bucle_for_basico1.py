#########################
#|  PYTHON FULL STACK   |
#| CORE 1               |
#| Hernán Soto          |
#########################

# Ejercicio 1. Básico:
print("__Ejercicio 1. Básico:_____________________________")

for x in range (101):
    print(x)

# Ejercicio 2. Múltiples de 2:
print("__Ejercicio 2. Múltiples de 2:_____________________")

for x in range (2,501):
    if x%2 == 0 :
        print(x)

# Ejercicio 3. Contando Vanilla Ice:
print("__Ejercicio 3. Contando Vanilla Ice:_______________")

for x in range (1,101):
    if x%10 == 0 :
        print("baby")
    elif x%5 == 0 :
        print("ice ice")
    else:
        print(x)

# Ejercicio 4. WoW. Número gigante a la vista:
print("__Ejercicio 4. WoW. Número gigante a la vista:_____")
wow = 0

for x in range(500001):
    if x%2 == 0 :
        wow += x

print(f"Suma total: {wow}")

# Ejercicio 5. Regrésame al 3:
print("__Ejercicio 5. Regrésame al 3:_____________________")

for x in range(2024,0,-3):
    print(x)

# Ejercicio 6. Contador dinámico:
print("__Ejercicio 6. Contador dinámico:__________________")

numInicial = 8
numFinal = 88
multiplo = 8

for x in range (numInicial,numFinal+1):
    if x%multiplo == 0 :
        print (x)