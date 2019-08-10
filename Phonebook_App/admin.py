"""
importin
"""
from django.contrib import admin

from Phonebook_App.models import Employee, Designation, EmployeeDesignation

admin.site.register(Employee)
admin.site.register(Designation)
admin.site.register(EmployeeDesignation)
