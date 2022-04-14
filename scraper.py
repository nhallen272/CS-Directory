#Scrape 
# Directory URL = https://odu.edu/compsci/directory
from asyncio.windows_events import NULL
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FacultyDisplay.settings")
import django
django.setup()

#from django.core.management import call_command
import requests
from bs4 import BeautifulSoup
from display.models import FacultyModel

CS_BASE_URL = "https://www.cs.odu.edu/"

class Faculty:
    def __init__(self, name, title, picURL, address, phone, email):
        self.name = name
        self.title = title
        self.pic = picURL
        self.address = address
        self.phone = phone
        self.email = email
        usernames = email.split("@")
        self.username = "~" + usernames[0]
        self.website = CS_BASE_URL + self.username 
    
    def print(self):
        print("Name {}".format(self.name))
        print("Title {}".format(self.title))
        print("Image URL {}".format(self.pic))
        print("Address {}".format(self.address))
        print("Phone {}".format(self.phone))
        print("Email {}".format(self.email))
        print("Username {}".format(self.username))
        print("Website {}".format(self.website))
        print(" ")

    def __eq__(self, other):
        return self.name == other.name




def main():
    directory_URL = "https://odu.edu/compsci/directory"
    page = requests.get(directory_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    raw_faclist1 = soup.find_all("section", {"class":"section profiles page basicpage clearfix grid-6 alpha layout-2"})
    raw_faclist2 = soup.find_all("section", {"class":"section profiles page basicpage clearfix grid-6 layout-2 omega"})
    
    # list of faculty
    FacList = []
    for fac in raw_faclist1:
        pic = fac.div.img['src']  #("div", class_="grid-2 faculty_listing no_margin_right")
        pic = "https://odu.edu" + pic
        name = fac.h3.text
        title, addr, phone = fac.ul.find_all("div")
        title = title.text
        addr = addr.text
        phone = phone.text
        email = fac.ul.find_all("li")
        email = email[1].text
        f = Faculty(name, title, pic, addr, phone, email)
        FacList.append(f)
        
    for fac in raw_faclist2:
        pic = fac.div.img['src']  #("div", class_="grid-2 faculty_listing no_margin_right")
        pic = "https://odu.edu" + pic
        name = fac.h3.text
        title, addr, phone = fac.ul.find_all("div")
        title = title.text
        addr = addr.text
        phone = phone.text
        email = fac.ul.find_all("li")
        email = email[1].text
        f = Faculty(name, title, pic, addr, phone, email)
        FacList.append(f)


#    heading = models.CharField(max_length=120, default=' ', null=True) # status
#    website = models.URLField(null=True)                               # link to their .cs.odu.edu website
#    research = models.ManyToManyField('ResearchCategory')              # research types
#    bio = models.TextField(default=' ', null=True)                     # personal biography, research, etc.
#    edited = models.BooleanField(default=False, null=True)

    # websites https://www.cs.odu.edu/~tkennedy
    for fac in FacList:
        fac.print()
        
        # check if already in DB
        if FacultyModel.objects.filter(name=fac.name).exists():
            print("Already Exists")
        else:
            facAdd = FacultyModel(title=fac.title, email=fac.email, phone=fac.phone, pic=fac.pic, name=fac.name, website=fac.website)
            facAdd.save()
            



    
  
if __name__ == "__main__":
    main()
