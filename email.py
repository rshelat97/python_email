

import smtplib
import datetime
import time

TO = 'receipent@mailservice.com'
CC = ['rshelat@gmu.edu']
BCC = []
SUBJECT = 'ENTER SUBJECT HERE'
TEXT = 'ENTER EMAIL BODY HERE'

# Gmail Sign In
mail_sender = 'youemail@mailservice.com'
mail_passwd = 'yourpassword here'


"""Gmail -> imap.gmail.com

Outlook.com/Hotmail.com -> imap-mail.outlook.com

Yahoo Mail  -> imap.mail.yahoo.com """

server = smtplib.SMTP('smtp.gmail.com',587) #465 for yahoo, otherwise 587
server.connect('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(mail_sender, mail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % mail_sender,
                    'CC: %s' %  CC,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

x = 5 # change this to change number of emails sent per receipent(TO, CC, BCC)

TOADDRS = [TO] + BCC + CC
try:
	for i in range(0,x): # allows you to send multiple messages at once 
		server.sendmail(mail_sender, TOADDRS, BODY)
		print ('email sent @ time: ' + str(datetime.datetime.now()))
		time.sleep(2)
except:
    print ('error sending mail')

print('Emails Sent: ' + str(x * len(TOADDRS)))

server.quit()