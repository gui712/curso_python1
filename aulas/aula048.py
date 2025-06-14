#join e split
# split divide um string strip corta os espacos
frase = 'Olha só que, coisa interessante'

lista_palavras = frase.split()
lista_frases = frase.split(',')
lista_nova = []
print(lista_palavras)
print(lista_frases)

for i, frase in enumerate(lista_frases):
    lista_nova.append(lista_frases[i].strip())

print(lista_nova)

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)