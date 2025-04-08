#Crie uma função que receba um array e um valor, e retorne quantas vezes esse valor aparece no array.
def receber(array,valor):
    return array.count(valor)

meu_array = [1, 2, 3, 4, 2, 2, 5]
procura= 2
res = receber(meu_array, procura)
print(f'{procura} aparece {res} vezes!')
    
