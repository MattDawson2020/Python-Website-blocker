import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
# r tells python to interpret this as a string and ignore any  \n or other special characters
# script will access this file at certain times of day to add the website list to the prohibited site list, and then remove it later
redirect="127.0.0.1"
website_list=['www.facebook.com', 'facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("working hours")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                    # code block checks whether website is already on blocked list and passes
                else:
                    file.write(redirect+" "+website+"\n")
    #checks the current generated time but a fixed time of whether it is after 9am and before 5pm
    else:
      with open(hosts_path, 'r+') as file:
          content=file.readlines() # extract file as a list of the lines
          file.seek()
          # move cursor to the start of the file
          for line in content:
              if not any(website in line for website in website_list):
                  file.write(line)
                  #write the contents of the file minus the websites
          file.truncate()
          #remove everything after the code block finishes
      print("fun hours")
    time.sleep(5)
    #sleep the script for 5 seconds so the loop checks regularly but not at a frequency that drains the processor
