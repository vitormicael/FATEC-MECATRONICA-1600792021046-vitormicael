# Informe os valores
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
valor3 = int(input('Informe o terceiro valor: '))
# o maior valor
if valor1 >= valor2 and valor1 >= valor3:
  maior = valor1
  print('o maior valor é', valor1)
elif valor2 >= valor1 and valor2 >= valor3:
  maior = valor2
  print('o maior valor é', valor2)
else:
  maior = valor3
  print('o maior valor é', maior)
## o menor valor
if valor1 <= valor2 and valor1 <= valor3:
  menor = valor1
  print('o menor valor é', valor1)
elif valor2 <= valor1 and valor2 <= valor3:
  menor = valor2
  print('o menor valor é', valor2)
else:
  menor = valor3
  print('o menor valor é', menor)
# a média dos valores
media = (valor1 + valor2 + valor3) / 3
print('a média dos três valores é',media)
