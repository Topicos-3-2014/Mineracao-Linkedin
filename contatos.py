from linkedin import server
from linkedin import linkedin # pip install python-linkedin
import json
from prettytable import PrettyTable # pip install prettytable
import networkx as nx
import matplotlib.pyplot as plt


CONSUMER_KEY = 'ezs4dy3ktwa4'
CONSUMER_SECRET = 'K7tXiFMkuCCkVeiW'


# Pass it in to the app...
app = server.quick_api(CONSUMER_KEY, CONSUMER_SECRET)

# Use the app...
profile = app.get_profile()
connections = app.get_connections()

connections_data = 'linkedin_connections_'+profile['firstName']+'.json'

f = open(connections_data, 'w')
f.write(json.dumps(connections, indent=1))
f.close()

G = nx.Graph(name="My Contacts linkedIn")

G.add_node(profile['firstName'])

for c in connections['values']:
	
	G.add_node(c['firstName'])
	G.add_edge(c['firstName'], profile['firstName'])
	#print '\n', c
	print "\nName: ", c['firstName']+ ' ' + c['lastName'],
	print "\nLocation: ", c['location'],
	print "\nHeadline: ", c['headline']

print('\n\n'+ nx.info(G))
print "Density ", nx.density(G)
print "Number of connected componnts: ", nx.number_connected_components(G)

nx.draw(G)
plt.show()
