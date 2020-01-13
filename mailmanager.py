# Barn Automation Email Manager

# Import Required Libraries
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

# Define Server Parameters
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Define Credentials
address = "stanleyembeddedtech@gmail.com"
passset = "St@nl3ys0lut!0n$t3ch"

# Define Email Sender Function
def send_email(recipient_list, subject, body, files=None):
    # Set Up MIME with Header Fields
    message = MIMEMultipart()
    message['From'] = address
    recipients = COMMASPACE.join( recipient_list )
    message['To'] = recipients
    message['Date'] = formatdate(localtime=True)
    message['Subject'] = subject
    # Generate Email Body
    message.attach(MIMEText(body))
    # Condition File Input
    if files != None and isinstance(files, str):
        files = [files] # Wrap as a List
    # Attach Any Available Files
    for f_nm in files or []:
        with open(f_nm, "rb") as f_obj:
            part = MIMEApplication( f_obj.read(), Name=basename(f_nm) )
        # After File is Closed
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(f_nm))
        message.attach(part)
    # Open SMTP Session and Send Mail
    session = smtplib.SMTP(smtp_server, smtp_port)
    session.starttls() # Enable Security
    session.login(address, passset) # Log In to Server
    # Load Content and Send
    session.sendmail(address, recipient_list, message.as_string())
    session.quit()


# Define Builtin Test Aparatus
if __name__ == '__main__' :
    recipients = [  'stan3926@vandals.uidaho.edu',
                    'engineerjoe440@yahoo.com',
                    'engineerjoe440@gmail.com']
    subject = "Embedded Test Email"
    body = "This is just a test message... Hope it works!"
    files = "mailmanager.py"
    # Send Email
    send_email( recipients, subject, body, files )
    print("Success")

# END