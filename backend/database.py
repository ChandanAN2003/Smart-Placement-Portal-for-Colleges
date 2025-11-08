"""
Database connection and utility functions
"""
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env (for local dev)
load_dotenv()

class Database:
    def __init__(self):
        # Local defaults (for XAMPP)
        self.host = os.getenv("MYSQL_HOST", "localhost")
        self.user = os.getenv("MYSQL_USER", "root")
        self.password = os.getenv("MYSQL_PASSWORD", "")
        self.database = os.getenv("MYSQL_DB", "placement_portal")
        self.port = int(os.getenv("MYSQL_PORT", 3306))

        # Render / TiDB Cloud override (if available)
        self.host = os.getenv("DB_HOST", self.host)
        self.user = os.getenv("DB_USER", self.user)
        self.password = os.getenv("DB_PASSWORD", self.password)
        self.database = os.getenv("DB_NAME", self.database)
        self.port = int(os.getenv("DB_PORT", self.port))

        # Enable SSL only for TiDB Cloud (Render)
        self.ssl = {"ssl": {}} if os.getenv("DB_SSL", "False").lower() == "true" else None

        self.connection = None

    def connect(self):
        """Establish database connection"""
        try:
            print("--------------------------------------------------")
            print("🌍 Connecting to database...")
            print(f"Host: {self.host}")
            print(f"Port: {self.port}")
            print(f"User: {self.user}")
            print(f"Database: {self.database}")
            print(f"SSL: {'Enabled' if self.ssl else 'Disabled'}")
            print("--------------------------------------------------")

            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                ssl=self.ssl,  # ✅ enables secure connection for TiDB Cloud
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=False
            )
            print("✅ Database connection successful!")
            return self.connection
        except Exception as e:
            print(f"❌ Database connection error: {e}")
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
            print(f"❌ Query execution error: {e}")
            raise

    def close(self):
        """Close database connection"""
        if self.connection and self.connection.open:
            self.connection.close()
            print("🔒 Database connection closed.")

# Global instance
db = Database()
