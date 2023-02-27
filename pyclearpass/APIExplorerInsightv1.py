
from pyclearpass.common import _generateParameterisedURL,_removeEmptyKeys,ClearPassAPILogin

#File Name: APIExplorerInsightv1.py

class apiInsight(ClearPassAPILogin):

    #Function Section Name:Alert  
    #Function Section Description: Operations for Alert

    def getAlert(self,offset="",limit="",calculate_count=""):
        '''
        Operation: Get all Insight alert configurations.
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Optional Query Parameter Name: offset, Description: Starting point to return rows from a result set. i.e Default: 0
        Optional Query Parameter Name: limit, Description: Limit the number of rows returned from a result set. i.e Default: 25
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/alert'
        dictQuery={'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newAlert(self,body=({})):
        '''
        Operation: Create an Insight alert configuration.
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Body Parameters (body description)- Alert {id (integer): Numeric id of the alert,name (string): Name of the alert,description (string, optional): Description of the alert,category (string): Category of the alert,subcategory (string): Sub category is the template name of the alert,email_targets (object): Send alert notification to the configured email targets, e.g. "email_targets":["...", "..."],sms_targets (object, optional): Send alert notification to the configured SMS targets, e.g. "sms_targets":["...", "..."],config (object, optional): Setting the alert filter configurations & adding CSV columns for the CSV report,
                    e.g. "config": {
                            "filter": {
                                "auth.ap_name": {
                                    "operator": "EQUALS",
                                    "value": ["..."]
                                },
                                "cppm_cluster.hostname": {
                                    "operator":"CONTAINS",
                                    "value":["...", "..."]
                                }
                            }
                        },severity (string): Severity of the alert, either "critical" or "warning",threshold (integer): Triggering the alert when reaching the specified numeric threshold value,interval (integer): Triggering the alert at the numeric interval,interval_unit (string): Interval units either "minute" or "hour",is_enabled (boolean, optional): Enable/Disable the alert,is_muted (boolean, optional): Mute/Unmute the alert}
        Required Body Parameters (type(dict) body example)- {
  "id": 0,
  "name": "",
  "description": "",
  "category": "",
  "subcategory": "",
  "email_targets": "object",
  "sms_targets": "object",
  "config": "object",
  "severity": "",
  "threshold": 0,
  "interval": 0,
  "interval_unit": "",
  "is_enabled": false,
  "is_muted": false
}
        '''
        urlPath='/alert'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getAlertById(self,id=""):
        '''
        Operation: Get an Insight alert configuration by id.
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the alert
        '''
        urlPath='/alert/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateAlertById(self,id="",body=({})):
        '''
        Operation: Partial update of an Insight alert configuration by id.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the alert
        Required Body Parameters (body description)- Alert {id (integer): Numeric id of the alert,name (string): Name of the alert,description (string, optional): Description of the alert,category (string): Category of the alert,subcategory (string): Sub category is the template name of the alert,email_targets (object): Send alert notification to the configured email targets, e.g. "email_targets":["...", "..."],sms_targets (object, optional): Send alert notification to the configured SMS targets, e.g. "sms_targets":["...", "..."],config (object, optional): Setting the alert filter configurations & adding CSV columns for the CSV report,
                    e.g. "config": {
                            "filter": {
                                "auth.ap_name": {
                                    "operator": "EQUALS",
                                    "value": ["..."]
                                },
                                "cppm_cluster.hostname": {
                                    "operator":"CONTAINS",
                                    "value":["...", "..."]
                                }
                            }
                        },severity (string): Severity of the alert, either "critical" or "warning",threshold (integer): Triggering the alert when reaching the specified numeric threshold value,interval (integer): Triggering the alert at the numeric interval,interval_unit (string): Interval units either "minute" or "hour",is_enabled (boolean, optional): Enable/Disable the alert,is_muted (boolean, optional): Mute/Unmute the alert}
        Required Body Parameters (type(dict) body example)- {
  "id": 0,
  "name": "",
  "description": "",
  "category": "",
  "subcategory": "",
  "email_targets": "object",
  "sms_targets": "object",
  "config": "object",
  "severity": "",
  "threshold": 0,
  "interval": 0,
  "interval_unit": "",
  "is_enabled": false,
  "is_muted": false
}
        '''
        urlPath='/alert/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceAlertById(self,id="",body=({})):
        '''
        Operation: Complete update of an Insight alert configuration by id.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the alert
        Required Body Parameters (body description)- Alert {id (integer): Numeric id of the alert,name (string): Name of the alert,description (string, optional): Description of the alert,category (string): Category of the alert,subcategory (string): Sub category is the template name of the alert,email_targets (object): Send alert notification to the configured email targets, e.g. "email_targets":["...", "..."],sms_targets (object, optional): Send alert notification to the configured SMS targets, e.g. "sms_targets":["...", "..."],config (object, optional): Setting the alert filter configurations & adding CSV columns for the CSV report,
                    e.g. "config": {
                            "filter": {
                                "auth.ap_name": {
                                    "operator": "EQUALS",
                                    "value": ["..."]
                                },
                                "cppm_cluster.hostname": {
                                    "operator":"CONTAINS",
                                    "value":["...", "..."]
                                }
                            }
                        },severity (string): Severity of the alert, either "critical" or "warning",threshold (integer): Triggering the alert when reaching the specified numeric threshold value,interval (integer): Triggering the alert at the numeric interval,interval_unit (string): Interval units either "minute" or "hour",is_enabled (boolean, optional): Enable/Disable the alert,is_muted (boolean, optional): Mute/Unmute the alert}
        Required Body Parameters (type(dict) body example)- {
  "id": 0,
  "name": "",
  "description": "",
  "category": "",
  "subcategory": "",
  "email_targets": "object",
  "sms_targets": "object",
  "config": "object",
  "severity": "",
  "threshold": 0,
  "interval": 0,
  "interval_unit": "",
  "is_enabled": false,
  "is_muted": false
}
        '''
        urlPath='/alert/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteAlertById(self,id=""):
        '''
        Operation: Delete an Insight alert configuration by id.
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the alert
        '''
        urlPath='/alert/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getAlertByName(self,name=""):
        '''
        Operation: Get an Insight alert configuration by name.
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the alert
        '''
        urlPath='/alert/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateAlertByName(self,name="",body=({})):
        '''
        Operation: Partial update of an Insight alert configuration by name.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the alert
        Required Body Parameters (body description)- Alert {id (integer): Numeric id of the alert,name (string): Name of the alert,description (string, optional): Description of the alert,category (string): Category of the alert,subcategory (string): Sub category is the template name of the alert,email_targets (object): Send alert notification to the configured email targets, e.g. "email_targets":["...", "..."],sms_targets (object, optional): Send alert notification to the configured SMS targets, e.g. "sms_targets":["...", "..."],config (object, optional): Setting the alert filter configurations & adding CSV columns for the CSV report,
                    e.g. "config": {
                            "filter": {
                                "auth.ap_name": {
                                    "operator": "EQUALS",
                                    "value": ["..."]
                                },
                                "cppm_cluster.hostname": {
                                    "operator":"CONTAINS",
                                    "value":["...", "..."]
                                }
                            }
                        },severity (string): Severity of the alert, either "critical" or "warning",threshold (integer): Triggering the alert when reaching the specified numeric threshold value,interval (integer): Triggering the alert at the numeric interval,interval_unit (string): Interval units either "minute" or "hour",is_enabled (boolean, optional): Enable/Disable the alert,is_muted (boolean, optional): Mute/Unmute the alert}
        Required Body Parameters (type(dict) body example)- {
  "id": 0,
  "name": "",
  "description": "",
  "category": "",
  "subcategory": "",
  "email_targets": "object",
  "sms_targets": "object",
  "config": "object",
  "severity": "",
  "threshold": 0,
  "interval": 0,
  "interval_unit": "",
  "is_enabled": false,
  "is_muted": false
}
        '''
        urlPath='/alert/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceAlertByName(self,name="",body=({})):
        '''
        Operation: Complete update of an Insight alert configuration by name.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the alert
        Required Body Parameters (body description)- Alert {id (integer): Numeric id of the alert,name (string): Name of the alert,description (string, optional): Description of the alert,category (string): Category of the alert,subcategory (string): Sub category is the template name of the alert,email_targets (object): Send alert notification to the configured email targets, e.g. "email_targets":["...", "..."],sms_targets (object, optional): Send alert notification to the configured SMS targets, e.g. "sms_targets":["...", "..."],config (object, optional): Setting the alert filter configurations & adding CSV columns for the CSV report,
                    e.g. "config": {
                            "filter": {
                                "auth.ap_name": {
                                    "operator": "EQUALS",
                                    "value": ["..."]
                                },
                                "cppm_cluster.hostname": {
                                    "operator":"CONTAINS",
                                    "value":["...", "..."]
                                }
                            }
                        },severity (string): Severity of the alert, either "critical" or "warning",threshold (integer): Triggering the alert when reaching the specified numeric threshold value,interval (integer): Triggering the alert at the numeric interval,interval_unit (string): Interval units either "minute" or "hour",is_enabled (boolean, optional): Enable/Disable the alert,is_muted (boolean, optional): Mute/Unmute the alert}
        Required Body Parameters (type(dict) body example)- {
  "id": 0,
  "name": "",
  "description": "",
  "category": "",
  "subcategory": "",
  "email_targets": "object",
  "sms_targets": "object",
  "config": "object",
  "severity": "",
  "threshold": 0,
  "interval": 0,
  "interval_unit": "",
  "is_enabled": false,
  "is_muted": false
}
        '''
        urlPath='/alert/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteAlertByName(self,name=""):
        '''
        Operation: Delete an Insight alert configuration by name.
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the alert
        '''
        urlPath='/alert/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def updateAlertByIdEnable(self,id=""):
        '''
        Operation: Enable an Insight alert configuration by id.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the alert
        '''
        urlPath='/alert/{id}/enable'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateAlertByIdDisable(self,id=""):
        '''
        Operation: Disable an Insight alert configuration by id.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the alert
        '''
        urlPath='/alert/{id}/disable'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateAlertByIdMute(self,id=""):
        '''
        Operation: Mute an Insight alert configuration by id.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the alert
        '''
        urlPath='/alert/{id}/mute'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateAlertByIdUnmute(self,id=""):
        '''
        Operation: Unmute an Insight alert configuration by id.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the alert
        '''
        urlPath='/alert/{id}/unmute'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateAlertByNameEnable(self,name=""):
        '''
        Operation: Enable an Insight alert configuration by name.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the alert
        '''
        urlPath='/alert/{name}/enable'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateAlertByNameDisable(self,name=""):
        '''
        Operation: Disable an Insight alert configuration by name.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the alert
        '''
        urlPath='/alert/{name}/disable'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateAlertByNameMute(self,name=""):
        '''
        Operation: Mute an Insight alert configuration by name.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the alert
        '''
        urlPath='/alert/{name}/mute'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateAlertByNameUnmute(self,name=""):
        '''
        Operation: Unmute an Insight alert configuration by name.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the alert
        '''
        urlPath='/alert/{name}/unmute'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        

    #Function Section Name:Report  
    #Function Section Description: Operations for Report

    def getReport(self,offset="",limit="",calculate_count=""):
        '''
        Operation: Get all Insight report configurations.
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Optional Query Parameter Name: offset, Description: Starting point to return rows from a result set. i.e Default: 0
        Optional Query Parameter Name: limit, Description: Limit the number of rows returned from a result set. i.e Default: 25
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/report'
        dictQuery={'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newReport(self,body=({})):
        '''
        Operation: Create an Insight report configuration.
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Body Parameters (body description)- Report {id (integer): Numeric id of the report,name (string): Name of the report,description (string, optional): Description of the report,category (string): Category of the report,subcategory (string): Sub category is the template name of the report,email_targets (object, optional): Send report to the configured email targets, e.g. "email_targets":["...", "..."],sms_targets (object, optional): Send report to the configured SMS targets, e.g. "sms_targets":["...", "..."],copy_remote (boolean, optional): Enable to copy the report to the configured SCP/SFTP server,config (object, optional): Setting the report filter configurations & adding CSV columns for the CSV report,
                    e.g. "config": {
                            "filter": {
                                "auth.ap_name": {
                                    "operator": "EQUALS",
                                    "value": ["..."]
                                },
                                "cppm_cluster.hostname": {
                                    "operator":"CONTAINS",
                                    "value":["...", "..."]
                                }
                            },
                            csv_cols": ["...", "...", "..."]
                        },schedule (object, optional): Scheduling the report. Options are [noRepeat, daily, weekly, monthly],
                    e.g. when running the report "now" itself => "schedule": {} - then "begin_dt" & "end_dt" are mandatory,
                         when scheduling the report at "daily" => "schedule": {"freq": "daily", "hour": 12}
                         when scheduling the report at "weekly" => "schedule": {"freq": "weekly", "day": 0, "hour": 12}
                         when scheduling the report at "monthly" => "schedule": {"freq": "monthly", "date": 1, "hour": 12}
                ,begin_dt (integer, optional): Collect the data for the report from this "begin_dt",end_dt (string, optional): Collect the data for the report till this "end_dt",is_enabled (boolean, optional): Enable/Disable the report}
        Required Body Parameters (type(dict) body example)- {
  "id": 0,
  "name": "",
  "description": "",
  "category": "",
  "subcategory": "",
  "email_targets": "object",
  "sms_targets": "object",
  "copy_remote": false,
  "config": "object",
  "schedule": "object",
  "begin_dt": 0,
  "end_dt": "",
  "is_enabled": false
}
        '''
        urlPath='/report'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getReportById(self,id=""):
        '''
        Operation: Get an Insight report configuration by id.
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the report
        '''
        urlPath='/report/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateReportById(self,id="",body=({})):
        '''
        Operation: Partial update of an Insight report configuration by id.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the report
        Required Body Parameters (body description)- Report {id (integer): Numeric id of the report,name (string): Name of the report,description (string, optional): Description of the report,category (string): Category of the report,subcategory (string): Sub category is the template name of the report,email_targets (object, optional): Send report to the configured email targets, e.g. "email_targets":["...", "..."],sms_targets (object, optional): Send report to the configured SMS targets, e.g. "sms_targets":["...", "..."],copy_remote (boolean, optional): Enable to copy the report to the configured SCP/SFTP server,config (object, optional): Setting the report filter configurations & adding CSV columns for the CSV report,
                    e.g. "config": {
                            "filter": {
                                "auth.ap_name": {
                                    "operator": "EQUALS",
                                    "value": ["..."]
                                },
                                "cppm_cluster.hostname": {
                                    "operator":"CONTAINS",
                                    "value":["...", "..."]
                                }
                            },
                            csv_cols": ["...", "...", "..."]
                        },schedule (object, optional): Scheduling the report. Options are [noRepeat, daily, weekly, monthly],
                    e.g. when running the report "now" itself => "schedule": {} - then "begin_dt" & "end_dt" are mandatory,
                         when scheduling the report at "daily" => "schedule": {"freq": "daily", "hour": 12}
                         when scheduling the report at "weekly" => "schedule": {"freq": "weekly", "day": 0, "hour": 12}
                         when scheduling the report at "monthly" => "schedule": {"freq": "monthly", "date": 1, "hour": 12}
                ,begin_dt (integer, optional): Collect the data for the report from this "begin_dt",end_dt (string, optional): Collect the data for the report till this "end_dt",is_enabled (boolean, optional): Enable/Disable the report}
        Required Body Parameters (type(dict) body example)- {
  "id": 0,
  "name": "",
  "description": "",
  "category": "",
  "subcategory": "",
  "email_targets": "object",
  "sms_targets": "object",
  "copy_remote": false,
  "config": "object",
  "schedule": "object",
  "begin_dt": 0,
  "end_dt": "",
  "is_enabled": false
}
        '''
        urlPath='/report/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceReportById(self,id="",body=({})):
        '''
        Operation: Complete update of an Insight report configuration by id.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the report
        Required Body Parameters (body description)- Report {id (integer): Numeric id of the report,name (string): Name of the report,description (string, optional): Description of the report,category (string): Category of the report,subcategory (string): Sub category is the template name of the report,email_targets (object, optional): Send report to the configured email targets, e.g. "email_targets":["...", "..."],sms_targets (object, optional): Send report to the configured SMS targets, e.g. "sms_targets":["...", "..."],copy_remote (boolean, optional): Enable to copy the report to the configured SCP/SFTP server,config (object, optional): Setting the report filter configurations & adding CSV columns for the CSV report,
                    e.g. "config": {
                            "filter": {
                                "auth.ap_name": {
                                    "operator": "EQUALS",
                                    "value": ["..."]
                                },
                                "cppm_cluster.hostname": {
                                    "operator":"CONTAINS",
                                    "value":["...", "..."]
                                }
                            },
                            csv_cols": ["...", "...", "..."]
                        },schedule (object, optional): Scheduling the report. Options are [noRepeat, daily, weekly, monthly],
                    e.g. when running the report "now" itself => "schedule": {} - then "begin_dt" & "end_dt" are mandatory,
                         when scheduling the report at "daily" => "schedule": {"freq": "daily", "hour": 12}
                         when scheduling the report at "weekly" => "schedule": {"freq": "weekly", "day": 0, "hour": 12}
                         when scheduling the report at "monthly" => "schedule": {"freq": "monthly", "date": 1, "hour": 12}
                ,begin_dt (integer, optional): Collect the data for the report from this "begin_dt",end_dt (string, optional): Collect the data for the report till this "end_dt",is_enabled (boolean, optional): Enable/Disable the report}
        Required Body Parameters (type(dict) body example)- {
  "id": 0,
  "name": "",
  "description": "",
  "category": "",
  "subcategory": "",
  "email_targets": "object",
  "sms_targets": "object",
  "copy_remote": false,
  "config": "object",
  "schedule": "object",
  "begin_dt": 0,
  "end_dt": "",
  "is_enabled": false
}
        '''
        urlPath='/report/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteReportById(self,id=""):
        '''
        Operation: Delete an Insight report configuration by id.
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the report
        '''
        urlPath='/report/{id}'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def getReportByName(self,name=""):
        '''
        Operation: Get an Insight report configuration by name.
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the report
        '''
        urlPath='/report/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateReportByName(self,name="",body=({})):
        '''
        Operation: Partial update of an Insight report configuration by name.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the report
        Required Body Parameters (body description)- Report {id (integer): Numeric id of the report,name (string): Name of the report,description (string, optional): Description of the report,category (string): Category of the report,subcategory (string): Sub category is the template name of the report,email_targets (object, optional): Send report to the configured email targets, e.g. "email_targets":["...", "..."],sms_targets (object, optional): Send report to the configured SMS targets, e.g. "sms_targets":["...", "..."],copy_remote (boolean, optional): Enable to copy the report to the configured SCP/SFTP server,config (object, optional): Setting the report filter configurations & adding CSV columns for the CSV report,
                    e.g. "config": {
                            "filter": {
                                "auth.ap_name": {
                                    "operator": "EQUALS",
                                    "value": ["..."]
                                },
                                "cppm_cluster.hostname": {
                                    "operator":"CONTAINS",
                                    "value":["...", "..."]
                                }
                            },
                            csv_cols": ["...", "...", "..."]
                        },schedule (object, optional): Scheduling the report. Options are [noRepeat, daily, weekly, monthly],
                    e.g. when running the report "now" itself => "schedule": {} - then "begin_dt" & "end_dt" are mandatory,
                         when scheduling the report at "daily" => "schedule": {"freq": "daily", "hour": 12}
                         when scheduling the report at "weekly" => "schedule": {"freq": "weekly", "day": 0, "hour": 12}
                         when scheduling the report at "monthly" => "schedule": {"freq": "monthly", "date": 1, "hour": 12}
                ,begin_dt (integer, optional): Collect the data for the report from this "begin_dt",end_dt (string, optional): Collect the data for the report till this "end_dt",is_enabled (boolean, optional): Enable/Disable the report}
        Required Body Parameters (type(dict) body example)- {
  "id": 0,
  "name": "",
  "description": "",
  "category": "",
  "subcategory": "",
  "email_targets": "object",
  "sms_targets": "object",
  "copy_remote": false,
  "config": "object",
  "schedule": "object",
  "begin_dt": 0,
  "end_dt": "",
  "is_enabled": false
}
        '''
        urlPath='/report/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def replaceReportByName(self,name="",body=({})):
        '''
        Operation: Complete update of an Insight report configuration by name.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the report
        Required Body Parameters (body description)- Report {id (integer): Numeric id of the report,name (string): Name of the report,description (string, optional): Description of the report,category (string): Category of the report,subcategory (string): Sub category is the template name of the report,email_targets (object, optional): Send report to the configured email targets, e.g. "email_targets":["...", "..."],sms_targets (object, optional): Send report to the configured SMS targets, e.g. "sms_targets":["...", "..."],copy_remote (boolean, optional): Enable to copy the report to the configured SCP/SFTP server,config (object, optional): Setting the report filter configurations & adding CSV columns for the CSV report,
                    e.g. "config": {
                            "filter": {
                                "auth.ap_name": {
                                    "operator": "EQUALS",
                                    "value": ["..."]
                                },
                                "cppm_cluster.hostname": {
                                    "operator":"CONTAINS",
                                    "value":["...", "..."]
                                }
                            },
                            csv_cols": ["...", "...", "..."]
                        },schedule (object, optional): Scheduling the report. Options are [noRepeat, daily, weekly, monthly],
                    e.g. when running the report "now" itself => "schedule": {} - then "begin_dt" & "end_dt" are mandatory,
                         when scheduling the report at "daily" => "schedule": {"freq": "daily", "hour": 12}
                         when scheduling the report at "weekly" => "schedule": {"freq": "weekly", "day": 0, "hour": 12}
                         when scheduling the report at "monthly" => "schedule": {"freq": "monthly", "date": 1, "hour": 12}
                ,begin_dt (integer, optional): Collect the data for the report from this "begin_dt",end_dt (string, optional): Collect the data for the report till this "end_dt",is_enabled (boolean, optional): Enable/Disable the report}
        Required Body Parameters (type(dict) body example)- {
  "id": 0,
  "name": "",
  "description": "",
  "category": "",
  "subcategory": "",
  "email_targets": "object",
  "sms_targets": "object",
  "copy_remote": false,
  "config": "object",
  "schedule": "object",
  "begin_dt": 0,
  "end_dt": "",
  "is_enabled": false
}
        '''
        urlPath='/report/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def deleteReportByName(self,name=""):
        '''
        Operation: Delete an Insight report configuration by name.
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the report
        '''
        urlPath='/report/{name}'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
    def updateReportByIdEnable(self,id=""):
        '''
        Operation: Enable an Insight report configuration by id.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the report
        '''
        urlPath='/report/{id}/enable'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateReportByIdDisable(self,id=""):
        '''
        Operation: Disable an Insight report configuration by id.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the report
        '''
        urlPath='/report/{id}/disable'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateReportByNameEnable(self,name=""):
        '''
        Operation: Enable an Insight report configuration by name.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the report
        '''
        urlPath='/report/{name}/enable'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateReportByNameDisable(self,name=""):
        '''
        Operation: Disable an Insight report configuration by name.
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the report
        '''
        urlPath='/report/{name}/disable'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def newReportByIdRun(self,id=""):
        '''
        Operation: Run an Insight report by id.
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric id of the report
        '''
        urlPath='/report/{id}/run'
        dictPath={'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post')
        
        
    def newReportByNameRun(self,name=""):
        '''
        Operation: Run an Insight report by name.
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the report
        '''
        urlPath='/report/{name}/run'
        dictPath={'name': name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post')
        
        
