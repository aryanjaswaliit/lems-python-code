import pandas as pd 
import requests
from bs4 import BeautifulSoup

###read the csv file
df = pd.read_csv("elms-kc-btech-6th-sem-cse.csv")

##lenth data in csv
nlen= len(df)
n = 0
while n < nlen-1: 
    name = df["Name"][n]
   
    
    roll = int(df["University HPTU Roll No"][n])
    email = df["Email"][n]

    ##############upoad

    url = "https://elms.xperiment.cloud/admin/main/student/add/"
    header = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "cookie": "csrftoken=uGPpdKsS00whAZDFthaKSNGmKKjvELECYNYeqZcF9zMrBGi6UepZv9t4vGC15xwL; sessionid=.eJxVjDsOwyAQBe9CHSE-ZsEp0_sMiIUlOIlAMnYV5e4RkoukfTPz3syHYy_-6LT5NbErk-zyu2GIT6oDpEeo98Zjq_u2Ih8KP2nnS0v0up3u30EJvYxam2y1g6yEysJERaSMA61ncsFCJAuAmFFYpyxkIAcIAFLJeaLJSfb5As8zNwU:1rfMB1:RohV2RoEgftDw_2ifA4gOTozZ_vFfe35G9kFkneK-q4",
        "Referer": "https://elms.xperiment.cloud/admin/main/student/",
        "User-Agent":"Nasa",
        "Referrer-Policy": "same-origin"
    }

    data = requests.get(url,headers=header)
    print(data)

    data_txt = BeautifulSoup(data.text)

    token = data_txt.find("input",{"name":"csrfmiddlewaretoken"})
    print(token["value"])
    token = str(token["value"])
    ##register

    url = "https://elms.xperiment.cloud/admin/main/student/add/"
    header = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundary8bBCfDhRHzkiKBLL",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "cookie": "csrftoken=uGPpdKsS00whAZDFthaKSNGmKKjvELECYNYeqZcF9zMrBGi6UepZv9t4vGC15xwL; sessionid=.eJxVjDsOwyAQBe9CHSE-ZsEp0_sMiIUlOIlAMnYV5e4RkoukfTPz3syHYy_-6LT5NbErk-zyu2GIT6oDpEeo98Zjq_u2Ih8KP2nnS0v0up3u30EJvYxam2y1g6yEysJERaSMA61ncsFCJAuAmFFYpyxkIAcIAFLJeaLJSfb5As8zNwU:1rfMB1:RohV2RoEgftDw_2ifA4gOTozZ_vFfe35G9kFkneK-q4",
        "Referer": "https://elms.xperiment.cloud/admin/main/student/add/",
        "Referrer-Policy": "same-origin"
    }
    #roll = "21011403001"
    #name = "aryan"
    #email = "aryanjaswaliit@gmail.com"
    body = '------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"csrfmiddlewaretoken\"\r\n\r\n'+str(token)+'\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"student_id\"\r\n\r\n'+str(roll)+'\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n'+str(name)+'\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\n'+str(email)+'\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n12345678\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"role\"\r\n\r\nStudent\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"course\"\r\n\r\n601\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"course\"\r\n\r\n602\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"course\"\r\n\r\n603\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"course\"\r\n\r\n604\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"course\"\r\n\r\n605\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"course\"\r\n\r\n606\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"course\"\r\n\r\n607\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"course\"\r\n\r\n611\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"course\"\r\n\r\n612\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"course\"\r\n\r\n613\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"photo\"; filename=\"\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"department\"\r\n\r\n1\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL\r\nContent-Disposition: form-data; name=\"_save\"\r\n\r\nSave\r\n------WebKitFormBoundary8bBCfDhRHzkiKBLL--\r\n'
    #print(body)
    data = requests.post(url,headers=header,data=body)
    print(data)
    #print(data.text)
    ############

    


    
    n = n +1
