frase = 'O Python é  uma linguagem de programação'\
        'multiparadigma. '\
        'Python foi criado por Guido van Rossum.'

print(frase.count('Python'))

qtd_apareceu = 0
letra_mais_apareceu = ''

i = 0
while(i < len(frase)):
    letra_atual = frase[i]

    if(letra_atual == ' '):
        i += 1
        continue

    quantas_vezez_letra = frase.count(letra_atual)

    if(qtd_apareceu < quantas_vezez_letra):
        qtd_apareceu = quantas_vezez_letra
        letra_mais_apareceu = letra_atual

    i += 1

print(f'A letra que mais apareceu foi: '
      f'{letra_mais_apareceu} '
      f'{qtd_apareceu} vezes')