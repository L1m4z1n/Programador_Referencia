#Nível Intermediário (POO)
#Sistema Bancário Simples
#Crie uma classe ContaBancária com atributos como saldo e titular.
#Funcionalidades: Adicione métodos para depositar(), sacar(), e verificarSaldo(). Implemente também um método para transferir dinheiro entre contas.

class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def depositar(self):
        deposito = int(input("Deposito: "))
        self.saldo+=deposito
        print(f"Seu novo saldo é de R${self.saldo}")

    def sacar(self):
        saca = int(input("Sacar: "))
        if saca <=self.saldo:
            self.saldo-=saca
            print(f"Seu novo saldo é de R${self.saldo}")

    def verificarSaldo(self):
        print(f"Saldo Atual: {self.saldo}")

verificar= ContaBancaria(1000,"Gabriel")
verificar.verificarSaldo()
verificar.depositar()
verificar.sacar()
