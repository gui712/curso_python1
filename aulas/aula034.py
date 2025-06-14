texto = "Python"

i = 0 
tamanho = len(texto)

while i < tamanho:
    print(texto[i])
    i += 1

print('Fim do While')

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'

print(novo_texto)


nome = 'Guilherme'

for letra in nome:
    print(letra)