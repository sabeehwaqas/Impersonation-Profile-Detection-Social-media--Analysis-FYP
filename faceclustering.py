from re import T
from turtle import onscreenclick
from webbrowser import Chrome
from complete  import pic_grouping
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib
import pycountry
import re
import mysql.connector
#from START_HERE import give_to_face_cluster

'''
from START_HERE import twitter_user_function
import pandas as pd
import mysql.connector

twitter_user = twitter_user_function()
print(twitter_user)


# Establish a connection to the MySQL database
conn = mysql.connector.connect(
 host="localhost",
 user="yourusername",
 password="yourpassword",
 database="yourdatabase"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the SQL query to retrieve the desired columns from the table
query = "SELECT Keywords, `Real-IDs` FROM feed_back_groups1_info"

# Execute the query and fetch the results
cursor.execute(query)
results = cursor.fetchall()

# Convert the results to a Pandas dataframe
df = pd.DataFrame(results, columns=['Keywords', 'Real-IDs'])

#my_id = df.iloc[i]['Real-IDS']

# Close the cursor and connection
cursor.close()
conn.close()
'''

# twitter search
user = 'imran khan'

# twitter id

Twitter_id = '@imrankhanpti'

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
        
        time.sleep(3)

        for i in range(len(list_to_search)):
            image(list_to_search[i], path, driver, who =1)

    except Exception as e:
        print(e)




def make_dir(user):
    newpath = fr'C:\Users\Dell\OneDrive\Desktop\Osint\{user}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath




def image(user,path_save,driver,who):
    if who == 0:
        driver.get(f"https://www.google.com/search?q={user}&tbm=isch")
        for i in range(1,3):
            Image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')))
            links = Image.get_attribute('src')
            data =  urllib.request.urlretrieve(links, f'{path_save}/{user}{i}.png') 

            

    if who ==1:
        driver.get(f"https://www.google.com/search?q={user}+logo&tbm=isch")
        for i in range(1,3):
            Image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')))
            links = Image.get_attribute('src')
            user1 = user + "_logo"
            data =  urllib.request.urlretrieve(links, f'{path_save}/{user1}{i}.png') 

    return path_save





## OSINT Khol haan



def get_full_name(Twitter_id):
    who = 0
    PATH = "C:\\Users\\Dell\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(f"https://twitter.com/{Twitter_id}")
    try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span/span[1]')))
            Full_name = element.text
    except Exception as e:
            print(e)

    osint_initial_search = Full_name + " " + Twitter_id + "wikipedia"
    driver.get(f"https://www.google.com/search?q={osint_initial_search}")

    try:
        Wikipedia = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
        Wikipedia.click()
    except Exception as e:
        print("The person is not famous")
    try:
        Osint_search1 = driver.find_element(By.CLASS_NAME,'mw-page-title-main')
        Osint_search = Osint_search1.text

    except Exception as e:
        print(e)

    try:
        Designation_or_not = driver.find_elements(By.CLASS_NAME, 'mw-headline')
        for headings in Designation_or_not:
            if headings.text.startswith("List") or headings.text.startswith("LIST"):
                who = 1
                print("designation")
    except Exception as e:
        print(e)
           
                                      

    driver.get(f"https://www.google.com/search?q={Osint_search}")

    try:
        Descreption = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rhs"]'))).text
        In_there = "Description" in Descreption
        if In_there:
            flag = 1

            lines = Descreption.split('\n')
            line_to_find = "Description"
            index_to_find = lines.index(line_to_find)
            line_to_get = lines[index_to_find + 1]
            About = line_to_get

            original_string = About
            modified_string = original_string.replace('"', '')
        if not In_there:
                print("no description given")

    except Exception as e:
         print(e)
    
    path_save = make_dir(Osint_search)
    image(Osint_search, path_save, driver, who)
    Affilation(modified_string, path_save ,driver )

    return modified_string, Osint_search

##                  HELLLLOO???

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
    return list11, list22



    



 
def start_all(Twitter_id, user, flag, lists, counter ):
    Description, Osint_search = get_full_name(Twitter_id.replace("@", ""))

    print(Description, Osint_search)




    list3, list2, list1 = pic_grouping(Twitter_id, Osint_search, user, flag, lists, counter )
    print(list3)
    print(list2)
    print(list1)
    '''

    list3 = (['C:\\Users\\Dell\\OneDrive\\Desktop\\elon musk\\results\\cluster_3', 'C:\\Users\\Dell\\OneDrive\\Desktop\\elon musk\\results\\cluster_4', 'C:\\Users\\Dell\\OneDrive\\Desktop\\elon musk\\results\\cluster_5', 'C:\\Users\\Dell\\OneDrive\\Desktop\\elon musk\\results\\cluster_13', 'C:\\Users\\Dell\\OneDrive\\Desktop\\elon musk\\results\\cluster_14', 'C:\\Users\\Dell\\OneDrive\\Desktop\\elon musk\\results\\cluster_15', 'C:\\Users\\Dell\\OneDrive\\Desktop\\elon musk\\results\\cluster_16'], [])

    list2 = ['@spangaloid.png', '@tropicthunderel.png', '@elonsuckzz.png', '@elonsuckzz.png']

    list1 = ['@anditoldyaso.png', '@dogecoin.png', '@spangaloid.png', '@srguo.png', '@spangaloid.png']
    '''

    list_face, list_object = filter(list3, list2, list1)
    return list_face, list_object



 
def start():
    #user, lists = give_to_face_cluster()


    #
    user = 'imran khan' 
    #print(user)
    lists = ['@faisaljavedkhan', '@imrankhanworld', '@ajimran', '@imranriazkhan', '@imrankhan' ,'@imeek218', '@imr4n25', '@imranzomg', '@imrankhanpti']



    Twitter_id_list = get_twitter_ids()


    flagq = 0
    counter = 0
    pic_grouping( "", "", user, flagq, lists, counter)

    flagq = 1

    for i in range(len(Twitter_id_list)):
        counter = counter + 1
        list1, list2 = start_all(Twitter_id_list[i], user, flagq, lists, counter)




        # 8bajy  okk..










def get_twitter_ids():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jaguar@123",
        database="sql_false_flag")
    cursor = cnx.cursor()
    #Copy_Table('UsersProfile','UsersProfile_Temp')
    query = f"SELECT * FROM after_feedback_groups1_info;"#" where Fullname LIKE '%DGISPR%'"
    #query = f"SELECT * FROM UsersProfile where Fullname LIKE '%DGISPR%'"
    #query = f"SELECT * FROM UsersProfile where Fullname LIKE '%imran%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    Username=[]
    for row in rows:
        dict1={'Main_User':row[0]}
        Username.append(row[0])
        #??????
    ##secondly get list of user names from sql
    twitter_ids = []
    return Username
    


#start()
#get_twitter_ids()



def enter_data_in_sql():

    import mysql.connector

    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jaguar@123",
        database="sql_false_flag"
    )

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Define the SQL query to insert a new row into the table
    sql = "INSERT INTO Pics_Grouping (Username, Username_based_on_Facial, Username_based_on_affiliation) VALUES (%s, %s)"
    values = ("john", "jane, bob, sara", "wef, wergf, wethg" )

    # Execute the query with the values
    mycursor.execute(sql, values)

    # Commit the changes to the database
    mydb.commit()

    print(mycursor.rowcount, "row inserted.")





