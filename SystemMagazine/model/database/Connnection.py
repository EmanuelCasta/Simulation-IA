from MySQLdb import _mysql
from dotenv import load_dotenv
import os


class ConnectionDB():
    def __init__(self):
        load_dotenv()
        self.data ={
                'names': os.getenv('DBNAME'),
                'host' : os.getenv('DBHOST'),
                'user' : os.getenv('DBUSER'),
                'passw' : os.getenv('DBPASS')
        }
       
    
    def connect(self):
        return _mysql.connect(self.data['host'], self.data['user'],self.data['passw'],self.data['names'])

        
if __name__ == '__main__':
    c =ConnectionDB()
    c=c.connect()
    c.close()
    del c
    