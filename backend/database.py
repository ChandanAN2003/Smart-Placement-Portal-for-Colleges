"""
Database connection and utility functions
"""
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.host = os.getenv('MYSQL_HOST', 'localhost')
        self.user = os.getenv('MYSQL_USER', 'root')
        self.password = os.getenv('MYSQL_PASSWORD', '')
        self.database = os.getenv('MYSQL_DB', 'placement_portal')
        self.connection = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=False
            )
            return self.connection
        except Exception as e:
            print(f"Database connection error: {e}")
            raise
    
    def get_connection(self):
        """Get existing connection or create new one"""
        if self.connection is None or not self.connection.open:
            return self.connect()
        return self.connection
    
    def execute_query(self, query, params=None, fetch_one=False, fetch_all=False):
        """Execute a query and return results"""
        conn = self.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                if fetch_one:
                    result = cursor.fetchone()
                elif fetch_all:
                    result = cursor.fetchall()
                else:
                    result = cursor.rowcount
                conn.commit()
                return result
        except Exception as e:
            conn.rollback()
            print(f"Query execution error: {e}")
            raise
    
    def close(self):
        """Close database connection"""
        if self.connection and self.connection.open:
            self.connection.close()

# Global database instance
db = Database()

