contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        continue

    if(contador >= 10 and contador <= 26):
        print('Não vou mostrar o ', contador)
        continue
    print(contador)

    if contador == 25:
        break

print('Acabou')
