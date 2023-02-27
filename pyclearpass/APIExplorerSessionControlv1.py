
from pyclearpass.common import _generateParameterisedURL,_removeEmptyKeys,ClearPassAPILogin

#File Name: APIExplorerSessionControlv1.py

class apiSessionControl(ClearPassAPILogin):

    #Function Section Name:ActiveSession  
    #Function Section Description: Manage active sessions

    def getSession(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of active sessions
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default -id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/session'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def getSessionById(self,id=""):
        '''
        Operation: Get an active session
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: URL parameter id
        '''
        urlPath='/session/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        

    #Function Section Name:ActiveSessionDisconnect  
    #Function Section Description: Disconnect an active session

    def newSessionByIdDisconnect(self,id="",body=({})):
        '''
        Operation: Disconnect active session
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the session to disconnect
        Required Body Parameters (body description)- ActiveSessionDisconnect {id (string): ID of the session to disconnect,confirm_disconnect (boolean): Flag to confirm disconnecting the active session}
        Required Body Parameters (type(dict) body example)- {
  "id": "",
  "confirm_disconnect": false
}
        '''
        urlPath='/session/{id}/disconnect'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:ActiveSessionReauthorize  
    #Function Section Description: Reauthorize an active session

    def getSessionByIdReauthorize(self,id="",template_type=""):
        '''
        Operation: Get reauthorization profile(s) for an active session
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: ID of the session to reauthorize
        Optional Query Parameter Name: template_type, Description: Reauthorize profile type (Disconnect/CoA)
        '''
        urlPath='/session/{id}/reauthorize'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'template_type': template_type}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newSessionByIdReauthorize(self,id="",body=({})):
        '''
        Operation: Reauthorize active session
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the session to reauthorize
        Required Body Parameters (body description)- ActiveSessionReauthorize {confirm_reauthorize (boolean, optional): Flag to confirm the session reauthorization,reauthorize_profile (string, optional): Specify the name of the reauthorization profile to apply to the session}
        Required Body Parameters (type(dict) body example)- {
  "confirm_reauthorize": false,
  "reauthorize_profile": ""
}
        '''
        urlPath='/session/{id}/reauthorize'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:SessionAction  
    #Function Section Description: Manage Session Action Methods

    def newSessionActionDisconnect(self,body=({}),async_=""):
        '''
        Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by multiple fields.
        HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
        Required Body Parameters (type(dict) body example)- {
  "filter": "object",
  "enforcement_profile": "object",
  "sort": ""
}
        Optional Query Parameter Name: async, Description: trigger asynchronous API calls
        '''
        urlPath='/session-action/disconnect'
        dictQuery={'async': async_}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def newSessionActionDisconnectMacByMac_address(self,body=({}),async_="",mac_address=""):
        '''
        Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by mac-address.
        HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
        Required Body Parameters (type(dict) body example)- {
  "filter": "object",
  "enforcement_profile": "object",
  "sort": ""
}
        Optional Query Parameter Name: async, Description: trigger asynchronous API calls
        Required Path Parameter Name: mac_address, Description: filter by mac-address
        '''
        urlPath='/session-action/disconnect/mac/{mac_address}'
        dictPath={'mac_address': mac_address}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'async': async_}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def newSessionActionDisconnectUsernameByUsername(self,body=({}),async_="",username=""):
        '''
        Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by username.
        HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
        Required Body Parameters (type(dict) body example)- {
  "filter": "object",
  "enforcement_profile": "object",
  "sort": ""
}
        Optional Query Parameter Name: async, Description: trigger asynchronous API calls
        Required Path Parameter Name: username, Description: filter by username
        '''
        urlPath='/session-action/disconnect/username/{username}'
        dictPath={'username': username}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'async': async_}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def newSessionActionDisconnectIpByClient_ip_address(self,body=({}),async_="",client_ip_address=""):
        '''
        Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by client-ip-address.
        HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
        Required Body Parameters (type(dict) body example)- {
  "filter": "object",
  "enforcement_profile": "object",
  "sort": ""
}
        Optional Query Parameter Name: async, Description: trigger asynchronous API calls
        Required Path Parameter Name: client_ip_address, Description: filter by client-ip-address
        '''
        urlPath='/session-action/disconnect/ip/{client_ip_address}'
        dictPath={'client_ip_address': client_ip_address}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'async': async_}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def newSessionActionCoa(self,body=({}),async_=""):
        '''
        Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by multiple fields.
        HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
        Required Body Parameters (type(dict) body example)- {
  "filter": "object",
  "enforcement_profile": "object",
  "sort": ""
}
        Optional Query Parameter Name: async, Description: trigger asynchronous API calls
        '''
        urlPath='/session-action/coa'
        dictQuery={'async': async_}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def newSessionActionCoaMacByMac_address(self,body=({}),async_="",mac_address=""):
        '''
        Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by mac-address.
        HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
        Required Body Parameters (type(dict) body example)- {
  "filter": "object",
  "enforcement_profile": "object",
  "sort": ""
}
        Optional Query Parameter Name: async, Description: trigger asynchronous API calls
        Required Path Parameter Name: mac_address, Description: filter by mac-address
        '''
        urlPath='/session-action/coa/mac/{mac_address}'
        dictPath={'mac_address': mac_address}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'async': async_}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def newSessionActionCoaUsernameByUsername(self,body=({}),async_="",username=""):
        '''
        Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by username.
        HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
        Required Body Parameters (type(dict) body example)- {
  "filter": "object",
  "enforcement_profile": "object",
  "sort": ""
}
        Optional Query Parameter Name: async, Description: trigger asynchronous API calls
        Required Path Parameter Name: username, Description: filter by username
        '''
        urlPath='/session-action/coa/username/{username}'
        dictPath={'username': username}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'async': async_}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def newSessionActionCoaIpByClient_ip_address(self,body=({}),async_="",client_ip_address=""):
        '''
        Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by client-ip-address.
        HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
        Required Body Parameters (type(dict) body example)- {
  "filter": "object",
  "enforcement_profile": "object",
  "sort": ""
}
        Optional Query Parameter Name: async, Description: trigger asynchronous API calls
        Required Path Parameter Name: client_ip_address, Description: filter by client-ip-address
        '''
        urlPath='/session-action/coa/ip/{client_ip_address}'
        dictPath={'client_ip_address': client_ip_address}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'async': async_}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getSessionActionByAction_id(self,action_id="",offset="",limit=""):
        '''
        Operation: Returns the current status of a disconnected or reauthorized active session by the action ID.
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: action_id, Description: request body
        Optional Query Parameter Name: offset, Description: Starting point to return rows from a result set. i.e Default: 0
        Optional Query Parameter Name: limit, Description: Limit the number of rows returned from a result set. i.e Default: 25
        '''
        urlPath='/session-action/{action_id}'
        dictPath={'action_id': action_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'offset': offset, 'limit': limit}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
