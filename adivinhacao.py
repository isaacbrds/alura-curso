import random

print("*********************************")
print('Bem vindo ao jogo de Adivinhação!')
print("*********************************")


numero_secreto = random.randrange(1,101)
numero_de_tentativas = 3
rodada = 1

for rodada in range(1, numero_de_tentativas + 1):
  print(f'Tentativa {rodada} de {numero_de_tentativas}')
  chute = int(input('Digite seu chute: '))

  print(f'Você digitou {chute}')

  if(chute < 1):
    print('Você digitou um número inválido ')
  acertou = numero_secreto == chute
  maior = chute > numero_secreto
  menor = chute < numero_secreto

  if(acertou):
    print("Você acertou!!")
    break
  elif(maior):
    print("Você errou, o chute foi maior que o número")
  elif(menor):
    print("Você errou, o chute foi menor que o número")
  
  rodada += 1
