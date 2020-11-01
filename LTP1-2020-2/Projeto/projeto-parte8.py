
import random
repeticao = 0
senha_id1 = '2468'
senha_id2 = '123456'
senha_id3 = '1234'
saldo_atualid1 = 1000
saldo_atualid2 = 250
saldo_atualid3 = 3000
resposta = 'Sim'
id1 = senha_id1
id2 = senha_id2
id3 = senha_id3
Sim = True
usuario = input('Informe o seu ID: ')
senha = input('Informe a sua senha: ')
email = input('Informe o seu e-mail: ')
while resposta == 'Sim':
  if usuario == 'id2':
    if senha == senha_id2:
      print('Seu saldo atual é de R$',saldo_atualid2)
      recebedor = input('Informe o ID recebedor do pagamento: ')
      if recebedor == 'id1':
        valor_pagamento = float(input('Informe o valor da transação: '))
        if saldo_atualid2 >= valor_pagamento:
           pagamento = (saldo_atualid2 - valor_pagamento)
           saldo_atualid2 = (saldo_atualid2 - valor_pagamento)
           print('Transação realizada com sucesso')
           print('Transação realizada por:', usuario)
           print('Transação realizada para:', recebedor)
           print('Valor da transação R$',valor_pagamento)
           print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
           print(email)
  usuario = input('Informe o seu ID: ')
  senha = input('Informe a sua senha: ')
  email = input('Informe o seu e-mail: ')
  if usuario == 'id3':
    if senha == senha_id3:
      print('Seu saldo atual é de R$', saldo_atualid3)
      recebedor = input('Informe o ID recebedor do pagamento: ')
      if recebedor == 'id1':
        valor_pagamento = float(input('Informe o valor da transação: '))
        if saldo_atualid3 >= valor_pagamento:
          pagamento = (saldo_atualid3 - valor_pagamento)
          saldo_atualid3 = (saldo_atualid3 - valor_pagamento)
          print('Transação realizada com sucesso')
          print('Transação realizada por:', usuario)
          print('Transação realizada para:', recebedor)
          print('Valor da transação R$',valor_pagamento)
          print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
          print(email)
  usuario = input('Informe o seu ID: ')
  senha = input('Informe a sua senha: ')
  email = input('Informe o seu e-mail: ')
  if usuario == 'id2':
    if senha == senha_id3:
      print('Seu saldo atual é de R$', saldo_atualid2)
      recebedor = input('Informe o ID recebedor do pagamento: ')
      if recebedor == 'id1':
        valor_pagamento = float(input('Informe o valor da transação: '))
        if saldo_atualid2 >= valor_pagamento:
          pagamento = (saldo_atualid2 - valor_pagamento)
          saldo_atualid2 = (saldo_atualid2 - valor_pagamento)
          print('Transação realizada com sucesso')
          print('Transação realizada por:', usuario)
          print('Transação realizada para:', recebedor)
          print('Valor da transação R$',valor_pagamento)
          print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
          print(email)
      else:
        print('Você não tem saldo o suficiente para realizar a transação')
  usuario = input('Informe o seu ID: ')
  senha = input('Informe a sua senha: ')
  email = input('Informe o seu e-mail: ')
  if usuario == 'id3':
    if senha == senha_id3:
      print('Seu saldo atual é de R$', saldo_atualid3)
      recebedor = input('Informe o ID recebedor do pagamento: ')
      if recebedor == 'id2':
        valor_pagamento = float(input('Informe o valor da transação: '))
        if saldo_atualid3 >= valor_pagamento:
          pagamento = (saldo_atualid3 - valor_pagamento)
          saldo_atualid3 = (saldo_atualid3 - valor_pagamento)
          print('Transação realizada com sucesso')
          print('Transação realizada por:', usuario)
          print('Transação realizada para:', recebedor)
          print('Valor da transação R$',valor_pagamento)
          print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
          print(email)
  
print('Fim do programa')
