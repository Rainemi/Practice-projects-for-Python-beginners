#the  algorithm to wrie a sendmail program is listed below as comments
#go over to your gmail and set up 2 factor authentification
#generate app password
#create the function to send mail 

from email.message import EmailMessage
import smtplib
import ssl

password = 'your password derived from app password'

Email_sender = ''
Email_password = password
Email_reciever = ''

subject = 'Reasons why you should workout'
body = '''
1. workout so as to build Muscle
2. workout to stabilise your mental health
3. workout to keep your organs from deteriorating 
'''

em = EmailMessage()
em['From'] = Email_sender
em['To'] = Email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(Email_sender,Email_password)
        server.sendmail(Email_sender, Email_reciever, em.as_string())
