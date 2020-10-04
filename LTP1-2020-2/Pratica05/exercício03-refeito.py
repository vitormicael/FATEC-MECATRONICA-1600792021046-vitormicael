valor_a = float(input('Informe o valor de a: '))
valor_b = float(input('Informe o valor de b: '))
valor_c = float(input('Informe o valor de c: '))
delta = (valor_b**2) - (4*valor_a*valor_c)
if delta < 0:
  print('Não tem raizes real')
elif delta > 0:
  x1 = (-valor_b + delta**0.5) / (2*valor_a)
  x2 = (-valor_b - delta**0.5) / (2*valor_a)
  print('O Valor de x1 é', x1, 'O valor de x2 é', x2)
else:
  x2 = (-valor_b - delta**0.5) / (2*valor_a)
  print('Raiz de x é', x2)
