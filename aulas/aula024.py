# Try except

numero = input('Vou dobrar o número que vc digitar: ')

numero_convertido = float(numero)

try:
    numero_convertido = float(numero)
    print(f'o dobro de {numero} é {numero_convertido * 2:.2f}')

except:
    print('Você não digitou um número')

