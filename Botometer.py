from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Scweet import utils


def botometer_analysis(Input_user,List0_file1,Logs_Print=1,Print_detail=1,Output_Options=0,Do_Headless=1):
    
    driver = utils.init_driver(headless=False)

    if Output_Options==1:
        l=0
        # pull data from sql
        #byass List0_file1 and get sql address instead

    Path = 'C:\chromedriver.exe'
    #options = Options()
    # this parameter tells Chrome that
    # it should be run without UI (Headless)
    #options.headless = False
    # initializing webdriver for Chrome with our options
    #driver = webdriver.Chrome(Path)

    if Logs_Print==1:
        print('*** Driver started')
    else:
        print('INITATED BOTOMETER ANALYSIS SUCCESSFULLY PLEASE WAIT')

    driver.get("https://botometer.osome.iu.edu/")
    time.sleep(1)
    original_window = driver.current_window_handle
    if Logs_Print==1:
        print('*** Website opened')


    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID,"inputSN")))

    searh1 = driver.find_element(By.ID, "inputSN")
    searh1.send_keys("@elonmusk")
    if Logs_Print==1:
        print('*** Inputting first input to start twitter login procedure' )

    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME,"btn.btn-default")))
    #time.sleep(2)
    sumbit = driver.find_element(By.CLASS_NAME, "btn.btn-default")
    sumbit.click()

    time.sleep(5)
    if Logs_Print==1:
        print('*** Twitter Login initiated')

    whandle = driver.window_handles[1]

    # switch to pop up window
    driver.switch_to.window(whandle)

    sign_in = driver.find_element(By.CLASS_NAME, "submit.button.selected")
    sign_in.click()
    #time.sleep(5)
    #print(driver.window_handles)
    if Logs_Print==1:
        print('*** Submit clicked')
    #time.sleep(2)


    email_xpath = '//input[@autocomplete="username"]'
    password_xpath = '//input[@autocomplete="current-password"]'
    username_xpath = '//input[@data-testid="ocfEnterTextTextInput"]'
    ele = 'nsm7Bb-HzV7m-LgbsSe-MJoBVe'
    username  = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,email_xpath ))).click()
    email = "Fyp56D"
    password = "Student@123"
    email_el = driver.find_element(by=By.XPATH, value=email_xpath)
    email_el.send_keys(email)
    email_el.send_keys(Keys.ENTER)
    if Logs_Print==1:
        print('*** Email entered')
    #time.sleep(2)

    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,password_xpath) ))

    password_el = driver.find_element(by=By.XPATH, value=password_xpath)
    password_el.send_keys(password)
    password_el.send_keys(Keys.ENTER)
    if Logs_Print==1:
        print('*** Password entered')


    time.sleep(2)

    #input from list 
    
    if List0_file1==0:
        #list or single
        users= Input_user
        
    elif List0_file1==1:
        #file      
        # code to take file username as input
        with open(Input_user, 'r') as f:
            lines = f.readlines()
            users = [line.strip() for line in lines]
    
    if Logs_Print==1:
        print('*** Twitter loggin successfull')
    
    current_user_details=[]
    #users = user111
    not_found_flag=[]
    for i in range(len(users)):
        one_current_user_details=[]
        if Print_detail==1:
            print(f'***************** User: {users[i]} *************')
            print('')
        #print(one_current_user_details)
        one_current_user_details.append(users[i])
        #print(one_current_user_details)
        try:
            Authorize = driver.find_element(By.XPATH,'//*[@id="allow"]')
            Authorize.click()
        except Exception as e:
            #print(e)
            l=0
        time.sleep(2)
        # switch to pop up window
        driver.switch_to.window(original_window)
        #driver.refresh()
        if Logs_Print==1:
            print('*** Refreshing')

        driver.get("https://botometer.osome.iu.edu/")

        searh1 = driver.find_element(By.ID, "inputSN")
        user = users[i]
        searh1.send_keys(user)
        if Logs_Print==1:
            print(f'*** Enterering user:{i}')

        #time.sleep(5)
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME,"btn.btn-default") ))
        
        sumbit = driver.find_element(By.CLASS_NAME, "btn.btn-default")
        sumbit.click()
        if Logs_Print==1:
            print(f'*** Submitting user ')

        detail =[]
        try:
            if Logs_Print==1:
                print('*** Getting bot score')
                
            
            rate = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,'user-bot-score.ng-binding.ng-scope' ))).text
            if Print_detail==1:
                print(rate)
            one_current_user_details.append(rate)
            not_found_flag.append(False)
               
        except Exception as e:
            print('BotScore Not Found')
            for z in range(0,44):
                if z!=44:
                    #print("HERE IS Z",z)
                    one_current_user_details.append('NA')
                    #print("ONE",one_current_user_details)
            #print("NNNN",one_current_user_details)
            current_user_details.append(one_current_user_details)
            not_found_flag.append(True)
            continue
                        #print(WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME,'user-bot-score.ng-binding.ng-scope' ))).text())

        'panel-body'
        if Logs_Print==1:
            print('*** In Progress')
        try:
            rate = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME,'panel-body' ))).click()
        except Exception as e:
            print("cant click",e)

        try:
            print('|ssadada')
            rate = driver.find_elements(By.CLASS_NAME,'category-score.ng-binding')
            for rates in rate:
                print("\ratessss",rates.text)
                detail.append(rates.text)
            print(detail)

            
            del detail[3:5]
            del detail[5:]
            print("UPDATED : ",detail)
        
            
            if Logs_Print==1:
                print('*** Successfully done')
            if Print_detail==1:
                print('Here is the final list')
                print(detail)
            one_current_user_details.append(detail)
            print("THE DETAILS: ",detail)
                
        except Exception as e:
            #print(e)
            print("SABEEH")
            name_rate = driver.find_elements(By.CLASS_NAME, 'category-title.ng-binding')
            rate = driver.find_elements(By.CLASS_NAME,'category-score.ng-binding')
            print("\rate=== ",rate)
            time.sleep(400)
            for rates in rate:
                print("\ratessss",rates.text)
                detail.append(rates.text)
            print(detail)
            


            del detail[:9]
            print("UPDATED : ",detail)
        
            
            if Logs_Print==1:
                print('*** Successfully done')
            if Print_detail==1:
                print('Here is the final list')
                print(detail)
            one_current_user_details.append(detail)
            print("THE DETAILS: ",detail)
                

        try:
            other_name=driver.find_elements(By.CLASS_NAME,'category-title')
            other_rate = driver.find_elements(By.CLASS_NAME, 'category-score.ng-binding')
            for i,j in zip(other_name,other_rate) :
                if other_name.text == 'Other':
                    #print(i.text,j.text)
                    l=0
                    
        except Exception as e:
            l=0
            #print('cant get',e)
            
            

        try:
            original_window = driver.current_window_handle
            driver.execute_script("window.open('');")
            child_window = driver.window_handles[1]
            driver.switch_to.window(child_window)
            driver.get(f'https://botometer.osome.iu.edu/userDetail/{user}')
            if Logs_Print==1:
                print('*** Opened Details')

        except Exception as e:
            print(e)

        try:

            maximum_display_height = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'nv-axisMaxMin.nv-axisMaxMin-y.nv-axisMax-y'))).text
            #print(maximum_display_height)
            maximum_display_height_float = float(maximum_display_height)
            height = driver.find_elements(By.CLASS_NAME,'discreteBar')
            heights = []
            for i in height:
                #print(i.get_attribute('height'))
                k = float(i.get_attribute('height'))
                heights.append(k)
            
            #print("HEIGHTS")
            #print(heights)
            #print('AAAAAA')
            #print(maximum_display_height_float)

            #print(heights)

            max_heights = max(heights)

            factor = max_heights/maximum_display_height_float

            #print(factor)

            points = []
            for i in range(len(heights)):
                points.append(heights[i]/factor)
            #print( "Here is the Tweets by day of week : ")
            #print(points)

        except Exception as e:
            box = driver.find_element(By.CLASS_NAME,'ng-isolate-scope')
            rectangles = box.find_elements_by_xpath('.//rect')

            heights = []
            for rectangle in rectangles:
                height = rectangle.get_attribute('height')
                heights.append(float(height))

            # Print the list of heights
            #print(heights)
        tweets_days_hour = []
        new_tweets_days_hour = []
        # locate the rectangle elements
        rectangles = driver.find_elements(By.CSS_SELECTOR,"rect")
        count = 1
        # iterate through the rectangles and print their heights
        for rect in rectangles:
            height = rect.get_attribute("height")  # or rect.value_of_css_property("height")
            if count>9:
                tweets_days_hour.append(float(height))
            if count<=9:
                new_tweets_days_hour.append(float(height))
            #print(height)
            #print("CHECK......")
            #print(new_tweets_days_hour)
        
            
            
            count = count + 1
        
        
        # removing the first and last data of the list because its of ours no use
        new_tweets_days_hour = new_tweets_days_hour[1:-1]
                
        #print("I am print hieghts hahaha")
        #print(tweets_days_hour)
        #print(new_tweets_days_hour)
        #print("TYPE")
        #print(type(new_tweets_days_hour))
        max_heights1 = max(new_tweets_days_hour)
        #print("HERE IS THE MAX OF LIST")
        #print(max_heights1)
        max_heights11 = float(max_heights1)
        factor1 = max_heights11/maximum_display_height_float
        #print('here is the height factor')
        #print(factor1)
        #print(type(factor1))
        
        #print("THE FINAL VALUES")
        points1 = []
        for i in range(len(new_tweets_days_hour)):
            points1.append(round(new_tweets_days_hour[i]/factor1))
        if Print_detail==1:
            print(f"Tweets by day of week : {points1} ")
            print('')
        one_current_user_details.append(points1)

        
        # now dealing with Tweets by day of week
        #print(tweets_days_hour)
        max_hour_day_height = max(tweets_days_hour)
        #print('check222')
        #print(max_hour_day_height)
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'nv-axisMaxMin.nv-axisMaxMin-y.nv-axisMax-y')))
        maximum_display_height1 = driver.find_elements(By.CLASS_NAME, 'nv-axisMaxMin.nv-axisMaxMin-y.nv-axisMax-y')
        #for ii in maximum_display_height1:
            #print("SAME CLASS VALUES"+ ii.text)
        maximum_display_height1 = (maximum_display_height1[-1]).text
        #print("CHECK......")
        #print(maximum_display_height1)
        
        ##############3
        ################
        
        factor2 = float(max_hour_day_height)/float(maximum_display_height1)
        
        points2 = []
        for i in range(len(tweets_days_hour)):
            points2.append(round(tweets_days_hour[i]/factor2))
        if Print_detail==1:
            print( "Tweets by hour of day : ")
            print(points2)
        one_current_user_details.append(points2)
        
        
        
        #Now getting Likes Recent tweets per week, retwett ratio
        
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'ng-binding')))
        profile_data_list = driver.find_elements(By.CLASS_NAME, 'ng-binding')
        #count = 0
        #for i in profile_data_list:
            
            #print("SAME CLASS VALUES"+ i.text)
            #count = count+1
        #print("values found = ")
        #print(count)
        
        #Most Recent post
        Most_recent_post_time = (profile_data_list[7]).text
        if Print_detail==1:
            print('Most Recent post')
            print(Most_recent_post_time)
        one_current_user_details.append(Most_recent_post_time)

        #Likes
        #Likes = (profile_data_list[11]).text
        Likes = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/dl/dd[4]").text
        if Print_detail==1:
            print('Likes')
            print(Likes)
        one_current_user_details.append(Likes)
        
        #Recent tweets per week
        #Recent_tweets_per_week = (profile_data_list[15]).text
        Recent_tweets_per_week = driver.find_element(By.XPATH,'/html/body/div/div/dl/dd[3]').text
        if Print_detail==1:
            print('Recent tweets per week')
            print(Recent_tweets_per_week)
        one_current_user_details.append(Recent_tweets_per_week)
        
        #Retweet ratio
        #Retweet_ratio = (profile_data_list[16]).text
        Retweet_ratio = driver.find_element(By.XPATH,"/html/body/div/div/dl/dd[4]").text
        if Print_detail==1:
            print('Retweet_ratio')
            print(Retweet_ratio)
        one_current_user_details.append(Retweet_ratio)
            
        
        
        

        time.sleep(1)
        driver.close()
        time.sleep(1)
        driver.switch_to.window(original_window)
        time.sleep(1)
        #print('one cruuent user',one_current_user_details)
        if Print_detail==1:
            print('')
            print('****************************************')
            print('')
        current_user_details.append(one_current_user_details)
        if Print_detail==1:
            print(current_user_details,not_found_flag)
    
    driver.close()
    print('one cruuent user',current_user_details)
    
    if Output_Options==0:   
        put_csv(current_user_details,not_found_flag)
    if Output_Options==1:
        return_to_call = put_csv(current_user_details,not_found_flag,Output_Options)
        return return_to_call

        ################## UPDATED ######################
        ################## UDPATED ###################3
 


