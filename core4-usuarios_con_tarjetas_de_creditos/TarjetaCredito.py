#########################
#|  PYTHON FULL STACK   |
#| CORE 3               |
#| Hernán Soto          |
#########################

class TarjetaCredito:

    todas_las_tarjetas = []

    #Incluye en este método valores por default
    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.limite_credito = limite_credito
        self.intereses = intereses/100
        self.saldo_pagar = saldo_pagar
        #Agregar al listado total:
        TarjetaCredito.todas_las_tarjetas.append(self)
        print(f"Tarjeta creada con éxito.")

    def compra(self, monto):
        #Comprobar límite de credito:
        if (self.saldo_pagar + monto) > self.limite_credito:
            print(f"Error: Tarjeta Rechazada, has alcanzado tu límite de crédito, cupo disponible: ${self.limite_credito - self.saldo_pagar}")
        else:
            self.saldo_pagar += monto
            print(f"Compra realizada con éxito (monto:${monto})")
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        print(f"Pago realizado con éxito (monto:${monto})")
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: ${self.saldo_pagar} - cupo disponible: ${self.limite_credito - self.saldo_pagar}")

    def cobrar_interes(self):
        interes = self.saldo_pagar * self.intereses
        self.saldo_pagar += interes
        print(f"Intereses aplicados (${interes})")
        return self
    
    @classmethod
    def mostrar_todas_tarjetas(cls):
        for indice,tarjeta in enumerate(cls.todas_las_tarjetas):
            print(f"__Tarjeta {indice}:__________________________________")
            print(f"    Saldo a pagar: ${tarjeta.saldo_pagar}")
            print(f"    Límite de crédito: ${tarjeta.limite_credito}")
            print(f"    Interes: {tarjeta.intereses*100}%")

# #EJERCICIO:
# print("")#Salto de linea

# # Crea 3 tarjetas:

# hernan_cmr = TarjetaCredito(3000000,2)
# hernan_crut = TarjetaCredito(1000000, 3)
# hernan_bci = TarjetaCredito(2000000, 4, 100000)
# print("")#Salto de linea

# # Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.

# hernan_cmr.compra(800000).compra(50000).pago(850000).cobrar_interes().mostrar_info_tarjeta()
# print("")#Salto de linea

# # Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.

# hernan_crut.compra(10000).compra(25000).compra(15000).pago(20000).pago(20000).cobrar_interes().mostrar_info_tarjeta()
# print("")#Salto de linea

# #Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. Luego muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.

# hernan_bci.compra(1200000).compra(200000).compra(150000).compra(200000).compra(200000).mostrar_info_tarjeta()
# print("")#Salto de linea

# #BONUS: crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas. En el capítulo pasado te dimos algunas pistas de cómo realizarlo.

# TarjetaCredito.mostrar_todas_tarjetas()
# print("")#Salto de linea