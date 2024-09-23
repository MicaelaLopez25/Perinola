

class Jugador: 
    def __init__(self):
      self.fichas = 5
      self.nombre= ['j1','j2','j3','j4']

    def __repr__(self): 
      return f"{self.nombre[0]} tiene: {self.fichas} fichas."
    
    def darFicha(self, cuantas=1): 
       self.fichas += cuantas
    
    def sacarFicha(self, cuantas=1):
       if (cuantas > self.fichas):
         raise ValueError ("El numero de fichas a sacar es mayor a las fichas del jugador, (jugador fichas: {self.fichas}, fichas a sacar: {cuantas}) ")
       self.fichas = self.fichas - cuantas

    def tieneFicha(self, cuantas=1):
       return (self.fichas >= cuantas )
    
    def sinFichas(self):
       return (self.fichas == 0)


J = Jugador()
result = J.sacarFicha(2)
print(J)
print(result)