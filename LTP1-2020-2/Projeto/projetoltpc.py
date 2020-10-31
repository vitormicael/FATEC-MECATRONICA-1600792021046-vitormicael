senha_id1 = '2468'
senha_id2 = '123456'
senha_id3 = '1234'
saldo_ID1 = 1000
saldo_ID2 = 250
saldo_ID3 = 3000
usuario = input('Informe o seu ID: ')
senha = input('Informe a sua senha: ')
email = input('Informe o seu e-mail: ')
if senha == senha_id1:
  recebdor = input('Informe o ID recebedor do pagamento: ')
  if saldo_ID1 > saldo_ID2:
    pagamento = (saldo_ID1-saldo_ID2)
    print('Transação realizada com sucesso!! Seu saldo atual é de', pagamento)
else:
  print('Senha incorreta')
