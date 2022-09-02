from model.database.Connnection import ConnectionDB
from model.Maganized import Maganized

class DBMagnazed(ConnectionDB):
    
    def __init__(self):
        ConnectionDB.__init__(self)

    def get_Maganized(self):
        process = self.connect()
        stringQuery = "SELECT * FROM scraping.revista where country is null and nombre is not null;"
        try:
            process.query(stringQuery)
            result = process.use_result().fetch_row(maxrows=0,how=1)
            process.close()
            return result
        except:
            process.close()
            return -1

    def insert_other_elements(self,maganized):
        process = self.connect()
        stringQuery = f"""update revista set q = '{maganized.cuart}', country = '{maganized.country}' WHERE idRevista ={maganized.idrevista}"""
        try:
            process.query(stringQuery)

            process.close()
            return True
        except:
            pass
        process.close()
        return False

        
        


if __name__ == '__main__':
    a = DBMagnazed()
    a.get_Maganized()