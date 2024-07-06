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

Name_Profession = ""
Descreption = ""
Parents = ""
DOB = ""
Spouse = ""
Children = ""
Nationality = ""
twitter = ""
total_data = ""
links = []
Name = ""

def About_user(user,Headless):
    global Descreption, Name, twitter, Name_Profession, DOB, Spouse, Children, Nationality, Parents, total_data, links, Name
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver.get(f"https://www.google.com/search?q={user}")
    try:
        time.sleep(2)
        correct = driver.find_element(By.ID,'fprsl')
        Name = correct.text
        print(Name)
        correct.click()
        time.sleep(2)
    except Exception as e:
        print("not found")

    try:
        try:

            name = driver.find_elements(By.CLASS_NAME,'yKMVIe')
            for i in name:
                Name_Profession = Name_Profession + i.text
            name = driver.find_elements(By.CLASS_NAME, 'EGmpye')
            for i in name:
                Name_Profession = Name_Profession+ "," + i.text


        except Exception as e:
            print(e)
        try:
            Descrip = driver.find_elements(By.CLASS_NAME,'kno-rdesc')
            for i in Descrip:
                Descreption = i.text

        except Exception as e:
            print("No descreption")

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



        except Exception as e:
            print(e)
        try:

            de = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="rhs"]')))
            total_data = de.text

        except Exception as e:
            print(e)

        try:
            LINKS = ['YouTube','Twitter','Instagram','Facebook','Spotify','Deezer']
            for i in range(len(LINKS)):
                Links_hyper = driver.find_element(By.LINK_TEXT, LINKS[i])
                LINks = Links_hyper.get_attribute('href')
                links.append(LINks)

        except Exception as e:
            print(e)

        try:
            Twitter_hyper = driver.find_element(By.LINK_TEXT, "Twitter")
            Twitter_link = Twitter_hyper.get_attribute('href')
            print(Twitter_link)
            for i in range(20,len(Twitter_link)):
                twitter = twitter+ Twitter_link[i]
            print(twitter)

        except Exception as e:
            print(e)


    except Exception as e:
        print("About page not displayed")

    print("Descrition", Descreption,type(Descreption))
    print("Name", Name_Profession,type(Name_Profession))
    print("Parents",Parents,type(Parents))
    print("date of birth", DOB,type(DOB))
    print("Spouse", Spouse, type(Spouse))
    print("Children", Children, type(Children))
    print("Nationality", Nationality, type(Nationality))
    print("Links ", links, type(links))

    return Descreption, Name_Profession, Parents, DOB, Spouse, Children, Nationality, total_data


def image(user,path_save):
    driver.get(f"https://www.google.com/search?q={user}+portrait&tbm=isch")
    for i in range(1,6):
        print(i)
        Image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')))
        links = Image.get_attribute('src')
        data = urllib.request.urlretrieve(links, f'{path_save}/{user}{i}.png')
    return path_save

def make_dir(user):
    newpath = f'UsersData\{user}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

def keywords(Text):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    try:    
        Text1 = Text.split('\n')
        sentence = Text1[1].replace("Wikipedia","")
        text = sentence
        #text = "Imran Ahmed Khan Niazi HI PP is a Pakistani politician and former cricket captain who served as the 22nd Prime Minister of Pakistan from August 2018 until April 2022, when he was ousted through a no-confidence motion in the National Assembly. He is the founder and chairman of Pakistan Tehreek-e-Insaf."
        #doc = nlp(text)
        doc = nlp(Text)

        key_phrases = []

        for chunk in doc.noun_chunks:
            if len(chunk) > 1:
                key_phrases.append(chunk.text)

        print(key_phrases)

        key_phrases1 = [chunk.text for chunk in doc.noun_chunks]

        # Print the key phrases
        print(key_phrases1)

        import yake
        doc = Text
        kw_extractor = yake.KeywordExtractor()
        keywords = kw_extractor.extract_keywords(doc)
        for kw in keywords:
            print(kw)

        return(key_phrases, key_phrases1)
    except Exception as e:
        print('--',e)

def designation(user,Headless):
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver.get(f"https://www.google.com/search?q={user}")

    try:
        time.sleep(2)
        correct = driver.find_element(By.ID,'fprsl')
        Name = correct.text
        print(Name)
        correct.click()
        time.sleep(2)
    except Exception as e:
        print("not found")

    driver.quit()

    try:
        time.sleep(2)
        Name = Name.upper()
        driver.get(f"https://en.wikipedia.org/wiki/{Name}")
        time.sleep(2)
        table = driver.find_element(By.CLASS_NAME,'wikitable')
        print(table.text)
        names = table.text.split('\n')
        namee = names[len(names)-1]
        return namee

    except Exception as e:
        print(e)

    driver.quit()
    

def affiliation(user,Text,Headless):
    import spacy

    # Load the pre-trained English language model
    nlp = spacy.load("en_core_web_sm")

    # Example text to analyze
    text = Text

    # Analyze the text with spaCy
    doc = nlp(text)

    # Extract company names
    companies = set([ent.text for ent in doc.ents if ent.label_ == "ORG"])

    # Print the results
    print(companies)

    if len(companies)==0:

        try:
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            #driver.get(f"https://en.wikipedia.org/wiki/{user}")
            time.sleep(2)
            company = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[2]/td/div[1]')
            if company.text == "Companies":
                companies = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[2]/td/ul[2]')
                print(companies.text)
            if company.text != "Companies":
                print("companies not mentioned")

        except Exception as e:
            print(e)
#user = "DG ISPR"
#path = make_dir(user)
#image(user,path)
#desc, Name, parents, dob, spouse, children, nationality, total_data1  = About_user(user,Headless)
Text='Imran Ahmed Khan Niazi HI(M) PP (Urdu: عمران احمد خان نیازی; born 5 October 1952) is a Pakistani politician and former cricket captain who served as the 22nd Prime Minister of Pakistan from August 2018 until April 2022, when he was ousted through a no-confidence motion in the National Assembly. He is the founder and chairman of Pakistan Tehreek-e-Insaf '
kewords2 = keywords(Text)
#designation(user,Headless)
#user1 = Name.split(',')

#affiliation(user1[0], desc ,Headless)

