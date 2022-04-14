#Scrape 
# Directory URL = https://odu.edu/compsci/directory
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FacultyDisplay.settings")
import django
django.setup()

#from django.core.management import call_command
import requests
from bs4 import BeautifulSoup
from display.models import FacultyModel

class Faculty:
    def __init__(self, name, title, picURL, address, phone, email):
        self.name = name
        self.title = title
        self.pic = picURL
        self.address = address
        self.phone = phone
        self.email = email
    
    def print(self):
        print("Name {}".format(self.name))
        print("Title {}".format(self.title))
        print("Image URL {}".format(self.pic))
        print("Address {}".format(self.address))
        print("Phone {}".format(self.phone))
        print("Email {}".format(self.email))
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


    for fac in FacList:
        fac.print()
        # check if already in DB
        facAdd = FacultyModel(name=fac.name, )
        if ( )


    
  
if __name__ == "__main__":
    main()
