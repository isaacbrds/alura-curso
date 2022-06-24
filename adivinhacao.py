print("*********************************")
print('Bem vindo ao jogo de Adivinhação!')
print("*********************************")

numero_secreto = 45

chute = int(input('Digite seu chute: '))

print(f'Você digitou {chute}')

if(numero_secreto == chute):
  print("Você acertou!!")
else:
  print("VocEê errou")