def put_csv(list1,not_found_flag,Output_Options=0):
    
    print("THE LIST IS HERE")
    print(list1)
    #print("FLAG",not_found_flag)
    # formation the list as per the csv headers
    list2=[]
    lenght = len(list1)
    #print("LLLLLLLLLLLl")
    #print(lenght)
    for j in range(lenght):
        print('J is ',j)
        print('not found flag is ',not_found_flag[j])
        if not_found_flag[j]==False:
            print("********************8",not_found_flag[j])
            print(list1[j][0])
            list2.append(list1[j][0])# @BeingSalmanKhan
            
            my_string = list1[j][1]
            slash_index = my_string.index("/")
            #print(float(list1[j][1][:slash_index]))
            list2.append(list1[j][1][:slash_index]) # bot score = 0.8
            #print(float(list1[j][2][0]))
            list2.append(list1[j][2][0])
            #print(float(list1[j][2][1]))
            list2.append(list1[j][2][1])
            #print(float(list1[j][2][2]))
            list2.append(list1[j][2][2])
            #print(float(list1[j][2][3]))
            list2.append(list1[j][2][3])
            #print(list1[j][2][4])
            list2.append(list1[j][2][4])
            #print(list1[j][5])
            list2.append(list1[j][5])   #'Sat Feb 18, 2023'
            #print(list1[j][6])
            list2.append(list1[j][6])
            #print(list1[j][7])
            list2.append(list1[j][7])
            #print(list1[j][8][:1])
            list2.append(list1[j][8][:1])
            #print(list1[j][3])
            list2.append(list1[j][3])
            for i in range(0,7):
                if i!=7:
                    #print(list1[j][3][i])
                    list2.append(list1[j][3][i])
            #print(list1[j][4])
            list2.append(list1[j][4])
            for i in range(0,24):
                if i!=24:
                    #print(list1[j][4][i])
                    list2.append(list1[j][4][i])
                
            list1[j] = list2
            list2=[]
        else:
            print("HERE IS Z")
            list2.append(list1[j][0])# @BeingSalmanKhan
            for z in range(0,44):
                if z!=44:
                    
                    list2.append('NA')
            print("list2 is ",list2)
            list1[j] = list2
            list2=[]

            
    if Output_Options==1:
        print('LIST1 is here : ',list1)
        return list1
        print('LIST1j')
        print(list1[j])
    #print("LIST1")
    #print(list1)
    
    
    header = ["User-name", "Bot_Score", "Echo_chamber", "Fake_follower", "Financial", "Self_declared", "Spammer", "Most_recent_post", "Likes", "Recent_tweets_per_week", "Retweet_ratio", "Tweets_by_day_of_week_list", "Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Tweets_by_hour_of_day_list", "12AM","1AM","2AM","3AM","4AM","5AM","6AM","7AM","8AM","9AM","10AM","11AM","12PM","1PM","2PM","3PM","4PM","5PM","6PM","7PM","8PM","9PM","10PM","11PM"]
    with open("C:\\Users\\msabeeh.bee56mcs\\Desktop\\LATEST LATEST FYP\\newvenvName\\botometer_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in list1:
            writer.writerow(row)

