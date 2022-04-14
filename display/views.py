from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import FacultyModel

# Create your views here

def index(request):
    faculty = FacultyModel.objects.all()
    context = {'faculty': faculty}

    return render(request, "index.html", context )

# bootstrap (Modal?) when a faculty is clicked on
def fac_detail(request, fac_pk):
    faculty = FacultyModel.objects.get(pk=fac_pk)
    return render(request, "fac_detail.html", {'faculty':faculty})

def fac_edit(request, fac_pk):
    # require LDAP authentication for logging in. 
    faculty = FacultyModel.objects.get(pk=fac_pk)
    return render(request, "fac_edit.html",{'faculty':faculty})