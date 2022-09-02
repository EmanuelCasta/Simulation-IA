import __init__
from MySQLdb import _mysql
from dotenv import load_dotenv
import sys
#sys.path.insert(0, '../')
from redirect import redirect

class ConnectionDB():
    def __init__(self):
        load_dotenv()
        self.data =redirect()
    
    def connect(self):
        return _mysql.connect(self.data.host, self.data.user,self.data.passw,self.data.names)