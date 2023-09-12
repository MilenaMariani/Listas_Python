palavras = ["bike", "carro", "motocicleta", "barquinho"]
palavra = []
for n in palavras:
    tamanho = len(n)
    if tamanho > 5:
        palavra.append (n)
    
print (palavra)