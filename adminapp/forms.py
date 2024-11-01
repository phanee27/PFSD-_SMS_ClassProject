from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

from .models import StudentList

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name','user']

class UploadFileForm(forms.Form):
    file = forms.FileField()


from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']
