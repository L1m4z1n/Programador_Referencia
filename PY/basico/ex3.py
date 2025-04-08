#Tabuada
#Crie um programa que recebe um número e imprime a tabuada desse número de 1 até 10.

x = int(input("Numero: "))
for i in range(10):
    i+=1
    tabu = i*x
    print(f"{i}x{x}={tabu}")