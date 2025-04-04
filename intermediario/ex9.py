#Crie uma função que verifique se um array de números é um palíndromo (se o array for o mesmo lido da esquerda para a direita e da direita para a esquerda).

def palindromo(num, array):
    for num in array:
        if num == ''.join(reversed(num)):
            print(f"O palíndromo de {num} é {num}!")
        else:
            print(f"{num} não é um palíndromo!")

array=["44","39","22","10"]
num=0
res = palindromo(num,array)
print(res)
