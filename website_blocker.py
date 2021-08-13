import time
from datetime import datetime as dt
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
# r tells python to interpret this as a string and ignore any  \n or other special characters
# script will access this file at certain times of day to add the website list to the prohibited site list, and then remove it later
redirect="127.0.0.1"
website_list=['www.facebook.com', 'facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("working hours")
    #checks the current generated time but a fixed time of whether it is after 9am and before 5pm
    else:
      print("fun hours")
    time.sleep(5)
    #sleep the script for 5 seconds so the loop checks regularly but not at a frequency that drains the processor
