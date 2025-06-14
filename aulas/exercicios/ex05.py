numero_str = input('Digite um número inteiro: ')


try:
    numero_convertido = int(numero_str)
    if(numero_convertido % 2 == 0):
        print(f'O  numero: {numero_convertido} é par')
    else:
        print(f'O  numero: {numero_convertido} é impar')
except:
    print('Não foi digitado um número inteiro')