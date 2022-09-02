import __init__
from models.DataBasePalabras import Palabras
from models.busqueda import BusquedaArticles

class controllerpalabras():

    def __init__(self,word_features = ['"Data mining"','"Genetic algorithms"','"Network algorithms"', '"Dynamic programming"', '"Game theory"', '"Graph theory"','"Clustering"','"Patterns"'],
                word_key = ['"Heart diagnostics"','"Heart failure"','"Cardiovascular diseases"','"Heart rhythms"','"Heart problem"','"Heart disease"','"Heart condition"','"Heart diseases"'],
                word_complementary  = ['"Artificial intelligence"','"Feature selection"','"Machine learning"','"Deep learning"','"Computer science"','"Computer programmed"','"Natural Language Processing"','"Computer"'], 
                logic= ['"AND"','"OR"','"AND NOT"'],word_no_necessary = ['"Mhealth"','"Image"'],
                rev=['International Journal Of Advanced Computer Science And Applications','Annals Of Operations Research','Cluster Computing','Arabian Journal For Science And Engineering','American Journal of Cardiology','International Journal Of Medical Informatics','IEEE Journal Of Biomedical And Health Informatics','Journal of Network and Computer Applications','Journal of Advanced Research','Journal of Building Engineering','Heart Rhythm','Revista Española de Cardiología','Journal of Cardiac Failure','Preventive Medicine','International Journal Of Environmental Research And Public Health','Journal Of Biomedical Informatics','Neural Networks','Engineering Applications of Artificial Intelligence','JACC: Cardiovascular Imaging','Artificial Intelligence in Precision Health, 2020','Personalized Health Systems for Cardiovascular Disease, 2022','Computers in Biology and Medicine','Journal of Cardiology','International Journal of Cardiology','Artificial Intelligence in Medicine','Computer Aided Chemical Engineering','European Journal of Operational Research','Computer Science Review','Expert Systems With Applications','Journal of the American College of Cardiology','Heart Failure Clinics','Advances In Intelligent Systems And Computing','Computer Methods and Programs in Biomedicine','Journal of King Saud University - Computer and Information Sciences','Advances in Computers','Canadian Journal of Cardiology']):
        self.name_Filters = {'word_features' : word_features, 'word_key' : word_key,'word_complementary'  : word_complementary,}
        self.logic= logic
        self.rev =rev
        self.infodb ={}
        self.word_no_necessary = word_no_necessary
        self.palabras=Palabras()

    def insertbd(self,name,link):
        for palabra in self.palabras.log:
            if palabra.name.startswith("db"):
                palabra.insert_palabra(name,link)
   
    def insertar_palabras(self):
        for key, values in self.name_Filters.items():
            for value in values:
                for palabra in self.palabras.log:
                    if palabra.name.lower() == key.lower():
                        palabra.insert_palabra(value)

        

        for value in self.logic:
            for palabra in self.palabras.log:
                if palabra.name.lower() == 'logic':
                    palabra.insert_palabra(value)
    
        for value in  self.word_no_necessary:
            for palabra in self.palabras.log:
                if palabra.name.lower() == 'word_no_necessary':
                    palabra.insert_palabra(value)

    def insertar_logic(self):
        for palabra in self.palabras.log:
            if palabra.name.startswith("logico"):
                palabra.insert_palabra()

    def insertar_searchs(self):
        for palabra in self.palabras.log:
            if palabra.name.startswith("busqueda"):
                palabra.insert_palabra()
 
    def insertar_rev(self):
        for value in self.rev:
            for palabra in self.palabras.log:
                if palabra.name.startswith("revista"):
                    palabra.insert_palabra(value)

    def insertar_articule(self,data):
        for palabra in self.palabras.log:
            if palabra.name.startswith("articulo"):
                return palabra.insert_palabra(data)
       
    def insertar_busquedaarticulo(self,data):
        for palabra in self.palabras.log:
            if palabra.name.startswith("buarticulo"):
                palabra.insert_palabra(data)

    

    def get_palabras(self):
        self.name_Filters['word_features'] =[]
        self.name_Filters['word_complementary'] =[]
        self.name_Filters['word_key'] =[]
        self.logic =[]
        self.word_no_necessary =[]
        for info in self.palabras.log:
            for values in info.get_palabra():
                for val in values.values():
                    if val == None:
                        continue
                    if not str.isdigit(val.decode(encoding='utf-8')):
                        for key in values.keys():
                                if key == "idPalabraCaracteristica":
                                    self.name_Filters['word_features'].append(f'"{val.decode(encoding="utf-8")}"')
                                if key=="idPalabraComplementaria":
                                    self.name_Filters['word_complementary'].append(f'"{val.decode(encoding="utf-8")}"')
                                if key=="idPalabraClave":
                                    self.name_Filters['word_key'].append(f'"{val.decode(encoding="utf-8")}"')
                                if key=="idOperadorLogico":
                                    self.logic.append(str(val.decode(encoding='utf-8')))
                                if key=="idPalabraCondicional":
                                    self.word_no_necessary.append(f'"{val.decode(encoding="utf-8")}"')
        
        return  self.name_Filters, self.logic,self.word_no_necessary

    def get_rev(self):
        info ={'nombre':[],'idRevista':[]}
        for palabra in self.palabras.log:
            if palabra.name.startswith("revista"):
                for values in palabra.get_palabra():
                    for key,val in values.items():
                            if val == None:
                                continue
                            if key=="idRevista":
                                info['idRevista'].append(f'{val.decode(encoding="utf-8")}')
                            if key=="nombre":
                                info['nombre'].append(f'{val.decode(encoding="utf-8")}')
        return info

    def get_db(self):
        self.infodb['idBasesDeDatos'] =[]
        self.infodb['nombre'] =[]
        for info in self.palabras.log:
            if info.name.startswith("db"):
                for values in info.get_palabra():
                    for key,val in values.items():
                            if val == None:
                                continue
                            if key == "idBasesDeDatos":
                                self.infodb['idBasesDeDatos'].append(f'{val.decode(encoding="utf-8")}')
                            if key=="nombre":
                                self.infodb['nombre'].append(f'{val.decode(encoding="utf-8")}')
        return self.infodb

    def get_all_combination(self,namedb):
        busqueda= BusquedaArticles()
        info ={}
        info['NombreClave']=[]
        info['LogicaClave']=[]
        info['Nombrecaracteristica']=[]
        info['LogicaCaracteristica']=[]
        info['NombreComplementario']=[]
        info['LogicaComplementaria']=[]
        encontrarbasesdatos=self.get_db()
        
        
        for count in range(len(encontrarbasesdatos['nombre'])):
            if namedb.lower() == encontrarbasesdatos['nombre'][count].lower():
                    ids=encontrarbasesdatos['idBasesDeDatos'][count]
                        
                      

                        
        for values in busqueda.get_combination(ids):
            for key,val in values.items():
                if key=="NombreClave":
                    info['NombreClave'].append(f'"{val.decode(encoding="utf-8")}"')
                if key=="LogicaClave":
                    info['LogicaClave'].append(f'{val.decode(encoding="utf-8")}')
                if key=="Nombrecaracteristica":
                    info['Nombrecaracteristica'].append(f'"{val.decode(encoding="utf-8")}"')
                if key=="LogicaCaracteristica":
                    info['LogicaCaracteristica'].append(f'{val.decode(encoding="utf-8")}')
                if key=="NombreComplementario":
                    info['NombreComplementario'].append(f'"{val.decode(encoding="utf-8")}"')
                if key=="LogicaComplementaria":
                    info['LogicaComplementaria'].append(f'{val.decode(encoding="utf-8")}')
        
        return info

    def get_numbersA(self,nombreClave,operadorClave,nombreCaracteristica,operadorCaracteristica,nombreComplemento, operadorComplemetp):
        busqueda= BusquedaArticles()
        info ={}
        info['idBasesDeDatos']=[]
        info['idBusqueda']=[]
        info['NombreClave']=[]
        info['LogicaClave']=[]
        info['Nombrecaracteristica']=[]
        info['LogicaCaracteristica']=[]
        info['NombreComplementario']=[]
        info['LogicaComplementaria']=[]
        info['numeroArticulos'] =[]
        info['idBasesDatosBusqueda'] =[]
        for values in busqueda.get_palabra(nombreClave,operadorClave,nombreCaracteristica,operadorCaracteristica,nombreComplemento, operadorComplemetp):
            for key,val in values.items():
                if key == "idBasesDeDatos":
                    info['idBasesDeDatos'].append(f'{val.decode(encoding="utf-8")}')
                if key == "idBasesDatosBusqueda":
                   info['idBasesDatosBusqueda'].append(f'{val.decode(encoding="utf-8")}')
                if key == "idBusqueda":
                   info['idBusqueda'].append(f'{val.decode(encoding="utf-8")}')
                if key=="NombreClave":
                    info['NombreClave'].append(f'{val.decode(encoding="utf-8")}')
                if key=="LogicaClave":
                    info['LogicaClave'].append(f'{val.decode(encoding="utf-8")}')
                if key=="Nombrecaracteristica":
                    info['Nombrecaracteristica'].append(f'{val.decode(encoding="utf-8")}')
                if key=="LogicaCaracteristica":
                    info['LogicaCaracteristica'].append(f'{val.decode(encoding="utf-8")}')
                if key=="NombreComplementario":
                    info['NombreComplementario'].append(f'{val.decode(encoding="utf-8")}')
                if key=="LogicaComplementaria":
                    info['LogicaComplementaria'].append(f'{val.decode(encoding="utf-8")}')
                if key=="numeroArticulos":
                    if val == None:
                        info['numeroArticulos'].append(None)
                    else:
                        info['numeroArticulos'].append(f'{val.decode(encoding="utf-8")}')
        
        return info
    
    



    

if __name__ == '__main__':
    
    logic= ['AND','OR','NOT']
    word_no_necessary = ['"Prototype"','"Mhealth"','"Image"']
    controllerpalabras().insertar_palabras()
    controllerpalabras().mostrar_palabras()