# AI-Integrated College Placement Management Portal

A comprehensive, production-ready web application for managing college placement processes with AI-powered resume analysis using Google Gemini API.

## 🎯 Project Overview

This portal automates and manages the entire campus placement process, integrating AI automation for:
- **Resume Analysis**: Extract skills, education, and experience
- **Job Fit Prediction**: Calculate job-fit percentage using AI
- **Intelligent Communication**: Generate professional emails automatically
- **Resume Improvement Suggestions**: AI-powered feedback

## 🏗️ Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend**: Flask (Python 3.11+)
- **Database**: MySQL (via XAMPP or hosted)
- **AI Integration**: Google Gemini API
- **Email**: Flask-Mail (SMTP)
- **Deployment**: Render (Backend) + Netlify (Frontend)

## 👥 User Roles

### 🧑‍🎓 Student
- Register and log in securely
- Upload resume (PDF/DOCX)
- View and apply for placement drives
- Receive AI resume feedback and job-fit percentage
- Track application status
- Receive email updates

### 🧑‍🏫 Head of Department (HOD)
- Approve or verify student profiles
- View department-level analytics
- Generate reports (Excel/PDF)

### 👨‍💼 Training & Placement Officer (TPO/Admin)
- Create and manage placement drives
- Upload offer letters
- Send automated emails
- View global placement statistics
- Export comprehensive reports

## 📁 Project Structure

```
college-placement-portal/
│
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── database.py            # Database connection utilities
│   ├── gemini_ai.py           # Google Gemini API integration
│   ├── mail_utils.py           # Email functionality
│   ├── init_db.py             # Database initialization
│   ├── requirements.txt        # Python dependencies
│   ├── Procfile               # Render deployment config
│   └── runtime.txt             # Python version
│
├── frontend/
│   ├── templates/             # HTML templates
│   │   ├── index.html
│   │   ├── student_dashboard.html
│   │   ├── hod_dashboard.html
│   │   └── tpo_dashboard.html
│   └── static/
│       ├── css/style.css
│       ├── js/script.js
│       └── uploads/           # User uploads (gitignored)
│
├── database/
│   ├── schema.sql             # Database schema
│   └── seed_data.sql          # Sample data
│
├── docs/
│   ├── README.md              # This file
│   ├── QUICKSTART.md          # Quick setup guide
│   ├── DEPLOYMENT.md          # Deployment instructions
│   └── PROJECT_SUMMARY.md     # Project summary
│
└── .gitignore
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- MySQL Server (XAMPP or standalone)
- Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))
- Gmail account with App Password (for email)

### Step 1: Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd college-placement-portal

# Create virtual environment
cd backend
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Database Setup

1. Start MySQL server (XAMPP or standalone)
2. Create database:

```bash
mysql -u root -p < ../database/schema.sql
```

3. Or manually:
```sql
CREATE DATABASE placement_portal;
USE placement_portal;
SOURCE database/schema.sql;
```

### Step 3: Environment Configuration

1. Copy environment template:
```bash
cp ../docs/env_example.txt .env
```

2. Edit `.env` with your credentials:
```env
# Database
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=placement_portal

# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

# Flask Config
SECRET_KEY=your-secret-key-change-this
UPLOAD_FOLDER=static/uploads
```

### Step 4: Initialize Database

```bash
python init_db.py
```

This creates default users:
- **TPO**: `tpo@college.edu` / `admin123`
- **HOD**: `hod.cs@college.edu` / `hod123`
- **Student**: `alice@college.edu` / `student123`

### Step 5: Run Application

```bash
python app.py
```

Access at: `http://localhost:5000`

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)**: Detailed setup instructions
- **[DEPLOYMENT.md](DEPLOYMENT.md)**: Production deployment guide
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)**: Project overview and features

## 🔑 Key Features

### AI Integration
- **Resume Parsing**: Extract skills, education, experience
- **Job Fit Analysis**: Calculate compatibility score (0-100%)
- **Email Generation**: AI-powered professional emails
- **Improvement Suggestions**: Actionable resume feedback

### Security
- Password hashing (Werkzeug)
- Session management
- Role-based access control
- File upload validation

### Reporting
- Excel export for HOD (department reports)
- Excel export for TPO (comprehensive reports)
- Real-time statistics dashboard

### Email Notifications
- Application status updates
- Offer letter delivery
- Automated notifications

## 🛠️ Development

### Running in Development Mode

```bash
export FLASK_ENV=development
python app.py
```

### Database Migrations

For schema changes, update `database/schema.sql` and re-run:

```bash
mysql -u root -p placement_portal < database/schema.sql
```

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify MySQL is running
   - Check credentials in `.env`
   - Ensure database exists

2. **Gemini API Error**
   - Verify API key in `.env`
   - Check API quota/limits
   - Ensure internet connection

3. **Email Not Sending**
   - Verify Gmail App Password (not regular password)
   - Check SMTP settings in `.env`
   - Review firewall settings

4. **File Upload Issues**
   - Check `UPLOAD_FOLDER` permissions
   - Verify file size limits
   - Ensure directory exists

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on the repository.

---

**Built with ❤️ for efficient college placement management**

