from tools.initial import initial
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import numpy as np
import re
from unicodedata import normalize

class Scrap(initial):

    def __init__(self,search_key,word):
        initial.__init__(self,search_key)
        self.driver.get(self.url)
        self.word=word
        


    def search_magnazine(self):
        pattern = "//div[@class='search_results']//child::a"
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,pattern)))
            posiblesNames= self.driver.find_elements_by_xpath(pattern)
        except:
            print("[ERROR] No found elements")

        pattern = './/span'
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,pattern)))
            for names in posiblesNames:
                result = names.find_element_by_xpath(pattern)
                s = self.word.lower()
                s = re.sub(
                        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
                        normalize( "NFD", s), 0, re.I
                    )
                s = normalize( 'NFC', s)
                b = self.word.lower()
                b = re.sub(
                        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
                        normalize( "NFD", b), 0, re.I
                    )
                b = normalize( 'NFC', b)
                if s==b:
                    result.click()
                    break
            
            return True
        except:
            print("[ERROR] No found element")
            return -1
    
    def get_characteristics(self):
        dataDataBase = {
            'COUNTRY':"",
            "Quartil":""
        }
        patternCountry="//div[@class='journalgrid']//child::div"
        patternCountryPart = './/h2'
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,patternCountry)))
            posiblesNames= self.driver.find_elements_by_xpath(patternCountry)
        except:
            print("[ERROR] No found other elements")
            dataDataBase['COUNTRY']="Error"
            dataDataBase['Quartil']="they took out the magazine"
            return dataDataBase
        
        # Search for each data element if the information is found, then insert that information

        #Get country
        for key in dataDataBase.keys():
            for names in posiblesNames:
                try:
                    if names.find_element_by_xpath(patternCountryPart).text.lower()==key.lower():
                        dataDataBase[key]=names.find_element_by_xpath(".//a").text.lower()
                except:
                    pass

        patternCube="//div[@class='combo_button table_button']"
        self.driver.find_element_by_xpath(patternCube).click()

        #Get quartil
        # Sort by largest number of quartile
        now = str(datetime.now()).split('-')

        Q=[]
        uniqueQ=[]
        try:
            tbody = self.driver.find_elements_by_xpath('//div[@class="dashboard"][1]/child::div[1]/child::div[2]/child::div[2]//table/tbody/child::*')
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="dashboard"][1]/child::div[1]/child::div[2]/child::div[2]//table/tbody/child::*')))
        except:
            pass
        for td in tbody:
            if str(int(now[0])) in str(td.text) or str(int(now[0])-1) in str(td.text):
                cuartil =str(td.text).split(" ")[-1:][0]
                if not cuartil in uniqueQ:
                    uniqueQ.append(cuartil)
                Q.append(cuartil)
        
        result = {'Q':Q}
        df= pd.DataFrame(result)

        maxnumber=df.groupby('Q')['Q'].count().max()
        Q=[]
        for cuartil in uniqueQ:
            if maxnumber == df.groupby('Q')['Q'].count()[str(cuartil)]:
                Q.append(cuartil)

        cuartilnumber = 9999
        cuartil = ""
        for maxcuartil in Q:
            if int("".join(maxcuartil.split("Q")))< cuartilnumber:
                cuartilnumber = int("".join(maxcuartil.split("Q")))
                cuartil=maxcuartil
        if cuartil == '':
            cuartil='No quartil'
        dataDataBase['Quartil'] =cuartil
        return dataDataBase


        

    

