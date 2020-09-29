valor1 = int(input('Informe um valor:'))
valor2 = int(input('Informe outro valor:'))
valor3 = int(input('Informe um 3 valor:'))
if valor1 >= valor2 and valor1 >= valor3:
  maior = valor1
elif valor2 >= valor1 and valor2 >= valor3:
  maior = valor2
else:
  maior = valor3
print('Maior valor:', maior)
if valor1 <= valor2 and valor1 <= valor3:
  menor = valor1
elif valor2 <= valor1 and valor2 <= valor3:
  menor = valor2
else:
  menor = valor3
print('Menor valor:', menor)
media = (valor1 + valor2 + valor3) / 3
print('Valor médio:', media)
