#Crie uma função que imprima todos os elementos de um array um por um.
def imprimir(elementos):
    for elemento in elementos:
        print(elemento)
elementos = [20,500,78,90,-100,10,2,6,4,5]
imprimir(sorted(elementos))

