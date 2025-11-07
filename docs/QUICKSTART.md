# Quick Start Guide

This guide will help you get the AI-Integrated College Placement Management Portal up and running quickly.

## ⚡ Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.11 or higher installed
- [ ] MySQL Server running (XAMPP or standalone)
- [ ] Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))
- [ ] Gmail account with App Password enabled
- [ ] Git installed (optional, for version control)

## 🚀 Installation Steps

### Step 1: Download and Extract

If you have the project files, navigate to the project directory:

```bash
cd college-placement-portal
```

### Step 2: Set Up Python Environment

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

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure MySQL Database

#### Option A: Using XAMPP

1. Start XAMPP Control Panel
2. Start Apache and MySQL services
3. Open phpMyAdmin (http://localhost/phpmyadmin)
4. Create a new database named `placement_portal`
5. Import the schema:

```sql
-- In phpMyAdmin SQL tab, run:
SOURCE database/schema.sql;
```

#### Option B: Using Command Line

```bash
# Login to MySQL
mysql -u root -p

# Create and use database
CREATE DATABASE placement_portal;
USE placement_portal;

# Import schema
SOURCE database/schema.sql;

# Exit MySQL
EXIT;
```

#### Option C: Direct Import

```bash
mysql -u root -p placement_portal < database/schema.sql
```

### Step 4: Configure Environment Variables

1. Copy the example environment file:

```bash
# From backend directory
cp ../docs/env_example.txt .env
```

2. Edit `.env` file with your settings:

```env
# Database Configuration
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=          # Leave empty if no password
MYSQL_DB=placement_portal

# Google Gemini API
GEMINI_API_KEY=your_actual_gemini_api_key_here

# Email Configuration (Gmail)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_gmail_app_password

# Flask Configuration
SECRET_KEY=generate-a-random-secret-key-here
UPLOAD_FOLDER=static/uploads
MAX_UPLOAD_SIZE=16777216
```

#### Getting Gmail App Password

1. Go to your Google Account settings
2. Enable 2-Step Verification
3. Go to App Passwords
4. Generate a new app password for "Mail"
5. Use this 16-character password in `.env`

#### Getting Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key to `.env`

### Step 5: Initialize Database with Default Users

```bash
# From backend directory
python init_db.py
```

This creates:
- **TPO Admin**: `tpo@college.edu` / `admin123`
- **HOD**: `hod.cs@college.edu` / `hod123`
- **Student**: `alice@college.edu` / `student123`

### Step 6: Create Upload Directories

```bash
# Windows PowerShell
New-Item -ItemType Directory -Force -Path "..\frontend\static\uploads\resumes", "..\frontend\static\uploads\offers"

# Linux/Mac
mkdir -p ../frontend/static/uploads/resumes
mkdir -p ../frontend/static/uploads/offers
```

### Step 7: Run the Application

```bash
# From backend directory
python app.py
```

You should see:
```
* Running on http://0.0.0.0:5000
```

### Step 8: Access the Portal

Open your browser and navigate to:
```
http://localhost:5000
```

## 🧪 Testing the Application

### Test Login

1. **As TPO Admin**:
   - Email: `tpo@college.edu`
   - Password: `admin123`
   - Can create drives, manage applications, upload offer letters

2. **As HOD**:
   - Email: `hod.cs@college.edu`
   - Password: `hod123`
   - Can approve students, view department stats

3. **As Student**:
   - Email: `alice@college.edu`
   - Password: `student123`
   - Can upload resume, apply for drives, view status

### Test Workflow

1. **Student Workflow**:
   - Login as student
   - Upload a resume (PDF or DOCX)
   - View active placement drives
   - Apply for a drive
   - Check AI resume analysis

2. **TPO Workflow**:
   - Login as TPO
   - Create a new placement drive
   - View applications
   - Update application status
   - Upload offer letter (if selected)

3. **HOD Workflow**:
   - Login as HOD
   - Approve pending students
   - View department statistics
   - Export department report

## 🔧 Troubleshooting

### Issue: "Module not found" error

**Solution**: Ensure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: Database connection error

**Solution**: 
- Verify MySQL is running
- Check credentials in `.env`
- Ensure database `placement_portal` exists

### Issue: Gemini API not working

**Solution**:
- Verify API key in `.env` is correct
- Check internet connection
- Verify API key has proper permissions

### Issue: Email not sending

**Solution**:
- Use Gmail App Password (not regular password)
- Verify 2-Step Verification is enabled
- Check SMTP settings in `.env`

### Issue: File upload fails

**Solution**:
- Check upload directory permissions
- Verify file size is under 16MB
- Ensure file is PDF or DOCX format

## 📝 Next Steps

- Read [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment
- Review [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for feature overview
- Customize the application for your college's needs

## 💡 Tips

- **Development Mode**: The app runs in debug mode by default. For production, set `FLASK_ENV=production`
- **Database Backup**: Regularly backup your MySQL database
- **API Keys**: Never commit `.env` file to version control
- **Security**: Change default passwords before production use

## 🆘 Need Help?

- Check the [README.md](README.md) for detailed documentation
- Review error messages in the terminal
- Verify all prerequisites are installed correctly

---

**Happy Coding! 🚀**

