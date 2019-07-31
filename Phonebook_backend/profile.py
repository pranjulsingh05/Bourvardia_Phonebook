from django.core.mail import mail_admins
from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Phonebook_backend.helper_function import getclient, session_manage
from Phonebook_backend.logging import profile_logger
from Phonebook_backend.models import *

from .serializers import *


class HomeView(generics.ListAPIView):  # API to show basic details of logged in user.
    """
        The Home_View object contains the basic details of the logged in user such as name, employee id, email, bio, image.

        ............................................

        Parameter :
        ListAPIView is a concrete view for listing a queryset derived from the base class Generic Views.

        :return:
        A queryset with basic details of the logged in user.

        ---
        :parameters:
            - client_id: client_id
              paramType: query
     """
    model = Employee
    serializer_class = HomeSerializers

    def get_queryset(self):
        """
            This function is used get the data of the logged in user from the database.

            ........................................

            Parameter :
            self (varchar) : This is the client_id which is used to filter the database for the particular user.
            :return:
            A queryset of the user with the requested client_id.
        """
        queryset = Employee.objects.all()
        client_id = getclient(self=self)
        if client_id != 'null':
            queryset = queryset.filter(client_id=client_id)
            return queryset
        elif client_id == 'null':
            return None

    def get_queryset2(self):
        """
            This function is used get the data of the logged in user from the database.

            ........................................

            Parameter :
            self (varchar) : This is the client_id which is used to filter the database for the particular user.
            :return:
            A queryset of the user with the requested client_id.
        """
        designation = EmployeeDesignation.objects.all()
        client_id = getclient(self=self)
        if client_id != 'null':
            des = designation.filter(client_id=client_id)
            return des
        elif client_id == 'null':
            return None

    def get_queryset3(self):
        """
            This function is used get the data of the logged in user from the database.

            ........................................

            Parameter :
            self (varchar) : This is the client_id which is used to filter the database for the particular user.
            :return:
            A queryset of the user with the requested client_id.
        """
        hierarchy = Hierarchy.objects.all()
        manager_detail = Employee.objects.all()
        client_id = getclient(self=self)
        if client_id != 'null':
            queryset = hierarchy.filter(client_id=client_id)
            manager_id = HierarchySerializers(queryset, many=True).data

            if manager_id:

                query = manager_detail.filter(client_id=manager_id[0]['manager_id'])
                return query
        elif client_id == 'null':
            return None

    def list(self, *args):
        """

            This function is used send the data of the logged in user from the database.

            ........................................

            Parameter :
            self (varchar) : This is the access token by which the user is authorized to access the resources.
            *args : The single asterisk form ( *args ) is used to pass a non-keyworded, variable-length argument list.
            :parameter: client_id

            :return:
            A queryset containing data depending upon the 'HomeSerializer' serializer class of the logged in user.


        """
        token = self.request.META.get('HTTP_AUTHORIZATION')
        if session_manage(self=token):
            view = self.get_queryset()
            designation = self.get_queryset2()
            manager = self.get_queryset3()
            if view or designation:
                serializer = HomeSerializers(view, many=True).data
                serializer2 = EmpDesSerializer(designation, many=True).data
                serializer3 = SearchSerializer(manager, many=True).data
                return Response({'User': serializer,
                                'Designation': serializer2,
                                 'Manager': serializer3
                                 })
            elif not view:
                profile_logger.error('Home Page Error')
                content = {'Error': 'No User Found!'}
                return Response(content, status=status.HTTP_200_OK)

        else:
            profile_logger.error('Session Error in Home View.')
            content = {'Error': 'Session Ended!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class UsersView(generics.ListAPIView):  # API to show details of logged in user.
    """
        The User_View object contains all the details of the users such as name, client_id, email, contact, emp_id, designation, skill, slack_id, location, language, image_url, projects, hobbies, manager_id, bio.
        ............................................

        Parameter :
        ListAPIView is a concrete view for listing a queryset derived from the base class Generic Views.

        :return:
        A queryset with all the details of the users.
     """

    serializer_class = EmpSerializers, EmpLocSerializer, EmpSkillSerializer, EmpProSerializer, EmpLangSerializer, EmpDesSerializer

    def basic_detail(self):
        """
            This function is used get the basic data of the users from the database.

            ........................................

            Parameter :
            self (varchar) : This is the email which is used to filter the database for the particular user.

            :return:
            A queryset of the user with the requested email.
        """

        basicdetail = Employee.objects.all()
        client_id = getclient(self=self)
        if client_id is not None and client_id != 'null':
            basic = basicdetail.filter(client_id=client_id)
            return basic
        elif not client_id or client_id == 'null':
            return None

    def designation(self):

        designation = EmployeeDesignation.objects.all()
        client_id = getclient(self=self)
        if client_id is not None and client_id != 'null':
            des = designation.filter(client_id=client_id)
            return des
        elif not client_id or client_id == 'null':
            return None

    def location(self):

        location = EmployeeLocation.objects.all()
        client_id = getclient(self=self)
        if client_id is not None and client_id != 'null':
            loc = location.filter(client_id=client_id)
            return loc
        elif not client_id or client_id == 'null':
            return None

    def skill(self):

        skills = EmployeeSkill.objects.all()
        client_id = getclient(self=self)
        if client_id is not None and client_id != 'null':
            skill = skills.filter(client_id=client_id)
            return skill
        elif not client_id or client_id == 'null':
            return None

    def project(self):

        projects = EmployeeProject.objects.all()
        client_id = getclient(self=self)
        if client_id is not None and client_id != 'null':
            project = projects.filter(client_id=client_id)
            return project
        elif not client_id or client_id == 'null':
            return None

    def language(self):

        languages = EmployeeLanguage.objects.all()
        client_id = getclient(self=self)
        if client_id is not None and client_id != 'null':
            language = languages.filter(client_id=client_id)
            return language
        elif not client_id or client_id == 'null':
            return None

    def list(self, *args):
        """
            This function is used send the data of the particular users from the database.

            ........................................

            Parameter :
            self (varchar) : This is the access token by which the user is authorized to access the resources.
            *args : The single asterisk form ( *args ) is used to pass a non-keyworded, variable-length argument list.

            :return:
            A queryset containing data depending upon the 'EmpSerializer' serializer class of the users.
        """
        '''Parameter: client_id=112497232779980669055'''

        # token = self.request.META.get('HTTP_AUTHORIZATION')
        # if session_manage(self=token):
        basic_details = self.basic_detail()
        designation = self.designation()
        location = self.location()
        skill = self.skill()
        project = self.project()
        language = self.language()
        base = EmpSerializers(basic_details, many=True)
        des = EmpDesSerializer(designation, many=True)
        loc = EmpLocSerializer(location, many=True)
        sk = EmpSkillSerializer(skill, many=True)
        pro = EmpProSerializer(project, many=True)
        lang = EmpLangSerializer(language, many=True)

        return Response(
            {
                "Basic": base.data,
                "Designation":des.data,
                "Location":loc.data,
                "Skill":sk.data,
                "Project":pro.data,
                "Language":lang.data
            }
        )
        # else:
        #     profile_logger.error('Session Error in user view.')
        #     content = {'Error': 'Session Ended!'}
        #     return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def addmanager(request, pk):
    """
        This function is used get all the data of the users from the database.

        ........................................

        Parameter :
        request : This is the request method which is used to perform function upon the database for the particular user.
        pk : This is the primary key which is used to identify the particular user upon which the functions will be appiled.
        :return:
            A status code response upon editing or updating the data of the user with the requested primary key.
        """

    try:
        client_id = Hierarchy.objects.get(pk=pk)
        print(client_id)
    except:
        profile_logger.error('Primary Key Error in Add Manager View.')
        return Response(status=status.HTTP_404_NOT_FOUND)
    if client_id != 'null':
        if request.method == 'PUT':
            hierarchyserializer = HierarchySerializers(client_id, data=request.data, context={'request': request})
            if hierarchyserializer.is_valid():
                hierarchyserializer.save()
                content = {'Manager Added Successfully.'}
                return Response(content, status=status.HTTP_200_OK)
            else:
                profile_logger.error('HierarchySerializer Error.')
                content = {'error': 'Check The Manager Input Field.'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            profile_logger.error('Only PUT method is allowed.')
            return status == status.HTTP_400_BAD_REQUEST
    else:
        profile_logger.error('No ID in Add Manager.')
        return status == status.HTTP_400_BAD_REQUEST


@api_view(['GET', 'PUT'])
def usersupdateview(request, pk):  # API to retrieve and update details of logged in user.
    """
        This function is used get all the data of the users from the database.

        ........................................

        Parameter :
        request : This is the request method which is used to perform function upon the database for the particular user.
        pk : This is the primary key which is used to identify the particular user upon which the functions will be appiled.
        :return:
            A status code response upon editing or updating the data of the user with the requested primary key.
        """

    # token = request.META.get('HTTP_AUTHORIZATION')
    # if session_manage(self=token):
    try:
        client_id = Employee.objects.get(pk=pk)
        desid = EmployeeDesignation.objects.get(pk=pk)
        locid = EmployeeLocation.objects.get(pk=pk)
        skillid = EmployeeSkill.objects.get(pk=pk)
        proid = EmployeeProject.objects.get(pk=pk)
        langid = EmployeeLanguage.objects.get(pk=pk)
        git_id = Employee.objects.get(pk=pk)
        link_id = Employee.objects.get(pk=pk)
    except ValueError:
        profile_logger.error('Primary Key Error in Update View.')
        return Response(status=status.HTTP_404_NOT_FOUND)

    if client_id != 'null':
        print(request.data)
        if request.method == 'GET':

            empserializer = EmpSerializers(client_id, context={'request': request})
            desserializer = EmpDesSerializer(desid, context={'request': request})
            locserializer = EmpLocSerializer(locid, context={'request': request})
            skillserializer = EmpSkillSerializer(skillid, context={'request': request})
            projectserializer = EmpProSerializer(proid, context={'request': request})
            langserializer = EmpLangSerializer(langid, context={'request': request})
            gitserializer = HomeSerializers(git_id, context = {'request' : request})
            linkserializer = HomeSerializers(link_id, context = {'request' : request})

            if empserializer:
                return Response(
                    {
                        "Basic": empserializer.data,
                        "Designation": desserializer.data,
                        "Location": locserializer.data,
                        "Skill": skillserializer.data,
                        "Project": projectserializer.data,
                        "Language": langserializer.data,
                        "Git_id": gitserializer.data,
                        "Link_id": linkserializer.data,
                    }
                )
            else:
                profile_logger.error('Update View Error.')
                return Response(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':

            empserializer = EmpUpdateSerializers(client_id, data=request.data, context={'request': request})
            locserializer = EmpLocSerializer(locid, data=request.data, context={'request': request})
            projectserializer = EmpProSerializer(proid, data=request.data, context={'request': request})
            langserializer = EmpLangSerializer(langid, data=request.data, context={'request': request})
            desserializer = EmpDesSerializer(desid, data=request.data,  context = {'request': request})
            gitserializer = HomeSerializers(git_id, data=request.data, context = {'request': request})
            linkserializer = HomeSerializers(link_id, data=request.data, context = {'request' : request})
            try:

                if empserializer.is_valid():
                    empserializer.save()
                else:
                    profile_logger.error('EmpUpdateSerializer Error.')
                    content = {'error': 'Check The CONTACT Input Field.'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

                if locserializer.is_valid():
                    locserializer.save()
                else:
                    profile_logger.error('UpdateLocSerializer Error.')
                    content = {'error': 'Check The Location Input Field.'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

                if desserializer.is_valid():
                    desserializer.save()
                else:
                    profile_logger.error('EmpDesSerializer Error')
                    content = {'error': 'Check the Designation Inpur Field'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

                if gitserializer.is_valid():
                    gitserializer.save()
                else:
                    profile_logger.error('GitSerializer Error')
                    content = {'error': 'Check the GitSerializer Inpur Field'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

                if linkserializer.is_valid():
                    linkserializer.save()
                else:
                    profile_logger.error('LinkSerializer Error')
                    content = {'error': 'Check the LinkSerializer Inpur Field'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

                skill = request.data['skill']
                skillset = list(skill.values())
                skills = ", ".join(skillset)
                skillserializer = EmpSkillSerializer(skillid, data={"skill": skills}, context={'request': request})
                print(skillserializer)
                try:
                    if skillserializer.is_valid():
                        skillserializer.save()
                except ValueError:
                    content = {'error': 'Check The Skill Input Field.'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

                if projectserializer.is_valid():
                    projectserializer.save()
                else:
                    profile_logger.error('UpdateProSerializer Error.')
                    content = {'error': 'Check The Project Input Field.'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

                if langserializer.is_valid():
                    langserializer.save()
                    content = {'error': 'Data Updated'}
                    mail_admins(' Profile Update Notification', 'Profile Updated by %s' %client_id)
                    return Response(content, status=status.HTTP_200_OK)
                else:
                    profile_logger.error('UpdateLangSerializer Error.')
                    content = {'error': 'Check The Language Input Field.'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

            except IntegrityError:
                profile_logger.error('Employee Integrity Error.')
                content = {'error': 'Check The EMP-ID Input Field.'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

    else:
        profile_logger.error('No ID in Update View Error.')
        return status == status.HTTP_400_BAD_REQUEST

    # elif request.method == 'PUT':
    #     profile_logger.error('Session Error in Update View.')
    #     content = {'error': 'Session Ended!'}
    #     return Response(content, status=status.HTTP_400_BAD_REQUEST)
    #
    # elif request.method == 'GET':
    #     profile_logger.error('Session Error in Update View.')
    #     content = {'error': 'Session Ended!'}
    #     return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def skillresponse(request):
    """

    :param request:
    :return:

    """
    if request.method == "GET":
        query = Skill.objects.all()
        skills = SkillSerializer(query, many=True).data

        return Response(skills)
    else:
        profile_logger.error('View Skill Error.')
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def designationresponse(request):
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        query = Designation.objects.all()
        designations = UpDateDesSerializer(query, many=True).data

        return Response(designations, status=status.HTTP_200_OK)

    else:
        profile_logger.error('Update Desigantion Error.')
        return Response(status=status.HTTP_400_BAD_REQUEST)
