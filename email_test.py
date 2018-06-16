

import smtplib
import datetime

TO = 'receipient@mailservice.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

# Gmail Sign In
gmail_sender = 'youemailaddress@mailservice.com'
gmail_passwd = 'enterpasswordhere'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent @ time: ' + str(datetime.datetime.now()) )
except:
    print ('error sending mail')

server.quit()