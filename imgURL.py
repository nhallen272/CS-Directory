import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FacultyDisplay.settings")
import django

django.setup()
from display.models import FacultyModel


for fac in FacultyModel.objects.all():
     if fac.pic.url == "/media/https%3A/odu.edu/content/dam/odu/faculty-staff/person-placeholder-2015.png/_jcr_content/renditions/cq5dam.thumbnail.319.319.png":
         fac.pic = "images/default_profile.png"
         fac.save()
         
         
