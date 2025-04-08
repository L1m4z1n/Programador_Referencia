#Mesclar Dois Arrays
#Crie uma função que mescle dois arrays em um só, garantindo que os elementos dos dois arrays estejam ordenados ao final.

def mesclar(ar,ray):
    a=ar
    b = ray
    mes= a,b
    return mes

ar = [1,2,3,4,5,6,7]
ray = [20,500,78,90,-100,10,2,6,4,5]
res = mesclar(ar,ray)
print(res)