# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *

class ResearchCategoryForm(form.ModelForm):
    class Meta:
        model = ResearchCategory
        fields = ['title']
        

class FacEditForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, required=False)                           # name
    title = forms.CharField(label='Job Title', max_length=60, required=False)                           # job title
    email = forms.CharField(label='Work email', max_length=60, required=False)                          # email
    phone = forms.CharField(label='Phone', max_length=15, required=False)                               # phone 
    address = forms.CharField(widget=forms.Textarea, label='Building, room number', required=False)
    website = forms.CharField(label='Website', required=False)                                          # link to their .cs.odu.edu website
    researchTypes = forms.ModelChoiceField(label='Research Categories', queryset=ResearchCategory.objects.all(), required=False)         # research types
    bio = forms.CharField(label='Bio, research, etc.', widget=forms.Textarea, required=False)                                          # personal biography, research, etc.
    customIMG = forms.ImageField(label='Profile Pic', required=False)                                                          # custom image upload by faculty
    

    def __init__(self, *args, **kwargs):
        super(FacEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Faculty'))

    
class FacultyForm(forms.ModelForm):

    class Meta:
        model = FacultyModel
        fields = ['name', 'title', 'email', 'phone', 'address', 'researchTypes' 'website', 'researchTypes', 'bio', 'pic']