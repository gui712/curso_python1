#listas + listas

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduardo', (0,10,20,30,40)]
]

print(salas[0][1])
print(salas[2][3][2])

for sala in salas:
    for aluno in sala:
        print(aluno)