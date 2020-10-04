comprimento = float(input('Digite em metros o comprimento de cada placa '))

lagura = float(input('Digite em metros a lagura de cada placa '))

tamanho = lagura*comprimento

print(f'o tamanho em metros² de cada placa é {tamanho}²')

comprimento_wall = float(input('Digite em metros o comprimento da sua parede'))

lagura_wall= float(input('Digite em metros a lagura da sua parede '))

tamanho_wall = lagura_wall*comprimento_wall

print(f'o tamanho em metros² da sua parede é de {tamanho_wall}²')
tplacas = tamanho_wall/tamanho 
print(f'voce vai precisar de {tplacas} placas para essa parede')

