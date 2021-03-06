from linkedin import server
from linkedin import linkedin # pip install python-linkedin
import json
from prettytable import PrettyTable # pip install prettytable

CONSUMER_KEY = 'ezs4dy3ktwa4'
CONSUMER_SECRET = 'K7tXiFMkuCCkVeiW'


# Pass it in to the app...
app = server.quick_api(CONSUMER_KEY, CONSUMER_SECRET)

# Use the app...
app.get_profile()

connections = app.get_connections()
connections_data = 'resources/ch03-linkedin/linkedin_connections.json'

#f = open(conections_data, 'w')
#f.write(json.dumps(connections, indent=1))
#f.close()
# You can reuse the data without using the API later like this...
# connections = json.loads(open(connections_data).read())


pt = PrettyTable(field_names=['Name', 'Location'])
pt.align = 'l'
[ pt.add_row((c['firstName'] + ' ' + c['lastName'], c['location']['name']))
for c in connections['values']
if c.has_key('location')]
print pt


# Display your own positions...
my_positions = app.get_profile(selectors=['positions'])
print json.dumps(my_positions, indent=1)

# Display positions for someone in your network...
# Get an id for a connection. We'll just pick the first one.
connection_id = connections['values'][0]['id']
connection_positions = app.get_profile(member_id=connection_id,
selectors=['positions'])
print json.dumps(connection_positions, indent=1)
