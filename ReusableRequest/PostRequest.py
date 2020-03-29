import requests
import json
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1Session
from requests_oauth2 import OAuth2BearerToken
def send_post_request(request_url,request_parameters):
    r = requests.put(url=request_url, data=request_parameters)
    return r
def send_get_request_with_Auth(request_url,request_parameters, user_name, password):
    r = requests.put(request_url, request_parameters, auth=HTTPBasicAuth(user_name, password))
    data = json.loads(r.content)
    return data
def send_post_request_with_Auth1(request_url,request_parameters,client_key, client_secret, resource_owner_key,resource_owner_secret):
    authentication = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
    r = authentication.put(request_url, data=request_parameters)
    data = json.loads(r.content)
    return data

def send_post_request_with_headers(request_url,request_parameters, headers ):
    r = requests.put(url=request_url, data=request_parameters, headers ={headers})
    return r
def send_get_request_with_Auth_with_headers(request_url,request_parameters, user_name, password, headers):
    r = requests.put(request_url, request_parameters, auth=HTTPBasicAuth(user_name, password), headers={headers})
    data = json.loads(r.content)
    return data
def send_post_request_with_Auth1_with_headers(request_url,request_parameters,client_key, client_secret, resource_owner_key,resource_owner_secret, headesrs):
    authentication = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
    r = authentication.put(request_url, data=request_parameters, headesrs={headesrs})
    data = json.loads(r.content)
    return data

def send_post_request_with_Auth2(request_url, access_token, request_parameters):

    with requests.Session() as s:
        s.auth = OAuth2BearerToken(access_token)
        r = s.post(request_url, request_parameters)
        r.raise_for_status()
        data = r.json()