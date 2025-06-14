#Desempacotamento
lista1 = ['Maria', 'Helena', 'Eduarda']

nome1, nome2, *resto = lista1

#print(nome1)

string = 'ABC'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python','é', 'legal'

a, b, *_,c = lista
print(a,c)
print(*string)
print(*lista)