import __init__
from models.MasterScraper import MasterScraper
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tools.functional.patch import webdriver_executable
from controllador.controllerpalabras import controllerpalabras
from tools.functional.read import generate_words
from tools.functional.read import move
from tools.functional.read import save,organizated_data_Scopus,delete_trash
from models.busqueda import BusquedaArticles

class Scopus(MasterScraper):

    def __init__(self,webdriver_path, articules_path,search_strin,rules,limit,rev,search_string="scopus"):
        MasterScraper.__init__(self,webdriver_path, articules_path,search_strin,rules,rev,search_string)
        self.limit = limit
        
    def search_link(self):
        print("[INFO] ENTER ADVANCED DOCUMENT")
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,f'//a[@class="alt"][1]')))
        except:
            print("[ERROR] No found link")
            pass
        
        self.driver.get(self.driver.find_element_by_xpath('//a[@class="alt"][1]').get_attribute('href'))
        self.urlreset = self.driver.current_url
        time.sleep(1)

    def get_informations(self,numbers,repeat=True):
        count = 0
        if repeat:
            while True:
                
                    delete_trash(names='scopus')
                    try:
                    
                            error = self.driver.find_element_by_xpath('//span[@id="pageTitleHeader"]')
                            if error.text.strip().lower() == 'error':
                                self.driver.get(self.urlreset)
                                print("[ERROR] ERROR PAGE")
                                return -1
                            else:
                                WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="ssadawsdwas"]')))
                                self.driver.find_element_by_xpath('//*[@id="ssadawsdwas"]')
                    except:
                            print("[INFO]  CORRECT")
                    try:
                        selectAll = '//label[@class="checkbox-label noLabel"]'
                        selectAll = self.driver.find_element_by_xpath(selectAll)
                        self.driver.execute_script("arguments[0].click();", selectAll)
                    except:
                        print("[ERROR ] NO FOUND selectAll")


                    try:
                        selecExport = '//button[@id="export_results"]'
                        selecExport = self.driver.find_element_by_xpath(selecExport)
                        self.driver.execute_script("arguments[0].click();", selecExport)
                    except:
                        print("[ERROR ] NO FOUND selectAll")
                        return -2

                    ####
                    try:
                        cvsForm = '//input[@name="exportRadio" and @id="CSV"]'
                        cvsForm =  self.driver.find_element_by_xpath(cvsForm)
                        self.driver.execute_script("arguments[0].click();", cvsForm)
                    except:
                        print("[ERROR ] NO FOUND selectAll")

                    

                    try:
                        abstractKeywords = '//label[@for="selectedAbstractInformationItemsAll-Export"]'
                        WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,abstractKeywords)))
                        abstractKeywords = self.driver.find_element_by_xpath(abstractKeywords)
                        self.driver.execute_script("arguments[0].click();", abstractKeywords)
                    except:
                        print("[ERROR ] NO FOUND selectAll")

                    try:
                        abstractDetails = '//label[@for="selectedFundInformationItemsAll-Export"]'
                        WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,abstractDetails)))
                        abstractDetails = self.driver.find_element_by_xpath(abstractDetails)
                        self.driver.execute_script("arguments[0].click();", abstractDetails)
                    except:
                        print("[ERROR ] NO FOUND selectAll")
                        
                    

                    export = '//button[@class="btn btn-primary btn-sm btnEnable"]'
                    export = self.driver.find_element_by_xpath(export)
                    self.driver.execute_script("arguments[0].click();", export)


                    time.sleep(5)

                    return move(names='scopus',extension='.csv',number=numbers)
                
        else:
          
            while True:
                try:
                    delete_trash(names='scopus')
                    try:
                            error = self.driver.find_element_by_xpath('//span[@id="pageTitleHeader"]')
                            if error.text.strip().lower() == 'error':
                                self.driver.get(self.urlreset)
                                print("[ERROR] ERROR PAGE")
                                return -1
                            else:
                                WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="ssadawsdwas"]')))
                                self.driver.find_element_by_xpath('//*[@id="ssadawsdwas"]')
                    except:
                            print("[INFO] CORRECT")
                    
                    try:
                        selectAll = '//label[@class="checkbox-label noLabel"]'
                        selectAll = self.driver.find_element_by_xpath(selectAll)
                        self.driver.execute_script("arguments[0].click();", selectAll)
                    except:
                        print("[ERROR ] NO FOUND selectAll")

                   
                    try:
                        selecExport = '//button[@id="export_results"]'
                        selecExport = self.driver.find_element_by_xpath(selecExport)
                        self.driver.execute_script("arguments[0].click();", selecExport)
                    except:
                        print("[ERROR ] NO FOUND selectAll")
                      
                    ####
                    
                    
                    export = '//button[@title="Export"]'
                    export = self.driver.find_element_by_xpath(export)
                    self.driver.execute_script("arguments[0].click();", export)


                    

                    return move(names='scopus',extension='.csv',number=numbers)
                except:
                    print("[ERROR PROBLEM] No found file")
                    return {'error':"No information"}
   
    def filtters_information(self):
        print("[INFO] Filtters Scopus")
        
        try:
            try:
                WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::*')))
            except:
                print("[Error] No found Principal")
            filters = self.driver.find_element_by_xpath('//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]')
            filters = filters.find_elements_by_xpath('./child::*')
            count = 0
            datas={
                    1:['2023','2022','2021','2020','2019','2018'],
                    2:['Book Chapter','Book chapters','Review articles','Review'],
                    3:self.rev,
                    4:["Computer Science","Engineering","Mathematics","Biochemistry", "Genetics and Molecular Biology","Neuroscience",'Medicine']
            }
            can = len(datas)
            for i in range(2,len(filters)):
                infototal = []
                if count > can-1:
                    break
                

                try:
                    WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//div[@class="dragDropBox"]//button')))
                    viewmoretitle = self.driver.find_element_by_xpath(f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//div[@class="dragDropBox"]//button')
                
                    if "False"==str(viewmoretitle.get_attribute('aria-expanded')).strip().capitalize():
                        print("[INFO] MORE INFORMATION")
                        self.driver.execute_script("arguments[0].click();", viewmoretitle)
                except:
                    print("[ADVE] NO MORE TITLE")
        
                
                try:
                    WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//ul[starts-with(@class,"list")]/child::*//a')))
                    viewmore=self.driver.find_element_by_xpath(f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//ul[starts-with(@class,"list")]/child::*//a')
                    viewmore.click()
                except:
                    print("[ADVE] NO MORE")

                
                try:
                    WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//ul')))
                    variables = self.driver.find_element_by_xpath(f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//ul')
                    variables = variables.find_elements_by_xpath('./child::*')
                except:
                    print("[ADVE] NO FOUND ITEM")

                try:                                                                                                  
                    WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//div[starts-with(@id,"cluster")]//ul[2]')))
                    variableshidden = self.driver.find_element_by_xpath(f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//div[starts-with(@id,"cluster")]//ul[2]')
                    variableshidden = variableshidden.find_elements_by_xpath('./child::*')
                except:
                    print("[ADVE] NO FOUND ITEM HIDDEN")

                unique = True
                error = False         
                posicionDelete = 0
                for posicion,values in datas.items():
                    posicionsTextData=[]
                    for value in values:
                        
                        for j in range(1,len( variables)+1):  
                            try:
                                WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//div[starts-with(@id,"cluster")]//ul/child::li[{j}]//label[@class="checkbox-label"]//span')))
                                if self.driver.find_element_by_xpath(f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//div[starts-with(@id,"cluster")]//ul/child::li[{j}]//label[@class="checkbox-label"]//span').text.strip().lower() == value.strip().lower():
                                    posicionsTextData.append(value)
                                    buttons = self.driver.find_element_by_xpath(f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//div[starts-with(@id,"cluster")]//ul/child::li[{j}]//label[@class="checkbox-label"]')
                                    buttons.click()
                                    if unique:
                                        unique =False
                                    posicionDelete = posicion
                                   
                                    print(f"[INFO] SELECT {value},{posicionDelete}")
                            except:
                                print("[ADVE] No found item no hidden")
                                error =True
                                break
                        for j in range(1,len( variableshidden)+1):
                            try:
                                WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//div[starts-with(@id,"cluster")]//ul[2]/child::li[{j}]//label[@class="checkbox-label"]//span')))
                                if self.driver.find_element_by_xpath(f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//div[starts-with(@id,"cluster")]//ul[2]/child::li[{j}]//label[@class="checkbox-label"]//span').text.strip().lower() == value.strip().lower():
                                    posicionsTextData.append(value)
                                    buttons = self.driver.find_element_by_xpath(f'//*[@id="RefineResults"][1]/child::div[2]/child::div[1]/child::div[3]/child::div[4]/child::div[{i}]//div[starts-with(@id,"cluster")]//ul[2]/child::li[{j}]//label[@class="checkbox-label"]')
                                    buttons.click()
                                    if unique:
                                        unique =False
                                    posicionDelete = posicion
                                    
                                    print(f"[INFO] SELECT {value},{posicionDelete}")
                            except:
                                print("[ADVE] No found item hidden")
                                error =True
                                break
                        
                        if error:
                            break
                    infototal.append(posicionsTextData)
                    if error or not unique:
                        break
                
                if not unique :
                    
                    self.otherdata[posicionDelete] = infototal[0]
                    print(f"[INFO] NUMBERS OF FILTTERS FOUND {count}")
                    count = count + 1

                if posicionDelete>0:
                    del datas[posicionDelete]
                    posicionDelete = 0
                
                
            
            
            pathlimit ='//div[@id="leftSideBar"]/child::div[3]//div[@class="bottom"]//div[@class="refineButtons"]//ul/child::li[1]//input'
            try:
                WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.XPATH,pathlimit)))
                pathlimit = self.driver.find_element_by_xpath(pathlimit)
                pathlimit.click()
            except:
                print("[ERROR] NO CLICK")




        except:
            print("[ERROR] No found Filtters")
    
    def info_system(self,NumerArticules,directbd,informationArticule):
        data = {}
        if NumerArticules != 0:
            data['number_articules'] = int(''.join(NumerArticules.split(' ')[0].split(',')))
        else:
            data['number_articules'] = NumerArticules
        data['FileAboutArticule']= informationArticule
        data['Word use']=self.setring
        data['Link'] = self.urlactual
        data['linkdbdirect'] = directbd
        data['Logic_use']=self.rules
        data['OtherInformation'] = self.otherdata
        return data

    def search_word(self):
        print("[INFO] Searching information")
        
        repeat =True
        for count in range(len(self.search_strin)):
            info =[]
            self.setring = ""
            self.urlactual =  ""
            self.otherdata={}
            self.driver.get(self.urlreset)
            
            print(f"====================== Next word {count+1} ========================")
            try:
                    try:
                
                        error = self.driver.find_element_by_xpath('//span[@id="pageTitleHeader"]')
                        if error.text.strip().lower() == 'error':
                            self.driver.get(self.urlreset)
                            print("Error")
                            continue
                        else:
                            WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="ssadawsdwas"]')))
                            self.driver.find_element_by_xpath('//*[@id="ssadawsdwas"]')
                    except:
                        print("[INFO] COMPLETE SYSTEM OPERATION")
                        
                    try:
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="contentEditLabel"]')))
                    except:
                        print("[ERROR] No found link")
                        return
                        
                    try:
                        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="searchfield"]')))
                        self.driver.find_element_by_xpath('//*[@id="searchfield"]').clear()
                        self.driver.find_element_by_xpath('//*[@id="searchfield"]').send_keys(self.search_strin[count])
                        button = self.driver.find_element_by_xpath('//*[@id="advSearch"]')
                        button.click()
                    except:
                        print("[ERROR] No found ")
                        continue
                    
                    #Filter parameters
                    self.filtters_information()
                    
                    #Filters number articules
                    try:
                        pathNumerArticules ="//h1[@class='documentHeader']//span[@class='resultsCount']"
                        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH,pathNumerArticules)))
                        pathNumerArticules = self.driver.find_element_by_xpath(pathNumerArticules).text.strip()
                    except:
                        pathNumerArticules = 0
                    
                    
                    
                    #Infomaticon
                    information =self.get_informations(count+1,repeat=repeat)
                    if information == -1:
                        count = count -1
                        self.rules = ""
                        self.setring=""
                        self.urlactual = self.driver.current_url
                        info.append(self.info_system(0,'https://www.scopus.com/',"None"))
                        continue
                    
                    if information != -2:
                        if repeat:
                            repeat =False
                    self.setring = self.search_strin[count]
                    self.rules=self.rul[count]
                    self.urlactual =  self.driver.current_url
                    info.append(self.info_system(pathNumerArticules,'https://www.scopus.com/',information))
                    
            except:
                continue
            save(info,name='DataScopus.txt')
            idbusqueda=self.put_db(self.rules,info[len(info)-1])
            self.put_articule(organizated_data_Scopus(last=True),idbusqueda)
            if count>=self.limit:
                break
            
    def put_articule(self,data,idBusqueda):
        controller = controllerpalabras()
        encontrarrevistas=controller.get_rev()
        
        
        ## Colocar el otro busqueda articulo mezlcado con el otro busqueda aqui mismo
        if type(data) != list:
            if not data.empty:
                for count in range(len(data)):
                    for i in range(len(encontrarrevistas['idRevista'])):
                        if encontrarrevistas['nombre'][i].lower() == data.iloc[count]['Source title'].lower() :    
                                idrevista = encontrarrevistas['idRevista'][i]
                                data.loc[count,'Source title']= idrevista
                                idArticulo =controller.insertar_articule(data.iloc[count])
                                if idArticulo == () :
                                    break
                                idArticulo= idArticulo[0]['idArticulo'].decode(encoding="utf-8")
                                datas ={'idArticulo': idArticulo,'idBusqueda':idBusqueda}
                                controller.insertar_busquedaarticulo(datas)
                                break
        
        
        
    def put_db(self,rules,file):
        controller = controllerpalabras()
        bus = BusquedaArticles()
        encontrarbasesdatos=controller.get_db()
        
        meterIdDatosBsuqueda=controller.get_numbersA(rules['words'][0],rules['logic'][0],rules['words'][1],rules['logic'][1],rules['words'][2],rules['logic'][2])
        
        for count in range(len(encontrarbasesdatos['nombre'])):
            if "scopus" == encontrarbasesdatos['nombre'][count].lower():
                for key,value in meterIdDatosBsuqueda.items():
                    if key =="idBasesDatosBusqueda":
                        idBasesDatosBusqueda=value[count]
                        cantidad_articulos= file['number_articules']
                        bus.insertar_articulos(cantidad_articulos,idBasesDatosBusqueda)
                    if key == 'idBusqueda':
                        idBusqueda=value[count]

        return idBusqueda
    
        

if __name__ == "__main__":
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    articules_path = os.path.normpath(os.path.join(os.getcwd(), 'articles'))
    
    #Agregar palabras
    controller = controllerpalabras()
    controller.insertar_palabras()
    name_Filters,logic,word_no_necessary = controller.get_palabras()

    #Programa principal Direct
    info =[]
    directDB = Scopus(webdriver_path,articules_path,name_Filters,logic,word_no_necessary)
    directDB.enter_systems()
    directDB.search_link()
    directDB.search_word()

    del directDB
    