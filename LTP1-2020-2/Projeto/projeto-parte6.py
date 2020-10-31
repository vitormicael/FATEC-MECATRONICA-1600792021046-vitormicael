
import random
repeticao = 0
senha_id1 = '2468'
senha_id2 = '123456'
senha_id3 = '1234'
saldo_ID1 = 1000
saldo_ID2 = 250
saldo_ID3 = 3000
resposta = 'Sim'
Sim = True
usuario = input('Informe o seu ID: ')
email = input('Informe o seu e-mail: ')
senha = input('Informe a sua senha: ')
while resposta == 'Sim':
 if usuario == 'id2':
  if senha == senha_id2:
    recebedor = input('Informe o ID recebedor do pagamento: ')
    if recebedor == 'id1':
      print('Seu saldo atual é de R$',saldo_ID2)
      valor_pagamento = float(input('Informe o valor a ser pago: '))
      if saldo_ID2 >= valor_pagamento:
        pagamento = (saldo_ID2 - valor_pagamento)
        saldo_ID1 = (saldo_ID1 + valor_pagamento)
        saldo_ID2 = (saldo_ID2 - valor_pagamento)
        print('Transação realizada com sucesso')
        print('Transação realizada por:', usuario)
        print('Transação realizada para:', recebedor)
        print('Valor da transação R$',valor_pagamento)
        print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
        print(email)
  if usuario == 'id3':
    if senha == senha_id3:
      recebedor = input('Informe o ID recebedor do pagamento: ')
      if recebedor == 'id1':
        print('Seu saldo atual é de R$', saldo_ID3)
   
