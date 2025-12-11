import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_TO = os.getenv('EMAIL_TO')


# Read email template and replace placeholders
with open('email_template.txt', 'r', encoding='utf-8') as f:
    email_body = f.read()

commit_id = os.getenv('COMMIT_ID', 'N/A')
commit_message = os.getenv('COMMIT_MESSAGE', 'N/A')
email_body = email_body.replace('{{COMMIT_ID}}', commit_id)
email_body = email_body.replace('{{COMMIT_MESSAGE}}', commit_message)

msg = MIMEMultipart()
msg['From'] = EMAIL_HOST_USER
msg['To'] = EMAIL_TO
msg['Subject'] = 'Test Email from GitHub Actions Demo'
msg.attach(MIMEText(email_body, 'plain'))

try:
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(msg)
    print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')
