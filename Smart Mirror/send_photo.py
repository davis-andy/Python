import smtplib, imghdr
from email.message import EmailMessage
# pylint: disable=unused-wildcard-import
from settings import *


class SendPhoto():

    def send_email(self, recipient, message):
        msg = EmailMessage()
        msg['From'] = HOTMAIL
        msg['To'] = recipient
        msg['Subject'] = ''

    
        img_data = open(message, 'rb').read()
        msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

        SMTP = smtplib.SMTP(HOTMAIL_SMTP, 587)
        SMTP.ehlo()
        SMTP.starttls()
        SMTP.login(HOTMAIL, HOTMAIL_PASSWORD)

        #email_status = EMAIL_SMTP.sendmail(EMAIL, recipient, 'Subject: \n' + msg)
        email_status = SMTP.send_message(msg)

        if email_status != {}:
            print("Error sending email to %s: %s" % (recipient, email_status))
        else:
            print("Photo sent")

        SMTP.quit()