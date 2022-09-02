from model.Scrap import Scrap
from model.Maganized import Maganized
from model.database.DBMagnazed import DBMagnazed
import time
class controllerMagnazited():

    def __init__(self):
        self.magnazed = DBMagnazed()
        self.search_keys=self.get_magnized()
        self.urls,self.word =  self.get_words()

    
    def put_information(self):
        count = 0
        for url in self.urls:
            scrap = Scrap(url,self.word[count])
            if scrap.search_magnazine():
                information = scrap.get_characteristics()
                self.search_keys[count].country = information['COUNTRY']
                self.search_keys[count].cuart = information['Quartil']
                self.magnazed.insert_other_elements(self.search_keys[count])
            scrap.driver.quit()
            del scrap
            count =count+1
            

   

    def get_magnized(self):
        datas = self.magnazed.get_Maganized()
        search_keys=[]
        for data in datas:
            search_keys.append(Maganized(data['idRevista'].decode(encoding="utf-8"),data['Q'].decode(encoding="utf-8"),data['nombre'].decode(encoding="utf-8"),''))

        return  search_keys
          

    def get_words(self):
        urls= []
        names = []
        for search in self.search_keys:
            urls.append("https://www.scimagojr.com/journalsearch.php?q=%s"%(search.name))
            names.append(search.name)
        
        new_url =[]
        for url in urls:
            new_url.append("+".join(url.split(" ")))

        return new_url,names