# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *

class ResearchCatForm(forms.ModelForm):
    class Meta:
        model = ResearchCategory
        fields = ['title']

class FacultyForm(forms.Form):
    
    class Meta:
        model = FacultyModel
        fields = ['name', 'title', 'email', 'phone', 'heading', 'website', 'researchTypes', 'bio' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Faculty'))
        

class FacEditForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, required=False)                               # name
    title = forms.CharField(label='Job Title (Professor, Lecturer, etc.)', max_length=40, required=False)                              # job title
    email = forms.CharField(label='Work email', max_length=60, required=False)                             # email
    phone = forms.CharField(label='Phone', max_length=15, required=False)                                # phone 
    address = forms.CharField(widget=forms.Textarea, required=False)
    heading = forms.CharField(label='Heading', max_length=120, required=False)                              # status
    website = forms.URLField(label='Website (e.g. www.cs.odu.edu/~uname)', required=False)                                          # link to their .cs.odu.edu website
    researchTypes = forms.ModelChoiceField(label='Research Categories', queryset=ResearchCategory.objects.all(), required=False)         # research types
    bio = forms.CharField(label='Bio, research, etc.', widget=forms.Textarea, required=False)                                          # personal biography, research, etc.
    customIMG = forms.ImageField(label='Profile Pic', required=False)                                                          # custom image upload by faculty
    

    def __init__(self, *args, **kwargs):
        super(FacEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Faculty'))

    
