#Somar os números de 1 a N
#Escreva um programa que recebe um número N e imprime a soma de todos os números de 1 a N.

x = int(input("Numero: "))
soma=0
i=1
while i <= x:
    
    soma =soma + i
    i= i+1
    print(soma)