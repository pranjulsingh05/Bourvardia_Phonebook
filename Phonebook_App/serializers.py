# pylint: disable=too-few-public-methods


"""
Import Rest Framework & from models.py import all the classes
"""
from rest_framework import serializers

from Phonebook_App.models import EmployeeLocation, Employee, EmployeeProject, EmployeeSkill,\
                                     EmployeeLanguage, EmployeeDesignation,\
                                     Hierarchy, Skill, Designation


class UserSerializers(serializers.ModelSerializer):  # Serializer for user_login API.
    """
        This serializers contain the model employee
        that have 5 fields at UserLogin.
    """

    class Meta:
        """
            This meta class is of UserSerializers class
        """

        model = Employee
        fields = ('client_id', 'name', 'email', 'emp_id', 'image_url', )


class HomeSerializers(serializers.ModelSerializer):  # Serializer for home_view API.
    """
        This serializers contain the model employee
        that have 8 fields for HomePage.
    """

    class Meta:
        """
            This meta class is of HomeSerializers class
        """

        model = Employee
        fields = ('name', 'emp_id', 'email', 'bio', 'image_url', 'git_id', 'link_id', 'slack_id',)


class ContactSerializers(serializers.ModelSerializer):  # Serializer for home_view API.
    """
        This serializers contain the model employee
        that have 1 fields for Homepage.
    """

    class Meta:
        """
            This meta class is of ContactSerializers class
        """

        model = Employee
        fields = ('contact', )


class EmpClientIDSerializers(serializers.ModelSerializer):  # Serializer for user_update_view API.
    """
        This serializers contain the model employee
        that have 1 fields.
    """

    class Meta:
        """
            This meta class is of EmpClientIDSerializers class
        """

        model = Employee
        fields = ('client_id', )


class EmpSerializers(serializers.ModelSerializer):  # Serializer for user_view API.
    """
        This serializers contain the model employee
        that have 10 fields for User_detail.
    """

    class Meta:
        """
            This meta class is of EmpSerializers class
        """
        model = Employee
        fields = ('name', 'email', 'contact', 'emp_id',
                  'slack_id', 'image_url', 'hobbies', 'bio', 'git_id', 'link_id', )


class SearchEmpSerializers(serializers.ModelSerializer):  # Serializer for user_view API.
    """
        This serializers contain the model employee
        that have 9 fields for Searched_User_detail.
    """

    class Meta:
        """
            This meta class is of SearchEmpSerializers class
        """
        model = Employee
        fields = ('name', 'email', 'emp_id', 'slack_id', 'image_url',
                  'hobbies', 'bio', 'git_id', 'link_id', )


class EmpUpdateSerializers(serializers.ModelSerializer):  # Serializer for user_update_view API.
    """
        This serializers contain the model employee
        that have 7 fields for User_Update_view.
    """

    class Meta:
        """
            This meta class is of EmpUpdateSerializers class
        """
        model = Employee
        fields = ('contact', 'emp_id', 'slack_id', 'hobbies', 'bio', 'git_id', 'link_id', )


class EmpIDSerializers(serializers.ModelSerializer):  # Serializer for user_update_view API.
    """
         This serializers contain the model employee
         that have 1 fields for EmpId need.
    """

    class Meta:
        """
            This meta class is of EmpIDSerializers class
        """
        model = Employee
        fields = ('emp_id', )


class UserDesignation(serializers.ModelSerializer):
    """
         This serializers contain the model EmployeeDesignation
         that have 1 fields for Designation of user.
    """

    class Meta:
        """
            This meta class is of DesignationClient class
        """
        model = EmployeeDesignation
        fields = ('client_id', )


class UserLocation(serializers.ModelSerializer):
    """
        This serializers contain the model EmployeeLocation
        that have 1 fields for location of user.
    """

    class Meta:
        """
            This meta class is of UserLocation class
        """
        model = EmployeeLocation
        fields = ('client_id', )


class UserLanguage(serializers.ModelSerializer):
    """
        This serializers contain the model EmployeeLanguage
        that have 1 fields for language of user.
    """

    class Meta:
        """
            This meta class is of Userlanguage class
        """
        model = EmployeeLanguage
        fields = ('client_id', )


class UserSkill(serializers.ModelSerializer):
    """
         This serializers contain the model EmployeeSkill
         that have 1 fields for Tech_skill of user.
    """

    class Meta:
        """
            This meta class is of UserSkill class
        """
        model = EmployeeSkill
        fields = ('client_id', )


class UserProject(serializers.ModelSerializer):
    """
        This serializers contain the model EmployeeProject
        that have 1 fields for Tech_skill of user.
    """

    class Meta:
        """
            This meta class is of UserProject class
        """
        model = EmployeeProject
        fields = ('client_id', )


