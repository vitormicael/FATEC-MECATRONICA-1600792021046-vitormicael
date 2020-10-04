lado1 = int(input('Informe o valor do primeiro lado: '))
lado2 = int(input('Informe o valor do segundo lado: '))
lado3 = int(input('Informe o valor do terceiro lado: '))
if (lado1 > 0) and (lado2 > 0) and (lado3 > 0):
  if (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2:
    print('Pode formar um triângulo')
