import keyword
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
import mysql.connector
import re
#import face_recognition
import json
#import torch
import spacy

conn = mysql.connector.connect(
host="localhost",
    user="root",
password="Jaguar@123",
database="sql_false_flag")
cursor = conn.cursor()



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
global Path
warnings.filterwarnings("ignore", category=DeprecationWarning)
Path = 'C:\chromedriver.exe'
options = Options()
options.headless = False

def About_user(user,driver):
    global Descreption, Name, twitter, Name_Profession, DOB, Spouse, Children, Nationality, Parents, total_data, links, Name

    driver.get(f"https://www.google.com/search?q={user}")
    try:
        time.sleep(2)
        correct = driver.find_element(By.ID,'fprsl')
        Name = correct.text
        correct.click()
        time.sleep(2)
    except Exception as e:
        print("")

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

        LINKS = ['YouTube', 'Twitter', 'Instagram', 'Facebook', 'Spotify', 'Deezer']
        for i in range(len(LINKS)):
            try:
                    Links_hyper = driver.find_element(By.LINK_TEXT, LINKS[i])
                    LINks = Links_hyper.get_attribute('href')
                    links.append(LINks)

            except Exception as e:
                a=1
                                
        try:
            Twitter_hyper = driver.find_element(By.LINK_TEXT, "Twitter")
            Twitter_link = Twitter_hyper.get_attribute('href')
            for i in range(20,len(Twitter_link)):
                twitter = twitter+ Twitter_link[i]


        except Exception as e:
            print(e)


    except Exception as e:
        print("About page not displayed")

#    print("Descrition", Descreption,type(Descreption))
#    print("Name", Name_Profession,type(Name_Profession))
#    print("Parents",Parents,type(Parents))
#    print("date of birth", DOB,type(DOB))
#    print("Spouse", Spouse, type(Spouse))
#    print("Children", Children, type(Children))
#    print("Nationality", Nationality, type(Nationality))
#    print("Links ", links, type(links))
    #print('----------------------Google_knowledge_panel---------------------')
    #print(total_data)
    lines = total_data.split('\n')

    line_to_find = "Description"

    index_to_find = lines.index(line_to_find)

    line_to_get = lines[index_to_find + 1]

    About = line_to_get
    #print("--------------------------------------------")
    #print(About)
    original_string = About
    modified_string = original_string.replace('"', '')
    #print(modified_string)
    #print('----------------------Twitter Acount---------------------')
    #print( twitter)
    return modified_string,twitter

def image(user,path_save,driver):

    driver.get(f"https://www.google.com/search?q={user}+portrait&tbm=isch")

    for i in range(1,6):
        #print(i)
        Image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')))
        links = Image.get_attribute('src')
        data = urllib.request.urlretrieve(links, f'"{path_save}"/{user}{i}.png')
    return path_save

def make_dir(user):
    newpath = fr'UsersData\{user}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

def keywords(Text):

    nlp = spacy.load("en_core_web_sm")
    #Text1 = Text.split('\n')
    #sentence = Text1[1].replace("Wikipedia","")
    #text = sentence
    #text = "Imran Ahmed Khan Niazi HI PP is a Pakistani politician and former cricket captain who served as the 22nd Prime Minister of Pakistan from August 2018 until April 2022, when he was ousted through a no-confidence motion in the National Assembly. He is the founder and chairman of Pakistan Tehreek-e-Insaf."
    doc = nlp(Text)

    key_phrases = []

#    for chunk in doc.noun_chunks:
#        if len(chunk) > 1:
#            key_phrases.append(chunk.text)

#    print(key_phrases)

    key_phrases1 = [chunk.text for chunk in doc.noun_chunks]

    # Print the key phrases
    #print(key_phrases1)

#    import yake
#    doc = Text
#    kw_extractor = yake.KeywordExtractor()
#    keywords = kw_extractor.extract_keywords(doc)
#    for kw in keywords:
#        print(kw)

#    return(key_phrases, key_phrases1)
    return(key_phrases1)

def Wikipedia_scraper(link,driver,user):
    global Descreption,twitter
    
    driver.get(link)
   # time.sleep(3)
    try:
        time.sleep(2)
        Descreption1 = WebDriverWait(driver,12).until(EC.presence_of_element_located((By.CLASS_NAME,'infobox')))
        Descreption = Descreption1.text
        #print("------------------------------------------------wikipedia box--------------------------------------")
        #print(Descreption)
    except Exception as e:
        for i in Descreption:
            print(i.text)
    Descreption = ""
    for i in range(2,3):
        Paragraph = driver.find_element(By.XPATH,f'//*[@id="mw-content-text"]/div[1]/p[{i}]')
        Descreption = Descreption + '\n' + Paragraph.text
    #print("---------------------------------------------------wikipedia paragraph------------------------------------")
    #print(Descreption)
    try:
        username = driver.find_element(By.CLASS_NAME,'mw-page-title-main')
        #print(username.text)

    except Exception as e:
        print(e)
    return(About_user(username.text,driver))



import random

