print("*********************************")
print('Bem vindo ao jogo de Adivinhação!')
print("*********************************")

numero_secreto = 45
numero_de_tentativas = 3
rodada = 1

while(rodada <= numero_de_tentativas):
  print(f'Tentativa {rodada} de {numero_de_tentativas}')
  chute = int(input('Digite seu chute: '))

  print(f'Você digitou {chute}')

  acertou = numero_secreto == chute
  maior = chute > numero_secreto
  menor = chute < numero_secreto

  if(acertou):
    print("Você acertou!!")
  elif(maior):
    print("Você errou, o chute foi maior que o número")
  elif(menor):
    print("Você errou, o chute foi menor que o número")
  
  rodada += 1
