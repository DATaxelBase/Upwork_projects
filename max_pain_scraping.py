#! /usr/bin/env python3

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import time
import re
import os
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
data = {
  "type": str(os.environ["type"]),
  "project_id": str(os.environ["project_id"]),
  "private_key_id": str(os.environ["private_key_id"]),
  "private_key": str(os.environ["private_key"]),
  "client_email": str(os.environ["client_email"]),
  "client_id": str(os.environ["client_id"]),
  "auth_uri": str(os.environ["auth_uri"]),
  "token_uri": str(os.environ["token_uri"]),
  "auth_provider_x509_cert_url": str(os.environ["auth_provider_x509_cert_url"]),
  "client_x509_cert_url": str(os.environ["client_x509_cert_url"]),
  "universe_domain": str(os.environ["universe_domain"])
}
creds = ServiceAccountCredentials.from_json_keyfile_dict(data, scope)
# authorize the clientsheet 
client = gspread.authorize(creds)
sheet = client.open('Yvan')#Name of sheet
sheet_instance = sheet.get_worksheet(0)
records_data = sheet_instance.col_values(1)

issue_on = []
for el in range(2,len(records_data)):
    driver.get('https://maximum-pain.com/options/'+records_data[el]) #Access to element
    time.sleep(16)
    first_tab_values = [i.text for i in driver.find_elements(By.XPATH,'//table[@class = "table table-striped table-bordered"]//tr//td[@class ="AlignRight"]')[:4]]
    try:
        max_pain = first_tab_values[2]
        date_pain = first_tab_values[0]
        #print(max_pain)
        val = max_pain.split('$')[1]
        sheet_instance.update_cell(el+1,3,val)
        sheet_instance.update_cell(el+1,4,date_pain)
    except:
        issue_on.append(records_data[el])
        continue
print(issue_on)
