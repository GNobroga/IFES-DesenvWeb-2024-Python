import sqlite3
from enum import Enum

class DatabaseType(Enum):
    SQLITE = 0

class DatabaseFactory:
    
    @staticmethod
    def get_connection(db_type: DatabaseType):
        if db_type == DatabaseType.SQLITE:
            return sqlite3.connect('data.db')