## estrutura de decisão
temp_limite = float(input('Informe uma temperatura limite: '))
temp_atual = float(input('Informe a temperatura atual: '))
##
if temp_atual >= temp_limite:
  print('A temperatura está acima do limite adequado')
elif temp_atual <= temp_limite:
  print('A temperatura está abaixo do limite')
