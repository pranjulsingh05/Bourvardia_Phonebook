from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from django.core.cache import cache
from Phonebook_backend.helper_function import start_session, authentication
from Phonebook_backend.logging import login_logger


class Users_Login(APIView):  # API to fetch data of logging/logged in user to store in database.
    """
        The users_Login object contains the basic details of the logging in user such as name, client_id, employee id, email, image.

        ........................................

        Parameter :
        APIView is a concrete view for listing and saving a queryset, derived from the base class Views from rest framework.

        :return:
        A response upon successfully logging in by a user.
     """

    model = Employee
    serializer_class = UserSerializers

    def post(self, request):
        """
        This function is used create data in the database of the user trying to log-in.

        ........................................

        Parameter :
        self (varchar) : This is the client_id which is used to filter the database for the particular user.
        request : This is the request method which is used to perform function upon the database for the particular user.
        :return:
            A status code as response upon logging in of the user.
        """

        token_id = request.META.get('HTTP_AUTHORIZATION')
        token = request.META.get('HTTP_ACCESS_TOKEN')
        serializer = UserSerializers(data=request.data)  # Retrieving data according to UserSerializers class.
        client_id = serializer.initial_data['client_id']
        email = serializer.initial_data['email']

        if serializer.is_valid() and request.method == 'POST':
            try:
                info = authentication(token_id=token_id)
                if client_id == info['id'] and email == info['email']:
                    serializer.save()
                    arr = [Designation_Client, Location_Client, Language_Client,
                           Skill_Client, Project_Client, Hierarchy_Client]
                    for i in arr:
                        serializers = i(data=request.data)
                        if serializers.is_valid():
                            serializers.save()
                    if start_session(emailid=email, token=token):
                        login_logger.info('Successful Login by %s.', email)
                        content = {'Note': 'Successful Login.'}
                        return Response(content, status=status.HTTP_201_CREATED)
                else:
                    login_logger.error('Unauthorized Login by %s.', email)
                    content = {'error': 'Authorization Denied.'}
                    return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            except ValueError:
                login_logger.error('Unauthorized Login by %s.', email)
                content = {'error': 'Authorization Denied.'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        else:
            try:
                info = authentication(token_id=token_id)
                if client_id == info['id'] and email == info['email'] and start_session(emailid=email, token=token):
                    login_logger.info('Successful Login by %s.', email)
                    content = {'Note': 'Successful Login.'}
                    return Response(content, status=status.HTTP_200_OK)
                else:
                    login_logger.error('Unauthorized Login by %s.', email)
                    content = {'error': 'Authorization Denied.'}
                    return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            except ValueError:
                login_logger.error('Unauthorized Login by %s.', email)
                content = {'error': 'Authorization Denied.'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def User_Logout(request):
    """
        This function is used delete data in the cache memory of the user to end the session.

        ........................................

        Parameter :
        request : This is the request method which is used to perform function upon the cache memory for the particular user.
        :return:
            A status code as response upon logging out of the user.
        """

    token = request.META.get('HTTP_ACCESS_TOKEN')
    email = cache.get(token)
    if request.method == 'POST':
        cache.delete(token)
        login_logger.info('Successful Logout by %s.', email)
        content = {'success': 'Successfully Logged Out.'}
        return Response(content, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


