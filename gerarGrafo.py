import json
import networkx as nx
import matplotlib.pyplot as plt


#connections_data = 'linkedin_connections_Jorge.json'

def getLista(G):
	nos = []
	for x in range(0, G.number_of_nodes()):
		nos.append(G.node)
		
	return nos



connections = json.loads(open('profiles').read())


def gerargrafo(arquivo, contato):
	G = nx.Graph(name="contato")
	G.add_node(contato)
	connections = json.loads(open(arquivo).read())

	for c in connections['values']:
		G.add_node(c['firstName'])
		G.add_edge(c['firstName'], contato)
	
	return G



Grafo = nx.Graph(name="contatos")

for c in connections:

	connections_data = 'linkedin_connections_'+c+'.json'
	
	G = gerargrafo(connections_data, c)

	Grafo = nx.compose(Grafo, G)


	print('\n\n'+ nx.info(Grafo))


lista = getLista(Grafo)


for s in lista:
	print s

nx.draw(Grafo)
plt.show()
	
	
