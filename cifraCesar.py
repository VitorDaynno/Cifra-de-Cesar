alfa = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

texto = 'Jogue me aos lobos e voltarei como lider deles' #insira o texto aqui
texto = texto.lower()
resposta = ''

i = 0
while i < len(texto):
	if texto[i] == ' ':
		resposta = resposta + ' '
	elif texto[i] == 'y':
		resposta = resposta + 'a'
	elif texto[i] == 'w':
		resposta = resposta +'b'
	elif texto[i] == 'z':
		resposta = resposta +'c'
	else:
		indice = alfa.index(texto[i])
		resposta = resposta + alfa[indice + 3]
	i = i + 1

print resposta
