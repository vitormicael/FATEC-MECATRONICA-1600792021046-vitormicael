#programa que calcula o valor de parcelas
valor = float(input('Informe o valor: '))
numero_parcelas = int(input('Informe o número de parcelas: '))
if numero_parcelas == 1:
  parcela = (valor * 0.95) / numero_parcelas
elif numero_parcelas == 2:
  parcela = (valor / numero_parcelas)
elif numero_parcelas == 3:
  parcela = (valor * 1.05) / numero_parcelas
else:
  parcela = (valor * 1.1) / numero_parcelas
print('Valor da parcela', parcela)
