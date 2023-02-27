
from pyclearpass.common import _generateParameterisedURL,_removeEmptyKeys,ClearPassAPILogin

#File Name: APIExplorerToolsAndUtilitiesv1.py

class apiToolsAndUtils(ClearPassAPILogin):

    #Function Section Name:EmailSend  
    #Function Section Description: Operations for Email Send

    def newEmailSend(self,body=({})):
        '''
        Operation: Send an Email
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- EmailSendCreate {to (object): List of Recipients Email Address (e.g., ["a@example.com", "b@example.com"]),subject (string, optional): Email Subject,message (string): Email Body,cc_recipients (object, optional): List of CC recipients Email Address (e.g., ["a@example.com", "b@example.com"]),bcc_recipients (object, optional): List of BCC recipients Email Address (e.g., ["a@example.com", "b@example.com"]),headers (object, optional): Email headers (e.g., {"Content-Type":"text/plain; charset=UTF-8","Content-Transfer-Encoding": "8bit"})}
        Required Body Parameters (type(dict) body example)- {
  "to": "object",
  "subject": "",
  "message": "",
  "cc_recipients": "object",
  "bcc_recipients": "object",
  "headers": "object"
}
        '''
        urlPath='/email/send'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:RandomMpskGenerator  
    #Function Section Description: Generate a random MPSK

    def getRandomMpsk(self,body=({})):
        '''
        Operation: 
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- EmailSendCreate {to (object): List of Recipients Email Address (e.g., ["a@example.com", "b@example.com"]),subject (string, optional): Email Subject,message (string): Email Body,cc_recipients (object, optional): List of CC recipients Email Address (e.g., ["a@example.com", "b@example.com"]),bcc_recipients (object, optional): List of BCC recipients Email Address (e.g., ["a@example.com", "b@example.com"]),headers (object, optional): Email headers (e.g., {"Content-Type":"text/plain; charset=UTF-8","Content-Transfer-Encoding": "8bit"})}
        Required Body Parameters (type(dict) body example)- {
  "to": "object",
  "subject": "",
  "message": "",
  "cc_recipients": "object",
  "bcc_recipients": "object",
  "headers": "object"
}
        '''
        urlPath='/random-mpsk'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get',query=body)
    def newRandomMpsk(self,body=({})):
        '''
        Operation: 
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- RandomMpskGenerator {random_mpsk_method (string, optional): The random MPSK method.  See the documentation for the allowed values.,random_mpsk_length (integer, optional): The desired length of the MPSK.,random_mpsk_picture (string, optional): The picture to be used for the ‘nwa_picture_password’ method.  See the documentation for the valid syntax.}
        Required Body Parameters (type(dict) body example)- {
  "random_mpsk_method": "",
  "random_mpsk_length": 0,
  "random_mpsk_picture": ""
}
        '''
        urlPath='/random-mpsk'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:RandomPasswordGenerator  
    #Function Section Description: Generate a random password

    def getRandomPassword(self,body=({})):
        '''
        Operation: 
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- RandomMpskGenerator {random_mpsk_method (string, optional): The random MPSK method.  See the documentation for the allowed values.,random_mpsk_length (integer, optional): The desired length of the MPSK.,random_mpsk_picture (string, optional): The picture to be used for the ‘nwa_picture_password’ method.  See the documentation for the valid syntax.}
        Required Body Parameters (type(dict) body example)- {
  "random_mpsk_method": "",
  "random_mpsk_length": 0,
  "random_mpsk_picture": ""
}
        '''
        urlPath='/random-password'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get',query=body)
    def newRandomPassword(self,body=({})):
        '''
        Operation: 
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- RandomPasswordGenerator {random_password_method (string, optional): The random password method.  See the documentation for the allowed values.,random_password_length (integer, optional): The desired length of the password.,random_password_picture (string, optional): The picture to be used for the ‘nwa_picture_password’ method.  See the documentation for the valid syntax.}
        Required Body Parameters (type(dict) body example)- {
  "random_password_method": "",
  "random_password_length": 0,
  "random_password_picture": ""
}
        '''
        urlPath='/random-password'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:SmsSend  
    #Function Section Description: Send SMS using Configuration -> SMS Services -> Send SMS

    def newSmsSend(self,body=({})):
        '''
        Operation: Send an SMS message
        HTTP Status Response Codes: 200 OK, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SmsSend {handler (integer, optional) = ['22']: Select the service to use when sending the message,recipient (string): Enter the mobile telephone number of the recipient in international format,carrier (string, optional) = ['' or '7-11 Speakout(GSM)' or 'Airtel (Andhra Pradesh, India)' or 'Airtel (Karnataka, India)' or 'Airtel Wireless' or 'Alaska Communications Systems' or 'Alltel Wireless' or 'aql' or 'AT&T Wireless' or 'AT&T Enterprise Paging' or 'BigRedGiant Mobile Solutions' or 'Bell Mobility & Solo Mobile' or 'Boost Mobile' or 'BPL Mobile' or 'Cellular One (Dobson)' or 'Cingular' or 'Centennial Wireless' or 'Cincinnati Bell' or 'Claro (Brasil)' or 'Claro (Nicaragua)' or 'Comcel' or 'Cricket' or 'CTI' or 'Emtel' or 'eOcean' or 'Esendex' or 'Fido' or 'General Communications Inc.' or 'Globalstar (satellite)' or 'Helio' or 'Illinois Valley Cellular' or 'Iridium (satellite)' or 'i wireless' or 'Koodo Mobile' or 'Mediaburst' or 'Meteor' or 'Mero Mobile' or 'MetroPCS' or 'Movicom' or 'Mobitel' or 'Movistar' or 'MTN' or 'MTS' or 'Nextel' or 'Nextel (Mexico)' or 'Nextel (Argentina)' or 'Orange Polska' or 'Personal' or 'Plateau Wireless' or 'Plus GSM' or 'President's Choice' or 'Qwest' or 'Rogers' or 'SL Interactive' or 'Sasktel' or 'Setar Mobile email (Aruba)' or 'Sprint (PCS)' or 'Sprint (Nextel)' or 'Suncom' or 'Sunrise' or 'T-Mobile' or 'T-Mobile Austria' or 'T-Mobile UK' or 'Telus Mobility' or 'Thumb Cellular' or 'Tigo (Formerly Ola)' or 'Tracfone (prepaid)' or 'Unicel' or 'US Cellular' or 'Verizon' or 'Vivo' or 'Virgin Mobile Canada' or 'Virgin Mobile' or 'Vodacom' or 'YCC' or 'MobiPCS' or 'SMSLink.ro']: The visitor’s mobile carrier,message (string): Enter the message to send (maximum 160 characters)}
        Required Body Parameters (type(dict) body example)- {
  "handler": 0,
  "recipient": "",
  "carrier": "",
  "message": ""
}
        '''
        urlPath='/sms/send'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
