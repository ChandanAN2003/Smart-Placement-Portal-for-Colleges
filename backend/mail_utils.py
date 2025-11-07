"""
Email utility functions using Flask-Mail
"""
from flask_mail import Mail, Message
from flask import current_app
import os

mail = Mail()

def init_mail(app):
    """Initialize Flask-Mail with app configuration"""
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', '')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', '')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME', '')
    
    mail.init_app(app)

def send_email(to, subject, body, html_body=None, attachments=None):
    """
    Send an email
    
    Args:
        to: Recipient email address
        subject: Email subject
        body: Plain text body
        html_body: Optional HTML body
        attachments: List of attachment file paths
    
    Returns:
        True if sent successfully, False otherwise
    """
    try:
        msg = Message(
            subject=subject,
            recipients=[to],
            body=body,
            html=html_body
        )
        
        if attachments:
            for attachment_path in attachments:
                with current_app.open_resource(attachment_path) as f:
                    msg.attach(
                        filename=os.path.basename(attachment_path),
                        content_type='application/octet-stream',
                        data=f.read()
                    )
        
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Email sending error: {e}")
        return False

def send_application_update_email(student_email, student_name, company_name, job_role, status, offer_letter_path=None):
    """
    Send application status update email to student
    
    Args:
        student_email: Student's email
        student_name: Student's name
        company_name: Company name
        job_role: Job role
        status: Application status
        offer_letter_path: Optional path to offer letter attachment
    """
    from gemini_ai import generate_email_content
    
    email_type = 'offer' if status == 'Selected' else ('shortlist' if status == 'Shortlisted' else 'rejection')
    
    email_content = generate_email_content(
        email_type=email_type,
        recipient_name=student_name,
        company_name=company_name,
        job_role=job_role
    )
    
    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
            <h2 style="color: #2c3e50;">Application Update</h2>
            <p>Dear {student_name},</p>
            <div style="background-color: #f4f4f4; padding: 15px; border-radius: 5px; margin: 20px 0;">
                {email_content['body'].replace(chr(10), '<br>')}
            </div>
            <p><strong>Company:</strong> {company_name}</p>
            <p><strong>Position:</strong> {job_role}</p>
            <p><strong>Status:</strong> {status}</p>
            <p style="margin-top: 30px;">Best regards,<br>Placement Office</p>
        </div>
    </body>
    </html>
    """
    
    attachments = [offer_letter_path] if offer_letter_path and os.path.exists(offer_letter_path) else None
    
    return send_email(
        to=student_email,
        subject=email_content['subject'],
        body=email_content['body'],
        html_body=html_body,
        attachments=attachments
    )

