import  base64
passwd_Main = input("Enter the main password to unlock :")
def view():
    with open("passwd.txt", "r") as psd:
        for line in psd.readlines():
            data = line.strip()
            user_name,password = data.split(" -- ")
            print("user_name : " , user_name , "--" , "password : ", password)


def add() :
    name = input("Enter user name :")
    passwd = input("Enter the password : ")
    with open("passwd.txt" , "a") as psd:
        psd.write(name + " -- " + passwd + "\n")


def text_modder():
    pass
'''
 ______   ______      
|__  __|  | ___ |  
   | |    ||___||     DOOOO ASAP 
   |_|    |_____|   
-> text encryption tool
-> to search only specific password
-> to make it work faster 
-> encrypt and decrypt the password to make it difficult to read using base64
-> to create a random password generator and also ask if they want to add it   
-> tick tack toe (Done)
-> text to speech converter and saving in a file
-> speech to text converter
-> phone base to add,replace ,delete
-> task scheduler (In-progress)
'''




while True :
    opt1 = " 1) View a password \n"
    opt2 = " 2) Add a password \n"
    opt3 = " q) quit \n"
    optins_menu = input("SELECT ANY OPTION \n" + opt1 + opt2 + opt3)
    if optins_menu == 'q':
        break

    if optins_menu == "1":
        view()
    elif optins_menu == "2":
        add()
    else:
        print("Invalid input")
        continue
'''

import base64

sample_string = "kind of cool"
sample_string_bytes = sample_string.encode("ascii")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

print(f"Encoded string: {base64_string}") '''





