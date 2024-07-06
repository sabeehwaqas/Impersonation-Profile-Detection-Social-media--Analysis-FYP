import shutil
import numpy as np
import face_recognition
import os
import face_recognition
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
import face_recognition
import os
from pathlib import Path
from feedback1 import find_cluster_id, image_detect_duplicates, image_detect, affiliated_images_for_feature_matching
from affiliation import Osint, Affilation, image, make_dir
from collections import OrderedDict
import mysql.connector


encodings = {}

def enter_user(user ,depth,Path,image_save_path):

    depth =depth +1
    userr1 = user
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(Path ,options = options)

    browser.get(f'https://twitter.com/search?q={userr1}&src=typed_query&f=user')
    text_path = image_save_path + '\\' + f'{user}.txt'
    time.sleep(3)

    for i in range(1 ,depth):

        try:
            time.sleep(4)
            print("========================================")
            follo = WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div')))
            time.sleep(3)
            following = follo.text
            # print(following)
        except Exception as e:
            print(e)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        with open(text_path ,'a' ,encoding="utf-8") as g:
            g.write(following)
    lists,dicts = Usernames(text_path)

    image_get(lists,browser,image_save_path)

    return lists


def Usernames(text_path):
    dict1 = {}
    List1 = []
    bookname = text_path
    bookFile = open(text_path, 'r', encoding="utf-8")
    bookString = bookFile.read()
    lowerBook = bookString.lower()
    wordList = lowerBook.split()
    flag = 0
    sentence = ''
    # print(wordList)
    a = 2
    for i, word in enumerate(wordList):
        # print(word)

        if flag == 0:
            if word == "follow":
                Username1 = wordList[i - 1]
                flag = 1
        if flag == 1:
            sentence = sentence + " " + word
            if word == "follow":
                Description = sentence
                Username2 = wordList[i - 1]
                words = sentence.split()
                sentence = " ".join(words[:-4])
                sentence1 = sentence
                # sentence1=extract_description(sentence)
                flag = 2
                List1.append(Username1)
                dict1[Username1] = sentence1
        if flag == 2:
            Username1 = Username2
            flag = 1
            sentence = ''
    my_list = list(set(List1))
    print(List1)
    return my_list, dict1

def image_get(list,driver,path):
    for i in range(len(list)):
        userr = list[i]
        driver.get(f"https://twitter.com/{userr}/photo")
        time.sleep(10)
        driver.save_screenshot(f"{path}/{userr}.png")


