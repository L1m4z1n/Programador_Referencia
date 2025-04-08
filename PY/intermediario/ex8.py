#Verificar se um Array é Palíndromo

nome= ["arara","bola","laranja","mimim"]

for palavra in nome:
    if palavra == ''.join(reversed(palavra)):
        print(f"O palindromo de {palavra} é {palavra}")
    else:
        print("Não é um palíndromo")