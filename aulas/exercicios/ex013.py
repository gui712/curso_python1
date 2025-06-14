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
"""

cpf = '74682489070'
nove_digitos = cpf[:9]
contador_1 = 10
resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += (int(digito_1) * contador_1)
    contador_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

