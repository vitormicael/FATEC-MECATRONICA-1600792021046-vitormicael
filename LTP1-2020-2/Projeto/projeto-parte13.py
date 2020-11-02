  
import random
repeticao = 0
senha_ID1 = '2468'
senha_ID2 = '123456'
senha_ID3 = '1234'
saldo_atualID1 = 1000.00
saldo_atualID2 = 250.00
saldo_atualID3 = 3000.00
resposta = 'Sim'
resposta1 = 'sim'
resposta2 = 'sim'
resposta3 = 'sim'
resposta4 = 'sim'
ID1 = senha_ID1
ID2 = senha_ID2
ID3 = senha_ID3
Sim = True
while resposta == 'Sim':
  while resposta1 == 'sim':
    print('ID1 gera uma operação de recebimento de R$ 250.00 para o ID2')
    print('ID1 é a usuária Ana')
    print('ID2 é o usuário Rodrigo')
    print('ID3 é o usuário Paulo')
    usuario = input('Informe o seu  ou nome de Usuário: ')
    senha = input('Informe a sua senha: ')
    email = input('Informe o seu e-mail: ')
    if usuario == 'ID2' or 'Rodrigo':
       if senha == senha_ID2:
         print('Seu saldo atual é de R$',saldo_atualID2)
         recebedor = input('Informe o ID recebedor do pagamento: ')
         if recebedor == 'ID1' or 'Ana':
           valor_pagamento = float(input('Informe o valor da transação: '))
           if saldo_atualID2 >= valor_pagamento:
             pagamento = (saldo_atualID2 - valor_pagamento)
             saldo_atualID2 = (saldo_atualID2 - valor_pagamento)
             saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
             print('Transação realizada com sucesso')
             print('Transação realizada por:', usuario)
             print('Transação realizada para:', recebedor)
             print('Valor da transação R$',valor_pagamento)
             print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
             print(email)
             print('Saldo atual de',recebedor,'é de R$',saldo_atualID1)
             print('Saldo atual de',usuario,'é de R$',saldo_atualID2)
             print('Saldo atual de Paulo é de R$',saldo_atualID3)
           elif saldo_atualID3 < valor_pagamento:
             print('Você não tem saldo o suficiente para realizar a transação')
             saldo_atualID1 = saldo_atualID1
             saldo_atualID2 = saldo_atualID2
       if senha != senha_ID2:
        print('Senha incorreta')
    if usuario != 'ID2' or 'Rodrigo':
      print('Usuário incorreta')
      resposta1 = input('Deseja repetir a operação? (sim ou não) ')
  while resposta2 == 'sim':
    print('ID1 gera uma operação de recebimento de R$ 250.00 para o ID3')
    usuario = input('Informe o seu ID: ')
    senha = input('Informe a sua senha: ')
    email = input('Informe o seu e-mail: ')
    if usuario == 'ID3' or 'Paulo':
      if senha == senha_ID3:
        print('Seu saldo atual é de R$', saldo_atualID3)
        recebedor = input('Informe o ID recebedor do pagamento: ')
        if recebedor == 'ID1' or 'Ana':
          valor_pagamento = float(input('Informe o valor da transação: '))
          if saldo_atualID3 >= valor_pagamento:
            pagamento = (saldo_atualID3 - valor_pagamento)
            saldo_atualID3 = (saldo_atualID3 - valor_pagamento)
            saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
            print('Transação realizada com sucesso')
            print('Transação realizada por:', usuario)
            print('Transação realizada para:', recebedor)
            print('Valor da transação R$',valor_pagamento)
            print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
            print(email)
            print(saldo_atualID1)
            print(saldo_atualID2)
            print(saldo_atualID3)    
          elif saldo_atualID3 < valor_pagamento:
            print('Você não tem saldo o suficiente para realizar a transação')
            saldo_atualID3 = saldo_atualID3
            saldo_atualID1 = saldo_atualID1
      if senha != senha_ID3:
        print('Senha incorreta')
    if usuario != 'ID3' or 'Paulo':
      print('Usuário incorreta')
      resposta2 = input('Deseja repetir a operação? (sim ou não) ')
  while resposta3 == 'sim':
    print('ID1 gera uma operação de recebimento de R$ 250.00 para o ID2')
    usuario = input('Informe o seu ID: ')
    senha = input('Informe a sua senha: ')
    email = input('Informe o seu e-mail: ')
    if usuario == 'ID2' or 'Rodrigo':
      if senha == senha_ID2:
        print('Seu saldo atual é de R$', saldo_atualID2)
        recebedor = input('Informe o ID recebedor do pagamento: ')
        if recebedor == 'ID1' or 'Ana':
          valor_pagamento = float(input('Informe o valor da transação: '))
          if saldo_atualID2 >= valor_pagamento:
            pagamento = (saldo_atualID2 - valor_pagamento)
            saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
            saldo_atualID2 = (saldo_atualID2 - valor_pagamento)
            print('Transação realizada com sucesso')
            print('Transação realizada por:', usuario)
            print('Transação realizada para:', recebedor)
            print('Valor da transação R$',valor_pagamento)
            print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
            print(email)
            print(saldo_atualID1 + pagamento)
            print(saldo_atualID2 + pagamento)
            print(saldo_atualID3 + pagamento)          
          elif saldo_atualID2 < valor_pagamento:
            print('Você não tem saldo o suficiente para realizar a transação')
            saldo_atualID1 = saldo_atualID1
            saldo_atualID2 = saldo_atualID2
            print(saldo_atualID1)
            print(saldo_atualID2)
            print(saldo_atualID3)
      if senha != senha_ID3:
        print('Senha incorreta')
    if usuario != 'ID3' or 'Paulo':
      print('Usuário incorreta')
      resposta3 = input('Deseja repetir a operação? (sim ou não) ')
  while resposta4 == 'sim':
    print('ID2 gera uma operação de recebimento de R$ 1000.00 para o ID3')
    usuario = input('Informe o seu ID: ')
    senha = input('Informe a sua senha: ')
    email = input('Informe o seu e-mail: ')
    if usuario == 'ID3' or 'Paulo':
      if senha == senha_ID3:
        print('Seu saldo atual é de R$', saldo_atualID3)
        recebedor = input('Informe o ID recebedor do pagamento: ')
        if recebedor == 'ID2' or 'Rodrigo':
          valor_pagamento = float(input('Informe o valor da transação: '))
          if saldo_atualID3 >= valor_pagamento:
            pagamento = (saldo_atualID3 - valor_pagamento)
            saldo_atualID3 = (saldo_atualID3 - valor_pagamento)
            saldo_atualID2 = (saldo_atualID2 + valor_pagamento)
            print('Transação realizada com sucesso')
            print('Transação realizada por:', usuario)
            print('Transação realizada para:', recebedor)
            print('Valor da transação R$',valor_pagamento)
            print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
            print(email)
            print(saldo_atualID1)
            print(saldo_atualID2)
            print(saldo_atualID3)          
          elif saldo_atualID3 < valor_pagamento:
            print('Você não tem saldo o suficiente para realizar a transação')
            saldo_atualID3 = saldo_atualID3
            saldo_atualID2 = saldo_atualID2
      if senha != senha_ID3:
        print('Senha incorreta')
    if usuario != 'ID3' or 'Paulo':
      print('Usuário incorreta')
      resposta4 = input('Deseja repetir a operação? (sim ou não) ')
  resposta = ('Deseja repetir as operações? (Sim ou Não)')
print('Fim do programa')
