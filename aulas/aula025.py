#Constante = variaveis que nao mudam

velocidade = 61
local_carro = 101


RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_radar1 = velocidade > RADAR_1 
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and  local_carro <= (LOCAL_1 + RADAR_RANGE)

if(vel_carro_radar1):
    print('Velocidade carro passou do radar 1')

if(carro_multado and vel_carro_radar1):
    print('Carro multado')