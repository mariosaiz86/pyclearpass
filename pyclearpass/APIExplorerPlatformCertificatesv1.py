
from pyclearpass.common import _generateParameterisedURL,_removeEmptyKeys,ClearPassAPILogin

#File Name: APIExplorerPlatformCertificatesv1.py

class apiPlatformCertificates(ClearPassAPILogin):

    #Function Section Name:CertSignRequest  
    #Function Section Description: Manage Certificate Signing Requests

    def newCertSignRequest(self,body=({})):
        '''
        Operation: Post a certificate sign request
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- CertSignRequestCreate {subject_CN (string): Common Name (CN),subject_O (string, optional): Organization (O),subject_OU (string, optional): Organizational Unit (OU),subject_L (string, optional): Location (L),subject_ST (string, optional): State (ST),subject_C (string, optional): Country (C),subject_SAN (string, optional): Subject Alternate Name (SAN),private_key_password (string): Private Key Password,private_key_type (string) = ['2048-bit rsa' or '3072-bit rsa' or '4096-bit rsa' or 'nist/secg curve over a 256 bit prime field' or 'nist/secg curve over a 384 bit prime field' or 'nist/secg curve over a 521 bit prime field']: null,digest_algorithm (string) = ['SHA-1' or 'SHA-224' or 'SHA-256' or 'SHA-384' or 'SHA-512']: Digest Algorithm}
        Required Body Parameters (type(dict) body example)- {
  "subject_CN": "",
  "subject_O": "",
  "subject_OU": "",
  "subject_L": "",
  "subject_ST": "",
  "subject_C": "",
  "subject_SAN": "",
  "private_key_password": "",
  "private_key_type": "",
  "digest_algorithm": ""
}
        '''
        urlPath='/cert-sign-request'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:CertTrustList  
    #Function Section Description: Manage Certificate Trust List

    def getCertTrustList(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of certificate trust list
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/cert-trust-list'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newCertTrustList(self,body=({})):
        '''
        Operation: Add a new certificate trust list
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- CertTrustListCreate {cert_file (string): Certificate trust list file,enabled (boolean, optional): Enable certificate trust list,cert_usage (array[string]) = ['AD/LDAP Servers' or 'Aruba Infrastructure' or 'Aruba Services' or 'Database' or 'EAP' or 'Endpoint Context Servers' or 'RadSec' or 'SAML' or 'SMTP' or 'EST' or 'Others']: Usage of the certificate}
        Required Body Parameters (type(dict) body example)- {
  "cert_file": "",
  "enabled": false,
  "cert_usage": [
    ""
  ]
}
        '''
        urlPath='/cert-trust-list'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getCertTrustListByCert_trust_list_id(self,cert_trust_list_id=""):
        '''
        Operation: Get a certificate trust list
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: cert_trust_list_id, Description: URL parameter cert_trust_list_id
        '''
        urlPath='/cert-trust-list/{cert_trust_list_id}'
        dictPath={'cert_trust_list_id': cert_trust_list_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateCertTrustListByCert_trust_list_id(self,cert_trust_list_id="",body=({})):
        '''
        Operation: Enbale certificate trust list
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: cert_trust_list_id, Description: URL parameter cert_trust_list_id
        Required Body Parameters (body description)- CertTrustListUpdate {cert_file (string, optional): Certificate trust list file,enabled (boolean, optional): Enable certificate trust list,cert_usage (array[string], optional) = ['AD/LDAP Servers' or 'Aruba Infrastructure' or 'Aruba Services' or 'Database' or 'EAP' or 'Endpoint Context Servers' or 'RadSec' or 'SAML' or 'SMTP' or 'EST' or 'Others']: Usage of the certificate}
        Required Body Parameters (type(dict) body example)- {
  "cert_file": "",
  "enabled": false,
  "cert_usage": [
    ""
  ]
}
        '''
        urlPath='/cert-trust-list/{cert_trust_list_id}'
        dictPath={'cert_trust_list_id': cert_trust_list_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def deleteCertTrustListByCert_trust_list_id(self,cert_trust_list_id=""):
        '''
        Operation: Delete a certificate trust list
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: cert_trust_list_id, Description: URL parameter cert_trust_list_id
        '''
        urlPath='/cert-trust-list/{cert_trust_list_id}'
        dictPath={'cert_trust_list_id': cert_trust_list_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:CertTrustListDetails  
    #Function Section Description: Manage Certificate Trust List details

    def getCertTrustListDetails(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of certificate trust list details
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/cert-trust-list-details'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def getCertTrustListDetailsByCert_trust_list_details_id(self,cert_trust_list_details_id=""):
        '''
        Operation: Get a certificate trust list details
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: cert_trust_list_details_id, Description: URL parameter cert_trust_list_details_id
        '''
        urlPath='/cert-trust-list-details/{cert_trust_list_details_id}'
        dictPath={'cert_trust_list_details_id': cert_trust_list_details_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        

    #Function Section Name:ClientCert  
    #Function Section Description: Manage Client Certificates

    def getClientCert(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of client certificates
        HTTP Status Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/client-cert'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newClientCert(self,body=({})):
        '''
        Operation: Add a client certificate
        HTTP Status Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- ClientCertCreate {certificate_url (string, optional): Certificate File URL,pkcs12_file_url (string, optional): PKCS12 File URL,pkcs12_passphrase (string, optional): PKCS12 passphrase}
        Required Body Parameters (type(dict) body example)- {
  "certificate_url": "",
  "pkcs12_file_url": "",
  "pkcs12_passphrase": ""
}
        '''
        urlPath='/client-cert'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getClientCertByClient_cert_id(self,client_cert_id=""):
        '''
        Operation: Get a client certificate
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: client_cert_id, Description: URL parameter client_cert_id
        '''
        urlPath='/client-cert/{client_cert_id}'
        dictPath={'client_cert_id': client_cert_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def deleteClientCertByClient_cert_id(self,client_cert_id=""):
        '''
        Operation: Delete a client certificate
        HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: client_cert_id, Description: URL parameter client_cert_id
        '''
        urlPath='/client-cert/{client_cert_id}'
        dictPath={'client_cert_id': client_cert_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:RevocationList  
    #Function Section Description: Manage Revocation Certificate List

    def getRevocationList(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of revocation certificate list
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/revocation-list'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newRevocationList(self,body=({})):
        '''
        Operation: Add a new revocation certificate list
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- RevocationListCreate {url (string): URL of the Certificate,bypass_proxy (boolean, optional): Bypass Proxy status of the Certificate,periodic_update (boolean, optional): Periodic Update status of the Certificate,periodic_update_interval (integer, optional): Periodic update time of the Certificate,last_update_status (string, optional): Last updated status,last_updated_time (string, optional): Last updated time,next_updated_time (string, optional): Next update time}
        Required Body Parameters (type(dict) body example)- {
  "url": "",
  "bypass_proxy": false,
  "periodic_update": false,
  "periodic_update_interval": 0,
  "last_update_status": "",
  "last_updated_time": "",
  "next_updated_time": ""
}
        '''
        urlPath='/revocation-list'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getRevocationListByRevocation_list_id(self,revocation_list_id=""):
        '''
        Operation: Get a certificate by id
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: revocation_list_id, Description: URL parameter revocation_list_id
        '''
        urlPath='/revocation-list/{revocation_list_id}'
        dictPath={'revocation_list_id': revocation_list_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def updateRevocationListByRevocation_list_id(self,revocation_list_id="",body=({})):
        '''
        Operation: Update a certificate
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: revocation_list_id, Description: URL parameter revocation_list_id
        Required Body Parameters (body description)- RevocationListUpdate {url (string, optional): URL of the Certificate,bypass_proxy (boolean, optional): Bypass Proxy status of the Certificate,periodic_update (boolean, optional): Periodic Update status of the Certificate,periodic_update_interval (integer, optional): Periodic update time of the Certificate,last_update_status (string, optional): Last updated status,last_updated_time (string, optional): Last updated time,next_updated_time (string, optional): Next update time}
        Required Body Parameters (type(dict) body example)- {
  "url": "",
  "bypass_proxy": false,
  "periodic_update": false,
  "periodic_update_interval": 0,
  "last_update_status": "",
  "last_updated_time": "",
  "next_updated_time": ""
}
        '''
        urlPath='/revocation-list/{revocation_list_id}'
        dictPath={'revocation_list_id': revocation_list_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch',query=body)
    def deleteRevocationListByRevocation_list_id(self,revocation_list_id=""):
        '''
        Operation: Delete a certificate list by id
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: revocation_list_id, Description: URL parameter revocation_list_id
        '''
        urlPath='/revocation-list/{revocation_list_id}'
        dictPath={'revocation_list_id': revocation_list_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        

    #Function Section Name:SelfSignedCert  
    #Function Section Description: Manage Self-Signed Certificates

    def newSelfSignedCert(self,body=({})):
        '''
        Operation: Create a Self-Signed Certificate
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- SelfSignedCertCreate {certificate_type (string) = ['SERVER' or 'SERVICE']: Certificate Type,server (string): Server hostname,type (string) = ['RADIUS/EAP Server Certificate' or 'HTTPS(ECC) Server Certificate' or 'HTTPS(RSA) Server Certificate' or 'RadSec Server Certificate' or 'Database Server Certificate']: Service Type,subject_CN (string): Common Name (CN),subject_O (string, optional): Organization (O),subject_OU (string, optional): Organizational Unit (OU),subject_L (string, optional): Location (L),subject_ST (string, optional): State (ST),subject_C (string, optional): Country (C),subject_SAN (string, optional): Subject Alternate Name (SAN),private_key_password (string): Private Key Password,private_key_type (string) = ['2048-bit rsa' or '3072-bit rsa' or '4096-bit rsa' or 'nist/secg curve over a 256 bit prime field' or 'nist/secg curve over a 384 bit prime field' or 'nist/secg curve over a 521 bit prime field']: Private Key Type,digest_algorithm (string) = ['SHA-1' or 'SHA-224' or 'SHA-256' or 'SHA-384' or 'SHA-512']: Digest Algorithm}
        Required Body Parameters (type(dict) body example)- {
  "certificate_type": "",
  "server": "",
  "type": "",
  "subject_CN": "",
  "subject_O": "",
  "subject_OU": "",
  "subject_L": "",
  "subject_ST": "",
  "subject_C": "",
  "subject_SAN": "",
  "private_key_password": "",
  "private_key_type": "",
  "digest_algorithm": ""
}
        '''
        urlPath='/self-signed-cert'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)

    #Function Section Name:ServerCert  
    #Function Section Description: Manage Server Certificates

    def getServerCert(self,body=({})):
        '''
        Operation: Get a list of server certificates
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Body Parameters (body description)- SelfSignedCertCreate {certificate_type (string) = ['SERVER' or 'SERVICE']: Certificate Type,server (string): Server hostname,type (string) = ['RADIUS/EAP Server Certificate' or 'HTTPS(ECC) Server Certificate' or 'HTTPS(RSA) Server Certificate' or 'RadSec Server Certificate' or 'Database Server Certificate']: Service Type,subject_CN (string): Common Name (CN),subject_O (string, optional): Organization (O),subject_OU (string, optional): Organizational Unit (OU),subject_L (string, optional): Location (L),subject_ST (string, optional): State (ST),subject_C (string, optional): Country (C),subject_SAN (string, optional): Subject Alternate Name (SAN),private_key_password (string): Private Key Password,private_key_type (string) = ['2048-bit rsa' or '3072-bit rsa' or '4096-bit rsa' or 'nist/secg curve over a 256 bit prime field' or 'nist/secg curve over a 384 bit prime field' or 'nist/secg curve over a 521 bit prime field']: Private Key Type,digest_algorithm (string) = ['SHA-1' or 'SHA-224' or 'SHA-256' or 'SHA-384' or 'SHA-512']: Digest Algorithm}
        Required Body Parameters (type(dict) body example)- {
  "certificate_type": "",
  "server": "",
  "type": "",
  "subject_CN": "",
  "subject_O": "",
  "subject_OU": "",
  "subject_L": "",
  "subject_ST": "",
  "subject_C": "",
  "subject_SAN": "",
  "private_key_password": "",
  "private_key_type": "",
  "digest_algorithm": ""
}
        '''
        urlPath='/server-cert'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get',query=body)
    def getServerCertNameByServer_uuidService_name(self,server_uuid="",service_name=""):
        '''
        Operation: Get a server certificate
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: service_name, Description: Service name (RADIUS, HTTPS(RSA), HTTPS(ECC) or RadSec)
        '''
        urlPath='/server-cert/name/{server_uuid}/{service_name}'
        dictPath={'server_uuid': server_uuid, 'service_name': service_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def replaceServerCertNameByServer_uuidService_name(self,server_uuid="",service_name="",body=({})):
        '''
        Operation: Add a server certificate
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: service_name, Description: Service name (RADIUS, HTTPS(RSA), HTTPS(ECC) or RadSec)
        Required Body Parameters (body description)- ServerCertReplace {certificate_url (string, optional): Certificate File URL,pkcs12_file_url (string, optional): PKCS12 File URL,pkcs12_passphrase (string, optional): PKCS12 passphrase}
        Required Body Parameters (type(dict) body example)- {
  "certificate_url": "",
  "pkcs12_file_url": "",
  "pkcs12_passphrase": ""
}
        '''
        urlPath='/server-cert/name/{server_uuid}/{service_name}'
        dictPath={'server_uuid': server_uuid, 'service_name': service_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='put',query=body)
    def updateServerCertNameByServer_uuidService_nameEnable(self,server_uuid="",service_name=""):
        '''
        Operation: Update a server certificate
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: service_name, Description: Service name (HTTPS(RSA) or HTTPS(ECC))
        '''
        urlPath='/server-cert/name/{server_uuid}/{service_name}/enable'
        dictPath={'server_uuid': server_uuid, 'service_name': service_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        
    def updateServerCertNameByServer_uuidService_nameDisable(self,server_uuid="",service_name=""):
        '''
        Operation: Update a server certificate
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: service_name, Description: Service name (HTTPS(RSA) or HTTPS(ECC))
        '''
        urlPath='/server-cert/name/{server_uuid}/{service_name}/disable'
        dictPath={'server_uuid': server_uuid, 'service_name': service_name}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='patch')
        
        

    #Function Section Name:ServiceCert  
    #Function Section Description: Manage Service Certificates

    def getServiceCert(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of service certificates
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        urlPath='/service-cert'
        dictQuery={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        urlPath = _generateParameterisedURL(parameters=dictQuery,url=urlPath)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def newServiceCert(self,body=({})):
        '''
        Operation: Add a service certificate
        HTTP Status Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- ServiceCertCreate {certificate_url (string, optional): Certificate File URL,pkcs12_file_url (string, optional): PKCS12 File URL,pkcs12_passphrase (string, optional): PKCS12 passphrase}
        Required Body Parameters (type(dict) body example)- {
  "certificate_url": "",
  "pkcs12_file_url": "",
  "pkcs12_passphrase": ""
}
        '''
        urlPath='/service-cert'
        body = _removeEmptyKeys(keys=body)
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='post',query=body)
    def getServiceCertByService_cert_id(self,service_cert_id=""):
        '''
        Operation: Get a service certificate
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: service_cert_id, Description: URL parameter service_cert_id
        '''
        urlPath='/service-cert/{service_cert_id}'
        dictPath={'service_cert_id': service_cert_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='get')
        
        
    def deleteServiceCertByService_cert_id(self,service_cert_id=""):
        '''
        Operation: Delete a service certificate
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: service_cert_id, Description: URL parameter service_cert_id
        '''
        urlPath='/service-cert/{service_cert_id}'
        dictPath={'service_cert_id': service_cert_id}
        for item in dictPath:
            urlPath=urlPath.replace('{'+item+'}',dictPath[item])
        return ClearPassAPILogin._sendRequest(self,url=urlPath,method='delete')
        
        
