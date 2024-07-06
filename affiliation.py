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
#import face_recognition
import json
import mysql.connector
#import torch
import spacy
import re
import pycountry


def Affilation(desc,path,driver):
#    regex = r"\b[A-Z][a-z](?: [A-Z][a-z])*(?:, Inc\.|, Ltd\.| Corporation| Corp\.| AG| SE)?\b"
    try:
        regex = r"\b[A-Z][a-z]*(?: [A-Z][a-z]*)*(?:, Inc\.|, Ltd\.| Corporation|founder|president| Corp\.| AG| SE)?\b"
        # Use re.findall() to extract all matches of the regular expression in the input string
        company_names = []
        list_to_search = []
        try:
            company_names_str = re.search(r'belonging to ([^.]+)\.', desc).group(1)
            company_names.append(company_names_str)
            list_to_search.append(company_names_str)

        except Exception as e:
            print("regex")
            company_names = re.findall(regex, desc)


        # Print the resulting list of company names
        print("company")
        print(company_names)


        for i in range(len(company_names)):
            if company_names[i] == "He":
                for r in range(i+1,len(company_names)):
                    list_to_search.append(company_names[r])
        print("list_to_search")
        print(list_to_search)
        list_to_search = list(set(list_to_search))
        try:
            list_to_search.remove("Inc")
        except Exception as e:
            df = 0
        try:
            list_to_search.remove("Wikipedia")
        except Exception as e:
            dfv = 0
        try:
            list_to_search.remove("Khan")
        except Exception as e:
            dfv = 0

        try:
            list_to_search.remove("Chief")
        except Exception as e:
            dfv = 0
        #-------------------------------------------

        countries = [country.name for country in pycountry.countries]

        for item in countries:
            if item in list_to_search:
                list_to_search.remove(item)

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December','Each']

        for items in months:
            if items in list_to_search:
                list_to_search.remove(items)



        print(list_to_search)
        for i in range(len(list_to_search)):
            image(list_to_search[i],path,driver,who = 0)
    except Exception as e:
        rf = 0
def make_dir(user):
    newpath = fr'C:\Users\Dell\OneDrive\Desktop\Osint\{user}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath
def Osint(user, path, Chrom_path, Headless):

    driver = webdriver.Chrome(r'C:\Users\Dell\Downloads\chromedriver_win32 (1)\chromedriver.exe')
    driver.get(f"https://www.google.com/search?q={user}")

    try:
        Descreption = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rhs"]'))).text
        In_there = "Description" in Descreption
        if In_there:
            flag = 1
            # print("---------------------------------------------------Scraping Google knowledge panel--------------------------------------------------------------")
            # print(Descreption)
            lines = Descreption.split('\n')
            line_to_find = "Description"
            index_to_find = lines.index(line_to_find)
            line_to_get = lines[index_to_find + 1]
            About = line_to_get

            line_to_find_1 = ""
            index_to_find = lines.index(line_to_find)
            line_to_get = lines[index_to_find + 1]
            About = line_to_get

            print(About)
            Affilation(About,path,driver)
            image(user,path,driver,who=1)

    except Exception as e:
        image(user, path, driver, who=1)

def image(user,path_save,driver,who):
    if who == 0:
        driver.get(f"https://www.google.com/search?q={user}&tbm=isch")
    if who ==1:
        driver.get(f"https://www.google.com/search?q={user}&tbm=isch")

    for i in range(1,3):
        #print(i)
        Image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')))
        links = Image.get_attribute('src')
        data = urllib.request.urlretrieve(links, f'{path_save}/{user}{i}.png')
    return path_save



'''
user = "omar sarfraz cheema"

path = make_dir(user)

Osint(user,path,Chrom_path="C:\\",Headless = False)

'''
