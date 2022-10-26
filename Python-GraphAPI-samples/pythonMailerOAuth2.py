import msal
import requests
client_id = '22709c59-2d1c-46e4-8208-fa7a3ae92147'
tenant_id = "830e513c-2845-4419-a3c1-ca0800392a77"
# this is the client secret value not the secret id -when u generate new client secret.
client_secret ="HHa8Q~ynizlMx4BozwQjQjwLI1k2rB1CZ0iMpcMW"


authority = f"https://login.microsoftonline.com/{tenant_id}"
app = msal.ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=authority)

scopes = ["https://graph.microsoft.com/.default"]
result = None
result = app.acquire_token_silent(scopes, account=None)

if not result:
    print(
        "No suitable token exists in cache. Let's get a new one from Azure Active Directory.")
    result = app.acquire_token_for_client(scopes=scopes)
# if "access_token" in result:
#     print("Access token is " + result["access_token"])

if "access_token" in result:
    print(result)
    userId = "indiarm001@outlook.com"
    endpoint = f'https://graph.microsoft.com/v1.0/users/{userId}/messages?$select=sender,subject'
    r = requests.get(endpoint,
                     headers={'Authorization': 'Bearer ' + result['access_token']})
    if r.ok:
        print('Retrieved emails successfully')
        data = r.json()
        for email in data['value']:
            print(email['subject'] + ' (' + email['sender']
                  ['emailAddress']['name'] + ')')
    else:
        print(r.json())
else:
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))