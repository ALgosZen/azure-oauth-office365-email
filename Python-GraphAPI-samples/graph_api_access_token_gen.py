# method 2 : login to aquire access token

import webbrowser
import requests
from msal import PublicClientApplication 
from msal import ConfidentialClientApplication

APPLICATION_ID = "5a771507-e347-4f23-a3e0-3865f9f0c676"
DIRECTORY_ID = "830e513c-2845-4419-a3c1-ca0800392a77"

CLIENT_SECRET ="lO~8Q~~IvOzfsomeSFUtcF5QUwfT2L22qvxQndaP"

authority_url = "https://login.microsoftonline.com/consumers/"
base_url = "https://graph.microsoft.com/v1.0"
endpoint =  base_url + "me"
SCOPES = ['User.Read']

# method 2 : login to aquire access token
# Enable Enable public client flows and save it.
app = PublicClientApplication(APPLICATION_ID, authority=authority_url)

accounts = app.get_accounts()
print(accounts)
if accounts:
    app.acquire_token_silent(scopes=SCOPES, account=accounts[0])

flow = app.initiate_device_flow(scopes=SCOPES)
print(flow)

# open the url
app_code = flow['user_code']
webbrowser.get('safari').open_new(flow['verification_uri'])

# to aquire access token

result = app.acquire_token_by_device_flow(flow)

access_token_id = result['access_token']
headers = {'Authorization': 'Bearer'+ access_token_id}
endpoint =  base_url + "me"

response = requests.get(endpoint, headers=headers)
print(response)
print(response.json())
