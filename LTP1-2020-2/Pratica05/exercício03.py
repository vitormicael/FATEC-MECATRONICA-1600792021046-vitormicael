a=float(input('Informe o valor de a: '))
b=float(input('Informe o valor de b: '))
c=float(input('Informe o valor de c: '))
delta=(b**2)-(4*a*c)
if delta<0:
  print('Não existem raízes reais')
elif delta>0:
  x1=(-b+delta**0.5)/2*a
  x2=(-b-delta**0.5)/2*a
  print('Raiz', x1, x2)
