from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import urllib
import urllib.request
import os
from selenium.webdriver.chrome.options import Options
import warnings


#import face_recognition
import json
import mysql.connector
#import torch

global Headless ,Path
Headless = True
Path = 'C:\chromedriver.exe'
options = Options()
    # this parameter tells Chrome that
    # it should be run without UI (Headless)
options.headless = Headless
# initializing webdriver for Chrome with our options
driver = webdriver.Chrome(Path, options=options)


def affiliation(user,Text,Headless):
    import spacy

    # Load the pre-trained English language model
    nlp = spacy.load("en_core_web_sm")
    text = Text
    doc = nlp(text)
    print(companies)
    if len(companies)==0:

        try:
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            #driver.get(f"https://en.wikipedia.org/wiki/{user}")
            company = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[2]/td/div[1]')
            if company.text == "Companies":
                companies = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[2]/td/ul[2]')
                print(companies.text)
            if company.text != "Companies":
                print("companies not mentioned")

        except Exception as e:
            print(e)
def designation():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
#    driver.get(f"https://www.google.com/search?q={user}")

    #try:
    #    time.sleep(2)
    #    correct = driver.find_element(By.ID,'fprsl')
    #    Name = correct.text
    #    print(Name)
    #    correct.click()
    #    time.sleep(2)
    #except Exception as e:
    #    print("not found")

    #driver.quit()

    try:
        time.sleep(2)
        #Name = Name.upper()
     #   driver.get(f"https://en.wikipedia.org/wiki/{Name}")
        #time.sleep(2)
        table = driver.find_element(By.CLASS_NAME,'wikitable')
        #print(table.text)
        names = table.text.split('\n')
        namee = names[len(names)-1]
        return namee

    except Exception as e:
        print(e)

    driver.quit()

def About_user(user,Headless):
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    global Descreption, Name, twitter, Name_Profession, DOB, Spouse, Children, Nationality, Parents, total_data, links, Name
    driver.get(f"https://www.google.com/search?q={user}")
    try:
        time.sleep(2)
        correct = driver.find_element(By.ID,'fprsl')
        Name = correct.text
        #print(Name)
        correct.click()
        time.sleep(2)
    except Exception as e:
        print("")

    try:
        FindAbout=driver.find_element_by_xpath('//*[@id="rhs"]')
        Wiki=driver.find_element_by_partial_link_text("Wikipedia")
        #print(FindAbout.text)
        if FindAbout:
            try:
            
                name = driver.find_elements(By.CLASS_NAME,'yKMVIe')
                for i in name:
                    Name_Profession = Name_Profession + i.text
                name = driver.find_elements(By.CLASS_NAME, 'EGmpye')
                for i in name:
                    Name_Profession = Name_Profession+ "," + i.text
    

            except Exception as e:
                print('Error in name: ',e)
                Name_Profession ='N/a'
            try:
                Descrip = driver.find_elements(By.CLASS_NAME,'kno-rdesc')
                for i in Descrip:
                    Descreption = i.text

            except Exception as e:
                print("No descreption")
                Descreption='N/a'
            try:
                desc = driver.find_elements(By.CLASS_NAME,'w8qArf')
                det = driver.find_elements(By.CLASS_NAME,'LrzXr.kno-fv.wHYlTd.z8gr9e')
                for i,j in zip(desc,det):

                    if i.text.startswith("Born"):
                        DOB = j.text+" " + DOB
                    if i.text.startswith("Spouse"):
                        Spouse = j.text + " " + Spouse
                    if i.text.startswith("Children"):
                        Children = j.text + " " + Children
                    if i.text.startswith("Nationality"):
                        Nationality = j.text + "" + Nationality
                    if i.text.startswith("Parents"):
                        Parents = j.text + " " + Parents
                elements = driver.find_elements_by_class_name("wDYxhc")
                for element in elements:
                    text = element.text
                    print(text)
            except Exception as e:
                print('No Family Info Provided',e)
                Parents='N/a'
                Nationality ='N/a'
                Children ='N/a'
                Spouse ='N/a'
                DOB='N/a'
                elements = driver.find_elements_by_class_name("wDYxhc")
                for element in elements:
                    text = element.text
                    print(text)
            try:
                de = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="rhs"]')))
                total_data = de.text
                print(total_data)
            except Exception as e:
                print('Error in De',e)
            try:
                links=[]
                Profiles=FindAbout.find_element_by_xpath('//div[@data-attrid="kc:/common/topic:social media presence"]')
                LINKS = ['YouTube','Twitter','Instagram','Facebook','Spotify','Deezer']
                for i in range(len(LINKS)):
                    try:
                        Links_hyper = Profiles.find_element(By.LINK_TEXT, LINKS[i])
                        LINks = Links_hyper.get_attribute('href')
                        links.append(LINks)
                    except:
                        links.append('N/a')
                #print(links)
            except Exception as e:
                print('Error in Links',e)
            try:
                twitter=''
                Twitter_hyper = driver.find_element(By.LINK_TEXT, "Twitter")
                Twitter_link = Twitter_hyper.get_attribute('href')
                #print(Twitter_link)
                for i in range(20,len(Twitter_link)):
                    twitter = twitter+ Twitter_link[i]
                print(Twitter_link)
            except Exception as e:
                print('Error in getting twitter link',e)
            try:    
                print("Descrition: ", Descreption,type(Descreption))
                print("Name", Name_Profession,type(Name_Profession))
                print("Parents",Parents,type(Parents))
                print("date of birth", DOB,type(DOB))
                print("Spouse", Spouse, type(Spouse))
                print("Children", Children, type(Children))
                print("Nationality", Nationality, type(Nationality))
                print("Links ", links, type(links))
                return Descreption, Name_Profession, Parents, DOB, Spouse, Children, Nationality, total_data    
            except Exception as e:
                print("Issue Somewhere",e)
        if Wiki:
            driver.execute_script("arguments[0].click();", Wiki)
            designation()
    except Exception as e:
        print("About page not displayed")
        Wiki=driver.find_element_by_partial_link_text("Wikipedia")
        #print(Wiki.text)
        driver.execute_script("arguments[0].click();", Wiki)
        designation()
About_user('Imran Khan former Prime Minister',Headless)
