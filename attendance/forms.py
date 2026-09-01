from django import forms
from .models import Employee,Attendance

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = [
            "employee_code",
            "name",
            "email",
            "phone",
            "department",
            "designation",
            "joining_date",
            "is_active",
        ]
        widgets = {
            "joining_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                },
                format="%Y-%m-%d"
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }
    