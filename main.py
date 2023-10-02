class Automovil:
  ruedas=4
  def __init__(self,color,marca,aceleracion) :
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=0

auto=Automovil("rojo","bmw",70)
print("aceleracion ", auto.aceleracion)
print("ruedas ",auto.ruedas)

#mod aceleracion
auto.aceleracion=50
print(auto.aceleracion)

def acelerar():
  auto.velocidad+=auto.aceleracion
  print("velocidad aumenta a:" ,auto.velocidad)
def frenar():
  auto.velocidad-=auto.aceleracion
  print("velocidad baja a:" ,auto.velocidad)  

print("aceleraa:")
acelerar()
print("frenaa:")
frenar()
print("frenaa:")
frenar()