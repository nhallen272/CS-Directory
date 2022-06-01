from urllib.request import Request
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .models import FacultyModel
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import FacEditForm, FacultyForm
import logging


def login(request):
    return render(request, 'login/login.html')


def index(request):
    faculty = FacultyModel.objects.order_by('name')
    context = {'faculty': faculty} 
    return render(request, "index.html", context) 

def research_category(request, r_cat):
    # get list of faculty that have a matching research category 'r_cat'
    faculty = FacultyModel.objects.filter(researchTypes__title__contains=r_cat)
    context = {'faculty': faculty, 'r_cat': r_cat}
    return render(request, 'research_category.html', context)

# (Modal view) when a faculty is clicked on
def fac_detail(request, fac_pk):
    faculty = FacultyModel.objects.get(pk=fac_pk)
   
    return render(request, "fac_detail.html", {'faculty':faculty, 'fac_pk':fac_pk})

def welcome(request, text=""):
    logger = logging.getLogger('editing')
    if request.user.is_authenticated:
        user = request.user
        if FacultyModel.objects.filter(email=user.email).exists():
            fac = FacultyModel.objects.filter(email=user.email)
            logger.info("Found Existing FacultModel: {}".format(fac.name))
        
        else:
            # create new  facultymodel if it doesn't exist
            facname = user.first_name + " " + user.last_name
            fac = FacultyModel(email=user.email, name=facname)
            fac.save()
            logger.info("Created new FacultyModel")
    
        logger.info("Login Success: {} ".format(user.email))
        return render(request, "welcome.html", {'fac':fac, 'user':request.user, 'text': text})
    
    else:
        logger.info("Login Failed")
        return redirect('/accounts/login')
        
    

def fac_edit(request, fac_pk):
    logger = logging.getLogger('editing')
    if request.user.is_authenticated:
        user = request.user
        fac = FacultyModel.objects.get(fac_pk)
            
        if request.method == 'POST':
            logger.info("Form POST")
            form = FacEditForm(request.POST, request.FILES)
            if form.is_valid():
                fac.pic = form.cleaned_data["customIMG"]
                fac.name = form.cleaned_data["name"]
                fac.title=form.cleaned_data["title"] 
                fac.email = user.email 
                fac.phone = form.cleaned_data["phone"]
                fac.website = form.cleaned_data["website"]
                fac.address = form.cleaned_data["address"]  
                fac.bio = form.cleaned_data["bio"]
                fac.researchTypes = form.cleaned_data["researchTypes"]
                fac.edited=True
                
                fac.save()
                form.save()
            # redirect home
            return HttpResponseRedirect('welcome', text="Successfully Edited!")

        # if a GET (or any other method) we'll create a blank form
        else:
            form = FacEditForm()
            return render(request, "fac_edit.html", {'form': form, 'faculty': fac})


    else:
        render(request, "edit_unauthed.html", {})


class FacEditView(UpdateView):
    model = FacultyModel
    form_class = FacEditForm
    fields = ['name', 'title', 'email', 'phone', 'address', 'researchTypes' 'website', 'researchTypes', 'bio', 'pic']
    template_name = "fac_edit.html"
    success_url = reverse_lazy('welcome', 'Successfully Edited')