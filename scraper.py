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
        pic = fac.div.img['src']  
        pic = "https://odu.edu" + pic
        name = fac.h3.text
        title_addr_ph = fac.ul.find_all("div")
        # if length of title_addr_phone is 3
        if len(title_addr_ph) == 3:
            title = title_addr_ph[0].text
            addr = title_addr_ph[1].text
            phone = title_addr_ph[2].text
        else:
            print("Title, Address, Phone contents:  ")
            print(title_addr_ph)   
        email = fac.ul.find_all("li")
        email = email[1].text
        f = Faculty(name, title, pic, addr, phone, email)
        FacList.append(f)
        
    for fac in raw_faclist2:
        pic = fac.div.img['src']  
        pic = "https://odu.edu" + pic
        name = fac.h3.text
        title_addr_ph = fac.ul.find_all("div")
        # if length of title_addr_phone is 3
        if len(title_addr_ph) == 3:
            title = title_addr_ph[0].text
            addr = title_addr_ph[1].text
            phone = title_addr_ph[2].text
        else:
            print("Name: ")
            print(name)
            print('\n')
            print(title_addr_ph)  
            
        email = fac.ul.find_all("li")
        email = email[1].text
        f = Faculty(name, title, pic, addr, phone, email)
        FacList.append(f)



    for fac in FacList:
        fac.print()
        
        # check if already in DB
        if FacultyModel.objects.filter(name=fac.name).exists():
            print("Already Exists \n Updating address")
            foundFac = FacultyModel.objects.get(name=fac.name)
            foundFac.address = fac.address
            foundFac.save()
        else:
            facAdd = FacultyModel(title=fac.title, email=fac.email, phone=fac.phone, pic=fac.pic, name=fac.name, website=fac.website, address=fac.address)
            facAdd.save()
            



if __name__ == "__main__":
    main()
