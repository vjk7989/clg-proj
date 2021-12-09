import time
from plyer import notification

import time
from plyer import notification



if __name__ == "__main__":
    '''
    run = False
    
    while run:

        notification.notify(
            title="hey!!!",
            message=" just checking you are alive",
            app_icon = "D:\pythonProject\clg-proj\He.ico",
            timeout=2,
            ticker = "honey money",
            toast = True
        )
    # waiting time
        time.sleep(9)'''
    Title= input("Enter the title : ")
    Message = input("Enter the message : ")
    Appr = int(input("Enter time in sec to show the message : "))
    print("\nmake it 0 if not required \n")
    Hour = int(input("Enter number of hours the message to appear in : "))
    miN = int(input("Enter number of minutes the message to appear in : "))
    sec = int(input("Enter number of second the message to appear in : "))
    timE_sleep = Hour*60*60 + miN*60 + sec
    while True :
        notification.notify(
            title= Title,
            message = Message,
            app_icon="D:\pythonProject\clg-proj\He.ico",
            timeout=Appr,
            ticker="Vit ap",
            toast=True
        )
        time.sleep(timE_sleep)