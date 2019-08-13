# pylint: disable=no-member, no-else-return, too-many-locals
"""
importing: Redis cache for getting token key:value
           Rest Framework for getting status response,
           responses, api_decorator
           serializers.py to import required classes.

"""
import os

from django.core.cache import cache
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from twilio.rest import Client
from decouple import config

from Phonebook_App.serializers import Employee, ContactSerializers,\
                                          EmpClientIDSerializers


@api_view(['POST', 'GET'])
def sendotp(request):
    """
     This function is used to send the opt to the mobile number
     through the sms
    :param request: to get the contact number
    :return: verification code
    """

    serializer = ContactSerializers(data=request.data)
    contacts = serializer.initial_data['contact']
    con = '+91'
    contact = con.__add__(contacts)
    print(contact)

    # Your Account SID from twilio.com/console
    account_sid = config('TWILIO_ACCOUNT_SID', '')

    # Your Auth Token from twilio.com/console
    auth_token = config('TWILIO_AUTH_TOKEN', '')

    client = Client(account_sid, auth_token)
    verification = client.verify \
        .services('VAc07ac478546894b8f660ccb4448fbe7b') \
        .verifications \
        .create(to=contact, channel='sms', locale='en')

    print(verification.sid)
    return Response(verification.sid, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def verify(request):
    """
     This function is used to verify the opt send to the mobile number
     through the sms
    :param request: to get the contact number
    :return: Response verify or nor
     """

    token = request.META.get('HTTP_AUTHORIZATION')
    print(token)
    otp = request.META.get('HTTP_OTPSEND')
    cont = request.META.get('HTTP_CONTACT')
    email = cache.get(token)
    query = Employee.objects.filter(email=email)
    print(query)
    client_id = EmpClientIDSerializers(query, many=True).data[0]['client_id']
    con = '+91'
    contact = con.__add__(cont)
    print(contact)
    print(otp)
    client_query = Employee.objects.get(pk=client_id)
    # Your Account SID from twilio.com/console
    account_sid = config('TWILIO_ACCOUNT_SID', '')
    # Your Auth Token from twilio.com/console
    auth_token = config('TWILIO_AUTH_TOKEN', '')

    client = Client(account_sid, auth_token)
    verification_check = client.verify \
        .services('VAc07ac478546894b8f660ccb4448fbe7b') \
        .verification_checks \
        .create(to=contact, code=otp)
    print(verification_check.status)
    context = verification_check.status
    if context == 'approved':
        serializer = ContactSerializers(client_query, data={'contact': cont})
        if serializer.is_valid():
            serializer.save()
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        context = {'UNAUTHORIZED!!!'}
        return Response(context, status=status.HTTP_401_UNAUTHORIZED)
