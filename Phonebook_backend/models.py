from django.db import models


class Employee(models.Model):

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
        return self.name


class Designation(models.Model):

    designation_id = models.IntegerField(primary_key=True, auto_created=True)
    designation = models.CharField(max_length=70, null=True)

    def __str__(self):
        return self.designation


class Employee_Designation(models.Model):

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    designation = models.CharField(max_length=50, blank=True)

    def function(self):
        return self.designation


class Location(models.Model):

    location_id = models.IntegerField(primary_key=True, auto_created=True)
    location = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.location


class Employee_Location(models.Model):

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    location = models.CharField(max_length=100, blank=True)

    def function(self):
        return self.location


class Skill(models.Model):

    skill_id = models.IntegerField(primary_key=True, auto_created=True)
    skill = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.skill


class Employee_Skill(models.Model):

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    skill = models.CharField(max_length=200, blank=True)

    def function(self):
        return self.skill


class Project(models.Model):

    project_id = models.IntegerField(primary_key=True, auto_created=True)
    project = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.project


class Employee_Project(models.Model):

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    current_project = models.CharField(max_length=50, blank=True)
    previous_project = models.CharField(max_length=300, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    date = models.DateTimeField(auto_now=True)

    def function(self):
        return self.current_project


class Language(models.Model):

    language_id = models.IntegerField(primary_key=True, auto_created=True)
    language = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.language


class Employee_Language(models.Model):

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    language = models.CharField(max_length=200, blank=True)

    def function(self):
        return self.language


class Hierarchy(models.Model):

    client_id = models.CharField(primary_key=True, max_length=100, default=None)
    manager_id = models.CharField(max_length=150, null=True)

    def function(self):
        return self.manager_id

