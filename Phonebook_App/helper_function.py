# pylint: disable=no-member, no-else-return, inconsistent-return-statements

"""
os: To get the App_id from the Environment variable.
"""
import os

from django.core.cache import cache

from google.auth.transport import requests
from google.oauth2 import id_token

from Phonebook_App.serializers import Employee


def authentication(token_id):
    """
    This function is used authorise the user that his
    id present in google account & domain is nineleaps.com

    :param token_id: getting token from the front-end and verifying it from google.

    :return: client_id(sub) & email(of the logged in user)

    """
    app_id = os.environ.get('APP_ID', '')
    # Specify the App_Id(CLIENT_ID) of the app that accesses the backend:
    id_info = id_token.verify_oauth2_token(token_id, requests.Request(), app_id)

    if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise ValueError('Wrong issuer.')

    if id_info['hd'] != 'nineleaps.com':
        raise ValueError('Wrong hosted Domain.')

    info = {"id": id_info['sub'], "email": id_info['email']}
    return info


def start_session(email_id, token):
    """
        This function is used start the user session.
        If user is new, his token_id wil be set in the Redis Cache.

        :param email_id: getting the email id of the user
        :param token: getting token from the front-end and verifying it from google.

        :return: True or False
    """
    token_value = cache.get(token)
    email = email_id
    try:
        if email == token_value:
            return True
        else:
            cache.set(token, email, timeout=60*60)
            return True
    except ValueError:
        return False


def session_manage(self):
    """
            This function is used manager the user session throughout Api_Call.
            If user is new, his token_id wil be set in the Redis Cache.

            :param self: to check the key(token) is having the value(email)
                        of the user.

            :return: True ot False
    """

    token_value = cache.get(self)
    queryset = Employee.objects.all()
    if token_value is not None and token_value != 'null':
        result = queryset.filter(email=token_value)
        if result:
            return True
        # else:
        #     return False
    else:
        return False


def getclient(self):
    """
        Accessing client_id as parameter to show manager of
        logged in and searched user in hierarchy
        .
        :param self: to get the Client_id of the user which is
                    unique

        :return: Client_id
    """
    client_id = self.request.query_params.get('client_id', None)
    if client_id is not None and client_id != 'null':
        return client_id
