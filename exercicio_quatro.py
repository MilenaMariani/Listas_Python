lista_de_compras = []

continuar = ""

while continuar != "parar":
    itens = (input("Digite os itens que deseja comprar: "))
    lista_de_compras.append (itens)

    continuar = (input("deseja continuar ou parar?: "))
    if continuar == 'parar':
        break
    
print(lista_de_compras)