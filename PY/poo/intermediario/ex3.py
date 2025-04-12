#Sistema de Notificação
#Crie uma classe Notificacao que tenha os atributos mensagem, data e lido.
#Funcionalidades: Implemente métodos para marcar como lida, exibir a notificação e verificar se ela foi lida.
from datetime import datetime
class Notificacao:
    def __init__(self,mensagem):
        self.mensagem=mensagem
        self.data=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.lido= False

    def marca_como_lido(self,condicao):
        if condicao == 1:
            if not self.lido:
                self.lido = True
                self.data=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"A mensagem foi lida as {self.data}")
            else:
                print("Notificação já foi lida!")
        else:
            print("Mensagem não lida!!")

    def exibir_not(self):
        status="Lido!" if self.lido else "Não lida!"
        print(f"Mensagem: {self.mensagem} \nData: {self.data} \nStatus: {status}")

n = Notificacao("Você tem uma notificação recebida!")
n.exibir_not()

try:
    condicao=int(input("Digite '1' para marcar como lida ou outro número para ignorar:\n"))
    n.marca_como_lido(condicao)
except ValueError:
    print("Insira um número válido!!")

n.exibir_not()
