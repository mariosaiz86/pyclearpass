import json
import requests
import urllib.parse,urllib3
urllib3.disable_warnings()

class ClearPassAPILogin():
    
    def __init__(self,granttype, clientid,clientsecret,username="", password="",server="", verifySSL=False):
        '''
        This is the class constructor for the ClearPassModule. 
        
        This constructor is required to be created before any modules can be used and must contain the following function arguments:
        
        grant_type (string) = ['client_credentials' or 'password' or 'refresh_token']: OAuth2 authentication method,client_id (string): Client ID defined in API Clients,
        client_secret (string, optional): Client secret, required if the API client is not a public client,
        username (string, optional): Username for authentication, required for grant_type "password",
        password (string, optional): Password for authentication, required for grant_type "password",
        server (string): Website for ClearPass services example - https://clearpass.test.com:443/api 
        verifySSL (boolean, optional): default value False. Allows use of an invalid SSL certificate. 
        }
     
        '''
        self.granttype = granttype
        self.clientid = clientid
        self.clientsecret = clientsecret
        self.username = username     
        self.password = password
        self.server = server
        self.apiToken = ""
        self.verifySSL = False

    def _sendRequest(self,url,method,query=""):
        """Sends a request to the ClearPass server
            :query: must contain the json request if model required
            :url: must contain the /url (e.g. /oauth)
            :method: must contain the post or get request type of method
            :apiToken optional[]: must contain the apiToken for the calls. 
        """
        FullUrlPath = self.server+url
     
        if len(self.apiToken) == 0:
            Cred = _getAPIKey(self)
            try:
                self.apiToken = Cred['access_token']
            except TypeError:
                pass

        if len(self.apiToken) != 0:
            header = {'Authorization':'Bearer '+self.apiToken}
            if method == "post":
                response= requests.post(url=FullUrlPath, json=query,headers=header,verify=self.verifySSL)
            if method == "patch":
                response= requests.patch(url=FullUrlPath, json=query,headers=header,verify=self.verifySSL)
            if method == "put":
                response= requests.put(url=FullUrlPath, json=query,headers=header,verify=self.verifySSL)
            if method == "get":
                response=requests.get(url=FullUrlPath, json=query,headers=header,verify=self.verifySSL)
            if method == "delete":
                response=requests.delete(url=FullUrlPath, json=query,headers=header,verify=self.verifySSL)
            if method == "":
                print("method needs to be supplied before sending a request to ClearPass")
                
            try:
                
                return(json.loads(response.text))
            except json.decoder.JSONDecodeError:
                return response.text
        else:
            print("Problem logging into ClearPass")
            return Cred


def _getAPIKey(self):
    
    '''
    Operation: Obtain an OAuth2 access token for making API calls
    HTTP Status Response Codes: 200 OK, 400 Bad Request, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 400 Bad Request, 406 Not Acceptable, 415 Unsupported Media Type
    Required Body Parameters (body description)- TokenEndpoint {grant_type (string) = ['client_credentials' or 'password' or 'refresh_token']: OAuth2 authentication method,client_id (string): Client ID defined in API Clients,client_secret (string, optional): Client secret, required if the API client is not a public client,username (string, optional): Username for authentication, required for grant_type "password",password (string, optional): Password for authentication, required for grant_type "password",scope (string, optional): Scope of the access request,refresh_token (string, optional): Refresh token issued to the client, required for grant_type "refresh_token"}
    Required Body Parameters (type(dict) body example)- {
    "grant_type": "",
    "client_id": "",
    "client_secret": "",
    "username": "",
    "password": "",
    "scope": "",
    "refresh_token": ""
    }
    '''
    model={
        "grant_type": self.granttype,
        "client_id": self.clientid,
        "client_secret": self.clientsecret,
        "username": self.username,
        "password": self.password,        
    }
    
    FullUrlPath = self.server+'/oauth'
    response= requests.post(url=FullUrlPath, json=model,verify=self.verifySSL)
   

    try:
        
        response = json.loads(str(response.text))
        return(response)

    except json.decoder.JSONDecodeError:
        return response
    
def _removeEmptyKeys(keys):
    RemoveEmptyValuesFromDict = []
    for item in keys:
        if keys[item] == "":
            RemoveEmptyValuesFromDict.append(item)
        else:
            #print(item,": ", keys[item])
            pass
    for removal in RemoveEmptyValuesFromDict:
        del keys[removal]
    return keys

def _generateParameterisedURL(url,parameters=""):
    
    parameters = _removeEmptyKeys(keys=parameters)

    if len(parameters) == 0:
        return url
    else:
        encodedURL = urllib.parse.urlencode(parameters)
        finalURL = url +'?'+ encodedURL
        return finalURL