class HierarchyClient(serializers.ModelSerializer):
    """
        This serializers contain the model Hierarchy
        that have 1 fields for Tech_skill of user.
    """

    class Meta:
        """
            This meta class is of Hierarchy class
        """
        model = Hierarchy
        fields = ('client_id', )


class EmpDesSerializer(serializers.ModelSerializer):
    """
      This serializers contain the model EmployeeDesignation
      that have 1 fields for Emp_designation of user.
    """

    class Meta:
        """
            This meta class is of EmpDesSerializers class
        """
        model = EmployeeDesignation
        fields = ('designation', )


class UpDateDesSerializer(serializers.ModelSerializer):
    """
      This serializers contain the model Designation
      that have 1 fields for Emp_designation of user.
    """

    class Meta:
        """
            This meta class is of UpDateDesSerializer class
        """
        model = Designation
        fields = ('designation',)


class EmpLocSerializer(serializers.ModelSerializer):
    """
      This serializers contain the model EmployeeLocation
      that have 1 fields for Emp_location of user.
    """

    class Meta:
        """
            This meta class is of EmpLocSerializers class
        """
        model = EmployeeLocation
        fields = ('location', )


class EmpSkillSerializer(serializers.ModelSerializer):
    """
        This serializers contain the model EmployeeSkill
        that have 1 fields for Emp_Skill of user.
    """

    class Meta:
        """
            This meta class is of EmpSkillSerializers class
        """
        model = EmployeeSkill
        fields = ('skill', )


class EmpProSerializer(serializers.ModelSerializer):
    """
        This serializers contain the model EmployeeProject
        that have 2 fields for Emp_Project of user.
    """

    class Meta:
        """
            This meta class is of EmpProSerializers class
        """
        model = EmployeeProject
        fields = ('current_project', 'previous_project', )


class ProjectSerializer(serializers.ModelSerializer):
    """
        This serializers contain the model EmployeeProject
        that have 1 fields for Emp_Project of user.
    """

    class Meta:
        """
            This meta class is of ProjectSerializers class
        """
        model = EmployeeProject
        fields = ('current_project', )


class EmpLangSerializer(serializers.ModelSerializer):
    """
        This serializers contain the model EmployeeLanguage
        that have 1 fields for Emp_language of user.
    """

    class Meta:
        """
            This meta class is of EmpLangSerializers class
        """
        model = EmployeeLanguage
        fields = ('language', )


class EmpHierarchySerializer(serializers.ModelSerializer):
    """
        This serializers contain the model Hierarchy
        that have 2 fields for Emp_Hierarchy of user.
    """

    class Meta:
        """
            This meta class is of EmpHierarchySerializers class
        """
        model = Hierarchy
        fields = ('client_id', 'manager_id')


class SearchSerializer(serializers.ModelSerializer):  # Serializer for users_search API.
    """
        This serializers contain the model Employee
        that have 3 fields for Emp_search of user.
    """

    class Meta:
        """
            This meta class is of SearchSerializers class
        """

        model = Employee
        fields = ('name', 'email', 'client_id', )


class HomePageSearch(serializers.ModelSerializer):
    """
       This serializers contain the model Employee
       that have 2 fields for Homepage of user.
    """

    class Meta:
        """
            This meta class is of HomePage class
        """

        model = Employee
        fields = ('email', 'client_id', )


class NameSerializers(serializers.ModelSerializer):  # Serializer for home_view API.
    """
       This serializers contain the model Employee
       that have 1 fields for Emp_name of user.
    """

    class Meta:
        """
            This meta class is of NameSerializers class
        """

        model = Employee
        fields = ('name', )


class HierarchySerializers(serializers.ModelSerializer):  # Serializer for view_hierarchy API.
    """
       This serializers contain the model Hierarchy
       that have 1 fields for Emp_manager_id of user.
    """

    class Meta:
        """
           This meta class is of HierarchySerializers class
        """

        model = Hierarchy
        fields = ('manager_id', )


class SkillSerializer(serializers.ModelSerializer):
    """
       This serializers contain the model Skill
       that have 1 fields for Emp_Skill of user.
    """

    class Meta:
        """
           This meta class is of SkillSerializers class
        """
        model = Skill
        fields = ('skill',)

# class LogoutSerializers(serializers.ModelSerializer):  # Serializer for user_logout API.
#     """
#        This serializers contain the model Employee
#        that have 1 fields for Emp_name of user.
#     """
#
#     class Meta:
#         model = Employee
#         fields = ('token',)

