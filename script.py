# python anti_private_IP_ubuntu.py
# make sure chromedriver.exe is the same version as the currently installed chrome
# ZTE F609 Modem

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os

ipAdrress = "http://192.168.1.1"
uName = "" #default ZTE Indihome username
uPassword = "" #default ZTE Indihome password

def restart():    
    browser.get(ipAdrress)

    username = browser.find_element_by_id("Frm_Username")
    password = browser.find_element_by_id("Frm_Password")
    submit   = browser.find_element_by_id("LoginId")

    username.send_keys(uName) 
    password.send_keys(uPassword)
    submit.click()

    #browser.get("http://192.168.1.1/getpage.gch?pid=1002&nextpage=manager_dev_conf_t.gch")
    browser.get(ipAdrress + "/getpage.gch?pid=1002&nextpage=manager_dev_conf_t.gch")

    reboot = browser.find_element_by_id("Submit1")
    reboot.click()

    reboot_confirm = browser.find_element_by_id("msgconfirmb")
    reboot_confirm.click()
    print("Modem ter-restart pada " + str(now))

def checkIP():
    browser.get(ipAdrress)

    username = browser.find_element_by_id("Frm_Username")
    password = browser.find_element_by_id("Frm_Password")
    submit   = browser.find_element_by_id("LoginId")

    username.send_keys(uName) 
    password.send_keys(uPassword)
    submit.click()

    browser.get(ipAdrress + "/getpage.gch?pid=1002&nextpage=IPv46_status_wan2_if_t.gch")
    IP_WAN = browser.find_element_by_id("TextPPPIPAddress0").get_attribute('value')
    print(IP_WAN)

    depan = IP_WAN.split(".")
    print(depan[0])
    if depan[0] == "10":
        print("Private IP")
        restart()
    else:
        print("Not private IP, skipping")

while True:
    # Headless mode to save RAM and GPU usage
    now = datetime.now()

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.BinaryLocation = "/usr/bin/chromium-browser"
    try:
      browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=options) 
      checkIP()
      browser.quit()
    except:
      print("Error, coba lagi")
      os.system("killall chromium-browser")
    print("Sleep for 1 hour")
    time.sleep(1*3600)
