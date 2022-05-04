from django.shortcuts import render
from .models import FacultyModel
from django.http import HttpResponseRedirect
from .forms import FacEditForm


# Create your views here

def index(request):
    faculty = FacultyModel.objects.all()
    context = {'faculty': faculty} 
    return render(request, "index.html", context ) 

def research_category(request, r_cat):
    # get list of faculty that have a matching research category 'r_cat'
    faculty = FacultyModel.objects.filter(researchTypes__title__contains=r_cat)
    context = {'faculty': faculty, 'r_cat': r_cat}
    return render(request, 'research_category.html', context)

# (Modal view) when a faculty is clicked on
def fac_detail(request, fac_pk):
    faculty = FacultyModel.objects.get(pk=fac_pk)
    return render(request, "fac_detail.html", {'faculty':faculty, 'fac_pk':fac_pk})

# login through ldap
def fac_login(request):
    return render(request, "fac_login.html")



def fac_edit(request, fac_pk):
    # ***** require LDAP authentication for logging in. 

    # specific faculty that we editing
    fac = FacultyModel.objects.get(pk=fac_pk)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = FacEditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            fac.name = form.cleaned_data["name"]
            fac.title = form.cleaned_data["title"]
            fac.email = form.cleaned_data["email"]
            fac.phone = form.cleaned_data["phone"]
            fac.address = form.cleaned_data["address"]
            fac.heading = form.cleaned_data["heading"]
            fac.website = form.cleaned_data["website"]
            # **ADD processing of QR code of website
            fac.researchTypes = form.cleaned_data["researchTypes"]
            fac.bio = form.cleaned_data["bio"]
            fac.customIMG = form.cleaned_data["customIMG"]

            fac.edited = True
            fac.save()
            # redirect home
            return HttpResponseRedirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FacEditForm()
    
    return render(request, "fac_edit.html", {'form': form, 'faculty': fac})
