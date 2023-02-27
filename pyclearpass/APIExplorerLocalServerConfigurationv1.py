
from pyclearpass.common import _generateParameterisedURL,_removeEmptyKeys,ClearPassAPILogin

#File Name: APIExplorerLocalServerConfigurationv1.py

class apiLocalServerConfiguration(ClearPassAPILogin):

    #Function Section Name:AccessControl  
    #Function Section Description: Manage Application access controls

    def getServerAccessControlByServer_uuid(self,server_uuid=""):
        '''
        Operation: Get all application access controls
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        '''
        urlPath='/server/access-control/{server_uuid}'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def getServerAccessControlByServer_uuidResource_name(self,server_uuid="",resource_name=""):
        '''
        Operation: Get an application access control by resource name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: resource_name, Description: Unique resource name of the access control
        '''
        urlPath='/server/access-control/{server_uuid}/{resource_name}'
        dictPath={'server_uuid': server_uuid, 'resource_name': resource_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def replaceServerAccessControlByServer_uuidResource_name(self,server_uuid="",resource_name="",body=({})):
        '''
        Operation: Replace an application access controls by resource name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: resource_name, Description: Unique resource name of the access control
        Required Body Parameters (body description)- AccessControlReplace {access (string) = ['Allow' or 'Deny']: Access type of the Access control application,networks (object): hostname, IP address or subnet (CIDR) of the Networks to be restricted (e.g. ["hostname.example.com", "1.2.3.4", "10.1.0.0/16"])}
        Required Body Parameters (type(dict) body example)- {
  "access": "",
  "networks": "object"
}
        '''
        urlPath='/server/access-control/{server_uuid}/{resource_name}'
        dictPath={'server_uuid': server_uuid, 'resource_name': resource_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteServerAccessControlByServer_uuidResource_name(self,server_uuid="",resource_name=""):
        '''
        Operation: Delete an application access control by resource name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: resource_name, Description: Unique resource name of the access control
        '''
        urlPath='/server/access-control/{server_uuid}/{resource_name}'
        dictPath={'server_uuid': server_uuid, 'resource_name': resource_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:ADDomain  
    #Function Section Description: Manage AD Domains

    def getAdDomainByServer_uuid(self,server_uuid=""):
        '''
        Operation: Get a list of AD Domains
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
        '''
        urlPath='/ad-domain/{server_uuid}'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def getAdDomainByServer_uuidNetbiosNameNetbios_name(self,server_uuid="",netbios_name=""):
        '''
        Operation: GET an AD domain by netbios_name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
        Required Path Parameter Name: netbios_name, Description: NetBIOS name of the domain
        '''
        urlPath='/ad-domain/{server_uuid}/netbios-name/{netbios_name}'
        dictPath={'server_uuid': server_uuid, 'netbios_name': netbios_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def replaceAdDomainJoinByServer_uuid(self,server_uuid="",body=({})):
        '''
        Operation: Join AD Domain
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
        Required Body Parameters (body description)- ADDomainJoin {domain_controller (string): FQDN of the domain controller,netbios_name (string): NetBIOS name of the domain,on_name_conflict (integer): Action to perform in case of a controller name conflict(1 - Use specified Domain Controller, 2 - Use Domain Controller returned by DNS query, 3 - Fail on conflict),username (string): Domain username ,password (string): Domain password}
        Required Body Parameters (type(dict) body example)- {
  "domain_controller": "",
  "netbios_name": "",
  "on_name_conflict": 0,
  "username": "",
  "password": ""
}
        '''
        urlPath='/ad-domain/join/{server_uuid}'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def replaceAdDomainLeaveByServer_uuid(self,server_uuid="",body=({})):
        '''
        Operation: Leave AD domain
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
        Required Body Parameters (body description)- ADDomainLeave {netbios_name (string): NetBIOS name of the domain,username (string): Domain username ,password (string): Domain password,force_leave (boolean): Leave domain even if AD is down}
        Required Body Parameters (type(dict) body example)- {
  "netbios_name": "",
  "username": "",
  "password": "",
  "force_leave": false
}
        '''
        urlPath='/ad-domain/leave/{server_uuid}'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def updateAdDomainPasswordServersByServer_uuid(self,server_uuid="",body=({})):
        '''
        Operation: Configure AD Password Servers
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
        Required Body Parameters (body description)- ADDomainUpdate {netbios_name (string): NetBIOS name of the domain,password_servers (object): List of Hostname or IP Address of the AD password servers}
        Required Body Parameters (type(dict) body example)- {
  "netbios_name": "",
  "password_servers": "object"
}
        '''
        urlPath='/ad-domain/password-servers/{server_uuid}'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)

    #Function Section Name:CppmVersion  
    #Function Section Description: Manage Cppm Version

    def getCppmVersion(self,server_uuid="",body=({})):
        '''
        Operation: Get Cppm version
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
        Required Body Parameters (body description)- ADDomainUpdate {netbios_name (string): NetBIOS name of the domain,password_servers (object): List of Hostname or IP Address of the AD password servers}
        Required Body Parameters (type(dict) body example)- {
  "netbios_name": "",
  "password_servers": "object"
}
        '''
        urlPath='/cppm-version'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get',query=body)

    #Function Section Name:ServerConfiguration  
    #Function Section Description: Manage cluster servers and per-server configuration

    def getClusterServer(self,server_uuid="",body=({})):
        '''
        Operation: Get a list of servers in the cluster
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
        Required Body Parameters (body description)- ADDomainUpdate {netbios_name (string): NetBIOS name of the domain,password_servers (object): List of Hostname or IP Address of the AD password servers}
        Required Body Parameters (type(dict) body example)- {
  "netbios_name": "",
  "password_servers": "object"
}
        '''
        urlPath='/cluster/server'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get',query=body)
    def getClusterServerByUuid(self,uuid=""):
        '''
        Operation: Get configuration of a server
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: uuid, Description: Server UUID, "publisher" or "this"
        '''
        urlPath='/cluster/server/{uuid}'
        dictPath={'uuid': uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateClusterServerByUuid(self,uuid="",body=({})):
        '''
        Operation: Update configuration of a server
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: uuid, Description: Server UUID, "publisher" or "this"
        Required Body Parameters (body description)- ServerConfigurationChange {is_insight_enabled (bool, optional): True if this server has Insight reporting enabled}
        Required Body Parameters (type(dict) body example)- {
  "is_insight_enabled": "bool"
}
        '''
        urlPath='/cluster/server/{uuid}'
        dictPath={'uuid': uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)

    #Function Section Name:ServerFips  
    #Function Section Description: Get server FIPS mode information

    def getServerFips(self,uuid="",body=({})):
        '''
        Operation: Get server FIPS mode information
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: uuid, Description: Server UUID, "publisher" or "this"
        Required Body Parameters (body description)- ServerConfigurationChange {is_insight_enabled (bool, optional): True if this server has Insight reporting enabled}
        Required Body Parameters (type(dict) body example)- {
  "is_insight_enabled": "bool"
}
        '''
        urlPath='/server/fips'
        dictPath={'uuid': uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get',query=body)

    #Function Section Name:ServerSnmp  
    #Function Section Description: Manage server snmp settings

    def getServerSnmpByServer_uuid(self,server_uuid=""):
        '''
        Operation: Get server snmp settings
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        '''
        urlPath='/server/snmp/{server_uuid}'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def replaceServerSnmpByServer_uuid(self,server_uuid="",body=({})):
        '''
        Operation: Replace server snmp settings
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Body Parameters (body description)- ServerSnmpReplace {system_location (string, optional): System location of the system monitoring settings for a server,system_contact (string, optional): System contact of the system monitoring settings for a server,engine_id (string): Engine ID of system monitoring settings,version (string) = ['V1' or 'V2C' or 'V3']: SNMP Version of the system monitoring settings,community_string (string, optional): Community String of the system monitoring settings,username (string, optional): Username for system monitoring settings,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security Level of system monitoring settings,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication Protocol of system monitoring settings,auth_key (string, optional): Authentication key of system monitoring settings,privacy_protocol (string, optional) = ['DES' or 'AES']: Privacy Protocol of system monitoring settings,privacy_key (string, optional): Privacy key of system monitoring settings}
        Required Body Parameters (type(dict) body example)- {
  "system_location": "",
  "system_contact": "",
  "engine_id": "",
  "version": "",
  "community_string": "",
  "username": "",
  "security_level": "",
  "auth_protocol": "",
  "auth_key": "",
  "privacy_protocol": "",
  "privacy_key": ""
}
        '''
        urlPath='/server/snmp/{server_uuid}'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def updateServerSnmpByServer_uuid(self,server_uuid="",body=({})):
        '''
        Operation: Update some fields of server snmp settings
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Body Parameters (body description)- ServerSnmpUpdate {system_location (string, optional): System location of the system monitoring settings for a server,system_contact (string, optional): System contact of the system monitoring settings for a server,engine_id (string, optional): Engine ID of system monitoring settings,version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP Version of the system monitoring settings,community_string (string, optional): Community String of the system monitoring settings,username (string, optional): Username for system monitoring settings,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security Level of system monitoring settings,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication Protocol of system monitoring settings,auth_key (string, optional): Authentication key of system monitoring settings,privacy_protocol (string, optional) = ['DES' or 'AES']: Privacy Protocol of system monitoring settings,privacy_key (string, optional): Privacy key of system monitoring settings}
        Required Body Parameters (type(dict) body example)- {
  "system_location": "",
  "system_contact": "",
  "engine_id": "",
  "version": "",
  "community_string": "",
  "username": "",
  "security_level": "",
  "auth_protocol": "",
  "auth_key": "",
  "privacy_protocol": "",
  "privacy_key": ""
}
        '''
        urlPath='/server/snmp/{server_uuid}'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)

    #Function Section Name:ServerVersion  
    #Function Section Description: Get server version information

    def getServerVersion(self,server_uuid="",body=({})):
        '''
        Operation: Get server version information
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Body Parameters (body description)- ServerSnmpUpdate {system_location (string, optional): System location of the system monitoring settings for a server,system_contact (string, optional): System contact of the system monitoring settings for a server,engine_id (string, optional): Engine ID of system monitoring settings,version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP Version of the system monitoring settings,community_string (string, optional): Community String of the system monitoring settings,username (string, optional): Username for system monitoring settings,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security Level of system monitoring settings,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication Protocol of system monitoring settings,auth_key (string, optional): Authentication key of system monitoring settings,privacy_protocol (string, optional) = ['DES' or 'AES']: Privacy Protocol of system monitoring settings,privacy_key (string, optional): Privacy key of system monitoring settings}
        Required Body Parameters (type(dict) body example)- {
  "system_location": "",
  "system_contact": "",
  "engine_id": "",
  "version": "",
  "community_string": "",
  "username": "",
  "security_level": "",
  "auth_protocol": "",
  "auth_key": "",
  "privacy_protocol": "",
  "privacy_key": ""
}
        '''
        urlPath='/server/version'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get',query=body)

    #Function Section Name:ServiceParameter  
    #Function Section Description: Manage service parameters

    def getServiceParameterByServer_uuidService_id(self,server_uuid="",service_id=""):
        '''
        Operation: Get service parameter details
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: service_id, Description: Unique id for the service
        '''
        urlPath='/service-parameter/{server_uuid}/{service_id}'
        dictPath={'server_uuid': server_uuid, 'service_id': service_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateServiceParameterByServer_uuidService_id(self,server_uuid="",service_id="",body=({})):
        '''
        Operation: Update service parameter values
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: service_id, Description: Unique id for the service
        Required Body Parameters (body description)- ServiceParameterUpdate {param_name_1 (string, optional): param_value_1,param_name_2 (string, optional): param_value_2...}
        Required Body Parameters (type(dict) body example)- {
  "param_name_1": "",
  "param_name_2": ""
}
        '''
        urlPath='/service-parameter/{server_uuid}/{service_id}'
        dictPath={'server_uuid': server_uuid, 'service_id': service_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)

    #Function Section Name:SystemServiceControl  
    #Function Section Description: Control services running on a server

    def getServerServiceByServer_uuid(self,server_uuid=""):
        '''
        Operation: Get all services
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        '''
        urlPath='/server/service/{server_uuid}'
        dictPath={'server_uuid': server_uuid}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def getServerServiceByServer_uuidService_name(self,server_uuid="",service_name=""):
        '''
        Operation: Get a service by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        Required Path Parameter Name: service_name, Description: Unique Name of the SystemServiceControl
        '''
        urlPath='/server/service/{server_uuid}/{service_name}'
        dictPath={'server_uuid': server_uuid, 'service_name': service_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateServerServiceByServer_uuidService_nameStart(self,server_uuid="",service_name=""):
        '''
        Operation: Start a service by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        Required Path Parameter Name: service_name, Description: Unique Name of the SystemServiceControl
        '''
        urlPath='/server/service/{server_uuid}/{service_name}/start'
        dictPath={'server_uuid': server_uuid, 'service_name': service_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateServerServiceByServer_uuidService_nameStop(self,server_uuid="",service_name=""):
        '''
        Operation: Stop a service by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        Required Path Parameter Name: service_name, Description: Unique Name of the SystemServiceControl
        '''
        urlPath='/server/service/{server_uuid}/{service_name}/stop'
        dictPath={'server_uuid': server_uuid, 'service_name': service_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
