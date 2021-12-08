import time
from plyer import notification

import time
from plyer import notification

if __name__ == "__main__":
    while True:

        notification.notify(
            title="hey!!!",
            message=" just checking you are alive",
            app_icon = "D:\pythonProject\clg-proj\He.ico",
            timeout=2,
            ticker = "honey money",
            toast = True
        )
    # waiting time
        time.sleep(9)