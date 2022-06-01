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
            fac = FacultyModel.objects.get(email=user.email)
            logger.info("Found Existing FacultyModel")
        
        else:
            # create new  facultymodel if it doesn't exist
            facname = user.first_name + " " + user.last_name
            fac = FacultyModel.objects.create(email=user.email, name=facname)
            fac.save()
            logger.info("Created new FacultyModel")
    
        logger.info("Login Success")
        return render(request, "welcome.html", {'fac':fac, 'user':request.user, 'text': text})
    
    else:
        logger.info("Login Failed")
        return redirect('/accounts/login')
        
    

def fac_edit(request):
    logger = logging.getLogger('editing')
    if request.user.is_authenticated:
        user = request.user
        fac = FacultyModel.objects.get(email=user.email)
        #fac = FacultyModel.objects.get(fac_pk)
        logger.info("Editing Faculty {}".format(fac))
        
        if request.method == 'POST':
            logger.info("Form POST")
            form = FacEditForm(request.POST, request.FILES)
            if form.is_valid():
                pic = form.cleaned_data.get("pic")
                if pic:
                    fac.pic = pic
                    fac.hasCustomPic = True
                else:
                    fac.pic = "images/default_profile.png"
                    fac.hasCustomPic = True
                logger.info("image: {}".format(fac.pic.url))
                fac.name = form.cleaned_data["name"]
                logger.info("name: {}".format(fac.name))
                fac.title = form.cleaned_data["title"]
                logger.info("title: {}".format(fac.title)) 
                fac.email = user.email 
                logger.info("email: {}".format(fac.email))
                fac.phone = form.cleaned_data["phone"]
                logger.info("phone: {}".format(fac.phone))
                fac.website = form.cleaned_data["website"]
                logger.info("website: {}".format(fac.website))
                fac.address = form.cleaned_data["address"] 
                logger.info("adddress: {}".format(fac.address)) 
                fac.bio = form.cleaned_data["bio"]
                logger.info("bio: {}".format(fac.bio))
                research = form.cleaned_data["researchTypes"]
                logger.info("researchTypes: {}".format(research))
                fac.researchTypes.add(*[research])
                #fac.researchTypes.set(research)
                fac.edited=True
                
                fac.save()
                #form.save()
            # redirect to welcome page

            return redirect('welcome')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = FacEditForm()
            return render(request, "fac_edit.html", {'form': form, 'faculty': fac})


    else:
       return redirect('/accounts/login')


class FacEditView(UpdateView):
    model = FacultyModel
    form_class = FacEditForm
    fields = ['name', 'title', 'email', 'phone', 'address', 'researchTypes' 'website', 'researchTypes', 'bio', 'pic']
    template_name = "fac_edit.html"
    success_url = reverse_lazy('welcome', 'Successfully Edited')