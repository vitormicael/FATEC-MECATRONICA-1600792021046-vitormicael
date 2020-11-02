  
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
    print('Ana gera uma operação de recebimento de R$ 250.00 para o Rodrigo')
    print('Faça login com a conta de Rodrigo e faça a transação para Ana')
    print('ID1 é a usuária Ana')
    print('ID2 é o usuário Rodrigo')
    print('ID3 é o usuário Paulo')
    usuario = input('Informe o seu nome de Usuário: ')
    senha = input('Informe a sua senha: ')
    email = input('Informe o seu e-mail: ')
    if usuario == 'Rodrigo' and senha == senha_ID2:
         print(f'Seu saldo atual é de R${saldo_atualID2: .2f}')
         recebedor = input('Informe o nome do recebedor do pagamento: ')
         if recebedor == 'Ana':
           valor_pagamento = float(input('Informe o valor da transação: '))
           if saldo_atualID2 >= valor_pagamento:
             pagamento = (saldo_atualID2 - valor_pagamento)
             saldo_atualID2 = (saldo_atualID2 - valor_pagamento)
             saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
             print('Transação realizada com sucesso')
             print('Transação realizada por:', usuario)
             print('Transação realizada para:', recebedor)
             print(f'Valor da transação R${valor_pagamento: .2f}')
             print("Sua chave de segurança é:"),print(random.randrange(1000, 9999))
             print('Email: ',email)
             print(f'Saldo atual de Ana é de R${saldo_atualID1: .2f}')
             print(f'Saldo atual de Rodrigo é de R${saldo_atualID2: .2f}')
             print(f'Saldo atual de Paulo é de R${saldo_atualID3: .2f}')
           elif saldo_atualID2 < valor_pagamento:
             print('Você não tem saldo o suficiente para realizar a transação')
             saldo_atualID1 = saldo_atualID1
             saldo_atualID2 = saldo_atualID2
    else:
        print('Usuário ou Senha incorreto')
    resposta1 = input('Deseja repetir a operação? (sim ou não) ')
   while resposta2 == 'sim':
    print('Ana gera uma operação de recebimento de R$ 250.00 para o Paulo')
    print('Faça login com a conta de Paulo e faça a transação para Ana')
    print('ID1 é a usuária Ana')
    print('ID2 é o usuário Rodrigo')
    print('ID3 é o usuário Paulo')
    usuario = input('Informe o seu nome de Usuário: ')
    senha = input('Informe a sua senha: ')
    email = input('Informe o seu e-mail: ')
    if usuario == 'Paulo' and senha == senha_ID3:
      if senha == senha_ID3:
        print('Seu saldo atual é de R$', saldo_atualID3)
        recebedor = input('Informe o nome do recebedor do pagamento: ')
        if recebedor == 'Ana':
          valor_pagamento = float(input('Informe o valor da transação: '))
          if saldo_atualID3 >= valor_pagamento:
            pagamento = (saldo_atualID3 - valor_pagamento)
            saldo_atualID3 = (saldo_atualID3 - valor_pagamento)
            saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
            print('Transação realizada com sucesso')
            print('Transação realizada por:', usuario)
            print('Transação realizada para:', recebedor)
            print(f'Valor da transação R${valor_pagamento: .2f}')
            print("Sua chave de segurança é:"),print(random.randrange(1000, 9999))
            print('Email: ',email)
            print(f'Saldo atual de Ana é de R${saldo_atualID1: .2f}')
            print(f'Saldo atual de Rodrigo é de R${saldo_atualID2: .2f}')
            print(f'Saldo atual de Paulo é de R${saldo_atualID3: .2f}')
          elif saldo_atualID3 < valor_pagamento:
            print('Você não tem saldo o suficiente para realizar a transação')
            saldo_atualID3 = saldo_atualID3
            saldo_atualID1 = saldo_atualID1
    else:
        print('Usuário ou Senha incorreto')
    resposta2 = input('Deseja repetir a operação? (sim ou não) ')
   while resposta3 == 'sim':
    print('Ana gera uma operação de recebimento de R$ 250.00 para o Rodrigo')
    print('Faça login com a conta de Rodrigo e faça a transação para Ana')
    print('ID1 é a usuária Ana')
    print('ID2 é o usuário Rodrigo')
    print('ID3 é o usuário Paulo')
    usuario = input('Informe o seu nome de Usuário: ')
    senha = input('Informe a sua senha: ')
    email = input('Informe o seu e-mail: ')
    if usuario == 'Rodrigo' and senha == senha_ID2:
        print(f'Seu saldo atual é de R$ {saldo_atualID2: .2f}')
        recebedor = input('Informe o nome do recebedor do pagamento: ')
        if recebedor == 'Ana':
          valor_pagamento = float(input('Informe o valor da transação: '))
          if saldo_atualID2 >= valor_pagamento:
            pagamento = (saldo_atualID2 - valor_pagamento)
            saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
            saldo_atualID2 = (saldo_atualID2 - valor_pagamento)
            print('Transação realizada com sucesso')
            print('Transação realizada por:', usuario)
            print('Transação realizada para:', recebedor)
            print(f'Valor da transação R${valor_pagamento: .2f}')
            print("Sua chave de segurança é:"),print(random.randrange(1000, 9999))
            print('Email: ',email)
            print(f'Saldo atual de Ana é de R${saldo_atualID1: .2f}')
            print(f'Saldo atual de Rodrigo é de R${saldo_atualID2: .2f}')
            print(f'Saldo atual de Paulo é de R${saldo_atualID3: .2f}')
          elif saldo_atualID2 < valor_pagamento:
            print('Você não tem saldo o suficiente para realizar a transação')
            saldo_atualID1 = saldo_atualID1
            saldo_atualID2 = saldo_atualID2
            print(saldo_atualID1)
            print(saldo_atualID2)
            print(saldo_atualID3)
    else:
        print('Usuário ou Senha incorreto')
    resposta3 = input('Deseja repetir a operação? (sim ou não) ')
   while resposta4 == 'sim':
    print('Rodrigo gera uma operação de recebimento de R$ 1000.00 para o Paulo')
    print('Faça login com a conta de Paulo e faça a transação para Rodrigo')
    print('ID1 é a usuária Ana')
    print('ID2 é o usuário Rodrigo')
    print('ID3 é o usuário Paulo')
    usuario = input('Informe o seu nome de Usuário: ')
    senha = input('Informe a sua senha: ')
    email = input('Informe o seu e-mail: ')
    if usuario == 'Paulo' and senha == senha_ID3:
        print('Seu saldo atual é de R$', saldo_atualID3)
        recebedor = input('Informe o nome do recebedor do pagamento: ')
        if recebedor == 'Rodrigo':
          valor_pagamento = float(input('Informe o valor da transação: '))
          if saldo_atualID3 >= valor_pagamento:
            pagamento = (saldo_atualID3 - valor_pagamento)
            saldo_atualID3 = (saldo_atualID3 - valor_pagamento)
            saldo_atualID2 = (saldo_atualID2 + valor_pagamento)
            print('Transação realizada com sucesso')
            print('Transação realizada por:', usuario)
            print('Transação realizada para:', recebedor)
            print(f'Valor da transação R${valor_pagamento: .2f}')
            print("Sua chave de segurança é:"),print(random.randrange(1000, 9999))
            print('Email: ',email)
            print(f'Saldo atual de Ana é de R${saldo_atualID1: .2f}')
            print(f'Saldo atual de Rodrigo é de R${saldo_atualID2: .2f}')
            print(f'Saldo atual de Paulo é de R${saldo_atualID3: .2f}')
          elif saldo_atualID3 < valor_pagamento:
            print('Você não tem saldo o suficiente para realizar a transação')
            saldo_atualID3 = saldo_atualID3
            saldo_atualID2 = saldo_atualID2
    else:
        print('Usuário ou Senha incorreto')
    resposta4 = input('Deseja repetir a operação? (sim ou não) ')
resposta = ('Deseja repetir as operações? (Sim ou Não)')
print('Fim do programa')
