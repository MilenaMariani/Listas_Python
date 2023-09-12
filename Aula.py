#vetor
numeros = [1, 2, 3, 4, 5,]
frutas = ["maçã", "banana", "laranja", "uva"]
vazia = []

print(numeros)
print(frutas)
print(vazia)

print(numeros[0])
print ("*"*10)

for n in numeros:
    print(n)

#append
for n in range (0 , 10):
    vazia.append (n)
    print (vazia)
    #len soma de itens
    print (len(vazia))
#remove
    if n %2 == 0:
        vazia.remove(n)

#concatenacao
frutas = [ "maçã", "banana", "chocolate" ]
bobeiras = ["biscoitos", "pizza", "hamburguer"]
comidas = frutas + bobeiras
print(comidas)

#subconjunto so pegar de alguma posicao, uma determinada posicao, um bloco da posicao 
num = [ 1, 2 ,3 ,4]
sublista_num = numeros[1:4] #inicial e final, sempre pega um anterior e um antes do ultimo
print(sublista_num)