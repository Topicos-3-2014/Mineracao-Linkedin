import json

file = open('lista_contatos', 'r')

contatos = json.loads(file.read())

for c in contatos:
	print c['nome']