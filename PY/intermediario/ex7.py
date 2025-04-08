#O Implemente uma função que recebe um array e um número, e retorne o índice da primeira ocorrência desse número no array. Caso o número não exista, retorne -1.

def receber(num):
    array=[44,25,41,7,89,5,6]
    if num in array:
         return array.index(num)
    else:
         return -1
num=1
res= receber(num)
print(f"{res}")
