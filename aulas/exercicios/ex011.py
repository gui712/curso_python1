lista = ['Maria', 'Helena', 'Luiz']
contador = 0

for nome in lista:
    print(contador, nome)
    contador +=1


lista2 = ['Maria', 'Helena', 'Guilherme']
indices = range(len(lista2))

for indice in indices:
    print(indice, lista2[indice], type(lista2[indice]))
