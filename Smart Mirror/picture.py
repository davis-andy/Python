import cv2 as cv
import os, time, smtplib, imghdr
from email.message import EmailMessage

# pylint: disable=unused-wildcard-import
from settings import *


def send_email(recipient, message):
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

    SMTP.quit()


# pylint: disable=no-member
cam = cv.VideoCapture(0)
s, img = cam.read()

path = "C:/Users/Andy/Desktop"
img_file = os.path.join(path, "test.jpg")

text = PHONE_NUMBER + ATT_MMS


while True:
    s, img = cam.read()
    cv.imshow("cam-test", img)
    
    if cv.waitKey(1) & 0xFF == ord('s'):
        cv.imwrite(img_file, img)
        break

cam.release()
cv.destroyAllWindows()

#time.sleep(2)
#send_email(text, img_file)
#time.sleep(5)
#os.remove(img_file)