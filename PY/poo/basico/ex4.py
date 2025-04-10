#Retângulo
#Crie uma classe Retângulo com atributos largura e altura.
#Funcionalidades: Adicione métodos para calcular a área e o perímetro do retângulo.

class Retangulo:
    def __init__(self,largura,altura):
        self.largura=largura
        self.altura=altura

    def calc(self):
          perimetro=2*(self.largura+self.altura)
          area=self.largura*self.altura
          print(f"O perimetro é igual a {perimetro}")
          print(f"A área é igual a {area}")

retangulo= Retangulo(20,5)
retangulo.calc()
