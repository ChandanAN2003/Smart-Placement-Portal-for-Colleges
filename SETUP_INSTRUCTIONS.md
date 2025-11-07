# Setup Instructions

## 🎯 Complete Setup Guide

Follow these steps to get your AI-Integrated College Placement Management Portal running.

## Step 1: Install Prerequisites

### Python
- Download Python 3.11+ from [python.org](https://www.python.org/downloads/)
- Verify installation: `python --version`

### MySQL
- **Option A**: Install XAMPP from [xampp.org](https://www.apachefriends.org/)
- **Option B**: Install MySQL standalone from [mysql.com](https://dev.mysql.com/downloads/)
- Start MySQL service

### Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key (you'll need it later)

### Gmail App Password (for email)
1. Go to [Google Account](https://myaccount.google.com/)
2. Enable 2-Step Verification
3. Go to App Passwords
4. Generate password for "Mail"
5. Copy the 16-character password

## Step 2: Clone/Download Project

If using Git:
```bash
git clone <repository-url>
cd college-placement-portal
```

Or extract the project files to a folder.

## Step 3: Set Up Python Environment

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 4: Configure Database

### Using XAMPP (Easiest)

1. Start XAMPP Control Panel
2. Start MySQL service
3. Open phpMyAdmin: http://localhost/phpmyadmin
4. Click "New" to create database
5. Name it: `placement_portal`
6. Click "Import" tab
7. Choose `database/schema.sql` file
8. Click "Go"

### Using Command Line

```bash
# Login to MySQL
mysql -u root -p

# Create database
CREATE DATABASE placement_portal;
USE placement_portal;

# Import schema
SOURCE database/schema.sql;

# Exit
EXIT;
```

## Step 5: Configure Environment Variables

1. Copy the example file:
```bash
# From backend directory
cp ../docs/env_example.txt .env
```

2. Edit `.env` file with your settings:

```env
# Database (adjust if using XAMPP default)
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=          # Leave empty if no password
MYSQL_DB=placement_portal

# Google Gemini API (paste your key here)
GEMINI_API_KEY=paste_your_gemini_api_key_here

# Email Configuration (Gmail)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_16_char_app_password

# Flask Configuration
SECRET_KEY=generate-random-key-here
UPLOAD_FOLDER=static/uploads
MAX_UPLOAD_SIZE=16777216
```

**Generate SECRET_KEY:**
```python
import secrets
print(secrets.token_hex(32))
```

## Step 6: Initialize Database

```bash
# From backend directory
python init_db.py
```

This creates default users:
- **TPO**: tpo@college.edu / admin123
- **HOD**: hod.cs@college.edu / hod123
- **Student**: alice@college.edu / student123

## Step 7: Verify Upload Directories

The directories should already exist, but verify:
- `frontend/static/uploads/resumes/`
- `frontend/static/uploads/offers/`

If missing, create them:
```bash
# Windows PowerShell
New-Item -ItemType Directory -Force -Path "..\frontend\static\uploads\resumes", "..\frontend\static\uploads\offers"

# Linux/Mac
mkdir -p ../frontend/static/uploads/resumes
mkdir -p ../frontend/static/uploads/offers
```

## Step 8: Run the Application

```bash
# From backend directory
python app.py
```

You should see:
```
* Running on http://0.0.0.0:5000
```

## Step 9: Access the Portal

Open your browser:
```
http://localhost:5000
```

## Step 10: Test the Application

### Test as TPO (Admin)
1. Login: `tpo@college.edu` / `admin123`
2. Create a placement drive
3. View applications

### Test as Student
1. Login: `alice@college.edu` / `student123`
2. Upload a resume (PDF or DOCX)
3. View active drives
4. Apply for a drive
5. Check AI analysis

### Test as HOD
1. Login: `hod.cs@college.edu` / `hod123`
2. View pending approvals
3. Approve students
4. Export report

## 🐛 Troubleshooting

### "Module not found" error
- Ensure virtual environment is activated
- Run: `pip install -r requirements.txt`

### Database connection error
- Verify MySQL is running
- Check credentials in `.env`
- Ensure database exists

### Gemini API not working
- Verify API key in `.env`
- Check internet connection
- Ensure API key is valid

### Email not sending
- Use Gmail App Password (not regular password)
- Verify 2-Step Verification is enabled
- Check SMTP settings

### File upload fails
- Check directory permissions
- Verify file size < 16MB
- Ensure file is PDF or DOCX

## ✅ Success Checklist

- [ ] Python environment activated
- [ ] Dependencies installed
- [ ] MySQL running and database created
- [ ] `.env` file configured
- [ ] Database initialized
- [ ] Application runs without errors
- [ ] Can login with default credentials
- [ ] Can upload resume
- [ ] Can create drive (TPO)
- [ ] Can apply for drive (Student)

## 📚 Next Steps

- Read [QUICKSTART.md](docs/QUICKSTART.md) for detailed guide
- Read [DEPLOYMENT.md](docs/DEPLOYMENT.md) for production deployment
- Customize the application for your needs

---

**Need help? Check the documentation in the `docs/` folder!**

