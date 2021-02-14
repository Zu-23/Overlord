import amino
import json
import time
#comm id: 195512655
#Official Overlord Chatroom  :  42019ba1-1907-468f-b1d6-608cdad01a4e
#Cult of Ra! Donations are welcome!  :  69b9a155-17db-4094-a158-486487821605
email="overlordbot99@gmail.com"
password="peroroncinoBOT2"
chatid = "7eb7e6ea-534c-4ce2-b527-1fa329a69b11"
client=amino.Client()
client.login(email,password)
print("logged in...")
subclient = amino.SubClient(comId='195512655', profile=client.profile)
print("joined")
#chats = subclient.get_public_chat_threads(size=100)
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
name=subclient.get_all_users(start = 0,size=300)
data = name.json
time1 = "2021-02-13T14:32:10Z"
while True:
    countdown(6)
    for person in data['userProfileList']:
        if person['modifiedTime'] > time1:
            print("we found one")
            subclient.comment(message=welc, userId= person['uid'])
            print("msg has been sent")
            time1 = person['modifiedTime']
        
#subclient.comment(message="hello", userId = "ad930284-3524-4a1e-be52-eb9a8ccc6f85")
#print(name.json)
#print(name.userId)
#print(name.age)
#print(name.gender)
#print(name.nickname)
#print(dir(name))

#for name, id in zip(subclient.get_public_chat_threads(size=100).title, subclient.get_public_chat_threads(size=100).chatId):
    #print(name," : ",id)



