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
SCOPES = ['User.Read','User.Export.All']

# method 1: authenticate with auth code
client_instance = ConfidentialClientApplication(client_id=APPLICATION_ID,client_credential=CLIENT_SECRET, authority=authority_url)

authorization_req_url = client_instance.get_authorization_request_url(SCOPES)
print(authorization_req_url)

#webbrowser.get('safari').open_new_tab(authorization_req_url)

# paste the auth code from the url generated above 
auth_code = "M.R3_BAY.0a3b6e06-5a0c-6ccc-0974-615a6d0b39fe"

access_token_json = client_instance.acquire_token_by_authorization_code(
    code=auth_code,
    scopes=SCOPES
)
print(access_token_json)

access_token_id = access_token_json['access_token']
headers = {'Authorization': 'Bearer'+access_token_id}
base_url = "https://graph.microsoft.com/v1.0"
endpoint =  base_url + "me"

response = requests.get(endpoint, headers=headers)


