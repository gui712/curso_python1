#validar o segundo digito do cpf

"""
Calculo primeiro digito_ do cpf
cpf: 746.824.890-70
Soma de todos os numeros multiplicando cada valor por uma contagem regressiva começando por 10

Ex: 746 824 890 70
10  9  8  7  6  5  4  3 2    
*7  4  6  8  2  4  8  9 0
70 36 48 56 12 20 32 27 0

somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
multiplicar o resultado por 10
301*10 = 3010
obter o resto da divisao da conta anterior por 11
3010 % 11 = 7

se o resultado for maior que 9 usa o 0
se o resultado for menor ou = a 9 usa o numero

para o segundo digito tem que incluir o primeiro digito e fazer a multiplicação dessa vez iniciando por 11
"""
import re 

#cpf = '746.824.890-70'\
#.replace('.','').replace('-','')

cpf = re.sub(
    r'[^0-9]',
    '',
    '746.824.890-70'
)

nove_digitos = cpf[:9]
contador_1 = 10
resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += (int(digito_1) * contador_1)
    contador_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
resultado_digito_2 = 0
contador_2 = 11

for digito_2 in dez_digitos:
    resultado_digito_2 += (int(digito_2) * contador_2)
    contador_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == novo_cpf:
    print(f'{cpf} é váliido')
else:
    print(f'CPF Inválido')