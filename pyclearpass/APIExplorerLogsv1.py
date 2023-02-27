
from pyclearpass.common import _generateParameterisedURL,_removeEmptyKeys,ClearPassAPILogin

#File Name: APIExplorerLogsv1.py

class apiLogs(ClearPassAPILogin):

    #Function Section Name:EndpointInfo  
    #Function Section Description: Collection of endpoints

    def getInsightEndpointMacByMac(self,mac=""):
        '''
        Operation: Get a single endpoint by MAC address
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: mac, Description: URL parameter mac
        '''
        urlPath='/insight/endpoint/mac/{mac}'
        dictPath={'mac': mac}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def getInsightEndpointIpByIp(self,ip=""):
        '''
        Operation: Look up endpoints by IP address
        HTTP Status Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: ip, Description: IPv4/IPv6 address to match with endpoints
        '''
        urlPath='/insight/endpoint/ip/{ip}'
        dictPath={'ip': ip}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def getInsightEndpointIpRangeByIp_range(self,ip_range=""):
        '''
        Operation: Look up endpoints by IP address range
        HTTP Status Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: ip_range, Description: IPv4/IPv6 address range, e.g. 192.168.1.1-255 or 2001:db8:a0b:12cd::a-f
        '''
        urlPath='/insight/endpoint/ip-range/{ip_range}'
        dictPath={'ip_range': ip_range}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def getInsightEndpointTimeRangeByFrom_timeTo_time(self,from_time="",to_time=""):
        '''
        Operation: Look up endpoints by time range
        HTTP Status Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: from_time, Description: Start time for search, as UNIX timestamp
        Required Path Parameter Name: to_time, Description: End time for search, as UNIX timestamp
        '''
        urlPath='/insight/endpoint/time-range/{from_time}/{to_time}'
        dictPath={'from_time': from_time, 'to_time': to_time}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        

    #Function Section Name:LoginAudit  
    #Function Section Description: Get previous login details for an admin user

    def getLoginAuditByName(self,name=""):
        '''
        Operation: Get previous login details for an admin user
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: User name of admin
        '''
        urlPath='/login-audit/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        

    #Function Section Name:SystemEvents  
    #Function Section Description: Collection of system events

    def getSystemEvent(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of system events
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +source)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/system-event'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newSystemEvent(self,body=({})):
        '''
        Operation: Create a new system event
        HTTP Status Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SystemEvents {source (string): Source,level (string) = ['INFO' or 'ERROR' or 'WARN']: Level,category (string): Category,action (string): Action,description (string): Description,timestamp (string): Timestamp}
        Required Body Parameters (type(dict) body example)- {
  "source": "",
  "level": "",
  "category": "",
  "action": "",
  "description": "",
  "timestamp": ""
}
        '''
        urlPath='/system-event'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
