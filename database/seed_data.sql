USE placement_portal;

-- Insert sample TPO/Admin (password: admin123)
INSERT INTO users (name, email, password_hash, role, department, is_approved) VALUES
('Admin TPO', 'tpo@college.edu', 'pbkdf2:sha256:600000$XxXxXxXx$hash_here', 'tpo', 'Placement', TRUE);

-- Insert sample HOD (password: hod123)
INSERT INTO users (name, email, password_hash, role, department, is_approved) VALUES
('Dr. John Smith', 'hod.cs@college.edu', 'pbkdf2:sha256:600000$XxXxXxXx$hash_here', 'hod', 'Computer Science', TRUE);

-- Insert sample students (password: student123)
INSERT INTO users (name, email, password_hash, role, department, is_approved) VALUES
('Alice Johnson', 'alice@college.edu', 'pbkdf2:sha256:600000$XxXxXxXx$hash_here', 'student', 'Computer Science', TRUE),
('Bob Williams', 'bob@college.edu', 'pbkdf2:sha256:600000$XxXxXxXx$hash_here', 'student', 'Computer Science', FALSE),
('Carol Davis', 'carol@college.edu', 'pbkdf2:sha256:600000$XxXxXxXx$hash_here', 'student', 'Electronics', TRUE);

-- Insert sample placement drives
INSERT INTO drives (company_name, job_role, job_description, eligibility, last_date, status, created_by) VALUES
('Tech Corp', 'Software Engineer', 'Looking for skilled software engineers with experience in Python and web development.', 'CGPA >= 7.5, No backlogs', '2024-12-31', 'active', 1),
('Data Systems', 'Data Analyst', 'Seeking data analysts proficient in SQL, Python, and data visualization.', 'CGPA >= 7.0, No backlogs', '2024-12-25', 'active', 1),
('Cloud Solutions', 'Cloud Architect', 'Cloud architect position requiring AWS/Azure certification.', 'CGPA >= 8.0, AWS/Azure certified', '2024-12-20', 'active', 1);

