a = float(input('Coeficiente A:'))
b = float(input('Coeficiente B:'))
c = float(input('Coeficiente C:'))
delta = (b**2) - (4*a*c)
if delta < 0:
  print('Nao possui raizes reais')
elif delta > 0:
  x1 = (-b + delta**0.5) / (2*a)
  x2 = (-b - delta**0.5) / (2*a)
  print('Raizes:', x1, x2)
else:
  x2 = (-b - delta**0.5) / (2*a)
  print('Raiz:', x2)
