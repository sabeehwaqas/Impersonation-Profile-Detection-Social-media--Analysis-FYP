from Scweet.user1 import get_user_information1

# code to take file username as input
with open(r'C:\Users\msabeeh.bee56mcs\Desktop\LATEST LATEST FYP\newvenvName\REAL CURENT SCRAPPER - Copy.txt', 'r') as f:
    lines = f.readlines()
    user111 = [line.strip() for line in lines]

Usernames=user111
auth=1         # 1 for real , 0 for fake
get_user_information1(Usernames,auth)

with open(r'C:\Users\msabeeh.bee56mcs\Desktop\LATEST LATEST FYP\newvenvName\FAKE CURENT SCRAPPER.txt', 'r') as f:
    lines = f.readlines()
    user111 = [line.strip() for line in lines]

Usernames=user111
auth=0         # 1 for real , 0 for fake
get_user_information1(Usernames,auth)