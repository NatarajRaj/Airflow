import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "anataraj95@gmail.com"  # Your Gmail address
smtp_password = "fxodanqwcocpcrds"  # Use the App Password generated in Gmail

sender_email = "anataraj95@gmail.com"
receiver_email = "anataraj95@gmail.com"  # Replace with your test email

# Create the email message
msg = MIMEMultipart()
msg['From'] = 'anataraj95@gmail.com'
msg['To'] = 'anataraj95@gmail.com'

msg['Subject'] = 'Test Email'
body = "This is a test email sent from Airflow."
msg.attach(MIMEText(body, 'plain'))

# Set up the server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Start TLS encryption
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()
