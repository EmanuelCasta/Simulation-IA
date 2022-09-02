import __init__
import os
from tools.functional.read import generate_words
from tools.functional.read import save,organizated_data_ScienceDirect
from models.Direct import Direct
from models.Scopus import Scopus
from tools.functional.patch import webdriver_executable
from controllador.controllerpalabras import controllerpalabras
from models.busqueda import BusquedaArticles
import pandas as pd

class controllerDB():

    def __init__(self,search_string,rules ,rev,limit=999999):
        self.webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'models/webdriver', webdriver_executable()))
        self.articules_path = os.path.normpath(os.path.join(os.getcwd(), 'articles'))
        self.search_string = search_string
        self.rules =rules
        self.rev =rev['nombre']
        self.outrev=rev
        self.limit= limit

    def ScrapingDirect(self):
        #Programa principal Direct
        
        directDB = Direct(self.webdriver_path,self.articules_path,self.search_string,self.rev)
        directDB.enter_systems()
        
        for count in range(len(self.search_string)):
            info =[]
            directDB.search_word(self.search_string[count],self.rules[count])
            info.append(directDB.find_article_urls())
            print("[INFO] NEXT WORD ",count )
            save(info,name="Direct.txt")
            idbusqueda=self.put_db(self.rules[count],info[len(info)-1])
            self.put_articule(organizated_data_ScienceDirect(last=True),idbusqueda)
            if count>=self.limit:
                break
            
        #GuardarInfo
        directDB.driver.close()
        del directDB

    def ScrapingScopus(self):
        ScopusDB = Scopus(self.webdriver_path,self.articules_path,self.search_string,self.rules,self.limit,self.rev)
        ScopusDB.enter_systems()
        ScopusDB.search_link()
        ScopusDB.search_word()
        ScopusDB.driver.close()
        del ScopusDB

    def put_articule(self,data,idBusqueda):
        controller = controllerpalabras()
        encontrarrevistas=controller.get_rev()
        
        ## Colocar el otro busqueda articulo mezlcado con el otro busqueda aqui mismo
        for count in range(len(data)):
            for i in range(len(encontrarrevistas['idRevista'])):
                if encontrarrevistas['nombre'][i].lower() == data.iloc[count]['Source title'].lower() :
                        idrevista = encontrarrevistas['idRevista'][i]
                        data.iloc[count]['Source title'] = idrevista
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
            if "sciencedirect" == encontrarbasesdatos['nombre'][count].lower():
                for key,value in meterIdDatosBsuqueda.items():
                    if key =="idBasesDatosBusqueda":
                        idBasesDatosBusqueda=value[count]
                        cantidad_articulos= file['number_articules']
                        bus.insertar_articulos(cantidad_articulos,idBasesDatosBusqueda)
                    if key == 'idBusqueda':
                        idBusqueda=value[count]

        return idBusqueda

