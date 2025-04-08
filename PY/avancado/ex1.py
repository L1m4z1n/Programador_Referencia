#Palíndromo
#Crie uma função que recebe uma string e retorna true se ela for um palíndromo (se pode ser lida da mesma forma de trás para frente), ou false caso contrário.

def palindromo(nome,array):
    for nome in array:
        if nome == ''.join(reversed(nome)):
            return True
        else:
            return False
    return nome
array = []
nome = input("Digite alguma palavra:\n")
array.append(nome)
res = palindromo(nome, array)
print(res)