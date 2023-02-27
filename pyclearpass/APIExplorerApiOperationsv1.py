
from pyclearpass.common import _generateParameterisedURL,_removeEmptyKeys,ClearPassAPILogin

#File Name: APIExplorerApiOperationsv1.py

class apiOperations(ClearPassAPILogin):

    #Function Section Name:TokenEndpoint  
    #Function Section Description: Obtain an OAuth2 access token for making API calls

    def newOauth(self,body=({})):
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
        urlPath='/oauth'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:TokenInfo  
    #Function Section Description: Returns OAuth2 authenticated client or user information

    def getOauthMe(self,body=({})):
        '''
        Operation: Returns OAuth2 authenticated client or user information
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
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
        urlPath='/oauth/me'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get',query=body)
    def newOauthMe(self,body=({})):
        '''
        Operation: Returns OAuth2 authenticated client or user information
        HTTP Status Response Codes: 200 OK, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- TokenInfo {info (string): Defaults to the operator profile name,name (string): Defaults to the authenticated username,... (string, optional): Additional properties may be returned for grant_type "password" if corresponding properties are defined in the OAuth API enforcement profile}
        Required Body Parameters (type(dict) body example)- {
  "info": "",
  "name": "",
  "...": ""
}
        '''
        urlPath='/oauth/me'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:TokenPrivileges  
    #Function Section Description: Determine the privileges available to the user

    def getOauthPrivileges(self,body=({})):
        '''
        Operation: Returns a list of privileges available to the user
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Body Parameters (body description)- TokenInfo {info (string): Defaults to the operator profile name,name (string): Defaults to the authenticated username,... (string, optional): Additional properties may be returned for grant_type "password" if corresponding properties are defined in the OAuth API enforcement profile}
        Required Body Parameters (type(dict) body example)- {
  "info": "",
  "name": "",
  "...": ""
}
        '''
        urlPath='/oauth/privileges'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get',query=body)
