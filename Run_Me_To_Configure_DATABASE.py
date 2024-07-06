import mysql.connector
conn = mysql.connector.connect(
host="localhost",
user="root",
password="Jaguar@123",
database="sql_false_flag")
cursor = conn.cursor()


query="DROP DATABASE IF EXISTS `sql_false_flag`;"
cursor.execute(query)
conn.commit()    
query="CREATE DATABASE sql_false_flag;"
cursor.execute(query)
conn.commit()    
query="use sql_false_flag;"
cursor.execute(query)
conn.commit()    


#query="DROP table IF EXISTS UsersProfile;"
#cursor.execute(query)
#conn.commit()                   
query="create table `UsersProfile` (`Username` varchar(128) NOT NULL,`Fullname` varchar(128) NOT NULL,`Location` varchar(86) ,`Description` LONGTEXT NOT NULL ,`Followers` bigint NOT NULL,`Following` bigint NOT NULL,`Join_Date` varchar(86) NOT NULL,`Verification_status` int NOT NULL,`Lists` int,`Likes` bigint,`Birthday` varchar(86)  ,`Profession` varchar(86),`Tweets` bigint NOT NULL,`Website` varchar(128) )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(query)
conn.commit()        
query="create table `UsersProfile_Temp` (`Username` varchar(128) NOT NULL,`Fullname` varchar(128) NOT NULL,`Location` varchar(86) ,`Description` LONGTEXT NOT NULL ,`Followers` bigint NOT NULL,`Following` bigint NOT NULL,`Join_Date` varchar(86) NOT NULL,`Verification_status` int NOT NULL,`Lists` int,`Likes` bigint,`Birthday` varchar(86)  ,`Profession` varchar(86),`Tweets` bigint NOT NULL,`Website` varchar(128) )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(query)
conn.commit()                    
query="create table `Pics_Grouping`(`Username` varchar(128), `Usernames` LONGTEXT)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci; "
cursor.execute(query)
conn.commit()                   
#-- select * from UsersProfile;
query="create table `UsersTweets` ( `Datetime` varchar(225) NOT NULL,`Tweet-Id` bigint NOT NULL,`tweet-text` LONGTEXT NOT NULL ,`Username` varchar(86) NOT NULL)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
#-- select * from UsersTweets;"
cursor.execute(query)
conn.commit()  
query="create table `UsersTweets_Temp` ( `Datetime` varchar(225) NOT NULL,`Tweet_Id` bigint NOT NULL,`tweet_text` LONGTEXT NOT NULL ,`Username` varchar(86) NOT NULL)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
#-- select * from UsersTweets;"
cursor.execute(query)
conn.commit()  
query="create table `Groups1_Info` (`Username` varchar(128), `Usernames` LONGTEXT,`Keywords` LONGTEXT,`Fullname` LONGTEXT )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
#-- select * from Groups1_Info ;"
cursor.execute(query)
conn.commit()  
query="create table `Feed_Back_Groups1_Info` (`Fullname` varchar(128), `description` varchar(255),`ID_twitter` LONGTEXT,`User_Pics` varchar(255))ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(query)
conn.commit()
query="create table `After_Feedback_Groups1_Info` (`Username` varchar(128), `Usernames` LONGTEXT,`Keywords` LONGTEXT,`Fullname` LONGTEXT )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;" 
cursor.execute(query)
conn.commit()  
query="create table `Sentiments`(`Username` varchar(255), `Positive` varchar(255) ,`Negative` varchar(255),`Neutral` varchar(255),`Overall` varchar(255))ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
cursor.execute(query)
conn.commit()  