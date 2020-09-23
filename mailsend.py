#!/usr/bin/env python3

import os
import smtplib
import getpass # <-- to conceal user input

# Set Variables
EMAIL_ADDRESS = input('Enter your email address: ')
EMAIL_PASSWORD = getpass.getpass()
# ^ Hide user PW input^


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Python is a lot of fun!!'
    body = 'Vim, Linux & Python. I use them everyday.'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'rsa.asym2048@gmail.com', msg)
