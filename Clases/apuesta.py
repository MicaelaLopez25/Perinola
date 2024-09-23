class Apuesta:
    def __init__(self) :
       self.fichas = 0

    def __repr__(self):
        return f'Apuesta: {self.fichas} fichas'
    
    def ponerFicha (self, cuantas=1):
      self.fichas = self.fichas + cuantas

    def tomarFicha (self, cuantas=1):
      if (cuantas > self.fichas):
       raise ValueError("No hay tantas fichas (no se pueden sacar {cuantas} quedan {self.fichas})  ")
      self.fichas = self.fichas - cuantas

    def tieneFicha(self, cuantas=1):
       return (self.fichas >= cuantas )
    
    def estaVacia(self):
       return (self.fichas == 0)
    
a = Apuesta()
print(a)
a.ponerFicha()
print(a)
a.ponerFicha(2)
print(a)
