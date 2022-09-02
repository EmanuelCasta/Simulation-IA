import __init__
from models.ConnectionDB import ConnectionDB


class DataBasePalabras():
    def __init__(self,name):
        self.db = ConnectionDB()
        self.name =name

    def insert_palabra(self,nombre):
        pass

    def get_palabra(self):
        pass

class Busqueda(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"busqueda")
    
    def insert_palabra(self,nombre="busqueda"):
        process = self.db.connect()
        try: 
            process.query(f"""insert into busqueda (idLogicoCaracteristica, idLogicoClave, idLogicoComplementaria) select  idLogicoCaracteristica, idLogicoClave, idLogicoComplementaria from logicocaracteristica inner join logicoclave inner join logicocomplementaria;""")
            process.query(f"""insert into basesdatosbusqueda (idBasesDeDatos,idBusqueda,numeroArticulos) select idBasesDeDatos,idBusqueda, null as numeroArticulos from basesdedatos natural inner join busqueda;""")
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")
        process.close()


    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM busqueda""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

class dbBases(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"db")
    
    def insert_palabra(self,nombre,link):
        process = self.db.connect()
        try: 
            process.query(f"""
            INSERT INTO basesdedatos (nombre, link) VALUES ('{nombre}', '{link}');
            """)
        except Exception:

            print(f"[ERROR] Same {nombre} ,{self.name}")
        process.close()


    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM basesdedatos""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

class LogicoCaracteristicas(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"logicocaracteristica")
    
    def insert_palabra(self,nombre="logicocaracteristica"):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO logicocaracteristica (idOperadorLogico, idPalabraCaracteristica) select idOperadorLogico,idPalabraCaracteristica  FROM scraping.palabracaracteristica as os inner join scraping.operadorlogico; ;""")
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")
        process.close()


    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM logicocaracteristica""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

class LogicoCondicional(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"logicocondicional")
    
    def insert_palabra(self,nombre="logicocondicional"):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO logicocondicional (idOperadorLogico,idPalabraCondicional)  select idOperadorLogico,idPalabraCondicional  FROM scraping.palabracondicional inner join scraping.operadorlogico; """)
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")
        process.close()


    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM logicocondicional""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

class LogicoClave(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"logicoclave")
    
    def insert_palabra(self,nombre="logicoclave"):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO logicoclave (idOperadorLogico,idPalabraClave) select idOperadorLogico,idPalabraClave  FROM scraping.palabraclave inner join scraping.operadorlogico;""")
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")
        process.close()


    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM logicoclave""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

class LogicoComplementaria(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"logicocomplementaria")
    
    def insert_palabra(self,nombre='logicocomplementaria'):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO logicocomplementaria (idOperadorLogico,idPalabraComplementaria)  select idOperadorLogico,idPalabraComplementaria  FROM scraping.palabracomplementaria inner join scraping.operadorlogico; """)
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")
        process.close()


    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM logicocomplementaria""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

class Palabraclave(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"word_key")

    def insert_palabra(self,nombre):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO palabraclave (nombre) VALUES ({nombre})""")
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")
        process.close()


    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM palabraclave""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

class Palabracaracteristica(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"word_features")

    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM palabracaracteristica""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name} ,{self.name}")
        process.close()

    def insert_palabra(self,nombre):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO palabracaracteristica (nombre) VALUES ({nombre});""")
        except Exception:
            print(f"[ADERROR] Same {nombre}")
        process.close()

class Palabracomplementaria(DataBasePalabras):
    def __init__(self):
            DataBasePalabras.__init__(self,"word_complementary")

    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM palabracomplementaria""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

    
    def insert_palabra(self,nombre):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO palabracomplementaria (nombre) VALUES ({nombre})""")
        except Exception:
            print(f"[ERROR] Same {nombre}  ,{self.name}")
        process.close()

class Palabracondicional(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"word_no_necessary")

    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM palabracondicional""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()
    
    def insert_palabra(self,nombre):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO palabracondicional (nombre) VALUES ({nombre})""")
        except Exception:
            
            print(f"[ERROR] Same {nombre}  ,{self.name}")
        process.close()

class Palabralogica(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"logic")

    def insert_palabra(self,nombre):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO operadorlogico (nombre) VALUES ({nombre});""")
        except Exception:
            print(f"[ERROR] Same {nombre}  ,{self.name}")
        process.close()

    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM scraping.operadorlogico order by idOperadorLogico asc""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

class Revista(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"revista")

    def insert_palabra(self,nombre):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO revista (nombre, Q) VALUES ('{nombre}', '');""")
        except Exception:
            print(f"[ERROR] Same {nombre}  ,{self.name}")
        process.close()

    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""SELECT * FROM revista""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

