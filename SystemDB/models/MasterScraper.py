import __init__
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException       
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#import helper libraries
import time
import os
import tools.functional.patch as patch 
from tools.functional.read import move
from dotenv import load_dotenv



class MasterScraper():
    
    def __init__(self,webdriver_path, articules_path,search_strin,rules,rev,db,min_resolution=(0,0),max_resolution=(900,1000)):
        articules_path = os.path.join(articules_path, "articulos")
        if not os.path.exists(articules_path):
            print("[INFO] Create new folder")
        while True:
            try:
                options = Options()
                options.add_argument('--disable-gpu')
                driver = webdriver.Chrome(webdriver_path, chrome_options=options)
                driver.set_window_size(1040,920)
                driver.get("https://google.com")
                break
            except:
                try:
                    driver
                except NameError:
                    is_patched = patch.download_lastest_chromedriver()
                else:
                    is_patched = patch.download_lastest_chromedriver(driver.capabilities['version'])
                if (not is_patched): 
                    exit("[ERR] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")
        self.rules = []
        self.otherdata = {}
        self.setring = ""
        self.driver = driver
        self.db =db
        self.search_strin =search_strin
        self.rul=rules
        self.search_string = ""
        self.rev =rev
        self.webdriver_path = webdriver_path
        self.url = 'https://tdea.basesdedatosezproxy.com/login'
        self.urlreset =""
        self.urlactual=""
        self.headless = False
        self.min_resolution = min_resolution
        self.max_resolution = max_resolution

    def enter_systems(self):
        print("====== ENTER SYSTEM [INFO] Scraping for DB link... Please wait. ======")
        time.sleep(1)
        self.driver.get(self.url)
        load_dotenv()
        try:
            #System plataform
            button = self.driver.find_element_by_xpath('//button[@class="btn btn-outline-info"]')
            button.click()
            username = self.driver.find_element_by_xpath('//input[@id="form-username"]')
            password = self.driver.find_element_by_xpath('//input[@id="form-password"]')
            button = self.driver.find_element_by_xpath('//button[@class="btn"]')
            username.send_keys(os.getenv('APICAMPUS_KEY'))
            password.send_keys(os.getenv('APICAMPUS_SECRET'))
            button.click()

            
            #Select DB
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH,f"//h2[contains(text(),'{self.db}')]//ancestor::a[@id='recurso']")))
            button = self.driver.find_element_by_xpath(f"//h2[contains(text(),'{self.db}')]//ancestor::a[@id='recurso']").get_attribute('href')
            self.driver.get(button)
          
            
        except Exception:
            pass

    def get_informations(self):
        pass

    def info_system(self,NumerArticules,directbd,informationArticule):
        data = {}

        data['number_articules'] = int(''.join(NumerArticules.split(' ')[0].split(',')))
        data['FileAboutArticule']= informationArticule
        data['Word use']=self.search_string
        data['Link'] = self.urlactual
        data['linkdbdirect'] = directbd
        data['Logic_use']=self.rules
        data['OtherInformation'] = self.otherdata
        return data

    def search_word(self):
        pass

