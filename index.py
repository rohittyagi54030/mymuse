import os
os.system("pip3 install -r requirements.txt")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from pyvirtualdisplay import Display
from sys import platform
import os
import datetime
import random

runBatFile = "no"
autocontrol = 'yes'
refresh = 'yes'


runs = 100
run = 0

options = webdriver.ChromeOptions()
uas = []
import csv

print("Select Device(Enter 1 or 2):- \n1.Mobile\n2.Desktop")
device = 1

if device == 1:
    csv_file = "./UserAgentMobile.csv"
    device_name = "Mobile"
elif device == 2:
    csv_file = "./DesktopUserAgent.csv"
    device_name = "Desktop"
else:
    print("Try Again!")
    time.sleep(10)
    exit()


with open(csv_file, "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        uas.append(row)
ua = random.choice(uas)
print('ua', ua)
options.add_argument(f"user-agent={ua[0]}")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("detach", True)
# Autocontrol
if (autocontrol == 'yes'):
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1420,1080")
    display = Display(visible=0, size=(1420, 1080))
    display.start()

url = "https://superadme.com/tracker/click.php?key=hzmor0k6r86et4njrg0s"
while True:
    s_time = datetime.datetime.now()
    if run < runs:
        print(f"Running for {device_name}:- ", run)

        driver = webdriver.Chrome(ChromeDriverManager(version='114.0.5735.90').install(), options=options)

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        move = ActionChains(driver)
        driver.get(url)

        time.sleep(3)
        button = driver.find_element(By.ID, 'submit_birthdate')
        button.click()

        #refresh
        if refresh == 'yes':
            for i in range(4):
                print("Sleeping for 40 second to refresh")
                time.sleep(40)
                driver.refresh()

        # RunBat
        if (runBatFile == "yes"):
            if (platform == 'linux'):
                activeNetworks = os.popen('nmcli con show --active').read()
                splitedActiveNetworks = activeNetworks.split('\n')
                b = splitedActiveNetworks[1][:splitedActiveNetworks[1].find('-')]
                c = b.split(' ')
                d = " "
                c = c[:-1]
                e = d.join(c)
                e = e.strip()

                os.popen("nmcli con down '" + e + "'").read()
                print("connection disconnected")
                time.sleep(10)
                os.popen("nmcli con up '" + e + "'").read()
                print("connection established")
                time.sleep(50)
            else:
                # driver.switch_to.window(driver.window_handles[1])
                driver.execute_script('javascript:document.title="run_bat1"')
                time.sleep(7)
                print("Chaning to hello world")
                driver.execute_script('javascript:document.title="hello_world"')
                time.sleep(33)



        driver.quit()
        run += 1
    else:
        break
