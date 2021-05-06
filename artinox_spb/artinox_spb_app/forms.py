from django import forms
from  .models import *

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UsersContacts

        fields = ['fullname', 'email', 'tel', 'address', 'product_name', 'task_text', 'technical_task', 'technical_plan']