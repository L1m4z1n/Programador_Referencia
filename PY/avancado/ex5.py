#Média de Números Positivos
#Crie uma função que receba um array de números e calcule a média apenas dos números positivos presentes nele.
def medpos(array):
    positivos = [num for num in array if num > 0] #Verifica se o número é positivo
    if positivos:
        return (sum(positivos))/int(len(positivos))
    else:
        return 0
array = [2,2,-2]
res = medpos(array)
print(res)