import amino
import json
import time
#comm id: 195512655
email="overlordbot99@gmail.com"
password="peroroncinoBOT2"
chatid = "7eb7e6ea-534c-4ce2-b527-1fa329a69b11"
client=amino.Client()
client.login(email,password)
print("logged in...")
subclient = amino.SubClient(comId='195512655', profile=client.profile)
print("joined")

#########################################################################################
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
  
############################################################################################
welc ='''

࿇Welcome to Overlord amino!࿇

❖To start things off, read the guidelines: http://aminoapps.com/p/kcwxb9

❖Then you could join the official chat to meet new people: http://aminoapps.com/p/henic9

❖If you are an overlord light novel reader and wish to talk about it with other light novel readers, you could join “Light novel discussion” chat: http://aminoapps.com/p/hj45xe

❖But be sure to join in on the #Introduction Challenge! We'd be so happy to know more about you ^^ http://aminoapps.com/p/x6ydsd

❖Feel free to contact any of the staff if you need any help.

💀Have fun💀
'''
name=subclient.get_all_users(start = 0,size=8)
data = name.json
time1 = "2021-02-13T14:32:10Z"
while True:
    countdown(3600)
    for person in data['userProfileList']:
        if person['modifiedTime'] > time1
            subclient.comment(message=welc, userId= person['uid'])
            time1 = person['modifiedTime']


