#########################
#|  PYTHON FULL STACK   |
#| CORE 4               |
#| Hernán Soto          |
#########################

from TarjetaCredito import TarjetaCredito

class Usuario:

    def __init__(self, nombre, apellido, email):
        print("")
        print(f"Nuevo Usuario: {nombre} {apellido}, bien venido!")
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = []
        tarjeta = TarjetaCredito(20000, 1.5) #Agregamos esta línea
        self.tarjetas.append(tarjeta)

    def hacerCompra(self, monto):
        print("")
        print(f"Realizando compra por el monto de ${monto}...")
        #permitir escoger tarjeta:
        for indice,tarjeta in enumerate(self.tarjetas):
            print(f"Tarjeta N° {indice})")
            tarjeta.mostrar_info_tarjeta()
        objetivo = int(input("Ingrese el número de tarjeta a utilizar:"))
        #validar selección:
        if objetivo < 0 or objetivo >= len(self.tarjetas):
            print("Error: ingresó mal su tarjeta!")
            return self
        #realizar compra:
        self.tarjetas[objetivo].compra(monto)
        return self

    def pagarTarjeta(self,monto):
        print("")
        print(f"Realizando pago por el monto de ${monto}...")
        #permitir escoger tarjeta:
        for indice,tarjeta in enumerate(self.tarjetas):
            print(f"Tarjeta N° {indice})")
            tarjeta.mostrar_info_tarjeta()
        objetivo = int(input("Ingrese el número de tarjeta a pagar:"))
        #validar selección:
        if objetivo < 0 or objetivo >= len(self.tarjetas):
            print("Error: ingresó mal su tarjeta!")
            return self
        #realizar pago:
        self.tarjetas[objetivo].pago(monto)
        return self
    
    def mostrarSaldo(self):
        print("")
        print(f"Hola {self.nombre} {self.apellido} su saldo es:")
        #para cada tarjeta del usuario:
        for indice,tarjeta in enumerate(self.tarjetas):
            print(f"Tarjeta N° {indice})")
            tarjeta.mostrar_info_tarjeta()

    def tarjetaNueva(self):
        self.tarjetas.append(TarjetaCredito(20000,1.5))


#EJERCICIO:

usuarioHernan = Usuario('Hernán', 'Soto','hernansg8@gmail.com')
# usuarioProfesor = Usuario('Sebastián','Poblete','sebapo@skillnest.com')

# usuarioHernan.hacerCompra(15000).mostrarSaldo()
# usuarioProfesor.hacerCompra(15000).pagarTarjeta(15000).mostrarSaldo()

#BONUS:

usuarioHernan.tarjetaNueva()
usuarioHernan.hacerCompra(15000).pagarTarjeta(10000).mostrarSaldo()