#Controle de Carro
#Crie uma classe Carro com atributos como modelo, ano, cor e placa.
#Funcionalidades: Defina métodos como ligar(), desligar(), acelerar(), etc.
class Carro:
    def __init__(self, modelo, ano, cor, placa):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa

    def ligar(self):
        print(f"O carro {self.modelo} do ano de {self.ano} da cor {self.cor} com o número da placa {self.placa} ligou!")   

    def desligar(self):
        print(f"O carro {self.modelo} do ano de {self.ano} da cor {self.cor} com o número da placa {self.placa} desligou!")            

    def acelerar(self):
        print(f"O carro {self.modelo} do ano de {self.ano} da cor {self.cor} com o número da placa {self.placa} acelerou!")            

carro = Carro("Fiat",2020,"Cinza","GLA2347")
carro.ligar()
carro.desligar()
carro.acelerar()