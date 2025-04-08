#Fatorial de um número
#Crie uma função que calcula o fatorial de um número n (n! = n * (n-1) * (n-2) * ... * 1).

def fat(num):
    # --Explicação do Código--
# Enquanto o 'count' for menor ou igual a 'num', ele vai multiplicar o 'res' pelo valor atual do 'count', depois incrementa 'count' para continuar o loop, e retornará o valor calculado do fatorial
    res=1
    count=1
    while count <= num: 
        res *= count
        count+=1
    return res
n = int(input("Digite um número: "))
resultado =fat(n)
print(f"O fatorial de {n} é {resultado}")