from django.core.cache import cache
from rest_framework import generics, status
from rest_framework.response import Response

from Phonebook_App.helper_function import getclient, session_manage
from Phonebook_App.logging import view_logger

from .serializers import *


class ManagerSearch(generics.ListAPIView):  # API to show details of searched user.
    """
        The Users_Search object contains the details of the searched user such as name, email, client_id.

        ............................................

        Parameter :
        ListAPIView is a concrete view for listing a queryset derived from the base class Generic Views.

        :return:
        A queryset with details of the searched user.
     """

    queryset = Employee.objects.all()
    serializer_class = SearchSerializer

    def get_queryset(self):
        """
            This function is used get the data of the searched user from the database.

            ........................................

            Parameter :
            self (varchar) : This is the name which is used to filter the database for the particular user.
        :return:
            A queryset of the user(s) with the requested name.
        """

        queryset = Employee.objects.all()
        name = self.request.query_params.get('name', None)  # Accessing name as key to retrieve details of searched user.

        if name is not None and name != 'null' and name != '':
            queryset = queryset.filter(name__icontains=name)
            return queryset

        elif not name or name == 'null':
            return None

    def list(self, *args):
        """
            This function is used send the data of the searched user from the database.

            ........................................

            Parameter :
            self (varchar) : This is the access token by which the user is authorized to access the resources.
            *args : The single asterisk form ( *args ) is used to pass a non-keyworded, variable-length argument list.

            :return:
            A queryset containing data depending upon the 'SearchSerializer' serializer class of the searched user.
        """

        # token = self.request.META.get('HTTP_AUTHORIZATION')
        # if session_manage(self=token):
        search = self.get_queryset()
        serializer = SearchSerializer(search, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     view_logger.error('Search Error in User Search.')
        #     content = {'error': 'No Data Found.'}
        #     return Response(content, status=status.HTTP_400_BAD_REQUEST)


class Search(generics.ListAPIView):

    serializer_class = HomePageSearch

    def get_queryset(self):

        queryset = Employee.objects.all()
        return queryset

    def list(self, *args):
        query = self.get_queryset()
        serializer = HomePageSearch(query, many=True).data
        for i in range(len(serializer)):
            client_id = serializer[i]['client_id']
            name_query = Employee.objects.filter(client_id=client_id)
            name = NameSerializers(name_query, many=True).data
            serializer[i].update({'value':name[0]['name']})
        return Response(serializer, status=status.HTTP_200_OK)


class SearchedUsersView(generics.ListAPIView):  # API to show details of logged in user.
    """
        The User_View object contains all the details of the users such as name, client_id, email, contact, emp_id, designation, skill, slack_id, location, language, image_url, projects, hobbies, manager_id, bio.
        ............................................

        Parameter :
        ListAPIView is a concrete view for listing a queryset derived from the base class Generic Views.

        :return:
        A queryset with all the details of the users.
     """

    serializer_class = EmpSerializers, EmpLocSerializer, EmpSkillSerializer, EmpProSerializer, EmpLangSerializer, EmpDesSerializer, EmpProSerializer

    def basic_detail(self):
        """
            This function is used get all the data of the users from the database.

            ........................................

            Parameter :
            self (varchar) : This is the email which is used to filter the database for the particular user.

            :return:
            A queryset of the user with the requested email.
        """

        basicdetail = Employee.objects.all()
        client_id = getclient(self=self)  # Fetching email through parameter.
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

        token = self.request.META.get('HTTP_AUTHORIZATION')
        print(token)
        email = cache.get(token)

        if session_manage(self=token):
            basic_details = self.basic_detail()
            designation = self.designation()
            location = self.location()
            skill = self.skill()
            project = self.project()
            language = self.language()

            query = Employee.objects.filter(email=email)
            userclientid = EmpClientIDSerializers(query, many=True).data[0]['client_id']
            query1 = EmployeeProject.objects.filter(client_id=userclientid)
            searchclientid = getclient(self=self)
            query2 = EmployeeProject.objects.filter(client_id=searchclientid)
            userproject = ProjectSerializer(query1, many=True).data
            searchproject = ProjectSerializer(query2, many=True).data
            print(userproject)
            print(searchproject)

            if userproject == searchproject:
                return Response(
                    {
                        "Basic": EmpSerializers(basic_details, many=True).data,
                        "Designation": EmpDesSerializer(designation, many=True).data,
                        "Location": EmpLocSerializer(location, many=True).data,
                        "Skill": EmpSkillSerializer(skill, many=True).data,
                        "Project": EmpProSerializer(project, many=True).data,
                        "Language": EmpLangSerializer(language, many=True).data
                    }
                )
            else:
                return Response(
                    {
                        "Basic": SearchEmpSerializers(basic_details, many=True).data,
                        "Designation": EmpDesSerializer(designation, many=True).data,
                        "Location": EmpLocSerializer(location, many=True).data,
                        "Skill": EmpSkillSerializer(skill, many=True).data,
                        "Project": EmpProSerializer(project, many=True).data,
                        "Language": EmpLangSerializer(language, many=True).data
                    }
                )
        else:
            view_logger.error('Session Error in Searched User View.')
            content = {'Error': 'Session Ended!'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)


class ViewHierarchy(generics.ListAPIView):  # API to show hierarchy of logged in and searched user.
    """
        The View_Hierarchy object contains the hierarchy details of the searched as well as logged in user such as manager details and interns details.

        ............................................

        Parameter :
        ListAPIView is a concrete view for listing a queryset derived from the base class Generic Views.

        :return:
        A queryset with hierarchy details of the searched as well as logged in user.
     """

    model = Employee, Hierarchy
    serializer_class = HierarchySerializers

    def get_manager(self):  # Function to show manager of logged in and searched user in hierarchy.
        """
            This function is used get the manager data of the searched as well as logged in user from the database.

            ........................................

            Parameter :
            self (varchar) : This is the client_id which is used to filter the database for the particular user.

            :return:
            A queryset of manager of the user(s) with the requested client_id.
        """

        client_id = getclient(self=self)
        if client_id != 'null':
            managers = Hierarchy.objects.filter(client_id=client_id)
            dict = HierarchySerializers(managers, many=True).data
            for i in range(len(dict)):
                managerid = dict[i]['manager_id']
                manager = Employee.objects.filter(client_id=managerid)
                return manager

        elif client_id == 'null':
            return None

    def get_intern(self):  # Function to show interns of logged in and searched user in hierarchy.
        """
            This function is used get the interns data of the searched as well as logged in user from the database.

            ........................................

            Parameter :
            self (varchar) : This is the client_id which is used to filter the database for the particular user.

            :return:
            A queryset of intern of the user(s) with the requested client_id.
        """

        client_id = getclient(self=self)
        if client_id != 'null':
            query = Hierarchy.objects.filter(manager_id=client_id)
            dict = EmpClientIDSerializers(query, many=True).data
            if dict:
                internid = dict[0]['client_id']
                intern = Employee.objects.filter(client_id=internid)
                for i in range(len(dict)):
                    internid = dict[i]['client_id']
                    interns = intern | Employee.objects.filter(client_id=internid)
                return interns
            else:
                return None
        elif client_id == 'null':
            return None

    def get_user(self):  # Function to show details of logged in and searched user in hierarchy.
        """
            This function is used get the user data of the searched as well as logged in user from the database.

            ........................................

            Parameter :
            self (varchar) : This is the client_id which is used to filter the database for the particular user.

            :return:
            A queryset of the user(s) with the requested client_id.
        """

        client_id = getclient(self=self)
        if client_id != 'null':
            users = Employee.objects.filter(client_id=client_id)
            return users
        elif client_id == 'null':
            return None

    def list(self, *args):  # Function to send the combined responses of all the functions of view_hierarchy API.
        """
            This function is used send the hierarchy details of the searched as well as logged in user from the database.

            ........................................

            Parameter :
            self (varchar) : This is the access token by which the user is authorized to access the resources.
            *args : The single asterisk form ( *args ) is used to pass a non-keyworded, variable-length argument list.

            :return:
            A queryset containing data depending upon the 'HierarchySerializer' serializer class of the searched as well as logged in user.
        """

        token = self.request.META.get('HTTP_AUTHORIZATION')
        if session_manage(self=token):
            client_id = getclient(self=self)
            if client_id is not None and client_id != 'null':
                manager = self.get_manager()
                intern = self.get_intern()
                users = self.get_user()
                serializer1 = SearchSerializer(manager, many=True)
                serializer2 = SearchSerializer(intern, many=True)
                serializer3 = SearchSerializer(users, many=True)
                return Response(
                    {
                        "Manager": serializer1.data,
                        "User": serializer3.data,
                        "Intern": serializer2.data
                    }
                )

            elif not client_id:
                view_logger.error('No ID in Hierarchy Error')
                content = {'error': 'No Data Found.'}
                return Response(content, status=status.HTTP_204_NO_CONTENT)

        else:
            view_logger.error('Session Error in View Hierarchy.')
            content = {'error': 'Session Ended.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class UserHierarchy(generics.ListAPIView):

    model = Employee, Hierarchy
    serializer_class = HierarchySerializers

    def get_senior(self):

        client_id = getclient(self=self)
        if client_id != 'null':
            query = Hierarchy.objects.filter(client_id=client_id)
            dict = HierarchySerializers(query, many=True).data

            if dict:
                for i in range(len(dict)):
                    manager_id = dict[i]['manager_id']
                    managers_manager = Hierarchy.objects.filter(client_id=manager_id)
                    dict1 = HierarchySerializers(managers_manager, many=True).data

                    for i in range(len(dict1)):
                        senior_id = dict1[i]['manager_id']
                        senior = Employee.objects.filter(client_id=senior_id)
                        return senior
            else:
                return None

    def get_manager(self):

        client_id = getclient(self=self)
        if client_id != 'null':
            query = Hierarchy.objects.filter(client_id=client_id)
            dict = HierarchySerializers(query, many=True).data

            if dict:
                for i in range(len(dict)):
                    manager_id = dict[i]['manager_id']
                    manager = Employee.objects.filter(client_id=manager_id)
                    return manager
            else:
                return None

    def get_queryset(self):

        client_id = getclient(self=self)
        if client_id != 'null':
            user = Employee.objects.filter(client_id=client_id)
            return user
        else:
            return None

    def get_junior(self):

        client_id = getclient(self=self)
        if client_id != 'null':
            intern_id = Hierarchy.objects.filter(manager_id=client_id)
            dict2 = EmpClientIDSerializers(intern_id, many=True).data
            internsum = []

            if dict2:

                for i in range(len(dict2)):
                    internid = dict2[i]['client_id']
                    query = Employee.objects.filter(client_id=internid)
                    interndetail = SearchSerializer(query, many=True).data
                    junior = Hierarchy.objects.filter(manager_id=internid)
                    dict3 = EmpClientIDSerializers(junior,  many=True).data

                    if dict3:

                        junior_id = dict3[0]['client_id']
                        juniordetails = Employee.objects.filter(client_id=junior_id)

                        for j in range(len(dict3)):
                            juniorid = dict3[j]['client_id']
                            juniors = juniordetails | Employee.objects.filter(client_id=juniorid)
                            interndetail[0].update({'children': SearchSerializer(juniors, many=True).data})
                        internsum = internsum.__add__(interndetail)

                    else:
                        internid = dict2[0]['client_id']
                        intern = Employee.objects.filter(client_id=internid)
                        for i in range(len(dict2)):
                            intern_id = dict2[i]['client_id']
                            interns = intern | Employee.objects.filter(client_id=intern_id)
                        interndetail = SearchSerializer(interns, many=True).data
                        return interndetail
                return internsum

            elif dict2 is None:
                content = {'error': 'No Data Found.'}
                return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'error': 'No Data Found.'}
            return Response(content, status=status.HTTP_204_NO_CONTENT)

    def list(self, *args):

        senior_set = self.get_senior()
        manager_set = self.get_manager()
        user_set = self.get_queryset()
        intern_set = self.get_junior()
        user = SearchSerializer(user_set, many=True).data

        if intern_set is not None:
            user[0].update({'children': intern_set})

            if senior_set and manager_set:
                senior = SearchSerializer(senior_set, many=True).data
                manager = SearchSerializer(manager_set, many=True).data

                if senior and manager:

                    manager[0].update({'children': user})
                    senior[0].update({'children': manager})
                    return Response(senior, status=status.HTTP_200_OK)

            elif manager_set:
                manager = SearchSerializer(manager_set, many=True).data
                manager[0].update({'children': user})
                return Response(manager, status=status.HTTP_200_OK)

            elif not senior_set and not manager_set:
                return Response(user, status=status.HTTP_200_OK)

            else:
                manager = SearchSerializer(manager_set, many=True).data
                manager[0].update({'children': user})
                return Response(manager, status=status.HTTP_200_OK)

        if senior_set and manager_set:
            senior = SearchSerializer(senior_set, many=True).data
            manager = SearchSerializer(manager_set, many=True).data

            if senior and manager:

                manager[0].update({'children': user})
                senior[0].update({'children': manager})
                return Response(senior, status=status.HTTP_200_OK)

            elif manager:
                manager[0].update({'children': user})
                return Response(manager, status=status.HTTP_200_OK)

            elif not senior and not manager:
                return Response(user, status=status.HTTP_200_OK)

        elif manager_set:
            manager = SearchSerializer(manager_set, many=True).data
            manager[0].update({'children': user})
            return Response(manager, status=status.HTTP_200_OK)

        else:
            return Response(user, status=status.HTTP_200_OK)
