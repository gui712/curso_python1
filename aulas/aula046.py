# enumerate - enumera iteráveis(indices)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

#lista_enumerada = enumerate(lista) O enumerate não é muito utilizado dessa forma no python porque ele esgota a lista
#for item in lista_enumerada:
#    print(item)

#dessa forma podemos fazer quantos for forem necessarios
#caso queira ver a lista enumerada tem que converter ela em lista

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)