import smtplib
import os 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

""" Send an email with specified subject and body to specified recipient.
        Paramaters:
            subject (str)
            body (str)
            to_email (str)
"""
def send_email(subject, body, to_email):
    from_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')
    
    msg = MIMEMultipart()
    
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smto.gmail.com', 587)
        server.startls()
        server.login(from_email, password)
        server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()
        

if __name__ == "main":
    subject = input("Enter subject: ")
    body = input("Enter body: ")
    to_email = input("Enter recipient email address: ")
    
    send_email(subject, body, to_email)
    
    
