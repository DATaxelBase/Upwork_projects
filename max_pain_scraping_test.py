#! /usr/bin/env python3

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path



    
driver = webdriver.Chrome()
# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('./scraping-uploading-02f2de4149d0.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)
sheet = client.open('Test_deployment')#Name of sheet
sheet_instance = sheet.get_worksheet(0)
records_data = sheet_instance.col_values(1)

issue_on = []
for el in range(2,len(records_data)):
    driver.get('https://maximum-pain.com/options/'+records_data[el]) #Access to element
    print(driver.title)
    with open('./Action_Results.txt', 'wb') as f:
        f.write(f"{driver.title}\n")