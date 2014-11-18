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


#lista = getLista(Grafo)
Grafo = calcularCentralidade(Grafo)

for x in Grafo.nodes():
	print Grafo.node[x] , "\n"


nx.draw(Grafo)

plt.show()


	
	

