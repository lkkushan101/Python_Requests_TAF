import requests
import json
from requests_oauthlib import OAuth1Session
from requests.auth import HTTPBasicAuth
from requests_oauth2 import OAuth2BearerToken
def send_delete_request(request_url):
    r = requests.delete(url=request_url)
    return r
def send_delete_request_with_Auth1(request_url,client_key, client_secret, resource_owner_key,resource_owner_secret):
    authentication = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
    r = authentication.delete(request_url)
    data = json.loads(r.content)
    return data
def send_get_request_with_Auth(request_url, user_name, password):
    r = requests.get(request_url, auth=HTTPBasicAuth(user_name, password))
    data = json.loads(r.content)
    return data
def send_delete_request_with_header(request_url, header):
    r = requests.delete(url=request_url, header={header})
    return r
def send_delete_request_with_Auth1_with_header(request_url,client_key, client_secret, resource_owner_key,resource_owner_secret, header):
    authentication = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
    r = authentication.delete(request_url,  header={header})
    data = json.loads(r.content)
    return data
def send_get_request_with_Auth_with_header(request_url, user_name, password, header):
    r = requests.get(request_url, auth=HTTPBasicAuth(user_name, password), header={header})
    data = json.loads(r.content)
    return data

def send_delete_request_with_Auth2(request_url, access_token):

    with requests.Session() as s:
        s.auth = OAuth2BearerToken(access_token)
        r = s.delete(request_url)
        r.raise_for_status()
        data = r.json()