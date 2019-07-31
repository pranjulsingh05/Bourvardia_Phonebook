from django.core.cache import cache
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from twilio.rest import Client

from .serializers import *


@api_view(['POST', 'GET'])
def sendotp(request):

    serializer = ContactSerializers(data=request.data)  # Retrieving data according to UserSerializers class.
    contacts = serializer.initial_data['contact']
    con = '+91'
    contact = con.__add__(contacts)
    print(contact)
    account_sid = 'AC11374718c812f729cbfcd5d6171d9ecf'
    auth_token = '137075228c7bed566210ae44a3e7d086'
    client = Client(account_sid, auth_token)
    verification = client.verify \
        .services('VAc07ac478546894b8f660ccb4448fbe7b') \
        .verifications \
        .create(to=contact, channel='sms', locale='en')

    print(verification.sid)
    return Response(verification.sid, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def verify(request):

    token = request.META.get('HTTP_AUTHENTICATION')
    print(token)
    otp = request.META.get('HTTP_OTPSEND')
    cont = request.META.get('HTTP_CONTACT')
    email = cache.get(token)
    print(email)
    query = Employee.objects.filter(email=email)
    client_id = EmpClientIDSerializers(query, many=True).data[0]['client_id']
    con = '+91'
    contact = con.__add__(cont)
    print(contact)
    print(otp)
    client_query = Employee.objects.get(pk=client_id)
    account_sid = 'AC11374718c812f729cbfcd5d6171d9ecf'
    auth_token = '137075228c7bed566210ae44a3e7d086'
    client = Client(account_sid, auth_token)
    verification_check = client.verify \
        .services('VAc07ac478546894b8f660ccb4448fbe7b') \
        .verification_checks \
        .create(to=contact, code=otp)
    print(verification_check.status)
    context = verification_check.status
    if context == 'approved':
        serializer = ContactSerializers(client_query, data={'contact': cont}, context={'request': request})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        context = {'UNAUTHORIZED!!!'}
        return Response(context, status=status.HTTP_401_UNAUTHORIZED)
