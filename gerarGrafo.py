import json
import networkx as nx
import matplotlib.pyplot as plt


#connections_data = 'linkedin_connections_Jorge.json'

def getLista(G):
	nos = []
	for x in range(0, G.number_of_nodes()):
		#print G.node[x],"\n\n"
		nos.append(G.node)
		
	return nos


def gerargrafo(arquivo, contato):
	G = nx.Graph(name="contato")

	G.add_node(contato,nome = contato)
	connections = json.loads(open(arquivo).read())

	for c in connections['values']:
		
		dic = {}.fromkeys(['nome','cargo', 'nome'])
		dic['nome'] =  c['firstName']
		dic['cargo'] = c['headline']
		dic['nome'] = c['firstName']
		
		#print dic,"\n"

		G.add_node(c['firstName'] , dic)
		G.add_edge( c['firstName'] , contato)

	
	return G



Grafo = nx.Graph(name="contatos")

connections = json.loads(open('profiles').read())

for c in connections:

	print c

	connections_data = 'linkedin_connections_'+c+'.json'
	
	G = gerargrafo(connections_data, c)


	Grafo = nx.compose(Grafo, G)


	print('\n\n'+ nx.info(Grafo))


#lista = getLista(Grafo)


for x in Grafo.nodes(data=True):
	print x, "\n"


nx.draw(Grafo)

plt.show()


	
	

