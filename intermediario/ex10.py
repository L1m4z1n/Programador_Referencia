#Função de Média
def media(num1,num2):
    media= (num1+num2)/2
    return media

n1=int(input("Digite o número:"))
n2=int(input("Digite o número:"))
res = media(n1,n2)
print(f"A média é igual a {res}")

