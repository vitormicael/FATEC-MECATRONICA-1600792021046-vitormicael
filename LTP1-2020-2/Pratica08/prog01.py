nome = input('Informe o seu nome: ')
time_futebol = input('Informe o seu time: ') 
quantidade = int(input('Informe quantos mudiais o seu time venceu: '))

print('Olá', nome)

if time_futebol == 'palmeiras':
  print('Seu time não tem mundial')
else:
  print('Seu time: ', time_futebol,'Venceu: ',quantidade)
