
import random

senha_id1 = '2468'
senha_id2 = '123456'
senha_id3 = '1234'
saldo_ID1 = 1000
saldo_ID2 = 250
saldo_ID3 = 3000
usuario = input('Informe o seu ID: ')
senha = input('Informe a sua senha: ')
email = input('Informe o seu e-mail: ')
if usuario == 'id2':
  if senha == senha_id2:
    recebedor = input('Informe o ID recebedor do pagamento: ')
    if recebedor == 'id1':
      print('Seu saldo atual é de R$',saldo_ID2)
      valor_pagamento = float(input('Informe o valor a ser pago: '))
      if saldo_ID2 >= valor_pagamento:
        pagamento = (saldo_ID2-valor_pagamento)
        print('Transação realizada com sucesso! Seu saldo atual é de R$', pagamento)
        print('Transação realizada por:', usuario)
        print('Transação realizada para:', recebedor)
        print('Valor da transação R$',valor_pagamento)
        print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
        print(email)
else:
  print('Senha ou usuário incorreto')
