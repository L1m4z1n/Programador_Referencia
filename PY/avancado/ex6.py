#Remover Elementos Duplicados
#Implemente uma função que recebe um array e remova todos os elementos duplicados, retornando um novo array com os valores únicos.

def dropduo(array):
    num= set(array)
    return num

array = [1,1,2,2,3,4,5,5,6,6,7]
res= dropduo(array)
print(res)