from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException       

#import helper libraries
import time
import urllib.request
import os
import requests
import io
import tools.functional.patch as patch 
from tools.functional.read import move,delete_trash
from dotenv import load_dotenv
from datetime import date

class Direct():
    def __init__(self,webdriver_path, articules_path,name_Filters,rev,min_resolution=(0,0),max_resolution=(900,1000)):
        articules_path = os.path.join(articules_path, "articulos")
        if not os.path.exists(articules_path):
            print("[INFO] Create new folder")
        while True:
            try:
                options = Options()
                options.add_argument('--disable-gpu')
                #options.add_experimental_option('excludeSwitches', ['enable-logging'])
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
        self.rev=rev
        self.otherdata = {}
        self.driver = driver
        self.search_string = ""
        self.name_Filters= name_Filters
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
        time.sleep(1)
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
            time.sleep(1)
            button.click()

            #system database
            
            #self.driver.get(self.driver.find_element_by_xpath('//a[@class="btn btn-info"]').get_attribute('href'))
            
            
            #Select DB
            time.sleep(2)
            button = self.driver.find_element_by_xpath("//h2[contains(text(),'sciencedirect')]//ancestor::a[@id='recurso']").get_attribute('href')
            self.driver.get(button)
            time.sleep(1)
            self.driver.get(self.driver.find_element_by_xpath('//a[@class="anchor advanced-search-link anchor-default"]').get_attribute('href'))
            self.urlreset = self.driver.current_url
            time.sleep(1)
        except Exception:
            pass
    
    def search_word(self,search_string,rules):
        self.search_string=search_string
        self.rules = rules
        try:
            self.driver.find_element_by_xpath('//*[@id="qs"]').clear()
            time.sleep(1)
            texta = self.driver.find_element_by_xpath('//*[@id="qs"]').send_keys(self.search_string)
            button = self.driver.find_element_by_xpath('//button[@class="button button-primary move-right"]')
            button.click()
            time.sleep(1)
            texta.clear()
        except:
            pass

    def filtters_search(self,arr,posicion):
        art =arr
    
        posicionsTextData=[]
        counts = 0
        while True:
            try:
                try:
                    WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH,f'//form[@name="filters"]/child::div/div[{posicion}]//ol//button[@class="button-link facet-link-container u-font-sans button-link-primary"]'))).click()
                except:
                    print("SHOW MORE [INFO] No more")
                    pass

                #show_more = self.driver.find_element_by_xpath(f'//form[@name="filters"]/child::div/div[{posicion}]//ol//button[@class="button-link facet-link-container u-font-sans button-link-primary"]')
                #show_more.click()
                time.sleep(1)
                articletype = self.driver.find_element_by_xpath(f'//form[@name="filters"]/child::div/div[{posicion}]//ol')
                
                li =articletype.find_elements_by_xpath('./child::*')
                count = 1
                for i in li:
                    
                    for j in art:
                        text = ""
                        for x in i.text.split():
                            value = ''.join(''.join(x.split("(")).split(")")[0].split(","))
                            if value.isnumeric():
                                value= int(value)
                            if type(value)==str:
                                text = text+" "+value
                    
                        if j.lower() == text.lower().strip():
                            print("Filtters search [INFO] Information select"+i.text)
                            posicionsTextData.append(text.strip())
                            #mirar el div con div es el lugar de la section y el otro li count dejarlo como esta
                            try:
                                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,f'//form[@name="filters"]/child::div/div[{posicion}]//ol/child::li[{count}]'))).click()
                            except:
                                pass
                            #article = self.driver.find_element_by_xpath(f'//form[@name="filters"]/child::div/div[{posicion}]//ol/child::li[{count}]')
                            #article.click()
                            break
                    count = count + 1
                
                self.otherdata[posicion] = posicionsTextData
                break
            except:
                if counts >= 2:
                    counts = 0
                    break
                counts = counts + 1
                print("[ERROR] No filtter")

    def find_article_urls(self):
        print("[INFO] Scraping for DB link... Please wait.")
       
        try:
            # Filter date
            time.sleep(1)
            dates = self.driver.find_element_by_xpath('//ol')
            da =dates.find_elements_by_xpath('./child::*')
            today = date.today()
            dat = []
            for i in da:
                if int(''.join(i.text.split(' ')[0]).isnumeric()):
                    if int(''.join(i.text.split(' ')[0])) > int(today.year-5):
                        dat.append(int(''.join(i.text.split(' ')[0])))
            for i in range(len(dat)):
                a = dates.find_element_by_xpath(f'//label[@for="years-{str(dat[i])}"]//span[@class="checkbox-check checkbox-small checkbox-label-indent"]')
                a.click()
            time.sleep(1)
        except:
            pass
        # Filter article
        datas={
            2:['Book chapters','Review articles'],
            3:self.rev,
            4:["Computer Science","Engineering","Mathematics","Biochemistry", "Genetics and Molecular Biology","Neuroscience",'Medicine']
        }

        print("== FIND URL[INFO] Wait page")
        time.sleep(1)
        count = 0
        error=False
        for key, value in datas.items():
            while True:
                try:
                    print("== FIND URL [INFO] Recovery information")
                    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="search-body-results-text"][1]')))
                    n = ''.join(self.driver.find_element_by_xpath('//*[@class="search-body-results-text"][1]').text.split(' ')[0].split(','))
                    if int(''.join(self.driver.find_element_by_xpath('//*[@class="search-body-results-text"][1]').text.split(' ')[0].split(',')))>20:
                        self.otherdata = {}
                        self.filtters_search(value,key)
                    break
                except:
                    if count >= 2:
                        count = 0
                        break
                    try:
                        if str(self.driver.find_element_by_xpath('//*[@class="error-zero-results"]/child::p').text).lower().strip() == "No results found.".lower().strip():
                            print("== FIND URL [EXIT] No information ==")
                            error=True
                            break
                    except:
                        print("== FIND URL [PROBLEMS] Trying recovery information ==")
                        self.driver.refresh()
                    count = 1 + count
        
        self.urlactual =  self.driver.current_url
        if error:
            self.driver.get(self.urlreset)
            return self.info_system(error=True)


        data=self.info_system(n=n)
        self.driver.get(self.urlreset)
        return data

    def get_informations(self):
        count = 0
        delete_trash()
        while True:
            try:
                localtedButton='//ol[@class="ResultsPerPage hor-separated-list prefix suffix"]/child::*'
                WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, localtedButton)))
                cant = len(self.driver.find_elements_by_xpath(localtedButton))
                try:
                    localtedButton=f'//ol[@class="ResultsPerPage hor-separated-list prefix suffix"]/child::li[{cant}]//a'
                                        
                    WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, localtedButton)))
                    button = self.driver.find_element_by_xpath(localtedButton).get_attribute('href')
                    self.driver.get(button)
                    
                except:
                    pass
            except:
                pass
            
            try:
                localtedButton='//label[@for="select-all-results"]/child::span[1]'
                try:
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, localtedButton)))
                except:
                    print("[INFO] Wait information")
                self.driver.find_element_by_xpath(localtedButton).click()
                localtedButtonDowloand = '//div[@class="ExportAllLink"]/child::button[1]'
                try:
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, localtedButtonDowloand)))
                except:
                    print("[INFO] Wait information")
                self.driver.find_element_by_xpath(localtedButtonDowloand).click()
                getDowloand = '//div[@class="preview-body export-options"]/child::button[4]'
                try:
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, getDowloand)))
                except:
                    print("[INFO] Wait information")
                self.driver.find_element_by_xpath(getDowloand).click()
            except:
                pass   
                
            
            try:
                localtedButton= "//ol[@id='srp-pagination']//li[@class='pagination-link next-link']//a"
                WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, localtedButton)))
                button = self.driver.find_element_by_xpath(localtedButton).get_attribute('href')
                self.driver.get(button)
            except:
                return move()
        
        
  
    def info_system(self,error=False,n=0):
        data = {}
        if error:
            data['number_articules'] = n
        else:
            data['number_articules'] = n
            data['FileAboutArticule']= self.get_informations()
        data['Word use']=self.search_string
        data['Link'] = self.urlactual
        data['linkdbdirect'] = 'https://www.sciencedirect.com/'
        data['Logic_use']=self.rules
        data['OtherInformation'] = self.otherdata
        #data['QR']
        return data
                

        

        
    