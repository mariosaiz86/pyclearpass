
from pyclearpass.common import _generateParameterisedURL,_removeEmptyKeys,ClearPassAPILogin

#File Name: APIExplorerIdentitiesv1.py

class apiIdentities(ClearPassAPILogin):

    #Function Section Name:ApiClient  
    #Function Section Description: Manage API clients at Administration -> API Services -> API Clients

    def getApiClient(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of API clients
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/api-client'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newApiClient(self,body=({})):
        '''
        Operation: Create a new API client
        HTTP Status Response Codes: 201 Created, 400 Client Error, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 400 Client Error, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- ApiClient {access_lifetime (string, optional): Lifetime of an OAuth2 access token,access_token_lifetime (string): Specify the lifetime of an OAuth2 access token,access_token_lifetime_units (string): Specify the lifetime of an OAuth2 access token,auto_confirm (integer, optional): Not supported at this time,client_description (string, optional): Use this field to store comments or notes about this API client,client_id (string): The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter,client_public (boolean, optional): Public clients have no client secret,client_refresh (boolean, optional): An OAuth2 refresh token may be used to obtain an updated access token.
Use grant_type=refresh_token for this,client_secret (string, optional): Use this value in the OAuth2 “client_secret” parameter. NOTE: This value is encrypted when stored and cannot be retrieved.,enabled (boolean, optional): Enable API client,id (string): The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter,grant_types (string, optional): Only the selected authentication method will be permitted for use with this client ID,profile_id (integer, optional): The operator profile applies role-based access control to authorized OAuth2 clients.
This determines what API objects and methods are available for use,profile_name (string, optional): Name of operator profile,redirect_uri (string, optional): Not supported at this time,refresh_lifetime (string, optional): Lifetime of an OAuth2 refresh token,refresh_token_lifetime (string): Specify the lifetime of an OAuth2 refresh token,refresh_token_lifetime_units (string): Specify the lifetime of an OAuth2 refresh token,scope (string, optional): Not supported at this time,user_id (string, optional): Not supported at this time}
        Required Body Parameters (type(dict) body example)- {
  "access_lifetime": "",
  "access_token_lifetime": "",
  "access_token_lifetime_units": "",
  "auto_confirm": 0,
  "client_description": "",
  "client_id": "",
  "client_public": false,
  "client_refresh": false,
  "client_secret": "",
  "enabled": false,
  "id": "",
  "grant_types": "",
  "profile_id": 0,
  "profile_name": "",
  "redirect_uri": "",
  "refresh_lifetime": "",
  "refresh_token_lifetime": "",
  "refresh_token_lifetime_units": "",
  "scope": "",
  "user_id": ""
}
        '''
        urlPath='/api-client'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getApiClientByClient_id(self,client_id=""):
        '''
        Operation: Get an API client
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: client_id, Description: URL parameter client_id
        '''
        urlPath='/api-client/{client_id}'
        dictPath={'client_id': client_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateApiClientByClient_id(self,client_id="",body=({})):
        '''
        Operation: Update some fields of an API client
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 400 Client Error, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 400 Client Error, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: client_id, Description: URL parameter client_id
        Required Body Parameters (body description)- ApiClient {access_lifetime (string, optional): Lifetime of an OAuth2 access token,access_token_lifetime (string): Specify the lifetime of an OAuth2 access token,access_token_lifetime_units (string): Specify the lifetime of an OAuth2 access token,auto_confirm (integer, optional): Not supported at this time,client_description (string, optional): Use this field to store comments or notes about this API client,client_id (string): The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter,client_public (boolean, optional): Public clients have no client secret,client_refresh (boolean, optional): An OAuth2 refresh token may be used to obtain an updated access token.
Use grant_type=refresh_token for this,client_secret (string, optional): Use this value in the OAuth2 “client_secret” parameter. NOTE: This value is encrypted when stored and cannot be retrieved.,enabled (boolean, optional): Enable API client,id (string): The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter,grant_types (string, optional): Only the selected authentication method will be permitted for use with this client ID,profile_id (integer, optional): The operator profile applies role-based access control to authorized OAuth2 clients.
This determines what API objects and methods are available for use,profile_name (string, optional): Name of operator profile,redirect_uri (string, optional): Not supported at this time,refresh_lifetime (string, optional): Lifetime of an OAuth2 refresh token,refresh_token_lifetime (string): Specify the lifetime of an OAuth2 refresh token,refresh_token_lifetime_units (string): Specify the lifetime of an OAuth2 refresh token,scope (string, optional): Not supported at this time,user_id (string, optional): Not supported at this time}
        Required Body Parameters (type(dict) body example)- {
  "access_lifetime": "",
  "access_token_lifetime": "",
  "access_token_lifetime_units": "",
  "auto_confirm": 0,
  "client_description": "",
  "client_id": "",
  "client_public": false,
  "client_refresh": false,
  "client_secret": "",
  "enabled": false,
  "id": "",
  "grant_types": "",
  "profile_id": 0,
  "profile_name": "",
  "redirect_uri": "",
  "refresh_lifetime": "",
  "refresh_token_lifetime": "",
  "refresh_token_lifetime_units": "",
  "scope": "",
  "user_id": ""
}
        '''
        urlPath='/api-client/{client_id}'
        dictPath={'client_id': client_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceApiClientByClient_id(self,client_id="",body=({})):
        '''
        Operation: Replace an API client
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 400 Client Error, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 400 Client Error, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: client_id, Description: URL parameter client_id
        Required Body Parameters (body description)- ApiClient {access_lifetime (string, optional): Lifetime of an OAuth2 access token,access_token_lifetime (string): Specify the lifetime of an OAuth2 access token,access_token_lifetime_units (string): Specify the lifetime of an OAuth2 access token,auto_confirm (integer, optional): Not supported at this time,client_description (string, optional): Use this field to store comments or notes about this API client,client_id (string): The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter,client_public (boolean, optional): Public clients have no client secret,client_refresh (boolean, optional): An OAuth2 refresh token may be used to obtain an updated access token.
Use grant_type=refresh_token for this,client_secret (string, optional): Use this value in the OAuth2 “client_secret” parameter. NOTE: This value is encrypted when stored and cannot be retrieved.,enabled (boolean, optional): Enable API client,id (string): The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter,grant_types (string, optional): Only the selected authentication method will be permitted for use with this client ID,profile_id (integer, optional): The operator profile applies role-based access control to authorized OAuth2 clients.
This determines what API objects and methods are available for use,profile_name (string, optional): Name of operator profile,redirect_uri (string, optional): Not supported at this time,refresh_lifetime (string, optional): Lifetime of an OAuth2 refresh token,refresh_token_lifetime (string): Specify the lifetime of an OAuth2 refresh token,refresh_token_lifetime_units (string): Specify the lifetime of an OAuth2 refresh token,scope (string, optional): Not supported at this time,user_id (string, optional): Not supported at this time}
        Required Body Parameters (type(dict) body example)- {
  "access_lifetime": "",
  "access_token_lifetime": "",
  "access_token_lifetime_units": "",
  "auto_confirm": 0,
  "client_description": "",
  "client_id": "",
  "client_public": false,
  "client_refresh": false,
  "client_secret": "",
  "enabled": false,
  "id": "",
  "grant_types": "",
  "profile_id": 0,
  "profile_name": "",
  "redirect_uri": "",
  "refresh_lifetime": "",
  "refresh_token_lifetime": "",
  "refresh_token_lifetime_units": "",
  "scope": "",
  "user_id": ""
}
        '''
        urlPath='/api-client/{client_id}'
        dictPath={'client_id': client_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteApiClientByClient_id(self,client_id=""):
        '''
        Operation: Delete an API client
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: client_id, Description: URL parameter client_id
        '''
        urlPath='/api-client/{client_id}'
        dictPath={'client_id': client_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:DenyListedUsers  
    #Function Section Description: Manage deny listed users

    def getDenyListedUsers(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of deny listed users
        HTTP Status Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/deny-listed-users'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def getDenyListedUsersByDeny_listed_users_id(self,deny_listed_users_id=""):
        '''
        Operation: Get a deny listed user
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: deny_listed_users_id, Description: Numeric ID of the deny listed user
        '''
        urlPath='/deny-listed-users/{deny_listed_users_id}'
        dictPath={'deny_listed_users_id': deny_listed_users_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def deleteDenyListedUsersByDeny_listed_users_id(self,deny_listed_users_id=""):
        '''
        Operation: Delete a deny listed user
        HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: deny_listed_users_id, Description: Numeric ID of the deny listed user
        '''
        urlPath='/deny-listed-users/{deny_listed_users_id}'
        dictPath={'deny_listed_users_id': deny_listed_users_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getDenyListedUsersUser_idByUser_idMac_addressMac_address(self,user_id="",mac_address=""):
        '''
        Operation: Get a deny listed user by Username and MAC Address
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: user_id, Description: User ID of the deny listed user
        Required Path Parameter Name: mac_address, Description: MAC address of the deny listed user
        '''
        urlPath='/deny-listed-users/user_id/{user_id}/mac_address/{mac_address}'
        dictPath={'user_id': user_id, 'mac_address': mac_address}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def deleteDenyListedUsersUser_idByUser_idMac_addressMac_address(self,user_id="",mac_address=""):
        '''
        Operation: Delete a deny listed user by Username and MAC Address
        HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: user_id, Description: User ID of the deny listed user
        Required Path Parameter Name: mac_address, Description: MAC address of the deny listed user
        '''
        urlPath='/deny-listed-users/user_id/{user_id}/mac_address/{mac_address}'
        dictPath={'user_id': user_id, 'mac_address': mac_address}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:Device  
    #Function Section Description: Manage device accounts

    def getDevice(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of device accounts
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default -id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/device'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newDevice(self,body=({}),change_of_authorization=""):
        '''
        Operation: Create a new device account
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- DeviceCreate {create_time (string, optional): Time at which the account was created,current_state (string, optional) = ['active' or 'disabled' or 'expired' or 'pending']: Read-only property indicating the current state of the account,enabled (boolean, optional): Flag indicating if the account is enabled,expire_time (string, optional): Time at which the account will expire,mac (string): MAC address of the device,notes (string, optional): Comments or notes stored with the account,role_id (integer): Role to assign to the account,role_name (string, optional): Name of the role assigned to the account,source (string, optional): Origin of the account,sponsor_name (string, optional): Name of the sponsor of the account,sponsor_profile (string, optional): Numeric operator profile ID for the account’s sponsor,sponsor_profile_name (string, optional): Name of the operator profile for the account’s sponsor,start_time (string, optional): Time at which the account will be enabled,visitor_name (string, optional): Name to display for the account,... (string, optional): Additional properties (custom fields) may be stored with the account}
        Required Body Parameters (type(dict) body example)- {
  "create_time": "",
  "current_state": "",
  "enabled": false,
  "expire_time": "",
  "mac": "",
  "notes": "",
  "role_id": 0,
  "role_name": "",
  "source": "",
  "sponsor_name": "",
  "sponsor_profile": "",
  "sponsor_profile_name": "",
  "start_time": "",
  "visitor_name": "",
  "...": ""
}
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/device'
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getDeviceByDevice_id(self,device_id=""):
        '''
        Operation: Get a device account
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: device_id, Description: Numeric ID of the device account
        '''
        urlPath='/device/{device_id}'
        dictPath={'device_id': device_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateDeviceByDevice_id(self,device_id="",body=({}),change_of_authorization=""):
        '''
        Operation: Update some fields of a device account
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: device_id, Description: Numeric ID of the device account
        Required Body Parameters (body description)- DeviceUpdate {create_time (string, optional): Time at which the account was created,current_state (string, optional) = ['active' or 'disabled' or 'expired' or 'pending']: Read-only property indicating the current state of the account,enabled (boolean, optional): Flag indicating if the account is enabled,expire_time (string, optional): Time at which the account will expire,id (integer, optional): Numeric ID of the device account (cannot be changed),mac (string, optional): MAC address of the device,mac_auth (boolean, optional): Flag indicating the account is a device, always set to true,notes (string, optional): Comments or notes stored with the account,password (string, optional),role_id (integer, optional): Role to assign to the account,role_name (string, optional): Name of the role assigned to the account,source (string, optional): Origin of the account,sponsor_name (string, optional): Name of the sponsor of the account,sponsor_profile (string, optional): Numeric operator profile ID for the account’s sponsor,sponsor_profile_name (string, optional): Name of the operator profile for the account’s sponsor,start_time (string, optional): Time at which the account will be enabled,username (string, optional),visitor_name (string, optional): Name to display for the account,... (string, optional): Additional properties (custom fields) may be stored with the account}
        Required Body Parameters (type(dict) body example)- {
  "create_time": "",
  "current_state": "",
  "enabled": false,
  "expire_time": "",
  "id": 0,
  "mac": "",
  "mac_auth": false,
  "notes": "",
  "password": "",
  "role_id": 0,
  "role_name": "",
  "source": "",
  "sponsor_name": "",
  "sponsor_profile": "",
  "sponsor_profile_name": "",
  "start_time": "",
  "username": "",
  "visitor_name": "",
  "...": ""
}
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/device/{device_id}'
        dictPath={'device_id': device_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceDeviceByDevice_id(self,device_id="",body=({}),change_of_authorization=""):
        '''
        Operation: Replace a device account
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: device_id, Description: Numeric ID of the device account
        Required Body Parameters (body description)- DeviceReplace {create_time (string, optional): Time at which the account was created,current_state (string, optional) = ['active' or 'disabled' or 'expired' or 'pending']: Read-only property indicating the current state of the account,enabled (boolean, optional): Flag indicating if the account is enabled,expire_time (string, optional): Time at which the account will expire,id (integer, optional): Numeric ID of the device account (cannot be changed),mac (string): MAC address of the device,notes (string, optional): Comments or notes stored with the account,role_id (integer): Role to assign to the account,role_name (string, optional): Name of the role assigned to the account,source (string, optional): Origin of the account,sponsor_name (string, optional): Name of the sponsor of the account,sponsor_profile (string, optional): Numeric operator profile ID for the account’s sponsor,sponsor_profile_name (string, optional): Name of the operator profile for the account’s sponsor,start_time (string, optional): Time at which the account will be enabled,visitor_name (string, optional): Name to display for the account,... (string, optional): Additional properties (custom fields) may be stored with the account}
        Required Body Parameters (type(dict) body example)- {
  "create_time": "",
  "current_state": "",
  "enabled": false,
  "expire_time": "",
  "id": 0,
  "mac": "",
  "notes": "",
  "role_id": 0,
  "role_name": "",
  "source": "",
  "sponsor_name": "",
  "sponsor_profile": "",
  "sponsor_profile_name": "",
  "start_time": "",
  "visitor_name": "",
  "...": ""
}
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/device/{device_id}'
        dictPath={'device_id': device_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteDeviceByDevice_id(self,device_id="",change_of_authorization=""):
        '''
        Operation: Delete a device account
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: device_id, Description: Numeric ID of the device account
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/device/{device_id}'
        dictPath={'device_id': device_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getDeviceMacByMacaddr(self,macaddr=""):
        '''
        Operation: Get a device account by MAC address
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: macaddr, Description: MAC address of the device account
        '''
        urlPath='/device/mac/{macaddr}'
        dictPath={'macaddr': macaddr}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateDeviceMacByMacaddr(self,macaddr="",body=({}),change_of_authorization=""):
        '''
        Operation: Update some fields of a device account by MAC address
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: macaddr, Description: MAC address of the device account
        Required Body Parameters (body description)- DeviceUpdate {create_time (string, optional): Time at which the account was created,current_state (string, optional) = ['active' or 'disabled' or 'expired' or 'pending']: Read-only property indicating the current state of the account,enabled (boolean, optional): Flag indicating if the account is enabled,expire_time (string, optional): Time at which the account will expire,id (integer, optional): Numeric ID of the device account (cannot be changed),mac (string, optional): MAC address of the device,mac_auth (boolean, optional): Flag indicating the account is a device, always set to true,notes (string, optional): Comments or notes stored with the account,password (string, optional),role_id (integer, optional): Role to assign to the account,role_name (string, optional): Name of the role assigned to the account,source (string, optional): Origin of the account,sponsor_name (string, optional): Name of the sponsor of the account,sponsor_profile (string, optional): Numeric operator profile ID for the account’s sponsor,sponsor_profile_name (string, optional): Name of the operator profile for the account’s sponsor,start_time (string, optional): Time at which the account will be enabled,username (string, optional),visitor_name (string, optional): Name to display for the account,... (string, optional): Additional properties (custom fields) may be stored with the account}
        Required Body Parameters (type(dict) body example)- {
  "create_time": "",
  "current_state": "",
  "enabled": false,
  "expire_time": "",
  "id": 0,
  "mac": "",
  "mac_auth": false,
  "notes": "",
  "password": "",
  "role_id": 0,
  "role_name": "",
  "source": "",
  "sponsor_name": "",
  "sponsor_profile": "",
  "sponsor_profile_name": "",
  "start_time": "",
  "username": "",
  "visitor_name": "",
  "...": ""
}
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/device/mac/{macaddr}'
        dictPath={'macaddr': macaddr}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceDeviceMacByMacaddr(self,macaddr="",body=({}),change_of_authorization=""):
        '''
        Operation: Replace a device account by MAC address
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: macaddr, Description: MAC address of the device account
        Required Body Parameters (body description)- DeviceReplace {create_time (string, optional): Time at which the account was created,current_state (string, optional) = ['active' or 'disabled' or 'expired' or 'pending']: Read-only property indicating the current state of the account,enabled (boolean, optional): Flag indicating if the account is enabled,expire_time (string, optional): Time at which the account will expire,id (integer, optional): Numeric ID of the device account (cannot be changed),mac (string): MAC address of the device,notes (string, optional): Comments or notes stored with the account,role_id (integer): Role to assign to the account,role_name (string, optional): Name of the role assigned to the account,source (string, optional): Origin of the account,sponsor_name (string, optional): Name of the sponsor of the account,sponsor_profile (string, optional): Numeric operator profile ID for the account’s sponsor,sponsor_profile_name (string, optional): Name of the operator profile for the account’s sponsor,start_time (string, optional): Time at which the account will be enabled,visitor_name (string, optional): Name to display for the account,... (string, optional): Additional properties (custom fields) may be stored with the account}
        Required Body Parameters (type(dict) body example)- {
  "create_time": "",
  "current_state": "",
  "enabled": false,
  "expire_time": "",
  "id": 0,
  "mac": "",
  "notes": "",
  "role_id": 0,
  "role_name": "",
  "source": "",
  "sponsor_name": "",
  "sponsor_profile": "",
  "sponsor_profile_name": "",
  "start_time": "",
  "visitor_name": "",
  "...": ""
}
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/device/mac/{macaddr}'
        dictPath={'macaddr': macaddr}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteDeviceMacByMacaddr(self,macaddr="",change_of_authorization=""):
        '''
        Operation: Delete a device account by MAC address
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: macaddr, Description: MAC address of the device account
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/device/mac/{macaddr}'
        dictPath={'macaddr': macaddr}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:Endpoint  
    #Function Section Description: Manage endpoints

    def getEndpoint(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of endpoints
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/endpoint'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newEndpoint(self,body=({})):
        '''
        Operation: Create a new endpoint
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- EndpointCreate {mac_address (string): MAC Address of the endpoint,description (string, optional): Description of the endpoint,status (string) = ['Known' or 'Unknown' or 'Disabled']: Status of the endpoint,device_insight_tags (string, optional): List of Device Insight Tags,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the endpoint}
        Required Body Parameters (type(dict) body example)- {
  "mac_address": "",
  "description": "",
  "status": "",
  "device_insight_tags": "",
  "attributes": "object"
}
        '''
        urlPath='/endpoint'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getEndpointByEndpoint_id(self,endpoint_id=""):
        '''
        Operation: Get an endpoint
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: endpoint_id, Description: Numeric ID of the endpoint
        '''
        urlPath='/endpoint/{endpoint_id}'
        dictPath={'endpoint_id': endpoint_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateEndpointByEndpoint_id(self,endpoint_id="",body=({})):
        '''
        Operation: Update some fields of an endpoint
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: endpoint_id, Description: Numeric ID of the endpoint
        Required Body Parameters (body description)- EndpointUpdate {mac_address (string, optional): MAC Address of the endpoint,description (string, optional): Description of the endpoint,status (string, optional) = ['Known' or 'Unknown' or 'Disabled']: Status of the endpoint,device_insight_tags (string, optional): List of Device Insight Tags,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the endpoint}
        Required Body Parameters (type(dict) body example)- {
  "mac_address": "",
  "description": "",
  "status": "",
  "device_insight_tags": "",
  "attributes": "object"
}
        '''
        urlPath='/endpoint/{endpoint_id}'
        dictPath={'endpoint_id': endpoint_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceEndpointByEndpoint_id(self,endpoint_id="",body=({})):
        '''
        Operation: Replace an endpoint
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: endpoint_id, Description: Numeric ID of the endpoint
        Required Body Parameters (body description)- EndpointReplace {mac_address (string): MAC Address of the endpoint,description (string, optional): Description of the endpoint,status (string) = ['Known' or 'Unknown' or 'Disabled']: Status of the endpoint,device_insight_tags (string, optional): List of Device Insight Tags,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the endpoint}
        Required Body Parameters (type(dict) body example)- {
  "mac_address": "",
  "description": "",
  "status": "",
  "device_insight_tags": "",
  "attributes": "object"
}
        '''
        urlPath='/endpoint/{endpoint_id}'
        dictPath={'endpoint_id': endpoint_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteEndpointByEndpoint_id(self,endpoint_id=""):
        '''
        Operation: Delete an endpoint
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: endpoint_id, Description: Numeric ID of the endpoint
        '''
        urlPath='/endpoint/{endpoint_id}'
        dictPath={'endpoint_id': endpoint_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getEndpointMacAddressByMac_address(self,mac_address=""):
        '''
        Operation: Get an endpoint by mac_address
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: mac_address, Description: Unique mac_address of the endpoint
        '''
        urlPath='/endpoint/mac-address/{mac_address}'
        dictPath={'mac_address': mac_address}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateEndpointMacAddressByMac_address(self,mac_address="",body=({})):
        '''
        Operation: Update some fields of an endpoint by mac_address
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: mac_address, Description: Unique mac_address of the endpoint
        Required Body Parameters (body description)- EndpointUpdate {mac_address (string, optional): MAC Address of the endpoint,description (string, optional): Description of the endpoint,status (string, optional) = ['Known' or 'Unknown' or 'Disabled']: Status of the endpoint,device_insight_tags (string, optional): List of Device Insight Tags,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the endpoint}
        Required Body Parameters (type(dict) body example)- {
  "mac_address": "",
  "description": "",
  "status": "",
  "device_insight_tags": "",
  "attributes": "object"
}
        '''
        urlPath='/endpoint/mac-address/{mac_address}'
        dictPath={'mac_address': mac_address}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceEndpointMacAddressByMac_address(self,mac_address="",body=({})):
        '''
        Operation: Replace an endpoint by mac_address
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: mac_address, Description: Unique mac_address of the endpoint
        Required Body Parameters (body description)- EndpointReplace {mac_address (string): MAC Address of the endpoint,description (string, optional): Description of the endpoint,status (string) = ['Known' or 'Unknown' or 'Disabled']: Status of the endpoint,device_insight_tags (string, optional): List of Device Insight Tags,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the endpoint}
        Required Body Parameters (type(dict) body example)- {
  "mac_address": "",
  "description": "",
  "status": "",
  "device_insight_tags": "",
  "attributes": "object"
}
        '''
        urlPath='/endpoint/mac-address/{mac_address}'
        dictPath={'mac_address': mac_address}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteEndpointMacAddressByMac_address(self,mac_address=""):
        '''
        Operation: Delete an endpoint by mac_address
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: mac_address, Description: Unique mac_address of the endpoint
        '''
        urlPath='/endpoint/mac-address/{mac_address}'
        dictPath={'mac_address': mac_address}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:ExternalAccount  
    #Function Section Description: Manage external accounts

    def getExternalAccount(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of external accounts
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/external-account'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newExternalAccount(self,body=({})):
        '''
        Operation: Add an external account
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- ExternalAccountCreate {name (string): Name of the external account,type (string) = ['SSH' or 'Domain' or 'SNMP']: Type of the external account,description (string, optional): Description of the external account,username (string, optional): User name for the external account,password (string, optional): Password for the external account,domain (string, optional): Domain for WMI external account,enable_password (string, optional): Enable-password for SSH external account,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP Version for SNMP external account,community (string, optional): Community string for V1 and V2C SNMP external account,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level for V3 SNMP external account,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authorization protocol for V3 SNMP external account,auth_key (string, optional): Authorization key for V3 SNMP external account,priv_protocol (string, optional) = ['DES_CBC' or 'AES_128' or 'AES_192' or 'AES_256']: Privacy protocol for V3 SNMP external account,priv_key (string, optional): Privacy key for V3 SNMP external account}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "type": "",
  "description": "",
  "username": "",
  "password": "",
  "domain": "",
  "enable_password": "",
  "snmp_version": "",
  "community": "",
  "security_level": "",
  "auth_protocol": "",
  "auth_key": "",
  "priv_protocol": "",
  "priv_key": ""
}
        '''
        urlPath='/external-account'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getExternalAccountByExternal_account_id(self,external_account_id=""):
        '''
        Operation: Get an external account
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: external_account_id, Description: Numeric ID of external account
        '''
        urlPath='/external-account/{external_account_id}'
        dictPath={'external_account_id': external_account_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateExternalAccountByExternal_account_id(self,external_account_id="",body=({})):
        '''
        Operation: Update some fields of an external account
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: external_account_id, Description: Numeric ID of external account
        Required Body Parameters (body description)- ExternalAccountUpdate {name (string, optional): Name of the external account,type (string, optional) = ['SSH' or 'Domain' or 'SNMP']: Type of the external account,description (string, optional): Description of the external account,username (string, optional): User name for the external account,password (string, optional): Password for the external account,domain (string, optional): Domain for WMI external account,enable_password (string, optional): Enable-password for SSH external account,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP Version for SNMP external account,community (string, optional): Community string for V1 and V2C SNMP external account,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level for V3 SNMP external account,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authorization protocol for V3 SNMP external account,auth_key (string, optional): Authorization key for V3 SNMP external account,priv_protocol (string, optional) = ['DES_CBC' or 'AES_128' or 'AES_192' or 'AES_256']: Privacy protocol for V3 SNMP external account,priv_key (string, optional): Privacy key for V3 SNMP external account}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "type": "",
  "description": "",
  "username": "",
  "password": "",
  "domain": "",
  "enable_password": "",
  "snmp_version": "",
  "community": "",
  "security_level": "",
  "auth_protocol": "",
  "auth_key": "",
  "priv_protocol": "",
  "priv_key": ""
}
        '''
        urlPath='/external-account/{external_account_id}'
        dictPath={'external_account_id': external_account_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceExternalAccountByExternal_account_id(self,external_account_id="",body=({})):
        '''
        Operation: Replace an external account
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: external_account_id, Description: Numeric ID of external account
        Required Body Parameters (body description)- ExternalAccountReplace {name (string): Name of the external account,type (string) = ['SSH' or 'Domain' or 'SNMP']: Type of the external account,description (string, optional): Description of the external account,username (string, optional): User name for the external account,password (string, optional): Password for the external account,domain (string, optional): Domain for WMI external account,enable_password (string, optional): Enable-password for SSH external account,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP Version for SNMP external account,community (string, optional): Community string for V1 and V2C SNMP external account,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level for V3 SNMP external account,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authorization protocol for V3 SNMP external account,auth_key (string, optional): Authorization key for V3 SNMP external account,priv_protocol (string, optional) = ['DES_CBC' or 'AES_128' or 'AES_192' or 'AES_256']: Privacy protocol for V3 SNMP external account,priv_key (string, optional): Privacy key for V3 SNMP external account}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "type": "",
  "description": "",
  "username": "",
  "password": "",
  "domain": "",
  "enable_password": "",
  "snmp_version": "",
  "community": "",
  "security_level": "",
  "auth_protocol": "",
  "auth_key": "",
  "priv_protocol": "",
  "priv_key": ""
}
        '''
        urlPath='/external-account/{external_account_id}'
        dictPath={'external_account_id': external_account_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteExternalAccountByExternal_account_id(self,external_account_id=""):
        '''
        Operation: Delete an external account
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: external_account_id, Description: Numeric ID of external account
        '''
        urlPath='/external-account/{external_account_id}'
        dictPath={'external_account_id': external_account_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getExternalAccountNameByName(self,name=""):
        '''
        Operation: Get an external account by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of external account
        '''
        urlPath='/external-account/name/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateExternalAccountNameByName(self,name="",body=({})):
        '''
        Operation: Update some fields of an external account by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of external account
        Required Body Parameters (body description)- ExternalAccountUpdate {name (string, optional): Name of the external account,type (string, optional) = ['SSH' or 'Domain' or 'SNMP']: Type of the external account,description (string, optional): Description of the external account,username (string, optional): User name for the external account,password (string, optional): Password for the external account,domain (string, optional): Domain for WMI external account,enable_password (string, optional): Enable-password for SSH external account,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP Version for SNMP external account,community (string, optional): Community string for V1 and V2C SNMP external account,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level for V3 SNMP external account,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authorization protocol for V3 SNMP external account,auth_key (string, optional): Authorization key for V3 SNMP external account,priv_protocol (string, optional) = ['DES_CBC' or 'AES_128' or 'AES_192' or 'AES_256']: Privacy protocol for V3 SNMP external account,priv_key (string, optional): Privacy key for V3 SNMP external account}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "type": "",
  "description": "",
  "username": "",
  "password": "",
  "domain": "",
  "enable_password": "",
  "snmp_version": "",
  "community": "",
  "security_level": "",
  "auth_protocol": "",
  "auth_key": "",
  "priv_protocol": "",
  "priv_key": ""
}
        '''
        urlPath='/external-account/name/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceExternalAccountNameByName(self,name="",body=({})):
        '''
        Operation: Replace an external account by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of external account
        Required Body Parameters (body description)- ExternalAccountReplace {name (string): Name of the external account,type (string) = ['SSH' or 'Domain' or 'SNMP']: Type of the external account,description (string, optional): Description of the external account,username (string, optional): User name for the external account,password (string, optional): Password for the external account,domain (string, optional): Domain for WMI external account,enable_password (string, optional): Enable-password for SSH external account,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP Version for SNMP external account,community (string, optional): Community string for V1 and V2C SNMP external account,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level for V3 SNMP external account,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authorization protocol for V3 SNMP external account,auth_key (string, optional): Authorization key for V3 SNMP external account,priv_protocol (string, optional) = ['DES_CBC' or 'AES_128' or 'AES_192' or 'AES_256']: Privacy protocol for V3 SNMP external account,priv_key (string, optional): Privacy key for V3 SNMP external account}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "type": "",
  "description": "",
  "username": "",
  "password": "",
  "domain": "",
  "enable_password": "",
  "snmp_version": "",
  "community": "",
  "security_level": "",
  "auth_protocol": "",
  "auth_key": "",
  "priv_protocol": "",
  "priv_key": ""
}
        '''
        urlPath='/external-account/name/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteExternalAccountNameByName(self,name=""):
        '''
        Operation: Delete an external account by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of external account
        '''
        urlPath='/external-account/name/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:GuestUser  
    #Function Section Description: Manage guest accounts

    def getGuest(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of guest accounts
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default -id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/guest'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newGuest(self,body=({}),change_of_authorization=""):
        '''
        Operation: Create a new guest account
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- GuestUserCreate {create_time (string, optional): Time at which the account was created,do_expire (integer, optional): Action to take when the expire_time is reached,email (string, optional): Email address for the account,enabled (boolean, optional): Flag indicating if the account is enabled,expire_time (string, optional): Time at which the account will expire,mac (string, optional): MAC address of the guest’s device,notes (string, optional): Comments or notes stored with the account,password (string): Password for the account,role_id (integer): Role to assign to the account,simultaneous_use (integer, optional): Number of simultaneous sessions allowed for the account,sponsor_email (string, optional): Email address of the sponsor,sponsor_name (string, optional): Name of the sponsor of the account,sponsor_profile (string, optional): Profile of the sponsor of the account,start_time (string, optional): Time at which the account will be enabled,username (string): Username of the account,visitor_company (string, optional): The guest’s company name,visitor_name (string, optional): The guest’s full name,visitor_phone (string, optional): The guest’s contact telephone number,... (string, optional): Additional properties (custom fields) may be stored with the account}
        Required Body Parameters (type(dict) body example)- {
  "create_time": "",
  "do_expire": 0,
  "email": "",
  "enabled": false,
  "expire_time": "",
  "mac": "",
  "notes": "",
  "password": "",
  "role_id": 0,
  "simultaneous_use": 0,
  "sponsor_email": "",
  "sponsor_name": "",
  "sponsor_profile": "",
  "start_time": "",
  "username": "",
  "visitor_company": "",
  "visitor_name": "",
  "visitor_phone": "",
  "...": ""
}
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/guest'
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getGuestByGuest_id(self,guest_id=""):
        '''
        Operation: Get a guest account
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
        '''
        urlPath='/guest/{guest_id}'
        dictPath={'guest_id': guest_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateGuestByGuest_id(self,guest_id="",body=({}),change_of_authorization=""):
        '''
        Operation: Update some fields of a guest account
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
        Required Body Parameters (body description)- GuestUserUpdate {create_time (string, optional): Time at which the account was created,do_expire (integer, optional): Action to take when the expire_time is reached,email (string, optional): Email address for the account,enabled (boolean, optional): Flag indicating if the account is enabled,expire_time (string, optional): Time at which the account will expire,id (integer, optional): Numeric ID of the guest account (cannot be changed),mac (string, optional): MAC address of the guest’s device,notes (string, optional): Comments or notes stored with the account,password (string, optional): Password for the account,role_id (integer, optional): Role to assign to the account,simultaneous_use (integer, optional): Number of simultaneous sessions allowed for the account,sponsor_email (string, optional): Email address of the sponsor,sponsor_name (string, optional): Name of the sponsor of the account,sponsor_profile (string, optional): Profile of the sponsor of the account,start_time (string, optional): Time at which the account will be enabled,username (string, optional): Username of the account,visitor_company (string, optional): The guest’s company name,visitor_name (string, optional): The guest’s full name,visitor_phone (string, optional): The guest’s contact telephone number,... (string, optional): Additional properties (custom fields) may be stored with the account}
        Required Body Parameters (type(dict) body example)- {
  "create_time": "",
  "do_expire": 0,
  "email": "",
  "enabled": false,
  "expire_time": "",
  "id": 0,
  "mac": "",
  "notes": "",
  "password": "",
  "role_id": 0,
  "simultaneous_use": 0,
  "sponsor_email": "",
  "sponsor_name": "",
  "sponsor_profile": "",
  "start_time": "",
  "username": "",
  "visitor_company": "",
  "visitor_name": "",
  "visitor_phone": "",
  "...": ""
}
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/guest/{guest_id}'
        dictPath={'guest_id': guest_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceGuestByGuest_id(self,guest_id="",body=({}),change_of_authorization=""):
        '''
        Operation: Replace a guest account
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
        Required Body Parameters (body description)- GuestUserReplace {create_time (string, optional): Time at which the account was created,do_expire (integer, optional): Action to take when the expire_time is reached,email (string, optional): Email address for the account,enabled (boolean, optional): Flag indicating if the account is enabled,expire_time (string, optional): Time at which the account will expire,id (integer, optional): Numeric ID of the guest account (cannot be changed),mac (string, optional): MAC address of the guest’s device,notes (string, optional): Comments or notes stored with the account,password (string): Password for the account,role_id (integer): Role to assign to the account,simultaneous_use (integer, optional): Number of simultaneous sessions allowed for the account,sponsor_email (string, optional): Email address of the sponsor,sponsor_name (string, optional): Name of the sponsor of the account,sponsor_profile (string, optional): Profile of the sponsor of the account,start_time (string, optional): Time at which the account will be enabled,username (string): Username of the account,visitor_company (string, optional): The guest’s company name,visitor_name (string, optional): The guest’s full name,visitor_phone (string, optional): The guest’s contact telephone number,... (string, optional): Additional properties (custom fields) may be stored with the account}
        Required Body Parameters (type(dict) body example)- {
  "create_time": "",
  "do_expire": 0,
  "email": "",
  "enabled": false,
  "expire_time": "",
  "id": 0,
  "mac": "",
  "notes": "",
  "password": "",
  "role_id": 0,
  "simultaneous_use": 0,
  "sponsor_email": "",
  "sponsor_name": "",
  "sponsor_profile": "",
  "start_time": "",
  "username": "",
  "visitor_company": "",
  "visitor_name": "",
  "visitor_phone": "",
  "...": ""
}
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/guest/{guest_id}'
        dictPath={'guest_id': guest_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteGuestByGuest_id(self,guest_id="",change_of_authorization=""):
        '''
        Operation: Delete a guest account
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/guest/{guest_id}'
        dictPath={'guest_id': guest_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getGuestUsernameByUsername(self,username=""):
        '''
        Operation: Get a guest account by username
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: username, Description: Unique username of the guest account
        '''
        urlPath='/guest/username/{username}'
        dictPath={'username': username}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateGuestUsernameByUsername(self,username="",body=({}),change_of_authorization=""):
        '''
        Operation: Update some fields of a guest account by username
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: username, Description: Unique username of the guest account
        Required Body Parameters (body description)- GuestUserUpdate {create_time (string, optional): Time at which the account was created,do_expire (integer, optional): Action to take when the expire_time is reached,email (string, optional): Email address for the account,enabled (boolean, optional): Flag indicating if the account is enabled,expire_time (string, optional): Time at which the account will expire,id (integer, optional): Numeric ID of the guest account (cannot be changed),mac (string, optional): MAC address of the guest’s device,notes (string, optional): Comments or notes stored with the account,password (string, optional): Password for the account,role_id (integer, optional): Role to assign to the account,simultaneous_use (integer, optional): Number of simultaneous sessions allowed for the account,sponsor_email (string, optional): Email address of the sponsor,sponsor_name (string, optional): Name of the sponsor of the account,sponsor_profile (string, optional): Profile of the sponsor of the account,start_time (string, optional): Time at which the account will be enabled,username (string, optional): Username of the account,visitor_company (string, optional): The guest’s company name,visitor_name (string, optional): The guest’s full name,visitor_phone (string, optional): The guest’s contact telephone number,... (string, optional): Additional properties (custom fields) may be stored with the account}
        Required Body Parameters (type(dict) body example)- {
  "create_time": "",
  "do_expire": 0,
  "email": "",
  "enabled": false,
  "expire_time": "",
  "id": 0,
  "mac": "",
  "notes": "",
  "password": "",
  "role_id": 0,
  "simultaneous_use": 0,
  "sponsor_email": "",
  "sponsor_name": "",
  "sponsor_profile": "",
  "start_time": "",
  "username": "",
  "visitor_company": "",
  "visitor_name": "",
  "visitor_phone": "",
  "...": ""
}
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/guest/username/{username}'
        dictPath={'username': username}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceGuestUsernameByUsername(self,username="",body=({}),change_of_authorization=""):
        '''
        Operation: Replace a guest account by username
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: username, Description: Unique username of the guest account
        Required Body Parameters (body description)- GuestUserReplace {create_time (string, optional): Time at which the account was created,do_expire (integer, optional): Action to take when the expire_time is reached,email (string, optional): Email address for the account,enabled (boolean, optional): Flag indicating if the account is enabled,expire_time (string, optional): Time at which the account will expire,id (integer, optional): Numeric ID of the guest account (cannot be changed),mac (string, optional): MAC address of the guest’s device,notes (string, optional): Comments or notes stored with the account,password (string): Password for the account,role_id (integer): Role to assign to the account,simultaneous_use (integer, optional): Number of simultaneous sessions allowed for the account,sponsor_email (string, optional): Email address of the sponsor,sponsor_name (string, optional): Name of the sponsor of the account,sponsor_profile (string, optional): Profile of the sponsor of the account,start_time (string, optional): Time at which the account will be enabled,username (string): Username of the account,visitor_company (string, optional): The guest’s company name,visitor_name (string, optional): The guest’s full name,visitor_phone (string, optional): The guest’s contact telephone number,... (string, optional): Additional properties (custom fields) may be stored with the account}
        Required Body Parameters (type(dict) body example)- {
  "create_time": "",
  "do_expire": 0,
  "email": "",
  "enabled": false,
  "expire_time": "",
  "id": 0,
  "mac": "",
  "notes": "",
  "password": "",
  "role_id": 0,
  "simultaneous_use": 0,
  "sponsor_email": "",
  "sponsor_name": "",
  "sponsor_profile": "",
  "start_time": "",
  "username": "",
  "visitor_company": "",
  "visitor_name": "",
  "visitor_phone": "",
  "...": ""
}
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/guest/username/{username}'
        dictPath={'username': username}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteGuestUsernameByUsername(self,username="",change_of_authorization=""):
        '''
        Operation: Delete a guest account by username
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: username, Description: Unique username of the guest account
        Optional Query Parameter Name: change_of_authorization, Description: true: Updates the network state using Disconnect-Request or CoA-Request, depending on the changes madefalse: No action is takenblank or unset: Use the default setting from Configuration » Authentication » Dynamic Authorization
        '''
        urlPath='/guest/username/{username}'
        dictPath={'username': username}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'change_of_authorization': change_of_authorization}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:LocalUser  
    #Function Section Description: Manage local users

    def getLocalUser(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of local users
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/local-user'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newLocalUser(self,body=({})):
        '''
        Operation: Create a new local user
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- LocalUserCreate {user_id (string): Unique user id of the local user,password (string): Password of the local user,username (string): User name of the local user,role_name (string): Role name of the local user,enabled (boolean, optional): Flag indicating if the account is enabled,change_pwd_next_login (boolean, optional): Flag indicating if the password change is required in next login,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the local user account}
        Required Body Parameters (type(dict) body example)- {
  "user_id": "",
  "password": "",
  "username": "",
  "role_name": "",
  "enabled": false,
  "change_pwd_next_login": false,
  "attributes": "object"
}
        '''
        urlPath='/local-user'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getLocalUserByLocal_user_id(self,local_user_id=""):
        '''
        Operation: Get a local user
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: local_user_id, Description: Numeric ID of the local user
        '''
        urlPath='/local-user/{local_user_id}'
        dictPath={'local_user_id': local_user_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateLocalUserByLocal_user_id(self,local_user_id="",body=({})):
        '''
        Operation: Update some fields of a local user
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: local_user_id, Description: Numeric ID of the local user
        Required Body Parameters (body description)- LocalUserUpdate {user_id (string, optional): Unique user id of the local user,password (string, optional): Password of the local user,username (string, optional): User name of the local user,role_name (string, optional): Role name of the local user,enabled (boolean, optional): Flag indicating if the account is enabled,change_pwd_next_login (boolean, optional): Flag indicating if the password change is required in next login,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the local user account}
        Required Body Parameters (type(dict) body example)- {
  "user_id": "",
  "password": "",
  "username": "",
  "role_name": "",
  "enabled": false,
  "change_pwd_next_login": false,
  "attributes": "object"
}
        '''
        urlPath='/local-user/{local_user_id}'
        dictPath={'local_user_id': local_user_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceLocalUserByLocal_user_id(self,local_user_id="",body=({})):
        '''
        Operation: Replace a local user
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: local_user_id, Description: Numeric ID of the local user
        Required Body Parameters (body description)- LocalUserReplace {user_id (string): Unique user id of the local user,password (string): Password of the local user,username (string): User name of the local user,role_name (string): Role name of the local user,enabled (boolean, optional): Flag indicating if the account is enabled,change_pwd_next_login (boolean, optional): Flag indicating if the password change is required in next login,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the local user account}
        Required Body Parameters (type(dict) body example)- {
  "user_id": "",
  "password": "",
  "username": "",
  "role_name": "",
  "enabled": false,
  "change_pwd_next_login": false,
  "attributes": "object"
}
        '''
        urlPath='/local-user/{local_user_id}'
        dictPath={'local_user_id': local_user_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteLocalUserByLocal_user_id(self,local_user_id=""):
        '''
        Operation: Delete a local user
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: local_user_id, Description: Numeric ID of the local user
        '''
        urlPath='/local-user/{local_user_id}'
        dictPath={'local_user_id': local_user_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getLocalUserUserIdByUser_id(self,user_id=""):
        '''
        Operation: Get a local user by user_id
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: user_id, Description: Unique user_id of the local user
        '''
        urlPath='/local-user/user-id/{user_id}'
        dictPath={'user_id': user_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateLocalUserUserIdByUser_id(self,user_id="",body=({})):
        '''
        Operation: Update some fields of a local user by user_id
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: user_id, Description: Unique user_id of the local user
        Required Body Parameters (body description)- LocalUserUpdate {user_id (string, optional): Unique user id of the local user,password (string, optional): Password of the local user,username (string, optional): User name of the local user,role_name (string, optional): Role name of the local user,enabled (boolean, optional): Flag indicating if the account is enabled,change_pwd_next_login (boolean, optional): Flag indicating if the password change is required in next login,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the local user account}
        Required Body Parameters (type(dict) body example)- {
  "user_id": "",
  "password": "",
  "username": "",
  "role_name": "",
  "enabled": false,
  "change_pwd_next_login": false,
  "attributes": "object"
}
        '''
        urlPath='/local-user/user-id/{user_id}'
        dictPath={'user_id': user_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceLocalUserUserIdByUser_id(self,user_id="",body=({})):
        '''
        Operation: Replace a local user by user_id
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: user_id, Description: Unique user_id of the local user
        Required Body Parameters (body description)- LocalUserReplace {user_id (string): Unique user id of the local user,password (string): Password of the local user,username (string): User name of the local user,role_name (string): Role name of the local user,enabled (boolean, optional): Flag indicating if the account is enabled,change_pwd_next_login (boolean, optional): Flag indicating if the password change is required in next login,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the local user account}
        Required Body Parameters (type(dict) body example)- {
  "user_id": "",
  "password": "",
  "username": "",
  "role_name": "",
  "enabled": false,
  "change_pwd_next_login": false,
  "attributes": "object"
}
        '''
        urlPath='/local-user/user-id/{user_id}'
        dictPath={'user_id': user_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteLocalUserUserIdByUser_id(self,user_id=""):
        '''
        Operation: Delete a local user by user_id
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: user_id, Description: Unique user_id of the local user
        '''
        urlPath='/local-user/user-id/{user_id}'
        dictPath={'user_id': user_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
