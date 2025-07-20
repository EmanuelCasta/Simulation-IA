import __init__
from models.ConnectionDB import ConnectionDB


class DataBasePalabras():
    def __init__(self,name):
        self.db = ConnectionDB()
        self.name =name

    def run_query(self, query, fetch=False):
        conn = self.db.connect()
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall() if fetch else None
        conn.commit()
        cur.close()
        conn.close()
        return data

    def insert_palabra(self,nombre):
        pass

    def get_palabra(self):
        pass

class Busqueda(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"busqueda")
    
    def insert_palabra(self,nombre="busqueda"):
        try:
            self.run_query(
                """insert into busqueda (idLogicoCaracteristica, idLogicoClave, idLogicoComplementaria)
                   select idLogicoCaracteristica, idLogicoClave, idLogicoComplementaria
                   from logicocaracteristica
                   inner join logicoclave
                   inner join logicocomplementaria;"""
            )
            self.run_query(
                """insert into basesdatosbusqueda (idBasesDeDatos,idBusqueda,numeroArticulos)
                   select idBasesDeDatos,idBusqueda, null as numeroArticulos
                   from basesdedatos natural inner join busqueda;"""
            )
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")


    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM busqueda", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

class dbBases(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"db")
    
    def insert_palabra(self,nombre,link):
        try:
            self.run_query(
                f"INSERT INTO basesdedatos (nombre, link) VALUES ('{nombre}', '{link}');"
            )
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")


    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM basesdedatos", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

class LogicoCaracteristicas(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"logicocaracteristica")
    
    def insert_palabra(self,nombre="logicocaracteristica"):
        try:
            self.run_query(
                """INSERT INTO logicocaracteristica (idOperadorLogico, idPalabraCaracteristica)
                   SELECT idOperadorLogico,idPalabraCaracteristica
                   FROM scraping.palabracaracteristica AS os
                   INNER JOIN scraping.operadorlogico;"""
            )
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")


    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM logicocaracteristica", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

class LogicoCondicional(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"logicocondicional")
    
    def insert_palabra(self,nombre="logicocondicional"):
        try:
            self.run_query(
                """INSERT INTO logicocondicional (idOperadorLogico,idPalabraCondicional)
                   SELECT idOperadorLogico,idPalabraCondicional
                   FROM scraping.palabracondicional
                   INNER JOIN scraping.operadorlogico;"""
            )
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")


    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM logicocondicional", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

class LogicoClave(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"logicoclave")
    
    def insert_palabra(self,nombre="logicoclave"):
        try:
            self.run_query(
                """INSERT INTO logicoclave (idOperadorLogico,idPalabraClave)
                   SELECT idOperadorLogico,idPalabraClave
                   FROM scraping.palabraclave
                   INNER JOIN scraping.operadorlogico;"""
            )
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")


    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM logicoclave", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

class LogicoComplementaria(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"logicocomplementaria")
    
    def insert_palabra(self,nombre='logicocomplementaria'):
        try:
            self.run_query(
                """INSERT INTO logicocomplementaria (idOperadorLogico,idPalabraComplementaria)
                   SELECT idOperadorLogico,idPalabraComplementaria
                   FROM scraping.palabracomplementaria
                   INNER JOIN scraping.operadorlogico;"""
            )
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")


    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM logicocomplementaria", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

class Palabraclave(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"word_key")

    def insert_palabra(self,nombre):
        try:
            self.run_query(f"INSERT INTO palabraclave (nombre) VALUES ({nombre})")
        except Exception:
            print(f"[ERROR] Same {nombre} ,{self.name}")


    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM palabraclave", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

class Palabracaracteristica(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"word_features")

    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM palabracaracteristica", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name} ,{self.name}")
            return []

    def insert_palabra(self,nombre):
        try:
            self.run_query(f"INSERT INTO palabracaracteristica (nombre) VALUES ({nombre});")
        except Exception:
            print(f"[ADERROR] Same {nombre}")

class Palabracomplementaria(DataBasePalabras):
    def __init__(self):
            DataBasePalabras.__init__(self,"word_complementary")

    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM palabracomplementaria", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

    
    def insert_palabra(self,nombre):
        try:
            self.run_query(f"INSERT INTO palabracomplementaria (nombre) VALUES ({nombre})")
        except Exception:
            print(f"[ERROR] Same {nombre}  ,{self.name}")

class Palabracondicional(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"word_no_necessary")

    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM palabracondicional", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []
    
    def insert_palabra(self,nombre):
        try:
            self.run_query(f"INSERT INTO palabracondicional (nombre) VALUES ({nombre})")
        except Exception:
            print(f"[ERROR] Same {nombre}  ,{self.name}")

class Palabralogica(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"logic")

    def insert_palabra(self,nombre):
        try:
            self.run_query(f"INSERT INTO operadorlogico (nombre) VALUES ({nombre});")
        except Exception:
            print(f"[ERROR] Same {nombre}  ,{self.name}")

    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM scraping.operadorlogico order by idOperadorLogico asc", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

class Revista(DataBasePalabras):

    def __init__(self):
        DataBasePalabras.__init__(self,"revista")

    def insert_palabra(self,nombre):
        try:
            self.run_query(f"INSERT INTO revista (nombre, Q) VALUES ('{nombre}', '');")
        except Exception:
            print(f"[ERROR] Same {nombre}  ,{self.name}")

    def get_palabra(self):
        try:
            return self.run_query("SELECT * FROM revista", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

class Articulo(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"articulo")

    def insert_palabra(self,nombres):
        try:
            self.run_query(
                f"""INSERT INTO articulo (nombre, Fecha, Link_Descarga, idRevista, authors, pagestart, pageend, doi, resumen, llaves, volume, issue)
                VALUES ( '{nombres['Title']}', '{nombres['Year']}', '{nombres['Link']}', {nombres['Source title']}, '{nombres['Authors']}', '{nombres['Page start']}', '{nombres['Page end']}', '{nombres['DOI']}', '{nombres['Abstract']}', '{nombres['Author Keywords']}', '{nombres['Volume']}', '{nombres['Issue']}');"""
            )
            result = self.run_query(
                f"SELECT idArticulo FROM articulo where nombre='{nombres['Title']}';",
                fetch=True
            )
            return result
        except Exception:
            print(f"[ERROR] Same  {(nombres['Title'], self.name)}")
            return ()
        

    def get_caracteristics(self,pather):
        word ="""SELECT max(idArticulo) as max FROM articulo;"""
        try:
            return self.run_query(word, fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

    def get_palabra(self):
        try:
            return self.run_query("select * from articulo", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []

class BusquedaArticlo(DataBasePalabras):
    def __init__(self):
        DataBasePalabras.__init__(self,"buarticulo")

    def insert_palabra(self,nombres):
        try:
            self.run_query(
                f"INSERT INTO busquedaarticulo (idBusqueda, idArticulo) VALUES ('{nombres['idBusqueda']}', '{nombres['idArticulo']}');"
            )
        except Exception:
            print(f"[ERROR] Same  {self.name}")

    def get_palabra(self):
        try:
            return self.run_query("select * from busquedaarticulo", fetch=True)
        except Exception:
            print(f"[ERROR] {self.name}")
            return []



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

