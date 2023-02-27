
from pyclearpass.common import _generateParameterisedURL,_removeEmptyKeys,ClearPassAPILogin

#File Name: APIExplorerGuestActionsv1.py

class apiGuestActions(ClearPassAPILogin):

    #Function Section Name:GenerateGuestDigitalPass  
    #Function Section Description: Operations for GenerateGuestDigitalPass

    def getGuestByGuest_idPassId(self,guest_id="",id=""):
        '''
        Operation: Generate digital pass for guest account based on template specified by ID
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
        Required Path Parameter Name: id, Description: Numeric ID of the digital pass template
        '''
        urlPath='/guest/{guest_id}/pass/{id}'
        dictPath={'guest_id': guest_id, 'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        

    #Function Section Name:GenerateGuestReceipt  
    #Function Section Description: Generate a guest account receipt

    def getGuestByGuest_idReceiptId(self,guest_id="",id=""):
        '''
        Operation: Generate print template for guest account, using specified template ID
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
        Required Path Parameter Name: id, Description: Numeric ID of the print template
        '''
        urlPath='/guest/{guest_id}/receipt/{id}'
        dictPath={'guest_id': guest_id, 'id': id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        

    #Function Section Name:SendSmsReceipt  
    #Function Section Description: Operations for SendSmsReceipt

    def newGuestByGuest_idSendreceiptSms(self,guest_id="",body=({})):
        '''
        Operation: Resend guest receipt for guest account, via SMS
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
        Required Body Parameters (body description)- SendSmsReceipt {confirm (boolean): Flag to confirm sending guest receipt via SMS}
        Required Body Parameters (type(dict) body example)- {
  "confirm": false
}
        '''
        urlPath='/guest/{guest_id}/sendreceipt/sms'
        dictPath={'guest_id': guest_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:SendSmtpReceipt  
    #Function Section Description: Operations for SendSmtpReceipt

    def newGuestByGuest_idSendreceiptSmtp(self,guest_id="",body=({})):
        '''
        Operation: Resend guest receipt for guest account,  via SMTP
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: URL parameter guest_id
        Required Body Parameters (body description)- SendSmtpReceipt {confirm (boolean): Flag to confirm sending guest receipt via SMTP}
        Required Body Parameters (type(dict) body example)- {
  "confirm": false
}
        '''
        urlPath='/guest/{guest_id}/sendreceipt/smtp'
        dictPath={'guest_id': guest_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:SponsorshipApproval  
    #Function Section Description: Sponsor confirmation for guest accounts

    def newGuestByGuest_idSponsor(self,guest_id="",body=({}),gsr_id=""):
        '''
        Operation: Accept or reject a guest sponsorship request
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
        Required Body Parameters (body description)- SponsorshipApproval {token (string): Registration token,register_token (string): Registration token,register_reject (boolean, optional): Set to true to reject the sponsorship request,role_id (integer, optional): Override the guest role,modify_expire_time (string, optional): Override the guest expiration time,confirm_expire_time (string, optional): Timestamp for new expiration time; used if modify_expire_time is "expire_time"}
        Required Body Parameters (type(dict) body example)- {
  "token": "",
  "register_token": "",
  "register_reject": false,
  "role_id": 0,
  "modify_expire_time": "",
  "confirm_expire_time": ""
}
        Optional Query Parameter Name: gsr_id, Description: Optional name of the self-registration with the sponsor confirmation configuration.
        '''
        urlPath='/guest/{guest_id}/sponsor'
        dictPath={'guest_id': guest_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        dictQuery={'gsr_id': gsr_id}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
