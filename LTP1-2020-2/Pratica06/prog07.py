#estrutura de repetição
numero_secreto = 8

acertou = False

while acertou == False:
  chute = float(input('Informe seu chute: '))
  if chute > numero_secreto:
    print('Errou por alto!')
  elif chute < numero_secreto:
    print('Errou por baixo!')
  else:
    acertou = True
    print('Acertou!')
print('Obrigado por jogar')
