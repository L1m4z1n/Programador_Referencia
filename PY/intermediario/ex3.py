#Ordenar um vetor
#Escreva um programa que recebe um vetor de números inteiros e ordena ele em ordem crescente.

def crescente(num):
    res= sorted(num)
    return res
numeros = [44,25,41,7,89,5,6,32,1,24,-5,-10,0]
res =crescente(numeros)
print(f"{res}")