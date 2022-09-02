from tools.patch import webdriver_executable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException      
import time
import urllib.request
import os
import requests

import tools.patch

class initial():

    def __init__(self, search_key,headless=True, min_resolution=(0, 0), max_resolution=(1920, 1080), max_missed=10):
        while(True):
            try:
                #try going to www.google.com
                options = Options()
                #if(headless):
                    #options.add_argument('--headless')
                
                driver = webdriver.Chrome(self.get_folder(), chrome_options=options)
                driver.set_window_size(1300,620)
                driver.get("https://www.google.com")
                break
            except:
                
                #patch chromedriver if not available or outdated
                try:
                    driver
                except NameError:
                    is_patched = tools.patch.download_lastest_chromedriver()
                else:
                    is_patched = tools.patch.download_lastest_chromedriver(driver.capabilities['version'])
                if (not is_patched): 
                    exit("[ERR] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")
               
        self.driver = driver
        self.search_key= search_key
        self.url = search_key
        self.headless=headless
        self.min_resolution = min_resolution
        self.max_resolution = max_resolution
        self.max_missed = max_missed

    def get_folder(self):
        webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'tools\webdriver', webdriver_executable()))
        return webdriver_path
    
    def enter_url(self):
        self.driver.get(self.url)

    def get_driver(self):
        return self.driver
        