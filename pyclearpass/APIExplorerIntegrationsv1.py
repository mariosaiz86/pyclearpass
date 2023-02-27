
from pyclearpass.common import _generateParameterisedURL,_removeEmptyKeys,ClearPassAPILogin

#File Name: APIExplorerIntegrationsv1.py

class apiIntegrations(ClearPassAPILogin):

    #Function Section Name:ContextServerAction  
    #Function Section Description: Manage Context Server Actions

    def getContextServerAction(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of Context Server Actions
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/context-server-action'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newContextServerAction(self,body=({})):
        '''
        Operation: Create a new Context Server Action
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- ContextServerActionCreate {server_type (string) = ['Aruba Activate' or 'VMware AirWatch' or 'JAMF' or 'MobileIron Core' or 'IBM MaaS360' or 'SAP Afaria' or 'SOTI' or 'Google Admin Console' or 'Palo Alto Networks Panorama' or 'Palo Alto Networks Firewall' or 'Juniper Networks SRX' or 'Citrix XenMobile' or 'Generic HTTP Context Server' or 'Aruba Airwave' or 'Aruba Central' or 'ClearPass Cloud Proxy' or 'Aruba IntroSpect']: Server Type of the Context Server Action,server_name (string, optional): Server Name of the Context Server Action,action_name (string): Action Name of the Context Server Action,action_type (string, optional) = ['Send_Login_Info' or 'Send_HIP_Report' or 'Register_Device' or 'Register_Role' or 'Register_Posture' or 'Send_Logout_Info' or 'Unregister_Device' or 'Unregister_Role' or 'Unregister_Posture']: Action Type of the Context Server Action,description (string, optional): Description of the Context Server Action,http_method (string) = ['GET' or 'POST' or 'PATCH' or 'PUT' or 'DELETE']: Http method of the Context Server Action,auth_method (string, optional) = ['none' or 'basic' or 'oauth2' or 'cert']: Authentication Method of the Context Server Action,url (string): URL of the Context Server Action,content_type (string, optional) = ['HTML' or 'JSON' or 'PLANE' or 'XML']: Content-Type of the Context Server Action. Note : For CUSTOM type use any string,content (string, optional): Content of the Context Server Action,headers (object, optional): Headers(key/value pairs) of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1"},{"attr_name":"key2", "attr_value":"value2"}]),attributes (object, optional): Attributes of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1", "is_sensitive":true},{"attr_name":"key2", "attr_value":"value2", "is_sensitive": false}])}
        Required Body Parameters (type(dict) body example)- {
  "server_type": "",
  "server_name": "",
  "action_name": "",
  "action_type": "",
  "description": "",
  "http_method": "",
  "auth_method": "",
  "url": "",
  "content_type": "",
  "content": "",
  "headers": "object",
  "attributes": "object"
}
        '''
        urlPath='/context-server-action'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getContextServerActionByContext_server_action_id(self,context_server_action_id=""):
        '''
        Operation: Get a Context Server Action
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: context_server_action_id, Description: Numeric ID of the csa
        '''
        urlPath='/context-server-action/{context_server_action_id}'
        dictPath={'context_server_action_id': context_server_action_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateContextServerActionByContext_server_action_id(self,context_server_action_id="",body=({})):
        '''
        Operation: Update some fields of a Context Server Action
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: context_server_action_id, Description: Numeric ID of the csa
        Required Body Parameters (body description)- ContextServerActionUpdate {server_type (string, optional) = ['Aruba Activate' or 'VMware AirWatch' or 'JAMF' or 'MobileIron Core' or 'IBM MaaS360' or 'SAP Afaria' or 'SOTI' or 'Google Admin Console' or 'Palo Alto Networks Panorama' or 'Palo Alto Networks Firewall' or 'Juniper Networks SRX' or 'Citrix XenMobile' or 'Generic HTTP Context Server' or 'Aruba Airwave' or 'Aruba Central' or 'ClearPass Cloud Proxy' or 'Aruba IntroSpect']: Server Type of the Context Server Action,server_name (string, optional): Server Name of the Context Server Action,action_name (string, optional): Action Name of the Context Server Action,action_type (string, optional) = ['Send_Login_Info' or 'Send_HIP_Report' or 'Register_Device' or 'Register_Role' or 'Register_Posture' or 'Send_Logout_Info' or 'Unregister_Device' or 'Unregister_Role' or 'Unregister_Posture']: Action Type of the Context Server Action,description (string, optional): Description of the Context Server Action,http_method (string, optional) = ['GET' or 'POST' or 'PATCH' or 'PUT' or 'DELETE']: Http method of the Context Server Action,auth_method (string, optional) = ['none' or 'basic' or 'oauth2' or 'cert']: Authentication Method of the Context Server Action,url (string, optional): URL of the Context Server Action,content_type (string, optional) = ['HTML' or 'JSON' or 'PLANE' or 'XML']: Content-Type of the Context Server Action. Note : For CUSTOM type use any string,content (string, optional): Content of the Context Server Action,headers (object, optional): Headers(key/value pairs) of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1"},{"attr_name":"key2", "attr_value":"value2"}]),attributes (object, optional): Attributes of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1", "is_sensitive":true},{"attr_name":"key2", "attr_value":"value2", "is_sensitive": false}])}
        Required Body Parameters (type(dict) body example)- {
  "server_type": "",
  "server_name": "",
  "action_name": "",
  "action_type": "",
  "description": "",
  "http_method": "",
  "auth_method": "",
  "url": "",
  "content_type": "",
  "content": "",
  "headers": "object",
  "attributes": "object"
}
        '''
        urlPath='/context-server-action/{context_server_action_id}'
        dictPath={'context_server_action_id': context_server_action_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceContextServerActionByContext_server_action_id(self,context_server_action_id="",body=({})):
        '''
        Operation: Replace a Context Server Action
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: context_server_action_id, Description: Numeric ID of the csa
        Required Body Parameters (body description)- ContextServerActionReplace {server_type (string) = ['Aruba Activate' or 'VMware AirWatch' or 'JAMF' or 'MobileIron Core' or 'IBM MaaS360' or 'SAP Afaria' or 'SOTI' or 'Google Admin Console' or 'Palo Alto Networks Panorama' or 'Palo Alto Networks Firewall' or 'Juniper Networks SRX' or 'Citrix XenMobile' or 'Generic HTTP Context Server' or 'Aruba Airwave' or 'Aruba Central' or 'ClearPass Cloud Proxy' or 'Aruba IntroSpect']: Server Type of the Context Server Action,server_name (string, optional): Server Name of the Context Server Action,action_name (string): Action Name of the Context Server Action,action_type (string, optional) = ['Send_Login_Info' or 'Send_HIP_Report' or 'Register_Device' or 'Register_Role' or 'Register_Posture' or 'Send_Logout_Info' or 'Unregister_Device' or 'Unregister_Role' or 'Unregister_Posture']: Action Type of the Context Server Action,description (string, optional): Description of the Context Server Action,http_method (string) = ['GET' or 'POST' or 'PATCH' or 'PUT' or 'DELETE']: Http method of the Context Server Action,auth_method (string, optional) = ['none' or 'basic' or 'oauth2' or 'cert']: Authentication Method of the Context Server Action,url (string): URL of the Context Server Action,content_type (string, optional) = ['HTML' or 'JSON' or 'PLANE' or 'XML']: Content-Type of the Context Server Action. Note : For CUSTOM type use any string,content (string, optional): Content of the Context Server Action,headers (object, optional): Headers(key/value pairs) of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1"},{"attr_name":"key2", "attr_value":"value2"}]),attributes (object, optional): Attributes of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1", "is_sensitive":true},{"attr_name":"key2", "attr_value":"value2", "is_sensitive": false}])}
        Required Body Parameters (type(dict) body example)- {
  "server_type": "",
  "server_name": "",
  "action_name": "",
  "action_type": "",
  "description": "",
  "http_method": "",
  "auth_method": "",
  "url": "",
  "content_type": "",
  "content": "",
  "headers": "object",
  "attributes": "object"
}
        '''
        urlPath='/context-server-action/{context_server_action_id}'
        dictPath={'context_server_action_id': context_server_action_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteContextServerActionByContext_server_action_id(self,context_server_action_id=""):
        '''
        Operation: Delete a Context Server Action
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: context_server_action_id, Description: Numeric ID of the csa
        '''
        urlPath='/context-server-action/{context_server_action_id}'
        dictPath={'context_server_action_id': context_server_action_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getContextServerActionByServer_typeActionNameAction_name(self,server_type="",action_name=""):
        '''
        Operation: Get a Context Server Action by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_type, Description: Server type of the context server action
        Required Path Parameter Name: action_name, Description: Unique action name of the context server action
        '''
        urlPath='/context-server-action/{server_type}/action-name/{action_name}'
        dictPath={'server_type': server_type, 'action_name': action_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateContextServerActionByServer_typeActionNameAction_name(self,server_type="",action_name="",body=({})):
        '''
        Operation: Update some fields of a Context Server Action by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_type, Description: Server type of the context server action
        Required Path Parameter Name: action_name, Description: Unique action name of the context server action
        Required Body Parameters (body description)- ContextServerActionUpdate {server_type (string, optional) = ['Aruba Activate' or 'VMware AirWatch' or 'JAMF' or 'MobileIron Core' or 'IBM MaaS360' or 'SAP Afaria' or 'SOTI' or 'Google Admin Console' or 'Palo Alto Networks Panorama' or 'Palo Alto Networks Firewall' or 'Juniper Networks SRX' or 'Citrix XenMobile' or 'Generic HTTP Context Server' or 'Aruba Airwave' or 'Aruba Central' or 'ClearPass Cloud Proxy' or 'Aruba IntroSpect']: Server Type of the Context Server Action,server_name (string, optional): Server Name of the Context Server Action,action_name (string, optional): Action Name of the Context Server Action,action_type (string, optional) = ['Send_Login_Info' or 'Send_HIP_Report' or 'Register_Device' or 'Register_Role' or 'Register_Posture' or 'Send_Logout_Info' or 'Unregister_Device' or 'Unregister_Role' or 'Unregister_Posture']: Action Type of the Context Server Action,description (string, optional): Description of the Context Server Action,http_method (string, optional) = ['GET' or 'POST' or 'PATCH' or 'PUT' or 'DELETE']: Http method of the Context Server Action,auth_method (string, optional) = ['none' or 'basic' or 'oauth2' or 'cert']: Authentication Method of the Context Server Action,url (string, optional): URL of the Context Server Action,content_type (string, optional) = ['HTML' or 'JSON' or 'PLANE' or 'XML']: Content-Type of the Context Server Action. Note : For CUSTOM type use any string,content (string, optional): Content of the Context Server Action,headers (object, optional): Headers(key/value pairs) of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1"},{"attr_name":"key2", "attr_value":"value2"}]),attributes (object, optional): Attributes of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1", "is_sensitive":true},{"attr_name":"key2", "attr_value":"value2", "is_sensitive": false}])}
        Required Body Parameters (type(dict) body example)- {
  "server_type": "",
  "server_name": "",
  "action_name": "",
  "action_type": "",
  "description": "",
  "http_method": "",
  "auth_method": "",
  "url": "",
  "content_type": "",
  "content": "",
  "headers": "object",
  "attributes": "object"
}
        '''
        urlPath='/context-server-action/{server_type}/action-name/{action_name}'
        dictPath={'server_type': server_type, 'action_name': action_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceContextServerActionByServer_typeActionNameAction_name(self,server_type="",action_name="",body=({})):
        '''
        Operation: Replace a Context Server Action by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_type, Description: Server type of the context server action
        Required Path Parameter Name: action_name, Description: Unique action name of the context server action
        Required Body Parameters (body description)- ContextServerActionReplace {server_type (string) = ['Aruba Activate' or 'VMware AirWatch' or 'JAMF' or 'MobileIron Core' or 'IBM MaaS360' or 'SAP Afaria' or 'SOTI' or 'Google Admin Console' or 'Palo Alto Networks Panorama' or 'Palo Alto Networks Firewall' or 'Juniper Networks SRX' or 'Citrix XenMobile' or 'Generic HTTP Context Server' or 'Aruba Airwave' or 'Aruba Central' or 'ClearPass Cloud Proxy' or 'Aruba IntroSpect']: Server Type of the Context Server Action,server_name (string, optional): Server Name of the Context Server Action,action_name (string): Action Name of the Context Server Action,action_type (string, optional) = ['Send_Login_Info' or 'Send_HIP_Report' or 'Register_Device' or 'Register_Role' or 'Register_Posture' or 'Send_Logout_Info' or 'Unregister_Device' or 'Unregister_Role' or 'Unregister_Posture']: Action Type of the Context Server Action,description (string, optional): Description of the Context Server Action,http_method (string) = ['GET' or 'POST' or 'PATCH' or 'PUT' or 'DELETE']: Http method of the Context Server Action,auth_method (string, optional) = ['none' or 'basic' or 'oauth2' or 'cert']: Authentication Method of the Context Server Action,url (string): URL of the Context Server Action,content_type (string, optional) = ['HTML' or 'JSON' or 'PLANE' or 'XML']: Content-Type of the Context Server Action. Note : For CUSTOM type use any string,content (string, optional): Content of the Context Server Action,headers (object, optional): Headers(key/value pairs) of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1"},{"attr_name":"key2", "attr_value":"value2"}]),attributes (object, optional): Attributes of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1", "is_sensitive":true},{"attr_name":"key2", "attr_value":"value2", "is_sensitive": false}])}
        Required Body Parameters (type(dict) body example)- {
  "server_type": "",
  "server_name": "",
  "action_name": "",
  "action_type": "",
  "description": "",
  "http_method": "",
  "auth_method": "",
  "url": "",
  "content_type": "",
  "content": "",
  "headers": "object",
  "attributes": "object"
}
        '''
        urlPath='/context-server-action/{server_type}/action-name/{action_name}'
        dictPath={'server_type': server_type, 'action_name': action_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteContextServerActionByServer_typeActionNameAction_name(self,server_type="",action_name=""):
        '''
        Operation: Delete a Context Server Action by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_type, Description: Server type of the context server action
        Required Path Parameter Name: action_name, Description: Unique action name of the context server action
        '''
        urlPath='/context-server-action/{server_type}/action-name/{action_name}'
        dictPath={'server_type': server_type, 'action_name': action_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:DeviceInsight  
    #Function Section Description: Manage Device Insight Integration

    def getDeviceInsight(self,server_type="",action_name=""):
        '''
        Operation: Get Device Insight Integration details
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_type, Description: Server type of the context server action
        Required Path Parameter Name: action_name, Description: Unique action name of the context server action
        '''
        urlPath='/device-insight'
        dictPath={'server_type': server_type, 'action_name': action_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newDeviceInsight(self,body=({})):
        '''
        Operation: Update Device Insight Integration values
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- DeviceInsightCreate {enable_device_insight (boolean, optional): Enable/Disable Device Insight Integration,activation_token (string, optional): Registration Token,primary_clearpass_server_uuid (string, optional): Primary ClearPass Server UUID,standby_clearpass_server_uuid (string, optional): null,bypass_proxy (boolean, optional): Bypass Proxy,polling_interval (integer, optional): Polling Interval,sync_time (integer, optional): Sync Time,activation_status (string, optional): Activation Status,activation_error (string, optional): Activation Error,activation_timestamp (string, optional): Activation Timestamp,registration_status (string, optional): Registration Status,last_sync_timestamp (string, optional): Last Sync Timestamp,last_sync_run (string, optional): Last Sync Run,aruba_central_tenant_id (string, optional): Aruba Central Tenant Id,device_insight_collector_id (string, optional): Device Insight Collector Id,tag_update_action (string, optional) = ['NONE' or 'ANY' or 'SELECTED']: Tags Update Action,tags_for_disconnect (string, optional): Tags for Disconnect,radius_coa_action (string, optional): Radius CoA action,analyzer_admin_url (string, optional): Analyzer Admin URL}
        Required Body Parameters (type(dict) body example)- {
  "enable_device_insight": false,
  "activation_token": "",
  "primary_clearpass_server_uuid": "",
  "standby_clearpass_server_uuid": "",
  "bypass_proxy": false,
  "polling_interval": 0,
  "sync_time": 0,
  "activation_status": "",
  "activation_error": "",
  "activation_timestamp": "",
  "registration_status": "",
  "last_sync_timestamp": "",
  "last_sync_run": "",
  "aruba_central_tenant_id": "",
  "device_insight_collector_id": "",
  "tag_update_action": "",
  "tags_for_disconnect": "",
  "radius_coa_action": "",
  "analyzer_admin_url": ""
}
        '''
        urlPath='/device-insight'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:EndpointContextServer  
    #Function Section Description: Manage Endpoint Context servers

    def getEndpointContextServer(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list endpoint context servers
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/endpoint-context-server'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newEndpointContextServer(self,body=({})):
        '''
        Operation: Create a new endpoint context server
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- EndpointContextServerCreate {server_type (string) = ['Aruba Activate' or 'VMware AirWatch' or 'JAMF' or 'MobileIron Core' or 'IBM MaaS360' or 'SAP Afaria' or 'SOTI' or 'Google Admin Console' or 'Palo Alto Networks Panorama' or 'Palo Alto Networks Firewall' or 'Juniper Networks SRX' or 'Citrix XenMobile' or 'Generic HTTP Context Server' or 'Aruba Airwave' or 'Aruba Central' or 'ClearPass Cloud Proxy' or 'Aruba IntroSpect']: Server Type,server_name (string): Server Name,server_base_url (string): Server Base URL,auth_method (string) = ['basic' or 'oauth2' or 'cert' or 'both']: Authentication Method of the Context Server,username (string, optional): Username,password (string, optional): Password,oauth2_client_id (string, optional): Client ID of OAuth2,oauth2_client_secret (string, optional): Client Secret of OAuth2,oauth2_access_token_url (string, optional): Access token URL of OAuth2,client_cert_CN (string, optional): Client Certificate CN,client_cert_expiry_date (string, optional): Client Certificate expiry date,vendor_attrs (object, optional): Attributes,validate_server (boolean): Enable to validate the server certificate,status (boolean): Enable Server,ip_version (string, optional) = ['ipV4' or 'ipV6' or 'ipBoth']: IP Version,bypass_proxy (boolean): Enable to bypass proxy server}
        Required Body Parameters (type(dict) body example)- {
  "server_type": "",
  "server_name": "",
  "server_base_url": "",
  "auth_method": "",
  "username": "",
  "password": "",
  "oauth2_client_id": "",
  "oauth2_client_secret": "",
  "oauth2_access_token_url": "",
  "client_cert_CN": "",
  "client_cert_expiry_date": "",
  "vendor_attrs": "object",
  "validate_server": false,
  "status": false,
  "ip_version": "",
  "bypass_proxy": false
}
        '''
        urlPath='/endpoint-context-server'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getEndpointContextServerByEndpoint_context_server_id(self,endpoint_context_server_id=""):
        '''
        Operation: Get an endpoint context server
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: endpoint_context_server_id, Description: URL parameter endpoint_context_server_id
        '''
        urlPath='/endpoint-context-server/{endpoint_context_server_id}'
        dictPath={'endpoint_context_server_id': endpoint_context_server_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateEndpointContextServerByEndpoint_context_server_id(self,endpoint_context_server_id="",body=({})):
        '''
        Operation: Update some fields of an endpoint context server
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: endpoint_context_server_id, Description: URL parameter endpoint_context_server_id
        Required Body Parameters (body description)- EndpointContextServerUpdate {server_type (string, optional) = ['Aruba Activate' or 'VMware AirWatch' or 'JAMF' or 'MobileIron Core' or 'IBM MaaS360' or 'SAP Afaria' or 'SOTI' or 'Google Admin Console' or 'Palo Alto Networks Panorama' or 'Palo Alto Networks Firewall' or 'Juniper Networks SRX' or 'Citrix XenMobile' or 'Generic HTTP Context Server' or 'Aruba Airwave' or 'Aruba Central' or 'ClearPass Cloud Proxy' or 'Aruba IntroSpect']: Server Type,server_name (string, optional): Server Name,server_base_url (string, optional): Server Base URL,auth_method (string, optional) = ['basic' or 'oauth2' or 'cert' or 'both']: Authentication Method of the Context Server,username (string, optional): Username,password (string, optional): Password,oauth2_client_id (string, optional): Client ID of OAuth2,oauth2_client_secret (string, optional): Client Secret of OAuth2,oauth2_access_token_url (string, optional): Access token URL of OAuth2,client_cert_CN (string, optional): Client Certificate CN,client_cert_expiry_date (string, optional): Client Certificate expiry date,vendor_attrs (object, optional): Attributes,validate_server (boolean, optional): Enable to validate the server certificate,status (boolean, optional): Enable Server,ip_version (string, optional) = ['ipV4' or 'ipV6' or 'ipBoth']: IP Version,bypass_proxy (boolean, optional): Enable to bypass proxy server}
        Required Body Parameters (type(dict) body example)- {
  "server_type": "",
  "server_name": "",
  "server_base_url": "",
  "auth_method": "",
  "username": "",
  "password": "",
  "oauth2_client_id": "",
  "oauth2_client_secret": "",
  "oauth2_access_token_url": "",
  "client_cert_CN": "",
  "client_cert_expiry_date": "",
  "vendor_attrs": "object",
  "validate_server": false,
  "status": false,
  "ip_version": "",
  "bypass_proxy": false
}
        '''
        urlPath='/endpoint-context-server/{endpoint_context_server_id}'
        dictPath={'endpoint_context_server_id': endpoint_context_server_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceEndpointContextServerByEndpoint_context_server_id(self,endpoint_context_server_id="",body=({})):
        '''
        Operation: Replace an endpoint context server
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: endpoint_context_server_id, Description: URL parameter endpoint_context_server_id
        Required Body Parameters (body description)- EndpointContextServerReplace {server_type (string) = ['Aruba Activate' or 'VMware AirWatch' or 'JAMF' or 'MobileIron Core' or 'IBM MaaS360' or 'SAP Afaria' or 'SOTI' or 'Google Admin Console' or 'Palo Alto Networks Panorama' or 'Palo Alto Networks Firewall' or 'Juniper Networks SRX' or 'Citrix XenMobile' or 'Generic HTTP Context Server' or 'Aruba Airwave' or 'Aruba Central' or 'ClearPass Cloud Proxy' or 'Aruba IntroSpect']: Server Type,server_name (string): Server Name,server_base_url (string): Server Base URL,auth_method (string) = ['basic' or 'oauth2' or 'cert' or 'both']: Authentication Method of the Context Server,username (string, optional): Username,password (string, optional): Password,oauth2_client_id (string, optional): Client ID of OAuth2,oauth2_client_secret (string, optional): Client Secret of OAuth2,oauth2_access_token_url (string, optional): Access token URL of OAuth2,client_cert_CN (string, optional): Client Certificate CN,client_cert_expiry_date (string, optional): Client Certificate expiry date,vendor_attrs (object, optional): Attributes,validate_server (boolean): Enable to validate the server certificate,status (boolean): Enable Server,ip_version (string, optional) = ['ipV4' or 'ipV6' or 'ipBoth']: IP Version,bypass_proxy (boolean): Enable to bypass proxy server}
        Required Body Parameters (type(dict) body example)- {
  "server_type": "",
  "server_name": "",
  "server_base_url": "",
  "auth_method": "",
  "username": "",
  "password": "",
  "oauth2_client_id": "",
  "oauth2_client_secret": "",
  "oauth2_access_token_url": "",
  "client_cert_CN": "",
  "client_cert_expiry_date": "",
  "vendor_attrs": "object",
  "validate_server": false,
  "status": false,
  "ip_version": "",
  "bypass_proxy": false
}
        '''
        urlPath='/endpoint-context-server/{endpoint_context_server_id}'
        dictPath={'endpoint_context_server_id': endpoint_context_server_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteEndpointContextServerByEndpoint_context_server_id(self,endpoint_context_server_id=""):
        '''
        Operation: Delete an endpoint context server
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: endpoint_context_server_id, Description: URL parameter endpoint_context_server_id
        '''
        urlPath='/endpoint-context-server/{endpoint_context_server_id}'
        dictPath={'endpoint_context_server_id': endpoint_context_server_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getEndpointContextServerServerNameByServer_name(self,server_name=""):
        '''
        Operation: Get an endpoint context server by server name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_name, Description: Unique name of the Endpoint Context Server
        '''
        urlPath='/endpoint-context-server/server-name/{server_name}'
        dictPath={'server_name': server_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateEndpointContextServerServerNameByServer_name(self,server_name="",body=({})):
        '''
        Operation: Update some fields of an endpoint context server by server name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_name, Description: Unique name of the Endpoint Context Server
        Required Body Parameters (body description)- EndpointContextServerUpdate {server_type (string, optional) = ['Aruba Activate' or 'VMware AirWatch' or 'JAMF' or 'MobileIron Core' or 'IBM MaaS360' or 'SAP Afaria' or 'SOTI' or 'Google Admin Console' or 'Palo Alto Networks Panorama' or 'Palo Alto Networks Firewall' or 'Juniper Networks SRX' or 'Citrix XenMobile' or 'Generic HTTP Context Server' or 'Aruba Airwave' or 'Aruba Central' or 'ClearPass Cloud Proxy' or 'Aruba IntroSpect']: Server Type,server_name (string, optional): Server Name,server_base_url (string, optional): Server Base URL,auth_method (string, optional) = ['basic' or 'oauth2' or 'cert' or 'both']: Authentication Method of the Context Server,username (string, optional): Username,password (string, optional): Password,oauth2_client_id (string, optional): Client ID of OAuth2,oauth2_client_secret (string, optional): Client Secret of OAuth2,oauth2_access_token_url (string, optional): Access token URL of OAuth2,client_cert_CN (string, optional): Client Certificate CN,client_cert_expiry_date (string, optional): Client Certificate expiry date,vendor_attrs (object, optional): Attributes,validate_server (boolean, optional): Enable to validate the server certificate,status (boolean, optional): Enable Server,ip_version (string, optional) = ['ipV4' or 'ipV6' or 'ipBoth']: IP Version,bypass_proxy (boolean, optional): Enable to bypass proxy server}
        Required Body Parameters (type(dict) body example)- {
  "server_type": "",
  "server_name": "",
  "server_base_url": "",
  "auth_method": "",
  "username": "",
  "password": "",
  "oauth2_client_id": "",
  "oauth2_client_secret": "",
  "oauth2_access_token_url": "",
  "client_cert_CN": "",
  "client_cert_expiry_date": "",
  "vendor_attrs": "object",
  "validate_server": false,
  "status": false,
  "ip_version": "",
  "bypass_proxy": false
}
        '''
        urlPath='/endpoint-context-server/server-name/{server_name}'
        dictPath={'server_name': server_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceEndpointContextServerServerNameByServer_name(self,server_name="",body=({})):
        '''
        Operation: Replace an endpoint context server by server name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_name, Description: Unique name of the Endpoint Context Server
        Required Body Parameters (body description)- EndpointContextServerReplace {server_type (string) = ['Aruba Activate' or 'VMware AirWatch' or 'JAMF' or 'MobileIron Core' or 'IBM MaaS360' or 'SAP Afaria' or 'SOTI' or 'Google Admin Console' or 'Palo Alto Networks Panorama' or 'Palo Alto Networks Firewall' or 'Juniper Networks SRX' or 'Citrix XenMobile' or 'Generic HTTP Context Server' or 'Aruba Airwave' or 'Aruba Central' or 'ClearPass Cloud Proxy' or 'Aruba IntroSpect']: Server Type,server_name (string): Server Name,server_base_url (string): Server Base URL,auth_method (string) = ['basic' or 'oauth2' or 'cert' or 'both']: Authentication Method of the Context Server,username (string, optional): Username,password (string, optional): Password,oauth2_client_id (string, optional): Client ID of OAuth2,oauth2_client_secret (string, optional): Client Secret of OAuth2,oauth2_access_token_url (string, optional): Access token URL of OAuth2,client_cert_CN (string, optional): Client Certificate CN,client_cert_expiry_date (string, optional): Client Certificate expiry date,vendor_attrs (object, optional): Attributes,validate_server (boolean): Enable to validate the server certificate,status (boolean): Enable Server,ip_version (string, optional) = ['ipV4' or 'ipV6' or 'ipBoth']: IP Version,bypass_proxy (boolean): Enable to bypass proxy server}
        Required Body Parameters (type(dict) body example)- {
  "server_type": "",
  "server_name": "",
  "server_base_url": "",
  "auth_method": "",
  "username": "",
  "password": "",
  "oauth2_client_id": "",
  "oauth2_client_secret": "",
  "oauth2_access_token_url": "",
  "client_cert_CN": "",
  "client_cert_expiry_date": "",
  "vendor_attrs": "object",
  "validate_server": false,
  "status": false,
  "ip_version": "",
  "bypass_proxy": false
}
        '''
        urlPath='/endpoint-context-server/server-name/{server_name}'
        dictPath={'server_name': server_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteEndpointContextServerServerNameByServer_name(self,server_name=""):
        '''
        Operation: Delete an endpoint context server by server name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_name, Description: Unique name of the Endpoint Context Server
        '''
        urlPath='/endpoint-context-server/server-name/{server_name}'
        dictPath={'server_name': server_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def updateEndpointContextServerByEndpoint_context_server_idTriggerPoll(self,endpoint_context_server_id=""):
        '''
        Operation: Trigger polling for an endpoint context server
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: endpoint_context_server_id, Description: URL parameter endpoint_context_server_id
        '''
        urlPath='/endpoint-context-server/{endpoint_context_server_id}/trigger-poll'
        dictPath={'endpoint_context_server_id': endpoint_context_server_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateEndpointContextServerServerNameByServer_nameTriggerPoll(self,server_name=""):
        '''
        Operation: Trigger polling for an endpoint context server by server name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_name, Description: Unique name of the Endpoint Context Server
        '''
        urlPath='/endpoint-context-server/server-name/{server_name}/trigger-poll'
        dictPath={'server_name': server_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        

    #Function Section Name:EventSources  
    #Function Section Description: Manage event sources

    def getEventSources(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of event sources
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/event-sources'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newEventSources(self,body=({})):
        '''
        Operation: Create a new event source
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- EventSourcesCreate {name (string): Event source Name,description (string, optional): Event source description,ipaddress (string): Unique IP Address of the event source,vendor (string) = ['Aruba IntroSpect' or 'Check Point' or 'Infoblox' or 'Juniper Networks' or 'Palo Alto Networks']: Vendor name,type (string) = ['Syslog']: Event source type,enable (boolean, optional): Enable event source}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "ipaddress": "",
  "vendor": "",
  "type": "",
  "enable": false
}
        '''
        urlPath='/event-sources'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getEventSourcesByEvent_sources_id(self,event_sources_id=""):
        '''
        Operation: Get an event source
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: event_sources_id, Description: Unique id of the Event source
        '''
        urlPath='/event-sources/{event_sources_id}'
        dictPath={'event_sources_id': event_sources_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateEventSourcesByEvent_sources_id(self,event_sources_id="",body=({})):
        '''
        Operation: Update some fields of an event source
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: event_sources_id, Description: Unique id of the Event source
        Required Body Parameters (body description)- EventSourcesUpdate {name (string, optional): Event source Name,description (string, optional): Event source description,ipaddress (string, optional): Unique IP Address of the event source,vendor (string, optional) = ['Aruba IntroSpect' or 'Check Point' or 'Infoblox' or 'Juniper Networks' or 'Palo Alto Networks']: Vendor name,type (string, optional) = ['Syslog']: Event source type,enable (boolean, optional): Enable event source}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "ipaddress": "",
  "vendor": "",
  "type": "",
  "enable": false
}
        '''
        urlPath='/event-sources/{event_sources_id}'
        dictPath={'event_sources_id': event_sources_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceEventSourcesByEvent_sources_id(self,event_sources_id="",body=({})):
        '''
        Operation: Replace an event source
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: event_sources_id, Description: Unique id of the Event source
        Required Body Parameters (body description)- EventSourcesReplace {name (string): Event source Name,description (string, optional): Event source description,ipaddress (string): Unique IP Address of the event source,vendor (string) = ['Aruba IntroSpect' or 'Check Point' or 'Infoblox' or 'Juniper Networks' or 'Palo Alto Networks']: Vendor name,type (string) = ['Syslog']: Event source type,enable (boolean, optional): Enable event source}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "ipaddress": "",
  "vendor": "",
  "type": "",
  "enable": false
}
        '''
        urlPath='/event-sources/{event_sources_id}'
        dictPath={'event_sources_id': event_sources_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteEventSourcesByEvent_sources_id(self,event_sources_id=""):
        '''
        Operation: Delete an event source
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: event_sources_id, Description: Unique id of the Event source
        '''
        urlPath='/event-sources/{event_sources_id}'
        dictPath={'event_sources_id': event_sources_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getEventSourcesNameByName(self,name=""):
        '''
        Operation: Get an event source by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the event source
        '''
        urlPath='/event-sources/name/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateEventSourcesNameByName(self,name="",body=({})):
        '''
        Operation: Update some fields of an event source by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the event source
        Required Body Parameters (body description)- EventSourcesUpdate {name (string, optional): Event source Name,description (string, optional): Event source description,ipaddress (string, optional): Unique IP Address of the event source,vendor (string, optional) = ['Aruba IntroSpect' or 'Check Point' or 'Infoblox' or 'Juniper Networks' or 'Palo Alto Networks']: Vendor name,type (string, optional) = ['Syslog']: Event source type,enable (boolean, optional): Enable event source}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "ipaddress": "",
  "vendor": "",
  "type": "",
  "enable": false
}
        '''
        urlPath='/event-sources/name/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceEventSourcesNameByName(self,name="",body=({})):
        '''
        Operation: Replace an event source by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the event source
        Required Body Parameters (body description)- EventSourcesReplace {name (string): Event source Name,description (string, optional): Event source description,ipaddress (string): Unique IP Address of the event source,vendor (string) = ['Aruba IntroSpect' or 'Check Point' or 'Infoblox' or 'Juniper Networks' or 'Palo Alto Networks']: Vendor name,type (string) = ['Syslog']: Event source type,enable (boolean, optional): Enable event source}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "ipaddress": "",
  "vendor": "",
  "type": "",
  "enable": false
}
        '''
        urlPath='/event-sources/name/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteEventSourcesNameByName(self,name=""):
        '''
        Operation: Delete an event source by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the event source
        '''
        urlPath='/event-sources/name/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:ExtensionInstance  
    #Function Section Description: Manage the system’s installed extensions

    def getExtensionInstance(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of installed extensions
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +name)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/extension/instance'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newExtensionInstance(self,body=({})):
        '''
        Operation: Install an extension
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- ExtensionInstanceCreate {state (string, optional) = ['stopped' or 'running']: Desired state of the extension,store_id (string): ID from the extension store,files (object, optional): Maps extension file IDs to local content items, with ‘public:’ or ‘private:’ prefix,ip_address (string, optional): IP address to allocate to the extension, or null,note (string, optional): Note to be displayed with the extension.}
        Required Body Parameters (type(dict) body example)- {
  "state": "",
  "store_id": "",
  "files": "object",
  "ip_address": "",
  "note": ""
}
        '''
        urlPath='/extension/instance'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getExtensionInstanceById(self,id=""):
        '''
        Operation: Get details of an installed extension
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: ID of the extension instance
        '''
        urlPath='/extension/instance/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateExtensionInstanceById(self,id="",body=({})):
        '''
        Operation: Change the state of an installed extension
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the extension instance
        Required Body Parameters (body description)- ExtensionInstanceModify {state (string, optional) = ['stopped' or 'running']: Desired state of the extension,note (string, optional): Note to be displayed with the extension.}
        Required Body Parameters (type(dict) body example)- {
  "state": "",
  "note": ""
}
        '''
        urlPath='/extension/instance/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def deleteExtensionInstanceById(self,id="",force=""):
        '''
        Operation: Uninstall an extension
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the extension instance
        Optional Query Parameter Name: force, Description: True to send a kill signal to the extension before deleting
        '''
        urlPath='/extension/instance/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'force': force}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:ExtensionInstanceConfig  
    #Function Section Description: Configure an installed extension

    def getExtensionInstanceByIdConfig(self,id=""):
        '''
        Operation: Get the configuration of an installed extension
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the extension instance
        '''
        urlPath='/extension/instance/{id}/config'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def replaceExtensionInstanceByIdConfig(self,id="",body=({})):
        '''
        Operation: Set the configuration of an installed extension
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the extension instance
        Required Body Parameters (body description)- ExtensionInstanceConfig {}
        Required Body Parameters (type(dict) body example)- {}
        '''
        urlPath='/extension/instance/{id}/config'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put')
        
        

    #Function Section Name:ExtensionInstanceLog  
    #Function Section Description: Read logs from an installed extension

    def getExtensionInstanceByIdLog(self,id="",stdout="",stderr="",since="",timestamps="",tail=""):
        '''
        Operation: Get the log output from an installed extension
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the extension instance
        Optional Query Parameter Name: stdout, Description: Include extension’s standard-output messages
        Optional Query Parameter Name: stderr, Description: Include extension’s standard-error messages
        Optional Query Parameter Name: since, Description: Specify a UNIX timestamp to only return log entries since that time
        Optional Query Parameter Name: timestamps, Description: Prefix every log line with its UTC timestamp
        Optional Query Parameter Name: tail, Description: Return this number of lines at the end of the logs, or "all" for everything
        '''
        urlPath='/extension/instance/{id}/log'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'stdout': stdout, 'stderr': stderr, 'since': since, 'timestamps': timestamps, 'tail': tail}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        

    #Function Section Name:ExtensionInstanceReinstall  
    #Function Section Description: Reinstall an extension

    def newExtensionInstanceByIdReinstall(self,id="",body=({})):
        '''
        Operation: Reinstall an extension
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the extension instance
        Required Body Parameters (body description)- ExtensionInstanceReinstall {state (string, optional) = ['stopped' or 'running']: Desired state of the extension,files (object, optional): Maps extension file IDs to local content items, with ‘public:’ or ‘private:’ prefix,ip_address (string, optional): IP address to allocate to the extension, or null}
        Required Body Parameters (type(dict) body example)- {
  "state": "",
  "files": "object",
  "ip_address": ""
}
        '''
        urlPath='/extension/instance/{id}/reinstall'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:ExtensionInstanceRestart  
    #Function Section Description: Restart an installed extension

    def newExtensionInstanceByIdRestart(self,id=""):
        '''
        Operation: Restart an installed extension
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the extension instance
        '''
        urlPath='/extension/instance/{id}/restart'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post')
        
        

    #Function Section Name:ExtensionInstanceStart  
    #Function Section Description: Start an installed extension

    def newExtensionInstanceByIdStart(self,id=""):
        '''
        Operation: Start an installed extension
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the extension instance
        '''
        urlPath='/extension/instance/{id}/start'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post')
        
        

    #Function Section Name:ExtensionInstanceStop  
    #Function Section Description: Stop an installed extension

    def newExtensionInstanceByIdStop(self,id=""):
        '''
        Operation: Stop an installed extension
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the extension instance
        '''
        urlPath='/extension/instance/{id}/stop'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post')
        
        

    #Function Section Name:ExtensionInstanceUpgrade  
    #Function Section Description: Upgrade an extension

    def getExtensionInstanceByIdUpgrade(self,id=""):
        '''
        Operation: Get information on an extension's available upgrade
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: ID of the extension instance
        '''
        urlPath='/extension/instance/{id}/upgrade'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newExtensionInstanceByIdUpgrade(self,id="",body=({})):
        '''
        Operation: Upgrade an extension
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: ID of the extension instance
        Required Body Parameters (body description)- ExtensionInstanceUpgrade {major (boolean, optional): Indicated whether to install major extension upgrades. False by default.,state (string, optional) = ['stopped' or 'running']: Desired state of the extension,files (object, optional): Maps extension file IDs to local content items, with ‘public:’ or ‘private:’ prefix,ip_address (string, optional): IP address to allocate to the extension, or null}
        Required Body Parameters (type(dict) body example)- {
  "major": false,
  "state": "",
  "files": "object",
  "ip_address": ""
}
        '''
        urlPath='/extension/instance/{id}/upgrade'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:ExtensionStore  
    #Function Section Description: Query the extension store

    def getExtensionStore(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Find a extension in the store
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +name)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/extension/store'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def getExtensionStoreById(self,id=""):
        '''
        Operation: Get details of an extension in the store
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: URL parameter id
        '''
        urlPath='/extension/store/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        

    #Function Section Name:IngressEventDictionary  
    #Function Section Description: Manage Ingress Event Dictionaries

    def getIngressEventDictionary(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of Ingress Event Dictionaries
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/ingress-event-dictionary'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newIngressEventDictionary(self,body=({})):
        '''
        Operation: Create a new Ingress Event Dictionary
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- IngressEventDictionaryCreate {vendor (string): Vendor of the ingress event,format_name (string): Format Name of the ingress event,prefix (string): Prefix of the ingress event,status (boolean, optional): Status of the ingress event,description (string, optional): Description of the ingress event,format (string, optional): Format of the ingress event,sample (string, optional): Sample of the ingress event,filter (string): Filter of the ingress event,fields (array[Fields]): Fields of the ingress event,generic_fields (array[GenericFields]): Generic Fields of the ingress event}Fields {attr_name (string): Ingress Event Field atrribute name,data_type (string): Ingress Event Field attribute type,allowed_values (string, optional): Allowed values for Ingress Event Field in CSV format}GenericFields {attr_name (string): Ingress Event Generic Field attribute name,generic_name (string): Ingress Event Generic name of the attribute}
        Required Body Parameters (type(dict) body example)- {
  "vendor": "",
  "format_name": "",
  "prefix": "",
  "status": false,
  "description": "",
  "format": "",
  "sample": "",
  "filter": "",
  "fields": [
    {
      "attr_name": "",
      "data_type": "",
      "allowed_values": ""
    }
  ],
  "generic_fields": [
    {
      "attr_name": "",
      "generic_name": ""
    }
  ]
}
        '''
        urlPath='/ingress-event-dictionary'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getIngressEventDictionaryByIngress_event_dictionary_id(self,ingress_event_dictionary_id=""):
        '''
        Operation: Get an Ingress Event Dictionary
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: ingress_event_dictionary_id, Description: Numeric ID of the ingress event dictionary
        '''
        urlPath='/ingress-event-dictionary/{ingress_event_dictionary_id}'
        dictPath={'ingress_event_dictionary_id': ingress_event_dictionary_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateIngressEventDictionaryByIngress_event_dictionary_id(self,ingress_event_dictionary_id="",body=({})):
        '''
        Operation: Update an Ingress Event Dictionary
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: ingress_event_dictionary_id, Description: Numeric ID of the ingress event dictionary
        Required Body Parameters (body description)- IngressEventDictionaryUpdate {vendor (string, optional): Vendor of the ingress event,format_name (string, optional): Format Name of the ingress event,prefix (string, optional): Prefix of the ingress event,status (boolean, optional): Status of the ingress event,description (string, optional): Description of the ingress event,format (string, optional): Format of the ingress event,sample (string, optional): Sample of the ingress event,filter (string, optional): Filter of the ingress event,fields (array[Fields], optional): Fields of the ingress event,generic_fields (array[GenericFields], optional): Generic Fields of the ingress event}Fields {attr_name (string): Ingress Event Field atrribute name,data_type (string): Ingress Event Field attribute type,allowed_values (string, optional): Allowed values for Ingress Event Field in CSV format}GenericFields {attr_name (string): Ingress Event Generic Field attribute name,generic_name (string): Ingress Event Generic name of the attribute}
        Required Body Parameters (type(dict) body example)- {
  "vendor": "",
  "format_name": "",
  "prefix": "",
  "status": false,
  "description": "",
  "format": "",
  "sample": "",
  "filter": "",
  "fields": [
    {
      "attr_name": "",
      "data_type": "",
      "allowed_values": ""
    }
  ],
  "generic_fields": [
    {
      "attr_name": "",
      "generic_name": ""
    }
  ]
}
        '''
        urlPath='/ingress-event-dictionary/{ingress_event_dictionary_id}'
        dictPath={'ingress_event_dictionary_id': ingress_event_dictionary_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceIngressEventDictionaryByIngress_event_dictionary_id(self,ingress_event_dictionary_id="",body=({})):
        '''
        Operation: Replace an Ingress Event Dictionary
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: ingress_event_dictionary_id, Description: Numeric ID of the ingress event dictionary
        Required Body Parameters (body description)- IngressEventDictionaryReplace {vendor (string): Vendor of the ingress event,format_name (string): Format Name of the ingress event,prefix (string): Prefix of the ingress event,status (boolean, optional): Status of the ingress event,description (string, optional): Description of the ingress event,format (string, optional): Format of the ingress event,sample (string, optional): Sample of the ingress event,filter (string): Filter of the ingress event,fields (array[Fields]): Fields of the ingress event,generic_fields (array[GenericFields]): Generic Fields of the ingress event}Fields {attr_name (string): Ingress Event Field atrribute name,data_type (string): Ingress Event Field attribute type,allowed_values (string, optional): Allowed values for Ingress Event Field in CSV format}GenericFields {attr_name (string): Ingress Event Generic Field attribute name,generic_name (string): Ingress Event Generic name of the attribute}
        Required Body Parameters (type(dict) body example)- {
  "vendor": "",
  "format_name": "",
  "prefix": "",
  "status": false,
  "description": "",
  "format": "",
  "sample": "",
  "filter": "",
  "fields": [
    {
      "attr_name": "",
      "data_type": "",
      "allowed_values": ""
    }
  ],
  "generic_fields": [
    {
      "attr_name": "",
      "generic_name": ""
    }
  ]
}
        '''
        urlPath='/ingress-event-dictionary/{ingress_event_dictionary_id}'
        dictPath={'ingress_event_dictionary_id': ingress_event_dictionary_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteIngressEventDictionaryByIngress_event_dictionary_id(self,ingress_event_dictionary_id=""):
        '''
        Operation: Delete an Ingress Event Dictionary
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: ingress_event_dictionary_id, Description: Numeric ID of the ingress event dictionary
        '''
        urlPath='/ingress-event-dictionary/{ingress_event_dictionary_id}'
        dictPath={'ingress_event_dictionary_id': ingress_event_dictionary_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getIngressEventDictionaryFormat_nameByFormat_name(self,format_name=""):
        '''
        Operation: Get an Ingress Event Dictionary by format_name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: format_name, Description: format_name of the ingress event dictionary
        '''
        urlPath='/ingress-event-dictionary/format_name/{format_name}'
        dictPath={'format_name': format_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateIngressEventDictionaryFormat_nameByFormat_name(self,format_name="",body=({})):
        '''
        Operation: Update an Ingress Event Dictionary by format_name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: format_name, Description: format_name of the ingress event dictionary
        Required Body Parameters (body description)- IngressEventDictionaryUpdate {vendor (string, optional): Vendor of the ingress event,format_name (string, optional): Format Name of the ingress event,prefix (string, optional): Prefix of the ingress event,status (boolean, optional): Status of the ingress event,description (string, optional): Description of the ingress event,format (string, optional): Format of the ingress event,sample (string, optional): Sample of the ingress event,filter (string, optional): Filter of the ingress event,fields (array[Fields], optional): Fields of the ingress event,generic_fields (array[GenericFields], optional): Generic Fields of the ingress event}Fields {attr_name (string): Ingress Event Field atrribute name,data_type (string): Ingress Event Field attribute type,allowed_values (string, optional): Allowed values for Ingress Event Field in CSV format}GenericFields {attr_name (string): Ingress Event Generic Field attribute name,generic_name (string): Ingress Event Generic name of the attribute}
        Required Body Parameters (type(dict) body example)- {
  "vendor": "",
  "format_name": "",
  "prefix": "",
  "status": false,
  "description": "",
  "format": "",
  "sample": "",
  "filter": "",
  "fields": [
    {
      "attr_name": "",
      "data_type": "",
      "allowed_values": ""
    }
  ],
  "generic_fields": [
    {
      "attr_name": "",
      "generic_name": ""
    }
  ]
}
        '''
        urlPath='/ingress-event-dictionary/format_name/{format_name}'
        dictPath={'format_name': format_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceIngressEventDictionaryFormat_nameByFormat_name(self,format_name="",body=({})):
        '''
        Operation: Replace an Ingress Event Dictionary by format_name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: format_name, Description: format_name of the ingress event dictionary
        Required Body Parameters (body description)- IngressEventDictionaryReplace {vendor (string): Vendor of the ingress event,format_name (string): Format Name of the ingress event,prefix (string): Prefix of the ingress event,status (boolean, optional): Status of the ingress event,description (string, optional): Description of the ingress event,format (string, optional): Format of the ingress event,sample (string, optional): Sample of the ingress event,filter (string): Filter of the ingress event,fields (array[Fields]): Fields of the ingress event,generic_fields (array[GenericFields]): Generic Fields of the ingress event}Fields {attr_name (string): Ingress Event Field atrribute name,data_type (string): Ingress Event Field attribute type,allowed_values (string, optional): Allowed values for Ingress Event Field in CSV format}GenericFields {attr_name (string): Ingress Event Generic Field attribute name,generic_name (string): Ingress Event Generic name of the attribute}
        Required Body Parameters (type(dict) body example)- {
  "vendor": "",
  "format_name": "",
  "prefix": "",
  "status": false,
  "description": "",
  "format": "",
  "sample": "",
  "filter": "",
  "fields": [
    {
      "attr_name": "",
      "data_type": "",
      "allowed_values": ""
    }
  ],
  "generic_fields": [
    {
      "attr_name": "",
      "generic_name": ""
    }
  ]
}
        '''
        urlPath='/ingress-event-dictionary/format_name/{format_name}'
        dictPath={'format_name': format_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteIngressEventDictionaryFormat_nameByFormat_name(self,format_name=""):
        '''
        Operation: Delete an Ingress Event Dictionary by format_name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: format_name, Description: format_name of the ingress event dictionary
        '''
        urlPath='/ingress-event-dictionary/format_name/{format_name}'
        dictPath={'format_name': format_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
