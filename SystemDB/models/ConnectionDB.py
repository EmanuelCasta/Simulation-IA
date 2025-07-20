import __init__
import psycopg2
from dotenv import load_dotenv
from redirect import redirect

class ConnectionDB:
    def __init__(self):
        load_dotenv()
        self.data = redirect()

    def connect(self):
        return psycopg2.connect(
            host=self.data.host,
            user=self.data.user,
            password=self.data.passw,
            dbname=self.data.names
        )
