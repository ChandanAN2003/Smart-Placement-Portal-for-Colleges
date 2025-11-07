# Deployment Guide

This guide covers deploying the AI-Integrated College Placement Management Portal to production using Render (backend) and Netlify (frontend).

## 🌐 Deployment Architecture

```
┌─────────────────┐         ┌─────────────────┐
│   Netlify       │         │     Render      │
│   (Frontend)    │─────────▶│   (Backend)     │
│   Static Files  │         │   Flask App     │
└─────────────────┘         └─────────────────┘
                                      │
                                      ▼
                            ┌─────────────────┐
                            │   MySQL DB      │
                            │   (Hosted)      │
                            └─────────────────┘
```

## 📋 Pre-Deployment Checklist

- [ ] All code is tested locally
- [ ] Environment variables are documented
- [ ] Database schema is finalized
- [ ] `.env` file is NOT committed to git
- [ ] All sensitive data is in environment variables
- [ ] Upload directories are properly configured
- [ ] Email service is configured
- [ ] Gemini API key is obtained

## 🗄️ Database Setup (Production)

### Option 1: Render MySQL (Recommended)

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "PostgreSQL" (or use external MySQL)
3. Create database instance
4. Note connection details:
   - Host
   - Port
   - Database name
   - Username
   - Password

### Option 2: External MySQL Hosting

Popular options:
- **PlanetScale** (Serverless MySQL)
- **AWS RDS** (MySQL)
- **DigitalOcean** (Managed Database)
- **Aiven** (MySQL)

### Initialize Production Database

1. Connect to your production MySQL:

```bash
mysql -h <host> -u <user> -p <database>
```

2. Import schema:

```sql
SOURCE database/schema.sql;
```

3. Create production admin user (manually or via script)

## 🚀 Backend Deployment (Render)

### Step 1: Prepare Repository

1. Ensure all files are committed:

```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. Verify `.gitignore` includes `.env`

### Step 2: Create Render Web Service

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure service:

**Settings:**
- **Name**: `placement-portal-backend`
- **Region**: Choose closest to users
- **Branch**: `main`
- **Root Directory**: `backend`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

### Step 3: Configure Environment Variables

In Render dashboard, go to "Environment" tab and add:

```env
MYSQL_HOST=your-mysql-host
MYSQL_USER=your-mysql-user
MYSQL_PASSWORD=your-mysql-password
MYSQL_DB=placement_portal

GEMINI_API_KEY=your-gemini-api-key

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-gmail-app-password

SECRET_KEY=generate-strong-random-secret-key
UPLOAD_FOLDER=static/uploads
MAX_UPLOAD_SIZE=16777216

APP_URL=https://your-render-app.onrender.com
```

**Important**: Generate a strong `SECRET_KEY`:
```python
import secrets
print(secrets.token_hex(32))
```

### Step 4: Update app.py for Production

Ensure `app.py` has production settings:

```python
if __name__ == '__main__':
    # Production settings
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
```

### Step 5: Deploy

1. Click "Create Web Service"
2. Render will build and deploy automatically
3. Wait for deployment to complete
4. Note your backend URL: `https://your-app.onrender.com`

### Step 6: Initialize Production Database

1. SSH into Render or use database client
2. Run initialization:

```bash
# Via Render Shell or local connection
python init_db.py
```

Or manually create admin user in production database.

## 🎨 Frontend Deployment (Netlify)

### Option A: Deploy with Flask (Simpler)

If frontend is served by Flask, no separate deployment needed. Backend on Render serves everything.

### Option B: Separate Frontend (Advanced)

If deploying frontend separately:

#### Step 1: Prepare Frontend

1. Create `netlify.toml` in project root:

```toml
[build]
  publish = "frontend"
  command = "echo 'No build needed'"

[[redirects]]
  from = "/api/*"
  to = "https://your-render-app.onrender.com/api/:splat"
  status = 200
  force = true
```

