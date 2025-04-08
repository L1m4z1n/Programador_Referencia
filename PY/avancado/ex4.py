#Ordenar um Array
#Crie uma função que ordene um array de números em ordem crescente.

def ordem(array):
    org= sorted(array)
    return org

array =[20,500,78,90,-100,10,2,6,4,5]
res = ordem(array)
print(res)