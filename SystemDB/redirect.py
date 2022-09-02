from dotenv import load_dotenv
import os

class redirect():
    def __init__(self):
        self.names = os.getenv('DBNAME')
        self.host = os.getenv('DBHOST')
        self.user = os.getenv('DBUSER')
        self.passw = os.getenv('DBPASS')


   