2. Update API URLs in JavaScript:

```javascript
// In frontend/static/js/script.js
const API_URL = "https://your-render-app.onrender.com";
```

#### Step 2: Deploy to Netlify

1. Go to [Netlify Dashboard](https://app.netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect GitHub repository
4. Configure:
   - **Base directory**: `frontend`
   - **Build command**: (leave empty or `echo 'No build'`)
   - **Publish directory**: `frontend`
5. Add environment variables if needed
6. Deploy

#### Step 3: Update CORS (if needed)

In `backend/app.py`, add CORS support:

```python
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "https://your-netlify-app.netlify.app"}})
```

## 🔒 Security Checklist

- [ ] `SECRET_KEY` is strong and unique
- [ ] Database credentials are secure
- [ ] API keys are in environment variables
- [ ] `.env` is in `.gitignore`
- [ ] HTTPS is enabled (automatic on Render/Netlify)
- [ ] File upload size limits are set
- [ ] SQL injection protection (using parameterized queries)
- [ ] XSS protection (Flask auto-escapes templates)

## 📧 Email Configuration

### Gmail Setup

1. Enable 2-Step Verification
2. Generate App Password:
   - Go to Google Account → Security
   - App Passwords → Generate
   - Use for "Mail"
3. Use App Password in `MAIL_PASSWORD`

### Alternative Email Services

- **SendGrid**: Professional email service
- **Mailgun**: Transactional emails
- **AWS SES**: Scalable email service

Update `MAIL_SERVER` and credentials accordingly.

## 🔄 Database Migrations

For production schema updates:

1. Update `database/schema.sql`
2. Connect to production database
3. Run migration SQL manually or via script
4. Test thoroughly before deploying

## 📊 Monitoring

### Render Monitoring

- View logs in Render dashboard
- Set up alerts for errors
- Monitor resource usage

### Application Monitoring

Consider adding:
- **Sentry**: Error tracking
- **LogRocket**: User session replay
- **New Relic**: Performance monitoring

## 🔄 Continuous Deployment

### Automatic Deploys

Both Render and Netlify support automatic deploys:
- Push to `main` branch → Auto deploy
- Configure in dashboard settings

### Manual Deploys

- Render: "Manual Deploy" button
- Netlify: "Trigger deploy" button

## 🐛 Troubleshooting

### Backend Issues

**Issue**: Application crashes on startup
- Check environment variables
- Review logs in Render dashboard
- Verify database connection

**Issue**: Database connection fails
- Verify MySQL credentials
- Check firewall rules
- Ensure database is accessible from Render

**Issue**: File uploads not working
- Check `UPLOAD_FOLDER` path
- Verify directory permissions
- Consider using cloud storage (S3, Cloudinary)

### Frontend Issues

**Issue**: API calls fail
- Check CORS configuration
- Verify API URL is correct
- Check browser console for errors

**Issue**: Static files not loading
- Verify file paths
- Check Netlify build output
- Ensure files are in correct directories

## 📈 Performance Optimization

1. **Database Indexing**: Add indexes on frequently queried columns
2. **Caching**: Implement Redis for session caching
3. **CDN**: Use Cloudflare for static assets
4. **Database Connection Pooling**: Configure in production
5. **File Storage**: Use S3/Cloudinary for uploads

## 🔐 Backup Strategy

1. **Database Backups**:
   - Automated daily backups
   - Store in secure location
   - Test restore procedures

2. **File Backups**:
   - Backup uploaded resumes/offer letters
   - Use cloud storage with versioning

## 📝 Post-Deployment

1. Test all user roles
2. Verify email sending
3. Test file uploads
4. Check AI analysis functionality
5. Monitor error logs
6. Update documentation with production URLs

## 🎯 Production URLs

After deployment, update:
- API endpoints in frontend
- Email links in templates
- Documentation

---

**Your application is now live! 🎉**

