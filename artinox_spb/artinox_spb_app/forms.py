from django import forms
from django.core.exceptions import ValidationError

from  .models import *

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UsersTasks
        fields = ['fullname', 'email', 'tel', 'address', 'product_name', 'task_text', 'technical_task', 'technical_plan']

    def clean_fullname(self):
        fullname = self.cleaned_data['fullname']
        if len(fullname) > 255:
            raise ValidationError('поле ФИО не должно превышать 255 символов')
        return  fullname