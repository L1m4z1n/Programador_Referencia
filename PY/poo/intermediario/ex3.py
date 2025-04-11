#Sistema de Notificação
#Crie uma classe Notificacao que tenha os atributos mensagem, data e lido.
#Funcionalidades: Implemente métodos para marcar como lida, exibir a notificação e verificar se ela foi lida.
from datetime import datetime
class Notificacao:
    def __init__(self,exibir,data,lido):
        self.exibir=exibir
        self.data=data
        self.lido=lido

    def get_exibir(self):
        return self.exibir
    
    def set_exibir(self):
        if self.exibir == 1:
            print(self.exibir)
        else:
            return 0

    def get_ler(self):
        return self.ler 

    def set_ler(self):
        if self.ler == self.lido:
            self.data = datetime.now().date()
            print("Notificação Vista as {self.data}!")
        else:
            print("Mensagem Disponivel!")


n = Notificacao("Olá","Date:","Mensagem Lida")
n.get_ler()
n.set_ler()
