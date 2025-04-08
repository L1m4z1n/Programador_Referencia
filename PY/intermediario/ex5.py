#Crie uma função que inverta um array, ou seja, faça o último elemento se tornar o primeiro e assim por diante.

# --O mesmo do código passado--
def inverter(num):
    res= num.reverse()
    return num
numeros = [44,25,41,7,89,5,6,32,1,24,-5,-10,0]
res =inverter(numeros)
print(f"{res}")