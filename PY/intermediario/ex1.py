#Verificar se um número é primo
#Escreva um programa que recebe um número e verifica se ele é primo ou não.

def primo(numero):
    if numero < 2:
        return False  # Números menores que 2 não são primos
    for i in range(2, numero):  # Verificar todos os números de 2 até (numero - 1)
        if numero % i == 0:  # Se o número for divisível por `i`, não é primo
            return False
    return True  # Se não encontrou nenhum divisor, é primo

n = int(input("Digite um número: "))
if primo(n):
    print("É primo!")
else:
    print("Não é primo!")

