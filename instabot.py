from time import sleep
from getpass import getpass
from instabot import Bot
from os import remove
my_bot = Bot()
#introduction to app
print("--WELCOME TO INSTABOT CLI APPLICATION--")
sleep(2)
print("setting up the connection with https://www.instagram.com/", end="")
for i in range(3):
 sleep(1)
 print('.', end="")
print()
sleep(2)
print("Connection established!")
#login user
username = input("username: ")
password = getpass(prompt="password: ")
my_bot.login(username=username, password=password)
print(f"---{username}-Loggedin sucessfully")
#opertions to perform
while True:
    print("Chose suitable option")
    print("""1. Follow\n2.Unfollow\n3.send message user\n4.Exit the app""")
    print("Enter opption you choose:",end="")
    n = int(input())
    if n==1:
        user = input("enter username:")
        my_bot.follow(user)
        print(F"--{user} FOLLOWED.--")
    elif n==2:
        user = input("enteer username")
        my_bot.unfollow(user)
        print(F"--{user}UNFOLLOWED.--")
    elif n==3:
        user = input("enter username:")
        message= input("message you want to send:")
        my_bot.send_message(message, user)
        print(F"--MESSAGE SUCESSFULLY SEND TO{user}.--",)
   
    elif n==4:
        my_bot.logout
        print("logging out the user",end="")
        for i  in range(3):
            sleep(1)
            print('.',end="")
        print()
        sleep(2)
        print("connection ended!")
        print("logged out successfully ")
        break
    else:
        print("--Wrong input,choose again")

        
remove('./config')        