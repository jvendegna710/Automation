from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time;

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:/Users/JVendegna20/AppData/Local/Google/Chrome/User Data/Default") #Path to your chrome profile
options.add_argument("--start-maximized")
options.add_argument("disable-infobars"); 
w = webdriver.Chrome(executable_path="C:/Users/JVendegna20/Downloads/chromedriver.exe", chrome_options=options)

w.get('https://www.paycomonline.net/v4/ee/web.php/app/login')
username = w.find_element_by_id("txtlogin")
password = w.find_element_by_id("txtpass")
ssn = w.find_element_by_id("userpinid")

username.send_keys("username")

password.send_keys("password")

ssn.send_keys("lst4")

time.sleep(3)

loginbutton = w.find_element_by_id("btnSubmit")
#loginbutton.click()
loginbutton.send_keys("\n")
time.sleep(3)
w.get('https://www.paycomonline.net/v4/ee/web.php/timeclock/WEB00')

time = w.find_element_by_id("arrowtime").click()
webtime = w.find_element_by_id("liNav1").click()
