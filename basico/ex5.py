#Crie um programa que receba um array de números e calcule a soma de todos os seus elementos.
elementos = []
while True:
    valor= int(input("Digite os valores: "))
    if valor == 0:
        print("Paroooou")
        break  
    elementos.append(valor)
soma = sum(elementos) 
print(f"A soma dos valores dentro do array é igual a {soma}")
print(f"Esses são os elementos guardados {elementos}")