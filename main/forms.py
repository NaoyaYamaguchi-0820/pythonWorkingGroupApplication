from django import forms
from .models import Employee

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'employeeNum',
            'lastName',
            'firstName',
            'lastKanaName',
            'firstKanaName',
            'phoneNumber',
            'email',
            'password',
            'checkedPassword',
            'birthday',
            'gender',
            'section',
            'jikoShokai',
        )

        widgets = {
            'gender': forms.RadioSelect()
        }