def perform_cluster(filepath,results_path,file,user):
    '''
    filenames = os.listdir(path)

    known_image = face_recognition.load_image_file(image_dir)
    known_encoding = face_recognition.face_encodings(known_image)[0]
    for files in filenames:
        if files != 'similarity':
            unknown_image_dir = os.path.join(path,files)
            unknown_image = face_recognition.load_image_file(unknown_image_dir)
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            print("Compare",files)
            results = face_recognition.compare_faces([known_encoding], unknown_encoding)
            print(image_dir)
            print(unknown_image_dir)
            print(results)
            print("-----------------------------------------------------------")
    '''
    try:
        img = face_recognition.load_image_file(filepath)
        fe = face_recognition.face_encodings(img)

        if fe:
            fe = fe[0]
        else: return
        action_taken = False
        curr_image_cluster_id = None
        for cluster_id, cluster_encodings in encodings.items():
            results = face_recognition.compare_faces(cluster_encodings, fe)
            print("results %s %s" % (results, cluster_id))
            if all(results):
                print("cluster_id %s" % cluster_id)
                curr_image_cluster_id = cluster_id
                encodings.get(cluster_id).append(fe)
                action_taken = True

        if not action_taken:
            curr_image_cluster_id = "cluster_%s" % (len(encodings.keys()) + 1)
            print("creating new cluster %s" % curr_image_cluster_id)
            encodings[curr_image_cluster_id] = [fe]
        curr_cluster = os.path.join(results_path, curr_image_cluster_id)
        print("egwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
        print(curr_cluster)
        print("sthsefffffffffffffffffffffffffffffffffffffffffffffffff")
        curr_cluster_dir = Path(curr_cluster)
        curr_cluster_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(filepath, os.path.join(curr_cluster_dir, file))
    except:
        rt = 0


def start_cluster(path, lists_of_code,user):
    encodings = {}
    filenames = os.listdir(path)
    list_of_done = []

    '''
    for files in filenames:
        image_dir = os.path.join(path,files)
        if files != 'similarity':
            print("--------------------------------------------------------")
            print("FILE ",files)
            perform_cluster(image_dir,path)
            list_of_done.append(files)
    print(lists_of_code)
    print(list_of_done)
    '''

    curr = 0
    #cwd = os.getcwd()

    results_path = os.path.join(path, 'results')

    for subdir, dirs, files in os.walk(path):
        total = len(files)
        for file in files:
            if file!='similarity' or file!= f'{user}.txt':
                filepath = os.path.join(subdir, file)
                print("File: %s" % filepath)
                print("file path", filepath)
                print("results path", results_path)
                print(file)
                if not filepath.startswith(rf'C:\Users\Dell\OneDrive\Desktop\{user}\similarity'):
                    if filepath != fr'C:\Users\Dell\OneDrive\Desktop\imran khan\{user}.txt':
                        perform_cluster(filepath,results_path,file,user)
                        curr += 1
                        print("file %s/%s - %s encodings" % (curr, total, len(encodings)))

def check(lists,path,user):
    list_of_code = []
    list_no_code = []
    newpath = path + '\\' + 'similarity'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for i in range(len(lists)):
        try:
            image = face_recognition.load_image_file(path +'\\'+ lists[i] + '.png')
            face_encoding = face_recognition.face_encodings(image)[0]
            list_of_code.append(lists[i])
        except Exception as e:
            print(f"moving {lists[i]} to sub directory")
            list_no_code.append(lists[i])
            try:
                shutil.move(path + '\\' + lists[i] + '.png' , newpath)
            except Exception as e:
                print('alreadey moved files to subdirectory')

    print(list_no_code)

    print(list_of_code)

    start_cluster(path,list_of_code,user)

def create_path(user):
    path = rf'C:\Users\Dell\OneDrive\Desktop\{user}'
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def similarity_check(dir):

    import cv2

    dir1 = dir + '\\' + '@imrankhanpti.png'
    print(dir1)
    dir2 = dir + '\\' + '@ajimran.png'

    img1 = cv2.imread(dir1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(dir2, cv2.IMREAD_GRAYSCALE)

    sift = cv2.xfeatures2d.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher()

    matches = bf.knnMatch(des1, des2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    if len(good_matches) > 1:
        print("The two images contain similar objects.")
    else:
        print("The two images do not contain similar objects.")

def find_file_location(Twitter_id, Osint_search, Twitter_search):
    filename = f"{Twitter_id}.png"  # replace with the actual filename
    dir = f"C:\\Users\\Dell\\OneDrive\Desktop\\{Twitter_search}"
    list_of_matched_faces = []
    list_of_duplicate_images = []
    for root, dirs, files in os.walk(dir):
        if filename in files:
            #print("File found:", os.path.join(root, filename))
            if os.path.join(root, filename).startswith(f"{dir}\\results"):
                name = os.path.join(root, filename).replace(f"{Twitter_id}.png", "")
                filenames = os.listdir(name)
                print(filenames)
                list_of_matched_faces = find_cluster_id(Twitter_search,Osint_search)
                break
            if os.path.join(root,filename).startswith(f"{dir}\\similarity"):
                print(f"where is the cluster of {Twitter_search}?")
                list_of_duplicate_images = image_detect_duplicates(Twitter_id,Twitter_search)
                list_of_matched_faces = find_cluster_id(Twitter_search, Osint_search)
                break


    print(list_of_matched_faces)
    print(list_of_duplicate_images)
    return list_of_matched_faces, list_of_duplicate_images






def filter(list3, list2, list1):
    face_ = []
    face_1 = []
    face_ = list3[0]
    face_recog_list = []
    face_recog_list1 = []
    for i in range(len(face_)):
        df = face_[i]

        filenames = os.listdir(df)
        for files in filenames:
            file = files.replace(".png", "")
            face_recog_list.append(file)
    face_1 = list3[1]
    if len(face_1)!= 0:
        for i in range(len(face_1)):
            facee = face_1[i].replace(".png", "")
            face_recog_list.append(facee)


    if len(list2)!= 0:
        for i in range(len(list2)):
            nameee = list2[i].replace(".png", "")
            face_recog_list1.append(nameee)

    if len(list1)!=0:
        for i in range(len(list1)):
            nameee = list1[i].replace(".png","")
            face_recog_list1.append(nameee)
    conn = mysql.connector.connect(
    host="localhost",
     user="root",
    password="Jaguar@123",
    database="sql_false_flag")
    cursor = conn.cursor()
    list11 = list(set(face_recog_list))
    list22 = list(set(face_recog_list1))
    intersection = set(list11) & set(list22)

    for items in intersection:
        for items1 in list22:
            if items == items1:
                list22.remove(items1)
    print("-----------------------------------------------------------------------------------------")
    print(list11)
    print(list22)

    query="INSERT INTO Pics_Grouping (Username,Usernames) VALUES(%s,%s);"
    values=(str(list11),str(list22))
    cursor.execute(query,values)
    conn.commit()





#twitter_id = '@officialdgispr'  ##twitter id osint ---------------------------------> About_User1 return twitter id
#osint_search = 'ispr'   ##title wikipedia ----------------------------> About_User1 return osint_search
#twitter_search = "dg ispr" ##------------------------------------------------------------> enter_user return

def pic_grouping(twitter_id, osint_search, twitter_search, flag, lists, counter):
    list3 = []
    list2 = []
    list1 = []
    #user = osint_search

    #path = make_dir(user)

    #Osint(user,path,Chrom_path="C:\\",Headless = False)

    #
   
    
    Path_chrome = 'C:\\Users\\Dell\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe'


    if flag == 0:
        driver = webdriver.Chrome(Path_chrome)
        image_save_path = create_path(twitter_search)
        image_get(lists,driver,image_save_path)


    #lists = enter_user(twitter_search,1,Path_chrome,image_save_path)

    if flag == 1:
        image_save_path = create_path(twitter_search)
        if counter == 1:
            check(lists,image_save_path,twitter_search)
    

        list3 = find_file_location(twitter_id,osint_search, twitter_search)
        list1 = image_detect(user_twitter_search=twitter_search,user_osint=osint_search)
        list2 = affiliated_images_for_feature_matching(user_twitter_search=twitter_search,user_osint=osint_search)

        return list3, list2, list1


    #filter(list3, list2, list1)



