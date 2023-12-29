from django import forms
from .models import *

# This is for employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

#this is for company
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

#class loginForm(forms.ModelForm):
    #class Meta:
        #model = Login
        #fields = "_all_"

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

class clientForm(forms.ModelForm):
    class Meta:
        model = clients
        fields = "__all__"

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"

class leaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = "__all__"