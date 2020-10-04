operacao = input('Informe a operação desejada:')
#soma
if operacao == '+':
  valor1 = float(input('Valor 1:'))
  valor2 = float(input('Valor 2:'))
  resultado = valor1 + valor2
  print(resultado)
#subtração
elif operacao == '-':
  valor1 = float(input('Valor 1:'))
  valor2 = float(input('Valor 2:'))
  resultado = valor1 - valor2
  print(resultado)
#multiplicação
elif operacao == '*':
  valor1 = float(input('Valor 1:'))
  valor2 = float(input('Valor 2:'))
  resultado = valor1 * valor2
  print(resultado)
#divisão
elif operacao == '/':
  valor1 = float(input('Valor 1:'))
  valor2 = float(input('Valor 2:'))
  if valor2 == 0:
    print('Não é possível dividir um número por zero!')
  else:
    resultado = valor1 / valor2
    print(resultado)
else:
  print('Operacao inválida!')
