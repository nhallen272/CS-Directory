from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import FacultyModel
from django.views.generic import TemplateView, View
from django.core import serializers
from django.http import JsonResponse
#from .forms import FacEditForm

# Create your views here

def index(request):
    faculty = FacultyModel.objects.all()
    context = {'faculty': faculty} 

    return render(request, "index.html", context ) 

# (Modal view) when a faculty is clicked on
def fac_detail(request, fac_pk):
    faculty = FacultyModel.objects.get(pk=fac_pk)
    return render(request, "fac_detail.html", {'faculty':faculty})


def fac_edit(request, fac_pk):
    # require LDAP authentication for logging in. 
    faculty = FacultyModel.objects.get(pk=fac_pk)
    return render(request, "fac_edit.html", locals())




class IndexView(TemplateView):
    template_name = "index.html"


class FacView(View):
    def get(self, request):
        faculty = FacultyModel.objects.all()
        data = serializers.serialize('json', faculty)
        return JsonResponse({'data':data}, safe=False)