# azure-oauth-office365-email
auth using OAuth and read emails from outlook

### reference doc :
https://github.com/ALgosZen/azure-oauth-office365-email.git


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


### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact