nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if(nome != '' and idade != ''):
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if '' in nome:
        print(f'o nome {nome} tem espaços!!')
    else:
        print(f'O nome {nome} não tem espaços')
    print(f'Sua idade é: {idade}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')