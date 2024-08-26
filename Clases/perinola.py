from random import choice

class Perinola:


    def __init__(self) :
      self.caras_visible = 'Toma 1'
      self.caras_posibles = 'Pon 1', 'Pon 2','Toma 1', 'Toma 2', 'Todos Toman','Ponen Todos'

    def __repr__(self):
       return f'salio: {self.caras_visible}'
    
    def tirar(self):
       caras = ('Pon 1', 'Pon 2','Toma 1', 'Toma 2', 'Todos Toman','Ponen Todos')
       self.caras_visible = choice(caras)
       return self.caras_visible
       

p = Perinola()
result = p.tirar()
print(p)
print(result)