lista  = [1, 1, 2, 3, 4, 4, 5, 5, 6]
duplicado = [] 
for n in lista:
    if n not in duplicado:
        duplicado.append(n) 
print(duplicado)
    