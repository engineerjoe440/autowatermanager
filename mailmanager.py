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
def send_email(recipient_list, content, files=None):
    # Interpret Subject/Body from Content
    subject = content['subject']
    body    = content['body']
    html    = content['html']
    # Set Up MIME with Header Fields
    message = MIMEMultipart("alternative", None, [MIMEText(body), MIMEText(html,'html')])
    message['From'] = address
    # Clean Up Recipient List and Prepare for Email Sender
    recipient_list = [i for i in recipient_list if i]
    recipients = COMMASPACE.join( recipient_list )
    message['To'] = recipients
    message['Date'] = formatdate(localtime=True)
    message['Subject'] = subject
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

# Define Email Template Reader Function
def emailtemplate(path,subjectcontext=None,bodycontext=None,htmlcontext=None):
    """
    Description of Template File Structure:
    
    '''
    *subject-line*
    
    *body-content*
    ;; *return-character*
    *more body-content*
    *cont'd*
    {{replacement}}
    *more body*
    <html>
    *html-body-content*
    '''
    
    Use of the {{context}} formatting option paired with a
    dictionary for either `subjectcontext`, `bodycontext`,
    or `htmlcontext` to fill template with contextual
    information.
    """
    # Validate Path
    if not path.endswith('.emlx'):
        raise ValueError("Improper File Type: Must be *.emlx file.")
    # Read Email Subject and Body
    with open(path,'r') as emlx:
        subj = emlx.readline()
        x = emlx.readline() # Dummy Separator Line
        body = ' '.join(emlx.readlines())
    # Change Standard Text to HTML Formatting
    if body.find('<html>') != -1:
        html = body
        body = ''
    else:
        html = ''
    # Clean Text Strings
    subj = subj.replace('\n','')
    body = body.replace('\n','').replace(';;','\n')
    # Perform Formatting Operations
    if isinstance(subjectcontext,dict):
        for key,val in subjectcontext.items():
            subj = subj.replace('{{'+str(key)+'}}', str(val))
    if isinstance(bodycontext,dict):
        for key,val in bodycontext.items():
            body = body.replace('{{'+str(key)+'}}', str(val))
    if isinstance(htmlcontext,dict):
        for key,val in htmlcontext.items():
            html = html.replace('{{'+str(key)+'}}', str(val))
    print(body,html)
    return({'subject':subj,'body':body,'html':html})

# Define Builtin Test Aparatus
if __name__ == '__main__' :
    recipients = [  'stan3926@vandals.uidaho.edu',
                    'engineerjoe440@yahoo.com',
                    'engineerjoe440@gmail.com']
    files = "mailmanager.py"
    # Evaluate Template
    x=emailtemplate("D:\\Files\\Stanley Solutions\\Auto (Horse) Water Manager\\email\\errnotice.emlx",
                    None,{'notice':'some test notice'})
    # Send Email
    send_email( recipients, x, files )
    print("Success")

# END