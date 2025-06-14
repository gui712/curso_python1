hora = input("Digite o horario: ")

try:
    hora_convertido = int(hora)
    if(hora_convertido >= 0 and hora_convertido <= 11):
        print("Bom dia!")
    elif(hora_convertido >= 12 and hora_convertido <= 17 ):
        print("Boa tarde")
    elif(hora_convertido >= 18 and hora_convertido <= 23 ):
        print("Boa noite")
    else:
        print("Não foi digitado um horario valido!!!")

except:
    print("Não foi digitado um horario valido!!!")