texto = 'a vinGAnça nunca é pLEna, MatA a aLma e envenena (Madruga, 1981)'

print(texto.capitalize())
print(texto.casefold())
print(texto.count('madruga'))
texto_minusculo = texto.lower()
print(texto_minusculo)
print(texto_minusculo.count('madruga'))
texto_maiusculo = texto.upper()
print(texto_maiusculo)
print(texto_maiusculo.find(','))
print(texto_maiusculo[:texto_maiusculo.find(',')])
