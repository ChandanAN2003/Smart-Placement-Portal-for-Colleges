"""
Database initialization script
"""
import os
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from database import db
from werkzeug.security import generate_password_hash

def init_database():
    """Initialize database with schema and seed data"""
    try:
        schema_path = Path(__file__).parent.parent / 'database' / 'schema.sql'
        if not schema_path.exists():
            schema_path = Path(__file__).parent.parent.parent / 'database' / 'schema.sql'

        if schema_path.exists():
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema_sql = f.read()

            statements = [s.strip() for s in schema_sql.split(';') if s.strip()]
            conn = db.connect()
            try:
                with conn.cursor() as cursor:
                    for statement in statements:
                        if statement:
                            cursor.execute(statement)
                conn.commit()
                print("✓ Database schema created successfully")
            finally:
                conn.close()

        create_default_users()
        print("✓ Database initialized successfully")

    except Exception as e:
        print(f"✗ Database initialization error: {e}")
        raise

def create_default_users():
    """Create default admin, HOD, and student users"""
    conn = db.get_connection()
    try:
        result = db.execute_query(
            "SELECT COUNT(*) as count FROM users WHERE role = 'tpo'",
            fetch_one=True
        )
        if result and result['count'] > 0:
            print("✓ Default users already exist")
            return

        # Default users
        tpo_password = generate_password_hash('admin123')
        db.execute_query(
            "INSERT INTO users (name, email, password_hash, role, department, is_approved) VALUES (%s,%s,%s,%s,%s,%s)",
            ('Admin TPO', 'tpo@college.edu', tpo_password, 'tpo', 'Placement', True)
        )

        hod_password = generate_password_hash('hod123')
        db.execute_query(
            "INSERT INTO users (name, email, password_hash, role, department, is_approved) VALUES (%s,%s,%s,%s,%s,%s)",
            ('Dr. John Smith', 'hod.cs@college.edu', hod_password, 'hod', 'Computer Science', True)
        )

        student_password = generate_password_hash('student123')
        db.execute_query(
            "INSERT INTO users (name, email, password_hash, role, department, is_approved) VALUES (%s,%s,%s,%s,%s,%s)",
            ('Alice Johnson', 'alice@college.edu', student_password, 'student', 'Computer Science', True)
        )

        print("✓ Default users created:")
        print("  TPO: tpo@college.edu / admin123")
        print("  HOD: hod.cs@college.edu / hod123")
        print("  Student: alice@college.edu / student123")

    except Exception as e:
        print(f"✗ Error creating default users: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # 🔥 Important: Don’t reset DB on Render!
    if os.getenv("RENDER") == "True":
        print("⚠️ Skipping database initialization on Render (production).")
    else:
        print("Initializing database locally...")
        init_database()
