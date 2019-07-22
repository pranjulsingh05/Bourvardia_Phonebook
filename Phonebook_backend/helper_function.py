from .serializers import *
from django.core.cache import cache
from google.oauth2 import id_token
from google.auth.transport import requests
import os


def authentication(token_id):

    App_Id = os.environ.get('APP_ID', '')
    # Specify the App_Id(CLIENT_ID) of the app that accesses the backend:
    idinfo = id_token.verify_oauth2_token(token_id, requests.Request(), App_Id)

    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise ValueError('Wrong issuer.')

    if idinfo['hd'] != 'nineleaps.com':
        raise ValueError('Wrong hosted Domain.')

    # ID token is valid. Get the user's Google Account ID from the decoded token using - idinfo['sub']
    # ID token is valid. Get the user's Google Email ID from the decoded token using - idinfo['email']
    info = {"id":idinfo['sub'], "email" : idinfo['email']}
    return info


def start_session(emailid, token):

    tokenvalue = cache.get(token)
    email = emailid
    try:
        if email == tokenvalue:
            return True
        else:
            cache.set(token, email, timeout=60*60)
            return True
    except ValueError:
        return False


def session_manage(self):

    tokenvalue = cache.get(self)
    queryset = Employee.objects.all()
    if tokenvalue is not None and tokenvalue != 'null':
        result = queryset.filter(email=tokenvalue)
        if result:
            return True
        elif not result:
            return False
    elif not tokenvalue:
        return False


def getclient(self):

    client_id = self.request.query_params.get('client_id', None)  # Accessing client_id as parameter to show manager of logged in and searched user in hierarchy.
    if client_id is not None and client_id != 'null':
        return client_id
