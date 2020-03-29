import requests
import json
from requests_oauth2 import OAuth2BearerToken
from requests_oauthlib import OAuth1Session
def send_post_request(request_url,request_parameters):
    r = requests.post(url=request_url, data = request_parameters)
    return r
def send_get_request_with_Auth(request_url,request_parameters, user_name, password):
    r = requests.post(request_url, request_parameters, auth=HTTPBasicAuth(user_name, password))
    data = json.loads(r.content)
    return data
def send_post_request_with_Auth1(request_url,request_parameters,client_key, client_secret, resource_owner_key,resource_owner_secret):
    authentication = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
    r = authentication.post(request_url, data=request_parameters)
    data = json.loads(r.content)
    return data
def send_post_request_with_header(request_url,request_parameters, header):
    r = requests.post(url=request_url, data=request_parameters, header={header})
    return r
def send_get_request_with_Auth_with_header(request_url,request_parameters, user_name, password,header):
    r = requests.post(request_url, request_parameters, auth=HTTPBasicAuth(user_name, password), header={header})
    data = json.loads(r.content)
    return data
def send_post_request_with_Auth1_with_header(request_url,request_parameters,client_key, client_secret, resource_owner_key,resource_owner_secret,header):
    authentication = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
    r = authentication.post(request_url, data=request_parameters, header={header})
    data = json.loads(r.content)
    return data

def send_put_request_with_Auth2(request_url, access_token, request_parameters):

    with requests.Session() as s:
        s.auth = OAuth2BearerToken(access_token)
        r = s.put(request_url, request_parameters)
        r.raise_for_status()
        data = r.json()