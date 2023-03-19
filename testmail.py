import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the email addresses and message
sender_email = "testingpy190@gmail.com"
receiver_email = "recipient_email@example.com"
password = input("Type your password and press enter: ")
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email"

# Add body to email
body = "This is a test email sent using Python"
message.attach(MIMEText(body, "plain"))

# Create SMTP session
session = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls()

# Login to Gmail
session.login(sender_email, password)

# Send the email
text = message.as_string()
session.sendmail(sender_email, receiver_email, text)

# Terminate the session
session.quit()

print("Email sent successfully!")