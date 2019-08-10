"""
    importing all the models from django.
"""
from django.db import models


class Employee(models.Model):
    """
    This Class Model is containing the Employee Model having all the basic detail
    of the employee.
    """

    client_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=10, blank=True)
    emp_id = models.CharField(max_length=15, blank=False, null=True, )
    slack_id = models.CharField(max_length=70, blank=True)
    image_url = models.CharField(max_length=250, blank=True)
    hobbies = models.CharField(max_length=250, blank=True)
    bio = models.CharField(max_length=1100, blank=True)
    git_id = models.CharField(max_length=100, blank=True)
    link_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """
        :return: Name of the employee
        """
        return self.name


class Designation(models.Model):
    """
       This Class Model is containing all the designation present
       in the organization.
    """

    designation_id = models.IntegerField(primary_key=True, auto_created=True)
    designation = models.CharField(max_length=70, null=True)

    def __str__(self):
        """
        :return: All the designation
        """
        return self.designation


class EmployeeDesignation(models.Model):
    """
      This Class Model is containing all the Employee designation present
      in the organization.
    """

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    designation = models.CharField(max_length=50, blank=True)

    def function(self):
        """
        :return: Employee-designation
        """
        return self.designation


class Location(models.Model):
    """
       This Class Model is containing all the location present
       in the organization.
    """

    location_id = models.IntegerField(primary_key=True, auto_created=True)
    location = models.CharField(max_length=200, null=True)

    def __str__(self):
        """
        :return: All the nineleaps Location
        """
        return self.location


class EmployeeLocation(models.Model):
    """
      This Class Model is containing all the Employee-Location present
      in the organization.
    """

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    location = models.CharField(max_length=100, blank=True)

    def function(self):
        """
        :return: Employee-Location from here he/she is working
        """
        return self.location


class Skill(models.Model):
    """
      This Class Model is containing all the Skill present
      in the organization.
    """

    skill_id = models.IntegerField(primary_key=True, auto_created=True)
    skill = models.CharField(max_length=100, null=True)

    def __str__(self):
        """
        :return: All the Skill present in the organization
        """
        return self.skill


class EmployeeSkill(models.Model):
    """
      This Class Model is containing all the Employee-Skill present
      in the organization.
    """

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    skill = models.CharField(max_length=200, blank=True)

    def function(self):
        """
        :return: employee-tech skill
        """
        return self.skill


class Project(models.Model):
    """
      This Class Model is containing all the Project present
      in the organization.
    """

    project_id = models.IntegerField(primary_key=True, auto_created=True)
    project = models.CharField(max_length=100, null=True)

    def __str__(self):
        """
        :return: All the nineleaps-projects
        """
        return self.project


class EmployeeProject(models.Model):
    """
      This Class Model is containing all the Employee-Project present
      in the organization.
    """

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    current_project = models.CharField(max_length=50, blank=True)
    previous_project = models.CharField(max_length=300, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def function(self):
        """
        :return: Employee-Project he/she has worked upon
        """
        return self.current_project


class Language(models.Model):
    """
      This Class Model is containing all the Language present
      in the organization.
    """

    language_id = models.IntegerField(primary_key=True, auto_created=True)
    language = models.CharField(max_length=150, null=True)

    def __str__(self):
        """
        :return: All the Language(nation) present in the organization
        """
        return self.language


class EmployeeLanguage(models.Model):
    """
      This Class Model is containing all the Employee-Language that
      they can speak in the organization.
    """

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    language = models.CharField(max_length=200, blank=True)

    def function(self):
        """
        :return: Employee-Language they can speak.
        """
        return self.language


class Hierarchy(models.Model):
    """
      This Class Model is containing all the Employee's --> Manager that are
      in the organization.
    """

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    manager_id = models.CharField(max_length=150, null=True)

    def function(self):
        """
        :return: User's--> manager_id
        """
        return self.manager_id
