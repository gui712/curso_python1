#Operadpr lógico and
#Qualquer condição falsa avalia a expressão como false

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = '1234'
if (entrada == 'E' and senha_digitada == senha_permitida):
    print('Entrar')
else:
    print('Sair')


print(entrada)