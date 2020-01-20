from django import forms
from .models import Semester


# class AddSemesterForm(forms.ModelForm):

#     class Meta:
#         model = Semester
#         fields = ['name']
#         labels = {
#             'name': 'نام نیمسال',
#         }

#     def __init__(self, *args, **kwargs):
#         super(AddSemesterForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs['class'] = 'form-control'


# class AdvertisementForm(forms.ModelForm):

#     ad1 =  forms.
