## This file will automatically send emails to
## designated list
## steps ## 
## 1) allow less secure app access
## 2) setup app password
## 3) hide password in environment variable


import os

## grab the environment variables
emailUser = os.environ.get('emailUser')
emailPass = os.environ.get('emailPass')

import smtplib
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    
    ## encrpt the traffic
    smtp.starttls()
    smtp.ehlo()
    
    ## login with email and pass word
    smtp.login(emailUser,emailPass)

    emailSubject = 'INSERT_SUBJECT'
    bodyOfEmail = 'INSERT_BODY_HERE'

    
    message =f'Subject:{emailSubject}\n\n{bodyOfEmail}'
    bcc = 'INSERT_EMAILS_HERE'
    #bcc = bcc.split(",")
    
    ## arguments are the sender then the reciever(s) and message
    smtp.sendmail(emailUser,bcc,message)