class Articulo(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"articulo")

    def insert_palabra(self,nombres):
        process = self.db.connect()
        try: 
       
            process.query(f"""INSERT INTO articulo ( nombre, Fecha, Link_Descarga, idRevista, authors, pagestart, pageend, doi, resumen, llaves, volume, issue) VALUES ( "{nombres['Title']}", "{nombres['Year']}", "{nombres['Link']}", {nombres['Source title']}, "{nombres['Authors']}","{nombres['Page start']}", "{nombres['Page end']}", "{nombres['DOI']}", "{nombres['Abstract']}", "{nombres['Author Keywords']}", "{nombres['Volume']}", '{nombres['Issue']}');""")
        except Exception:
            print(f"[ERROR] Same  {nombres['Title'],self.name}")
        process.close()
        process = self.db.connect()
        try:
            process.query(f"""SELECT idArticulo FROM articulo where nombre="{nombres['Title']}"; """)
            return process.use_result().fetch_row(maxrows=0,how=1)#[0]['idArticulo'].decode(encoding="utf-8")
        except:
            return ()
        

    def get_caracteristics(self,pather):
        word ="""SELECT max(idArticulo) as max FROM articulo;"""
        process = self.db.connect()
        try: 
            process.query(word)
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""select * from articulo""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()

class BusquedaArticlo(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"buarticulo")

    def insert_palabra(self,nombres):
        process = self.db.connect()
        try: 
            process.query(f"""INSERT INTO busquedaarticulo (idBusqueda, idArticulo) VALUES ('{nombres['idBusqueda']}', '{nombres['idArticulo']}');""")
        except Exception:
            print(f"[ERROR] Same  {self.name}")
        process.close()

    def get_palabra(self):
        process = self.db.connect()
        try: 
            process.query("""select * from busquedaarticulo""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            print(f"[ERROR] {self.name}")
        process.close()



class Palabras():
    def __init__(self):
        palabraClave = Palabraclave()
        palabraLogica = Palabralogica()
        palabracomplementaria = Palabracomplementaria()
        palabracondicional = Palabracondicional()
        palabracaracteristica = Palabracaracteristica()
        logicoComplementaria = LogicoComplementaria()
        LogicoCaracteristica = LogicoCaracteristicas()
        LogicoCondiciona = LogicoCondicional()
        LogicoClav = LogicoClave()
        busqueda = Busqueda()
        dbs= dbBases()
        rev= Revista()
        art =Articulo()
        busquedaArticulo = BusquedaArticlo()
        self.log = [busquedaArticulo,art,rev,dbs,busqueda,palabraClave,palabraLogica,palabracomplementaria,palabracondicional,palabracaracteristica,logicoComplementaria,LogicoCaracteristica,LogicoCondiciona,LogicoClav]


if __name__ == '__main__':

    name_Filters = {
        'word_features' : ['"Data mining"','"Genetic algorithms"','"Network algorithms"', '"Dynamic programming"', '"Game theory"', '"Graph theory"','"Clustering"','"Patterns"'],
        'word_key' : ['"Heart diagnostics"','"Heart failure"','"Cardiovascular diseases"','"Heart rhythms"','"Heart problem"','"Heart disease"','"Heart condition"','"Heart diseases"'],
        'word_complementary'  : ['"Artificial intelligence"','"Feature selection"','"Machine learning"','"Deep learning"','"Computer science"','"Computer programmed"','"Natural Language Processing"','"Computer"'],
    }
    logic= ['"AND"','"OR"','"NOT"']
    word_no_necessary = ['"Prototype"','"First study"','"Animals"','"Mhealth"','"Image"']

    palabras=Palabras()
    '''
    for key, values in name_Filters.items():
        for value in values:
            for palabra in palabras.log:
                if palabra.name.lower() == key.lower():
                    palabra.insert_palabra(value)

    for value in logic:
        for palabra in palabras.log:
            if palabra.name.lower() == 'logic':
                palabra.insert_palabra(value)
    
    for value in word_no_necessary:
        for palabra in palabras.log:
            if palabra.name.lower() == 'word_no_necessary':
                palabra.insert_palabra(value)
    
    


    ## IMprimir
    for info in palabras.log:
        for values in info.get_palabra():
            print(info.name)
            for key,value in values.items():
                print("Key: "+ key)
                print("Value :"+str(value.decode(encoding='utf-8')) )
                print("")
    
    ## IMprimir
    for info in palabras.log:
        for values in info.get_palabra():
            if info.name.startswith("logico"):
                print(info.name+"++++++++++++++++++++++++++++++++++++++++++")
                for key,value in values.items():
                    print("Key: "+ key)
                    print("Value :"+str(value.decode(encoding='utf-8')) )
                    print("")

    
    

    for palabra in palabras.log:
        if palabra.name.startswith("logico"):
            palabra.insert_palabra()'''

