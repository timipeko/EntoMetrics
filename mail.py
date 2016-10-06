#!/usr/bin/python

from smtplib import SMTPException
import smtplib
import datetime
import email
import imaplib
import mailbox

def checkmail():
    EMAIL_ACCOUNT = "entometrics1@gmail.com"
    PASSWORD = "osmicetrti1992"

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, "UNSEEN")  # (ALL/UNSEEN)
    i = len(data[0].split())

    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        # result, email_data = conn.store(num,'-FLAGS','\\Seen')
        # this might work to set flag to seen, if it doesn't already
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        # Header Details
        date_tuple = email.utils.parsedate_tz(email_message['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            local_message_date = "%s" % (str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From']))).split()[-1]
        subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

        sendmail((email_from.replace("<", "").replace(">", "")))

def sendmail(mail):
    import smtplib

    to = mail
    gmail_user = 'entometrics1@gmail.com'
    gmail_pwd = 'osmicetrti1992'
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
    print(header)
    msg = header + '\n Hello, I am EntoMetrics. Soon I will be online! \n\n'
    smtpserver.sendmail(gmail_user, to, msg)
    print('done!')
    smtpserver.close()