usuario_1 = 'Vmicael'
usuario_2 = 'Fmodesto'
usuario_3 = 'Jbonifacio'
senha_1 = '12345'
senha_2 = '1234'
senha_3 = '123'
resposta = 'Sim'
resposta1 = 'Sim'
resposta2 = 'Sim'
resposta3 = 'Sim'
while resposta1 == 'Sim':
  idd = input('Informe o seu usuário: ')
  password = input ('Informe a sua senha: ')
  if idd == usuario_1 and senha_1 == password or idd == usuario_2 and password == senha_2 or idd == usuario_3 and senha_3 == password:
    print('Acesso permitido')
    if idd == usuario_1:
      print('Tome o seu remédio vermelho as 09:00')
      print('Tome o seu remédio verde às 11:20')
      print('Você tem consulta no dia 12/02/2021 às 14:00 na R. São João, nº 213')
      resposta1 = input ('Deseja fazer outra consulta?')
    elif idd == usuario_2:
      print('Tome o seu remédio vermelho as 09:55')
      print('Tome o seu remédio verde às 14:30')
      print('Você tem consulta no dia 11/12/2021 às 14:50 na R. São João, nº 514')
      resposta1 = input ('Deseja fazer outra consulta?')
    elif idd == usuario_3:
      print('Tome o seu remédio vermelho as 15:30')
      print('Tome o seu remédio verde às 17:00')
      print('Você tem consulta no dia 03/06/2021 às 09:15 na R. São João, nº 115')
      resposta1 = input ('Deseja fazer outra consulta?')
  else: 
    print('Usuário ou Senha incorreto')
    resposta1 = input ('Deseja tentar novamente?')
print('Fim do programa')
