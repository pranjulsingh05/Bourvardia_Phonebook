from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):  # Serializer for user_login API.

    class Meta:

        model = Employee
        fields = ('client_id', 'name', 'email', 'emp_id', 'image_url', )


class HomeSerializers(serializers.ModelSerializer):  # Serializer for home_view API.

    class Meta:

        model = Employee
        fields = ('name', 'emp_id', 'email', 'bio', 'image_url', 'git_id', 'link_id', 'slack_id', )


class ContactSerializers(serializers.ModelSerializer):  # Serializer for home_view API.

    class Meta:

        model = Employee
        fields = ('contact', )


class EmpClientIDSerializers(serializers.ModelSerializer):  # Serializer for user_update_view API.

    class Meta:
        model = Employee
        fields = ('client_id', )


class EmpSerializers(serializers.ModelSerializer):  # Serializer for user_view API.

    class Meta:
        model = Employee
        fields = ('name', 'email', 'contact', 'emp_id', 'slack_id', 'image_url', 'hobbies', 'bio', 'git_id', 'link_id', )


class SearchEmpSerializers(serializers.ModelSerializer):  # Serializer for user_view API.

    class Meta:
        model = Employee
        fields = ('name', 'email', 'emp_id', 'slack_id', 'image_url', 'hobbies', 'bio', 'git_id', 'link_id', )


class EmpUpdateSerializers(serializers.ModelSerializer):  # Serializer for user_update_view API.

    class Meta:
        model = Employee
        fields = ('contact', 'emp_id', 'slack_id', 'hobbies', 'bio', 'git_id', 'link_id', )


class EmpIDSerializers(serializers.ModelSerializer):  # Serializer for user_update_view API.

    class Meta:
        model = Employee
        fields = ('emp_id', )


class Designation_Client(serializers.ModelSerializer):

    class Meta:
        model = Employee_Designation
        fields = ('client_id', )


class Location_Client(serializers.ModelSerializer):

    class Meta:
        model = Employee_Location
        fields = ('client_id', )


class Language_Client(serializers.ModelSerializer):

    class Meta:
        model = Employee_Language
        fields = ('client_id', )


class Skill_Client(serializers.ModelSerializer):

    class Meta:
        model = Employee_Skill
        fields = ('client_id', )


class Project_Client(serializers.ModelSerializer):

    class Meta:
        model = Employee_Project
        fields = ('client_id', )


class Hierarchy_Client(serializers.ModelSerializer):

    class Meta:
        model = Hierarchy
        fields = ('client_id', )


class EmpDesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Employee_Designation
        fields = ('designation', )


class UpDateDesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = ('designation',)


class EmpLocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee_Location
        fields = ('location', )


class EmpSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee_Skill
        fields = ('skill', )


class EmpProSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee_Project
        fields = ('current_project', 'previous_project', )


class ProSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee_Project
        fields = ('current_project', )


class EmpLangSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee_Language
        fields = ('language', )


class EmpHierarchySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hierarchy
        fields = ('client_id', 'manager_id')


class SearchSerializer(serializers.ModelSerializer):  # Serializer for users_search API.

    class Meta:

        model = Employee
        fields = ('name', 'email', 'client_id', )


class HomePageSearch(serializers.ModelSerializer):

    class Meta:

        model = Employee
        fields = ('email', 'client_id', )


class NameSerializers(serializers.ModelSerializer):  # Serializer for home_view API.

    class Meta:

        model = Employee
        fields = ('name', )


class HierarchySerializers(serializers.ModelSerializer):  # Serializer for view_hierarchy API.

    class Meta:
        model = Hierarchy
        fields = ('manager_id', )


class LogoutSerializers(serializers.ModelSerializer):  # Serializer for user_logout API.

    class Meta:
        model = Employee
        fields = ('token',)


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('skill',)