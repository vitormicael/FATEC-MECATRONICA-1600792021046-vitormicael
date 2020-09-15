#programa que calcula o valor de parcelas
valor_total=float(input('Informe o valor total: '))
numero_parcelas=float(input('Informe o número de parcelas: '))
if numero_parcelas==1:
  parcela=(valor_total*0.95)/numero_parcelas
elif numero_parcelas==2:
  parcela=valor_total/numero_parcelas
elif numero_parcelas==3:
  parcela=(valor_total*1.05)/numero_parcelas
else:
  parcela=(valor_total*1.1)/numero_parcelas
print('Valor da parcela', parcela)
