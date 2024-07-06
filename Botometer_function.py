from Botometer import botometer_analysis

'''
def botometer_analysis(Input_user,List0_file1,Logs_Print=1,Print_detail=1,Output_Options=1,Do_Headless=0):
Input_user: enter the list or file address.
List0_file1:  0 for if you are sending List,  1 for if you are sending file address
Logs_Print,: 0 for not print logs, 1 for print logs.
Print_detail: 0 for NOT print the user scrapped detail, 1 for print the user scrapped detail.
Output_Options: 0 for getting a csv form data output file, 1 for pushing in SQL DB
Do_Headless: 0 for watching the bot working, 1 for headless

'''

#for List of single user
#botometer_analysis(["@omarcheema14","ImrankhanPTI"],0,1,1,0)
bot_values= botometer_analysis(["@TheMahiraKhan"], 0, 1, 1, 1)
print("HERE :",bot_values)
print('lenght ofc', len(bot_values))
for j in range(len(bot_values)):
        print("c[j] : ",bot_values[j][0])
        
        

#for text file with user
#botometer_analysis(r'C:\Users\msabeeh.bee56mcs\Desktop\LATEST LATEST FYP\newvenvName\sabeehmlprofilesReal.txt',1,1,1,0)