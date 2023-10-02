from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def conducir(self):
        pass

    @abstractmethod
    def volar(self):
        pass

class Automovil(Transporte):
    ruedas = 4

    def __init__(self, color, marca, aceleracion):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += self.aceleracion

    def frenar(self):
        self.velocidad -= self.aceleracion


    def conducir(self):
        print("Conduciendo automóvil")

    def volar(self):
        print("volando")
        pass  # No se puede volar en un automóvil
  
auto = Automovil("rojo", "bmw", 70)
auto2 = Automovil("gris", "bmw", 80)

print("Aceleracion:", auto.aceleracion)
print("Ruedas:", auto.ruedas)

# Modify acceleration auto 1
auto.aceleracion = 50
print("----------AUTO 1:--------------", auto.aceleracion)
auto.conducir()
print('Auto 1 velocidad de:', auto.velocidad)
auto.acelerar()
print('Auto 1 velocidad de:', auto.velocidad)
auto.acelerar()
print('Auto 1 velocidad de:', auto.velocidad)
auto.frenar()
print('Auto 1 velocidad de:', auto.velocidad)

# Modify acceleration auto 2
auto2.aceleracion = 150
print("-------------AUTO 2:--------------", auto2.aceleracion)
auto2.conducir()
print('Auto 2 velocidad de:', auto2.velocidad)
auto2.acelerar()
print('Auto 2 velocidad de:', auto2.velocidad)
auto2.frenar()
print('Auto 2 velocidad de:', auto2.velocidad)
auto2.frenar()
print('Auto 2 velocidad de:', auto2.velocidad)




class AutomovilVolador(Automovil):
    ruedas = 6


    def __init__(self, color, marca, aceleracion, estaVolando=True):
        super().__init__(color, marca, aceleracion)
        self.estaVolando = estaVolando

    def vuela(self):
        self.estaVolando = True

    def noVuela(self):
        self.estaVolando = False

    
print("---------AUTO VOLADOR----------")
volador = AutomovilVolador("rojo", "ford", 90.0, False)  # Aceleración en decimal
volador.volar()