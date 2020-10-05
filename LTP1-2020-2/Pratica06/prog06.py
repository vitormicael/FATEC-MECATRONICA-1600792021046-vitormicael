## classificador de nível gamer
#mouse com RGB
#teclado com RGB
#monitor com RGB
#mouse - teclado - monitor - classificação
#SIM   -  SIM    -   SIM   - Viciado
#NÃO   -  SIM    -   NÃO   - NOIA
#SIM   -  NÃO    -   NÃO   - QUASE NORMAL
#NÃO   -  NÃO    -   NÃO   - -50fps
print('Descubra seu nível Gamer!!')
mouse = input('Seu mouse tem RGB?')
teclado = input('Seu teclado tem RGB?')
monitor = input('Seu monitor tem RGB?')

if mouse == 'Sim' and teclado == 'Sim' and monitor == 'Sim':
  print('Viciado!!')
elif mouse == 'Não' and teclado == 'Sim' and monitor == 'Não':
  print('Noia')
elif mouse == 'Sim' and teclado == 'Não' and monitor == 'Não':
  print('Quase normal')
elif mouse == 'Não' and teclado == 'Não' and monitor == 'Não':
  print('-50fps')
else:
  print('Sem classificação')
