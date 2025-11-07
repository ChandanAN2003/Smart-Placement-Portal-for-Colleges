"""
Setup script for the Placement Portal
"""
import os
import sys
from pathlib import Path

def setup_environment():
    """Create .env file from template if it doesn't exist"""
    env_path = Path(__file__).parent / '.env'
    template_path = Path(__file__).parent.parent / 'docs' / 'env_example.txt'
    
    if env_path.exists():
        print("✓ .env file already exists")
        return
    
    if template_path.exists():
        print("Creating .env file from template...")
        with open(template_path, 'r') as template:
            with open(env_path, 'w') as env_file:
                env_file.write(template.read())
        print("✓ .env file created. Please edit it with your credentials.")
    else:
        print("✗ Template file not found. Creating basic .env...")
        with open(env_path, 'w') as env_file:
            env_file.write("""# Database Configuration
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DB=placement_portal

# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

# Flask Configuration
SECRET_KEY=change-this-to-a-random-secret-key
UPLOAD_FOLDER=static/uploads
MAX_UPLOAD_SIZE=16777216
""")
        print("✓ Basic .env file created. Please edit it with your credentials.")

def create_directories():
    """Create necessary directories"""
    base_dir = Path(__file__).parent.parent
    uploads_dir = base_dir / 'frontend' / 'static' / 'uploads'
    resumes_dir = uploads_dir / 'resumes'
    offers_dir = uploads_dir / 'offers'
    
    for directory in [uploads_dir, resumes_dir, offers_dir]:
        directory.mkdir(parents=True, exist_ok=True)
    
    print("✓ Upload directories created")

if __name__ == '__main__':
    print("Setting up Placement Portal...")
    setup_environment()
    create_directories()
    print("\n✓ Setup complete!")
    print("\nNext steps:")
    print("1. Edit backend/.env with your credentials")
    print("2. Initialize database: python backend/init_db.py")
    print("3. Run application: python backend/app.py")

