import pandas as pd 

###read the csv file
df = pd.read_csv("elms-kc-btech-student-detail-kc-btech.csv")

##lenth data in csv
nlen= len(df)
n = 0
while n < nlen-1: 
    name = df["Name"][n]
   
    
    roll = int(df["University HPTU Roll No"][n])
    email = df["Email"][n]





    
    n = n +1
