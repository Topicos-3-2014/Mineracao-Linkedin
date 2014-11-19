import json
import networkx as nx
import matplotlib.pyplot as plt


#connections_data = 'linkedin_connections_Jorge.json'

def Centralidades(no):
	return no['somaCentralidade']

def getLista(G):
	nos = []
	for x in Grafo.nodes():
		nos.append(G.node[x])
		
	return nos


def gerargrafo(arquivo, contato):
	G = nx.Graph(name="contato")

	dic = {}.fromkeys(['nome','cargo', 'somaCentralidade', 'degree_centrality', 
			'betweenness_centrality', 'closeness_centrality'], "null")

	dic['nome'] =  contato

		
	G.add_node(contato, dic)
	connections = json.loads(open(arquivo).read())

	for c in connections['values']:
		
		dic = {}.fromkeys(['nome','cargo', 'somaCentralidade', 'degree_centrality', 
			'betweenness_centrality', 'closeness_centrality'], "null")

		dic['nome'] =  c['firstName']
		dic['cargo'] = c['headline']
	
		

		G.add_node(c['firstName'] , dic)
		G.add_edge( c['firstName'] , contato)

	
	return G


def calcularCentralidade(G):
	for x in Grafo.nodes():
		Grafo.node[x]['degree_centrality'] = nx.degree_centrality(G).get(x) 
		Grafo.node[x]['betweenness_centrality'] = nx.betweenness_centrality(G).get(x)
		Grafo.node[x]['closeness_centrality'] = nx.closeness_centrality(G).get(x)

		Grafo.node[x]['somaCentralidade'] = Grafo.node[x]['degree_centrality']  + Grafo.node[x]['betweenness_centrality'] + Grafo.node[x]['closeness_centrality']

	return G


Grafo = nx.Graph(name="contatos")

connections = json.loads(open('profiles').read())

for c in connections:

	print c

	connections_data = 'linkedin_connections_'+c+'.json'
	
	G = gerargrafo(connections_data, c)


	Grafo = nx.compose(Grafo, G)


	print('\n\n'+ nx.info(Grafo))



Grafo = calcularCentralidade(Grafo)

#lista contendo todos os nos do grafo
lista = getLista(Grafo)
#ordena a lista com base na soma das centralidades
lista.sort(reverse=True, key=Centralidades)



f = open('lista_contatos', 'w')
f.write(json.dumps(lista, indent=1))
f.close()

for x in lista:
	print x['nome'],",", x['betweenness_centrality'],",", x['degree_centrality'],",", x['closeness_centrality']


nx.draw(Grafo)

plt.show()


	
	

