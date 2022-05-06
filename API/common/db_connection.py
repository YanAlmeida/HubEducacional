from common.code_utils import SingletonMeta
from mysql.connector import connect
from os import getenv

class DBConnectionSingleton(metaclass=SingletonMeta):
    
    def __init__(self):
        self.conn = connect(
            user=getenv("USER_DB"),
            password=getenv("PASSWORD_DB", "apipassword"),
            database=getenv("DATABASE_NAME", "hubeducacional"),
            host=getenv("HOST_DB", "localhost"),
            port=getenv("PORT_DB", "3306")       
        )

    def get_conn(self):
        return self.conn

    def get_cursor(self):
        return self.conn.cursor()

    def commit_conn(self):
        self.conn.commit()

    def rollback_conn(self):
        self.conn.rollback()

    def end_conn(self):
        self.conn.close()
        DBConnectionSingleton._instances = {}
