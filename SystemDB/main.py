import os
from tools.functional.read import generate_words
from controllador.controllerpalabras import controllerpalabras
from controllador.controllerDB import controllerDB
import time


def startScrap(db):
    controller = controllerpalabras()
    controller.insertbd('Scopus',f'http://Scopus.com')
    controller.insertbd('ScienceDirect',f'http://ScienceDirect.com')
    controller.insertar_palabras()
    controller.insertar_logic()
    controller.insertar_searchs()
    controller.insertar_rev()

 
    numerMaxiwAIT = 50
    del controller
    while True:
        controller = controllerpalabras()
        try:
            
            rev=controller.get_rev()
            search_string,rules = generate_words(controller.get_all_combination(db))
            #Programa principal 
            controllerScraping = controllerDB(search_string,rules ,rev,limit=200)
            if db.lower() == 'scopus':
                controllerScraping.ScrapingScopus()
            else:
                controllerScraping.ScrapingDirect()
            
            break
        except:
            del controller
            time.sleep(10)
            if numerMaxiwAIT <= 0:
                break
            numerMaxiwAIT -= 1
    del controllerScraping


if __name__ == "__main__":
    variable = int(input("""Copia la BD 
    1- Scopus *** 
    2- ScienceDirect ***
:"""))
    if variable == 1:
        startScrap('Scopus')
    else:
        startScrap('ScienceDirect')
    #Definir palabras actualizar bases de datos y estructurarla
    





   