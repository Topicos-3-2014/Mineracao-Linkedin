from linkedin import linkedin # pip install python-linkedin
import json
from prettytable import PrettyTable # pip install prettytable

# Define CONSUMER_KEY, CONSUMER_SECRET,
# USER_TOKEN, and USER_SECRET from the credentials
# provided in your LinkedIn application

CONSUMER_KEY = '77xdv685p8ovh5'
CONSUMER_SECRET = 'EFTK1Nf0s9WuLx11'
USER_TOKEN = '2c83cd93-a7cc-4594-8afe-cc4c6851763a'
USER_SECRET = 'cbc4f4f9-96c5-429c-b25b-22d1ecf1c8de'
RETURN_URL = 'http://localhost:8000' # Not required for developer authentication


# Instantiate the developer authentication class
auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,
                                USER_TOKEN, USER_SECRET,
                                RETURN_URL,
                                permissions=linkedin.PERMISSIONS.enums.values())


# Pass it in to the app...
app = linkedin.LinkedInApplication(auth)

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
