"""
Google Gemini API integration for AI features
"""
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def analyze_resume(resume_text, job_role, job_description=""):
    """
    Analyze resume using Gemini API and return job-fit analysis
    
    Args:
        resume_text: Text content extracted from resume
        job_role: Job role/position name
        job_description: Optional job description
    
    Returns:
        dict with keys: skills, education, experience, job_fit_score, suggestions
    """
    if not GEMINI_API_KEY:
        return {
            'skills': [],
            'education': 'Not analyzed',
            'experience': 'Not analyzed',
            'job_fit_score': 0,
            'suggestions': 'Gemini API key not configured'
        }
    
    try:
        prompt = f"""
        Analyze this resume for the role: {job_role}
        
        Job Description: {job_description if job_description else 'Not provided'}
        
        Resume Content:
        {resume_text[:5000]}  # Limit to 5000 chars
        
        Please provide a JSON response with the following structure:
        {{
            "skills": ["skill1", "skill2", ...],
            "education": "Summary of education",
            "experience": "Summary of experience",
            "job_fit_score": 85,
            "suggestions": "Improvement suggestions"
        }}
        
        Calculate job_fit_score (0-100) based on:
        - Relevant skills match
        - Education alignment
        - Experience relevance
        - Overall fit for the role
        
        Provide specific, actionable suggestions for improvement.
        """
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        # Parse response (Gemini may return markdown or plain text)
        response_text = response.text.strip()
        
        # Try to extract JSON from response
        import json
        import re
        
        # Look for JSON in the response
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            try:
                result = json.loads(json_match.group())
                return result
            except:
                pass
        
        # Fallback: parse manually if JSON extraction fails
        return {
            'skills': extract_skills_from_text(response_text),
            'education': extract_field(response_text, 'education'),
            'experience': extract_field(response_text, 'experience'),
            'job_fit_score': extract_score(response_text),
            'suggestions': response_text[:500] if len(response_text) > 500 else response_text
        }
        
    except Exception as e:
        print(f"Gemini API error: {e}")
        return {
            'skills': [],
            'education': 'Analysis failed',
            'experience': 'Analysis failed',
            'job_fit_score': 0,
            'suggestions': f'Error: {str(e)}'
        }

def extract_skills_from_text(text):
    """Extract skills list from text"""
    skills = []
    # Common tech skills to look for
    tech_skills = ['Python', 'Java', 'JavaScript', 'SQL', 'HTML', 'CSS', 'React', 'Node.js', 
                   'Flask', 'Django', 'AWS', 'Azure', 'Git', 'Docker', 'Machine Learning']
    for skill in tech_skills:
        if skill.lower() in text.lower():
            skills.append(skill)
    return skills[:10]  # Limit to 10 skills

def extract_field(text, field_name):
    """Extract a specific field from text"""
    import re
    pattern = rf'{field_name}[:\-]?\s*(.+?)(?:\n|$)'
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else 'Not specified'

def extract_score(text):
    """Extract job fit score from text"""
    import re
    # Look for numbers 0-100
    scores = re.findall(r'\b([0-9]{1,2}|100)\b', text)
    for score in scores:
        score_int = int(score)
        if 0 <= score_int <= 100:
            return score_int
    return 50  # Default score

def generate_email_content(email_type, recipient_name, company_name, job_role, additional_info=""):
    """
    Generate professional email content using Gemini
    
    Args:
        email_type: 'offer', 'rejection', 'shortlist', 'reminder'
        recipient_name: Name of recipient
        company_name: Company name
        job_role: Job role
        additional_info: Any additional context
    
    Returns:
        Email subject and body
    """
    if not GEMINI_API_KEY:
        return get_default_email(email_type, recipient_name, company_name, job_role)
    
    try:
        prompt = f"""
        Generate a professional {email_type} email for a college placement scenario.
        
        Recipient: {recipient_name}
        Company: {company_name}
        Position: {job_role}
        Additional Info: {additional_info}
        
        Email Type: {email_type}
        
        Requirements:
        - Professional and courteous tone
        - Clear and concise
        - Include relevant details
        - Appropriate for college placement context
        
        Provide the email in this format:
        SUBJECT: [subject line]
        BODY:
        [email body]
        """
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        response_text = response.text.strip()
        
        # Parse subject and body
        lines = response_text.split('\n')
        subject = ""
        body_lines = []
        in_body = False
        
        for line in lines:
            if line.startswith('SUBJECT:'):
                subject = line.replace('SUBJECT:', '').strip()
            elif line.startswith('BODY:'):
                in_body = True
            elif in_body:
                body_lines.append(line)
        
        body = '\n'.join(body_lines).strip() if body_lines else response_text
        
        if not subject:
            subject = get_default_subject(email_type, company_name, job_role)
        
        return {
            'subject': subject,
            'body': body if body else get_default_email(email_type, recipient_name, company_name, job_role)['body']
        }
        
    except Exception as e:
        print(f"Email generation error: {e}")
        return get_default_email(email_type, recipient_name, company_name, job_role)

def get_default_email(email_type, recipient_name, company_name, job_role):
    """Fallback default emails if Gemini fails"""
    templates = {
        'offer': {
            'subject': f'Congratulations! Offer Letter from {company_name}',
            'body': f'Dear {recipient_name},\n\nWe are pleased to inform you that you have been selected for the position of {job_role} at {company_name}.\n\nPlease find the offer letter attached.\n\nCongratulations!\n\nBest regards,\nPlacement Office'
        },
        'rejection': {
            'subject': f'Application Update - {company_name}',
            'body': f'Dear {recipient_name},\n\nThank you for your interest in the {job_role} position at {company_name}.\n\nAfter careful consideration, we regret to inform you that we will not be moving forward with your application at this time.\n\nWe wish you the best in your future endeavors.\n\nBest regards,\nPlacement Office'
        },
        'shortlist': {
            'subject': f'Shortlisted for {job_role} - {company_name}',
            'body': f'Dear {recipient_name},\n\nCongratulations! You have been shortlisted for the {job_role} position at {company_name}.\n\nFurther details regarding the interview process will be shared soon.\n\nBest regards,\nPlacement Office'
        }
    }
    return templates.get(email_type, templates['rejection'])

def get_default_subject(email_type, company_name, job_role):
    """Default email subjects"""
    subjects = {
        'offer': f'Congratulations! Offer Letter from {company_name}',
        'rejection': f'Application Update - {company_name}',
        'shortlist': f'Shortlisted for {job_role} - {company_name}'
    }
    return subjects.get(email_type, f'Update from {company_name}')

