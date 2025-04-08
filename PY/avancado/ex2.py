#Calculadora simples
#Crie uma calculadora que faça as operações de soma, subtração, multiplicação e divisão, recebendo os números e a operação do usuário.

def calculadora(op):
    match op:
        case 1:
            x=int(input("Digite o primeiro valor: "))
            y=int(input("Digite o segundo valor: "))
            s=x+y
            return s
        case 2:
            x=int(input("Digite o primeiro valor: "))
            y=int(input("Digite o segundo valor: "))
            sb=x-y
            return sb
        case 3:
            x=int(input("Digite o primeiro valor: "))
            y=int(input("Digite o segundo valor: "))
            m=x*y
            return m
        case 4:
            x=int(input("Digite o primeiro valor: "))
            y=int(input("Digite o segundo valor: "))
            d=x/y
            return d
        
op=int(input("Selecione qual operação será a desejada: \n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n"))

res= calculadora(op)
print(res)