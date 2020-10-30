preco = input('Informe o preço: ')
real = ''
centavos = ''
achei_virgula = False
for caracter in preco:
  if caracter != ',':
    if achei_virgula == False:
      real = real + caracter
    else:
      centavos = centavos + caracter
  else:
    achei_virgula = True
if achei_virgula == True:
  print('Reais: ', real, 'centavos', centavos)
else:
  print('Reais', real)
