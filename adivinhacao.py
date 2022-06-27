import random

print("*********************************")
print('Bem vindo ao jogo de Adivinhação!')
print("*********************************")


numero_secreto = random.randrange(1,101)
numero_de_tentativas = 0

print('Qual o nível de dificuldade? ')
print('(1) Fácil (2) Médio (3) Difícil ')
nivel = int(input('Digite o nível desejado: '))

if nivel == 1:
  numero_de_tentativas = 20
elif nivel == 2:
  numero_de_tentativas = 10
else:
  numero_de_tentativas = 5

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
