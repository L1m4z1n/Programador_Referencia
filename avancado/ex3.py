#Contagem de vogais e consoantes
#Escreva um programa que recebe uma string e conta quantas vogais e consoantes ela contém.

def contador(palavra):
    vogais ="aeiouAEIOU"
    consoantes= "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contar_v=0
    contar_c=0

    for letra in palavra:
        if letra in vogais:
            contar_v += 1
        elif letra in consoantes:
            contar_c +=1

    return contar_v, contar_c
    
palavra = input("Digite uma palavra:")
contador_vogal,contador_consoante = contador(palavra)
print(f"A palavra {palavra}\n Possui {contador_vogal} Vogais\n Possui {contador_consoante} Consoantes")