#---------------------------------------------------------------------------------------------------#
def OSINT():
    try:
        driver = webdriver.Chrome(Path, options=options)
    except Exception as e:
        print('Please Check your Internet Connection!!')
    query="select Username from Groups1_Info;"
    cursor.execute(query)
    Username=cursor.fetchall()

    #print(Groups[0])
    Username_List=[]
    for usernames in Username:
        usernames=usernames[0][1:]
        Username_List.append("@"+usernames)
    #print(Username_List)
    User_Dict={}
    Main_List=[]
    Full_name=[]
    for user in Username_List:
        query=f"select keywords from Groups1_Info where Username='{user}';"
        cursor.execute(query)
        keywords=list(cursor.fetchall())
        query=f"select Usernames from Groups1_Info where Username='{user}';"
        cursor.execute(query)
        Groups=cursor.fetchall()
        query=f"select Keywords from Groups1_Info where Username='{user}';"
        cursor.execute(query)
        Keys=cursor.fetchall()
        keywords_list=[]
        for info in Keys:
            info = str(info)
            #print(info)
            str1=''
            for ii in info:
                str1=str1+''+ii  
                #print(str1)
                if ii == ',':
                    str1=str1.replace('\n','')
                    pattern = r'[^a-zA-Z0-9]+'
                    str1 = re.sub(pattern, '', str1)
                    #print(str1)
                    keywords_list.append(str1)
                    str1=''
#---------------------------------------------------------------------------------------------------#        
        query=f"select Fullname from UsersProfile_Temp where Username='{user}';"
        cursor.execute(query)
        Fullname=cursor.fetchone()
#---------------------------------------------------------------------------------------------------#
        User_Dict={'Username':user,'Groups':Groups,'Fullname':Fullname,'Keys':keywords_list}
        Main_List.append(User_Dict)
    #print(Main_List)
#---------------------------------------------------------------------------------------------------#                
    finaldict=[]
    flag12=0
    #---------------------------------------------------------------------------------------------------#
    global Descreption, Name, twitter, Name_Profession, DOB, Spouse, Children, Nationality, Parents, total_data, links, Name
    for i,USER in enumerate(Main_List):
         # YAHAN PE YE KAR SKTE HAIN K AGAR 
            ## ye loop khtam karri Keys wala
            #User_Pics = make_dir(user)
        user=''
        links=''
        found=False
        twitter=''
        Descreption=''
        #print(USER['Fullname'])
        try:
            user='  '+ USER['Fullname'][0]+' '+USER['Username']+' '+'Wikipedia'
            #print(user
            try:
                driver.get(f"https://www.google.com/search?q={user}")
            except Exception as e:
                print('Please Check your Internet Connection!!')
            time.sleep(3)
            flag = 1
            #---------------------------------------------------------------------------------------------------#
            try:
                time.sleep(2)
                Descreption = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rhs"]'))).text
                In_there = "Description" in Descreption
                if In_there:
                    flag = 1
                    #print("---------------------------------------------------Scraping Google knowledge panel--------------------------------------------------------------")
                    #print(Descreption)
                    lines = Descreption.split('\n')
                    line_to_find = "Description"
                    index_to_find = lines.index(line_to_find)
                    line_to_get = lines[index_to_find + 1]
                    About = line_to_get
                    #print("-----------------------------------------------------About--------------------------------------------------------------------------------------")
                    #print(About)
                    original_string = About
                    modified_string = original_string.replace('"', '')
                    #print(modified_string)
                    try:
                        Twitter_hyper = driver.find_element(By.LINK_TEXT, "Twitter")
                        Twitter_link = Twitter_hyper.get_attribute('href')
                        print(Twitter_link)
                        for i in range(20, len(Twitter_link)):
                            twitter = twitter + Twitter_link[i]
                        #print("--------------------------------------------------------------Twitter account---------------------------------------")
                        #print(twitter)
                    except Exception as e:
                        print(e)
                    LINKS = ['YouTube', 'Twitter', 'Instagram', 'Facebook']
                    for i in range(len(LINKS)):
                        try:
                            Links_hyper = driver.find_element(By.LINK_TEXT, LINKS[i])
                            LINks = Links_hyper.get_attribute('href')
                            links.append(LINks)
                        except Exception as e:
                            print(e)
                    #---------------------------------------------------------------------------------------------------#
                else:
                    flag = 0
                if flag == 0:
                    #print("Scraping Wikipedia")
                    time.sleep(2)
                    Wikipedia = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
                    #print(Wikipedia.get_attribute('href'))
                    Wikipedia_scraper(Wikipedia.get_attribute('href',driver,user))
                    #---------------------------------------------------------------------------------------------------#
            except Exception as e:
                try:
                    time.sleep(2)
                    Wikipedia = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
                    modified_string,twitter = Wikipedia_scraper(Wikipedia.get_attribute('href'),driver,user)
                except:    
                    continue
                #---------------------------------------------------------------------------------------------------#
            try:
                if '/' in twitter:
                    twitter = twitter.split("/")[-1]
                dict1={'Description':modified_string,'Real_Account':twitter }
                for dict12 in finaldict:
                    if dict12.get("Real_Account") == twitter :
                        found = True
                if found==False:
                    Fullname = modified_string.split("is", 1)[0].strip()
                    query="insert into Feed_Back_Groups1_Info (`Fullname`,`description`,`ID_twitter`,`User_Pics`) VALUES(%s,%s,%s,%s)"
                    values=(Fullname,modified_string,twitter," ")
                    cursor.execute(query,values)
                    conn.commit()
                    finaldict.append(dict1)
                    #---------------------------------------------------------------------------------------------------#                    
            except Exception as e:
                print(e)
            user=''
        except Exception:    
            print(Exception)         
            #---------------------------------------------------------------------------------------------------#
    #print(finaldict)

    #return 0#finaldict aarhi hai.

##notes tu ne hi lgawya wa hai. idhra hi hun 
##when onve clicked dont click again
##name check

# description feedback mein aik issue aarha hai. haan sai hai..






#user = "Christiano Ronaldo"
#path = make_dir(user)
#image(user,path)
#
#Description,Twitter=About_User1("Imran khan Former Prime minister", Headless= True)
#print(Description,Twitter)
#OSINT()
