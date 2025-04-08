#Buscar Elemento em um Array

def busca(num,lista):
    if num in lista:
        print(f"{num}")
    else:
        print(f"Não tem esse valor na lista")
    return num
numeros = [44,25,41,7,89,5,6,32,1,24,-5,-10,0]
find = int(input("Qual elemento você acha que está na lista:"))
res =busca(find,numeros)

