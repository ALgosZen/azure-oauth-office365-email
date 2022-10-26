# azure-oauth-office365-email
auth using OAuth and read emails from outlook

### reference doc :
https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth

### Graph API Explorer:
https://developer.microsoft.com/en-us/graph/graph-explorer


![OAuth2](/images/img1.png?raw=true "Azure OAuth2")

#### Sample app flow : When user signs in, an access token is requested and added to the HTTP requests through the authorization header. This token will then be used to acquire the user's profile as well as emails using MS Graph API

Azure AD admin consent - Application owner can grant the consent for the app .
consent has to be provided before using the resource



# Notes #

Integrating apps with Microsoft Office 365 Outlook –Process involves few steps as follows. Since the Azure documentation is not well organized, I’ve listed the steps involved in an order and sample code (in nodejs and python) to leverage for any application needs.

1.	APP registration
2.	Enable scopes
3.	Authentication using Auth code - Method 1: Generate access token using client secret 
OR 
4.	Authentication using prompt login - Method 2: Generate acess token using prompt user to login


### What is this repository for? ###

* App registration – call redirect URI
App must be registered in Azure portal. Registration involves in generatating following assets required for API calls.
•	Application ID: A unique identifier assigned by the Microsoft identity platform.
•	Redirect URI/URL: One or more endpoints at which your app will receive responses from the Microsoft identity platform. (For native and mobile apps, the URI is assigned by the Microsoft identity platform.)
•	Client secret: A password or a public/private key pair that your app uses to authenticate with the Microsoft identity platform. (Not needed for native or mobile apps.)


![SAML](/images/img2.png?raw=true "SAML")

As a best practice, request the least privileged permissions that your app needs in order to access data and function correctly. Requesting permissions with more than the necessary privileges is poor security practice, which may cause users to refrain from consenting and affect your app's usage.

Protocol	Permission scope string
* IMAP	https://outlook.office.com/IMAP.AccessAsUser.All 
* POP	https://outlook.office.com/POP.AccessAsUser.All
* SMTP AUTH	https://outlook.office.com/SMTP.Send

This is available in Azure portal -> API permissions -> Add permissions -> Application permissions -> choose  POP.AccessAsApp , IMAP.AccessAsApp etc., 

### Generate client secret:
![SECRET](/images/img5.png?raw=true "SECRET")

### Enable public client flows:
![SECRET](/images/img6.png?raw=true "SECRET")

#### Scenario: Daemon application that calls web APIs (Non interactive Method) 
- https://learn.microsoft.com/en-us/azure/active-directory/develop/scenario-daemon-overview

- During application registration, the reply URI isn't needed. Share secrets or certificates or signed assertions with Azure AD. You also need to request application permissions and grant admin consent to use those app permissions.
- The application configuration needs to provide client credentials as shared with Azure AD during the application registration.
- The scope used to acquire a token with the client credentials flow needs to be a static scope.

#### Steps to follow :
1. App Registration
2. Code Configuration
3. Aquire Token
4. Call a web API
5. Move to Production

- see the flow in pictures below

![img7](/images/img7.png?raw=true "img7")
![img8](/images/img8.png?raw=true "img8")
![img9](/images/img9.png?raw=true "img9")
- Make sure to 'Grant Admin Consent'
![img10](/images/img10.png?raw=true "img10")
- Make sure to 'Grant Admin Consent'